import subprocess
from abc import ABC, abstractmethod

class BaseManager(ABC):
    """
    Abstract base class for environment managers.
    """

    @abstractmethod
    def create_environment(self, env_name, env_path):
        """
        Create a new environment in env_path with the given name.
        """
        pass

    def is_available(self):
        """
        Check if this environment manager is available on the current system.
        Subclasses should override this if they need a specific check.
        """
        return True

    def run_command(self, cmd):
        """
        Convenience method to run shell commands and return output/status.
        """
        print(f"[Manager] Running command: {cmd}")
        try:
            result = subprocess.run(
                cmd, shell=True, check=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            return result.stdout.decode().strip()
        except subprocess.CalledProcessError as e:
            print(f"[Manager] Error: {e.stderr.decode().strip()}")
            return None

