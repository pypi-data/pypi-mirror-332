import os
import sys
import subprocess
from .base_manager import BaseManager

class VenvManager(BaseManager):
    def create_environment(self, env_name, env_path):
        """
        Creates a virtual environment using the built-in venv module.
        """
        os.makedirs(env_path, exist_ok=True)
        python_exec = sys.executable  # The current Python interpreter
        cmd = f"{python_exec} -m venv \"{env_path}\""
        self.run_command(cmd)

    def is_available(self):
        # We'll do a quick check if `python -m venv --help` runs successfully.
        python_exec = sys.executable
        test_cmd = f"{python_exec} -m venv --help"
        try:
            subprocess.run(
                test_cmd, shell=True, check=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            return True
        except subprocess.CalledProcessError:
            return False

