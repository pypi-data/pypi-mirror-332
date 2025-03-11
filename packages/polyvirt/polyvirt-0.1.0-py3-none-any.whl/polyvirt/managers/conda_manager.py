import os
import shutil
from .base_manager import BaseManager

class CondaManager(BaseManager):
    def create_environment(self, env_name, env_path):
        """
        Creates a conda environment with the given name in env_path.
        """
        os.makedirs(env_path, exist_ok=True)
        cmd = f"conda create --yes --prefix \"{env_path}\" python=3.9"
        self.run_command(cmd)

    def is_available(self):
        # Check if 'conda' is on PATH
        return shutil.which("conda") is not None

