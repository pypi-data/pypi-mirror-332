import importlib
import ctypes
import os
import sys

class ProtocolLibrary:
    def __init__(self, so_file_path: str, protocol_name: str):
        self.so_file_path = so_file_path
        self.protocol_name = protocol_name.lower()

        # Add the parent directory of 'silent_compute' to sys.path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.insert(0, base_dir)

        # Dynamically import the correct protocol module
        try:
            module_name = f"silent_compute.sil_compute.{self.protocol_name}"
            self.protocol_module = importlib.import_module(module_name)
        except ModuleNotFoundError as e:
            raise ValueError(f"Unsupported protocol: {self.protocol_name}. Error: {e}")

        # Load the shared library into the protocol module with error handling
        try:
            if not os.path.isfile(self.so_file_path):
                raise FileNotFoundError(f"Shared library file not found: {self.so_file_path}")

            self.lib = ctypes.CDLL(self.so_file_path)
            self.protocol_module.load_shared_library(self.lib)
        except OSError as e:
            raise ValueError(f"Failed to load shared library: {self.so_file_path}. "
                             f"Ensure the file is a valid .so binary. Error: {e}")

    def __getattr__(self, name: str):
        """Delegate function calls to the protocol module."""
        if hasattr(self.protocol_module, name):
            return getattr(self.protocol_module, name)
        raise AttributeError(f"'{self.protocol_name}' protocol has no method '{name}'")


def load(so_file_path: str, protocol_name: str) -> ProtocolLibrary:
    """Factory function to load the protocol library."""
    return ProtocolLibrary(so_file_path, protocol_name)
