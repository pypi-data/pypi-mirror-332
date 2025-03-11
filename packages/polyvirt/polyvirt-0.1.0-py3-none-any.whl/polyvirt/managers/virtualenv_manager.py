import os
import shutil
from .base_manager import BaseManager

class VirtualenvManager(BaseManager):
    def create_environment(self, env_name, env_path):
        """
        Creates a virtual environment with `virtualenv`.
        """
        os.makedirs(env_path, exist_ok=True)
        cmd = f"virtualenv \"{env_path}\""
        self.run_command(cmd)

    def is_available(self):
        # Check if 'virtualenv' is on PATH
        return shutil.which("virtualenv") is not None

