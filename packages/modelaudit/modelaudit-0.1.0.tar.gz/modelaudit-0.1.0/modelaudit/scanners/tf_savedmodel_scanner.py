import os
from typing import Optional, Dict, Any, List, Set
from .base import ScanResult, BaseScanner, IssueSeverity

# Try to import TensorFlow, but handle the case where it's not installed
try:
    import tensorflow as tf
    from tensorflow.core.protobuf.saved_model_pb2 import SavedModel
    HAS_TENSORFLOW = True
except ImportError:
    HAS_TENSORFLOW = False
    # Create a placeholder for type hints when TensorFlow is not available
    class SavedModel:
        """Placeholder for SavedModel when TensorFlow is not installed"""
        meta_graphs = []

# List of suspicious TensorFlow operations that could be security risks
SUSPICIOUS_OPS = {
    # File I/O operations
    "ReadFile", "WriteFile", "MergeV2Checkpoints", "Save", "SaveV2",
    # Python execution
    "PyFunc", "PyCall",
    # System operations
    "ShellExecute", "ExecuteOp", "SystemConfig",
    # Other potentially risky operations
    "DecodeRaw", "DecodeJpeg", "DecodePng"
}

class TensorFlowSavedModelScanner(BaseScanner):
    """Scanner for TensorFlow SavedModel format"""
    name = "tf_savedmodel"
    description = "Scans TensorFlow SavedModel for suspicious operations"
    supported_extensions = [".pb", ""]  # Empty string for directories
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        super().__init__(config)
        # Additional scanner-specific configuration
        self.suspicious_ops = set(self.config.get("suspicious_ops", SUSPICIOUS_OPS))
        
    @classmethod
    def can_handle(cls, path: str) -> bool:
        """Check if this scanner can handle the given path"""
        if not HAS_TENSORFLOW:
            return False
            
        if os.path.isfile(path):
            # For single file, check extension
            ext = os.path.splitext(path)[1].lower()
            return ext == ".pb"
        elif os.path.isdir(path):
            # For directory, check if saved_model.pb exists
            return os.path.exists(os.path.join(path, "saved_model.pb"))
        return False
        
    def scan(self, path: str) -> ScanResult:
        """Scan a TensorFlow SavedModel file or directory"""
        # Check if path is valid
        path_check_result = self._check_path(path)
        if path_check_result:
            return path_check_result
        
        # Store the file path for use in issue locations
        self.current_file_path = path
        
        # Check if TensorFlow is installed
        if not HAS_TENSORFLOW:
            result = self._create_result()
            result.add_issue(
                "TensorFlow not installed, cannot scan SavedModel.",
                severity=IssueSeverity.ERROR,
                location=path,
                details={"path": path}
            )
            result.finish(success=False)
            return result
        
        # Determine if path is file or directory
        if os.path.isfile(path):
            return self._scan_saved_model_file(path)
        elif os.path.isdir(path):
            return self._scan_saved_model_directory(path)
        else:
            result = self._create_result()
            result.add_issue(
                f"Path is neither a file nor a directory: {path}",
                severity=IssueSeverity.ERROR,
                location=path,
                details={"path": path}
            )
            result.finish(success=False)
            return result
            
    def _scan_saved_model_file(self, path: str) -> ScanResult:
        """Scan a single SavedModel protobuf file"""
        result = self._create_result()
        file_size = self.get_file_size(path)
        result.metadata["file_size"] = file_size
        
        try:
            with open(path, "rb") as f:
                content = f.read()
                result.bytes_scanned = len(content)
                
                saved_model = SavedModel()
                saved_model.ParseFromString(content)
                
                self._analyze_saved_model(saved_model, result)
                
        except Exception as e:
            result.add_issue(
                f"Error scanning TF SavedModel file: {str(e)}",
                severity=IssueSeverity.ERROR,
                location=path,
                details={"exception": str(e), "exception_type": type(e).__name__}
            )
            result.finish(success=False)
            return result
            
        result.finish(success=True)
        return result
        
    def _scan_saved_model_directory(self, dir_path: str) -> ScanResult:
        """Scan a SavedModel directory"""
        result = self._create_result()
        
        # Look for saved_model.pb in the directory
        saved_model_path = os.path.join(dir_path, "saved_model.pb")
        if not os.path.exists(saved_model_path):
            result.add_issue(
                "No saved_model.pb found in directory.",
                severity=IssueSeverity.ERROR,
                location=dir_path,
                details={"directory": dir_path}
            )
            result.finish(success=False)
            return result
            
        # Scan the saved_model.pb file
        file_scan_result = self._scan_saved_model_file(saved_model_path)
        result.merge(file_scan_result)
        
        # Check for other suspicious files in the directory
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                # Look for potentially suspicious Python files
                if file.endswith('.py'):
                    result.add_issue(
                        f"Found Python file in SavedModel directory: {os.path.join(root, file)}",
                        severity=IssueSeverity.WARNING,
                        location=os.path.join(root, file),
                        details={"file_type": "python"}
                    )
                    
        result.finish(success=True)
        return result
        
    def _analyze_saved_model(self, saved_model: SavedModel, result: ScanResult) -> None:
        """Analyze the saved model for suspicious operations"""
        suspicious_op_found = False
        op_counts: Dict[str, int] = {}
        
        for meta_graph in saved_model.meta_graphs:
            graph_def = meta_graph.graph_def
            
            # Scan all nodes in the graph for suspicious operations
            for node in graph_def.node:
                # Count all operation types
                if node.op in op_counts:
                    op_counts[node.op] += 1
                else:
                    op_counts[node.op] = 1
                    
                # Check if the operation is suspicious
                if node.op in self.suspicious_ops:
                    suspicious_op_found = True
                    result.add_issue(
                        f"Suspicious TensorFlow operation: {node.op}",
                        severity=IssueSeverity.ERROR,
                        location=f"{self.current_file_path} (node: {node.name})",
                        details={
                            "op_type": node.op,
                            "node_name": node.name,
                            "meta_graph": meta_graph.meta_info_def.tags[0] if meta_graph.meta_info_def.tags else "unknown"
                        }
                    )
                    
        # Add operation counts to metadata
        result.metadata["op_counts"] = op_counts
        result.metadata["suspicious_op_found"] = suspicious_op_found
