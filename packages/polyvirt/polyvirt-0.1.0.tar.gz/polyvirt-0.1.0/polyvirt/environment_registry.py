import os
import json
from pathlib import Path
from colored import fg, attr
from tqdm import tqdm

REGISTRY_FILENAME = ".polyvirt_db.json"

class EnvironmentRegistry:
    """
    Maintains a database of known Python virtual environments
    in a JSON file stored by default in the user's home directory.
    """

    def __init__(self, registry_path=None):
        if registry_path is None:
            home_dir = Path.home()
            self._registry_file = home_dir / REGISTRY_FILENAME
        else:
            self._registry_file = Path(registry_path)
        
        self._registry_data = {
            "environments": []
        }

        # Load existing data if present
        if self._registry_file.exists():
            self._load()

    def _load(self):
        try:
            with open(self._registry_file, "r", encoding="utf-8") as f:
                self._registry_data = json.load(f)
        except (json.JSONDecodeError, IOError):
            print(f"{fg('red')}[PolyVirt] Failed to read registry file. Starting fresh...{attr('reset')}")
            self._registry_data = {"environments": []}

    def _save(self):
        try:
            with open(self._registry_file, "w", encoding="utf-8") as f:
                json.dump(self._registry_data, f, indent=2)
        except IOError as e:
            print(f"{fg('red')}[PolyVirt] Error writing to registry: {e}{attr('reset')}")

    def add_environment(self, manager, name, path):
        """
        Add a new environment to the registry, if it doesn't already exist.
        """
        env_path = os.path.abspath(path)
        for env in self._registry_data["environments"]:
            if env["path"] == env_path and env["manager"] == manager:
                print(f"{fg('yellow')}[PolyVirt] Environment already tracked: {env_path}{attr('reset')}")
                return
        
        env_record = {
            "manager": manager,
            "name": name,
            "path": env_path
        }
        self._registry_data["environments"].append(env_record)
        self._save()
        print(f"{fg('green')}[PolyVirt] Environment added to registry: {env_record}{attr('reset')}")

    def remove_environment(self, name):
        """
        Remove an environment from the registry by name.
        Returns True if removed, False if not found.
        """
        found_index = None
        for i, env in enumerate(self._registry_data["environments"]):
            if env["name"] == name:
                found_index = i
                break
        if found_index is not None:
            self._registry_data["environments"].pop(found_index)
            self._save()
            return True
        return False

    def list_environments(self):
        """
        Return a dict grouped by manager for easy display:
        {
          "venv": [ { "name": ..., "path": ... }, ...],
          "conda": [...],
          "virtualenv": [...]
        }
        """
        grouped = {}
        for env in self._registry_data["environments"]:
            mgr = env["manager"]
            if mgr not in grouped:
                grouped[mgr] = []
            grouped[mgr].append({
                "name": env["name"],
                "path": env["path"]
            })
        return grouped

    def find_environment(self, name):
        """
        Find a single environment by name (case-sensitive).
        Returns the environment record or None.
        """
        for env in self._registry_data["environments"]:
            if env["name"] == name:
                return env
        return None

    def scan_filesystem_for_envs(self, start_path="/", max_depth=6):
        """
        Scan filesystem starting at `start_path` for directories that appear 
        to be Python virtual environments. This is naive and can be time-consuming 
        on large file systems.

        :param start_path: Where to start scanning (default '/')
        :param max_depth: Limit search depth for performance.
        :return: A list of discovered environment info (not yet in the registry).
        """
        discovered = []
        start_path = os.path.abspath(start_path)
        print(f"{fg('blue')}[PolyVirt] Scanning {start_path} up to depth {max_depth}...{attr('reset')}")

        def depth(path):
            return len(Path(path).resolve().parts) - len(Path(start_path).resolve().parts)

        for root, dirs, files in tqdm(os.walk(start_path), desc="Scanning", unit="dirs"):
            if depth(root) > max_depth:
                dirs[:] = []
                continue
            
            # Check for common markers:
            # venv/virtualenv marker => "pyvenv.cfg"
            # conda marker => "conda-meta" directory
            env_info = None
            if "pyvenv.cfg" in files:
                env_info = {
                    "manager": "venv_or_virtualenv",
                    "name": os.path.basename(root),
                    "path": root
                }
            elif "conda-meta" in dirs:
                env_info = {
                    "manager": "conda",
                    "name": os.path.basename(root),
                    "path": root
                }
            
            if env_info:
                already_tracked = any(
                    env["path"] == env_info["path"] for env in self._registry_data["environments"]
                )
                if not already_tracked:
                    discovered.append(env_info)

        if discovered:
            print(f"{fg('green')}[PolyVirt] Discovered {len(discovered)} untracked env(s).{attr('reset')}")
        else:
            print(f"{fg('yellow')}[PolyVirt] No untracked environments found in this scan.{attr('reset')}")

        return discovered

    def add_discovered_envs(self, discovered_envs):
        """
        Add a list of discovered envs from a scan into the registry, ignoring duplicates.
        """
        for env in discovered_envs:
            self.add_environment(env["manager"], env["name"], env["path"])

