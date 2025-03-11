import argparse
import sys
import shutil
from colored import fg, attr

from polyvirt.environment_registry import EnvironmentRegistry
from polyvirt.managers.venv_manager import VenvManager
from polyvirt.managers.conda_manager import CondaManager
from polyvirt.managers.virtualenv_manager import VirtualenvManager
from polyvirt.utils import print_activation_instructions


def main():
    parser = argparse.ArgumentParser(
        description="PolyVirt: Manage and track Python virtual environments.",
        epilog="""
Examples:
  1) Create a new venv environment:
     polyvirt create --manager venv --name myenv --path /home/user/myenv

  2) Create a conda environment:
     polyvirt create --manager conda --name condaenv --path /home/user/condaenv

  3) List all tracked environments:
     polyvirt list

  4) Scan filesystem for untracked environments:
     polyvirt scan --start /home/user --max-depth 4

  5) Show activation instructions for an environment:
     polyvirt activate --name myenv

  6) Remove environment from registry only:
     polyvirt remove --name myenv

  7) Remove environment from registry AND delete it from disk:
     polyvirt remove --name myenv --purge

"""
    )
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # create sub-command
    create_parser = subparsers.add_parser("create", help="Create a new environment.")
    create_parser.add_argument(
        "--manager", 
        choices=["venv", "conda", "virtualenv"], 
        required=True,
        help="Which environment manager to use (venv, conda, or virtualenv)."
    )
    create_parser.add_argument(
        "--name", 
        required=True,
        help="A name/identifier for the environment."
    )
    create_parser.add_argument(
        "--path",
        required=True,
        help="The directory path where the environment will be created."
    )

    # list sub-command
    list_parser = subparsers.add_parser("list", help="List tracked environments.")

    # scan sub-command
    scan_parser = subparsers.add_parser("scan", help="Scan filesystem for untracked environments.")
    scan_parser.add_argument(
        "--start", 
        default="/", 
        help="Filesystem path to start scanning (default '/')."
    )
    scan_parser.add_argument(
        "--max-depth", 
        type=int, 
        default=6, 
        help="Maximum depth to recurse (default 6)."
    )

    # activate sub-command
    activate_parser = subparsers.add_parser("activate", help="Show activation instructions for an environment.")
    activate_parser.add_argument(
        "--name",
        required=True,
        help="The name of the environment to activate."
    )

    # remove sub-command
    remove_parser = subparsers.add_parser("remove", help="Remove an environment from registry (and optionally disk).")
    remove_parser.add_argument(
        "--name",
        required=True,
        help="The name of the environment to remove."
    )
    remove_parser.add_argument(
        "--purge",
        action="store_true",
        help="If set, also delete the environment folder from disk."
    )

    args = parser.parse_args()
    registry = EnvironmentRegistry()

    if args.command == "create":
        handle_create(args, registry)
    elif args.command == "list":
        handle_list(registry)
    elif args.command == "scan":
        handle_scan(args, registry)
    elif args.command == "activate":
        handle_activate(args, registry)
    elif args.command == "remove":
        handle_remove(args, registry)
    else:
        parser.print_help()


def handle_create(args, registry):
    manager_type = args.manager
    env_name = args.name
    env_path = args.path

    # Instantiate the appropriate manager class
    if manager_type == "venv":
        manager = VenvManager()
    elif manager_type == "conda":
        manager = CondaManager()
    elif manager_type == "virtualenv":
        manager = VirtualenvManager()
    else:
        print(f"{fg('red')}[PolyVirt] Unsupported manager: {manager_type}{attr('reset')}")
        sys.exit(1)

    # Check if the chosen manager is actually available on this system
    if not manager.is_available():
        print(f"{fg('red')}[PolyVirt] The '{manager_type}' manager is not available on this system.{attr('reset')}")
        sys.exit(1)

    print(f"{fg('green')}[PolyVirt] Creating environment '{env_name}' using {manager_type} at {env_path}...{attr('reset')}")
    manager.create_environment(env_name, env_path)

    # Add to registry
    registry.add_environment(manager_type, env_name, env_path)


def handle_list(registry):
    grouped = registry.list_environments()
    if not grouped:
        print(f"{fg('yellow')}[PolyVirt] No environments found in registry.{attr('reset')}")
        return

    print(f"{fg('blue')}[PolyVirt] Environments in registry (grouped by manager):{attr('reset')}")
    for manager, envs in grouped.items():
        print(f"  {fg('green')}{manager}:{attr('reset')}")
        for env in envs:
            print(f"    - {env['name']} => {env['path']}")


def handle_scan(args, registry):
    discovered = registry.scan_filesystem_for_envs(
        start_path=args.start,
        max_depth=args.max_depth
    )
    if discovered:
        print(f"{fg('blue')}[PolyVirt] Adding discovered envs to registry...{attr('reset')}")
        registry.add_discovered_envs(discovered)


def handle_activate(args, registry):
    env_name = args.name
    env = registry.find_environment(env_name)
    if not env:
        print(f"{fg('red')}[PolyVirt] Environment '{env_name}' not found in registry.{attr('reset')}")
        sys.exit(1)
    print_activation_instructions(env)


def handle_remove(args, registry):
    env_name = args.name
    to_purge = args.purge

    env = registry.find_environment(env_name)
    if not env:
        print(f"{fg('red')}[PolyVirt] Environment '{env_name}' not found in registry.{attr('reset')}")
        sys.exit(1)

    # First remove from registry
    removed = registry.remove_environment(env_name)
    if removed:
        print(f"{fg('green')}[PolyVirt] Removed '{env_name}' from registry.{attr('reset')}")
    else:
        print(f"{fg('yellow')}[PolyVirt] Could not remove '{env_name}' from registry (not found).{attr('reset')}")

    # If purge is requested, remove from disk
    if to_purge:
        env_path = env["path"]
        try:
            shutil.rmtree(env_path)
            print(f"{fg('green')}[PolyVirt] Deleted environment folder from disk: {env_path}{attr('reset')}")
        except FileNotFoundError:
            print(f"{fg('yellow')}[PolyVirt] Environment folder not found on disk: {env_path}{attr('reset')}")
        except PermissionError:
            print(f"{fg('red')}[PolyVirt] Permission denied while deleting {env_path}{attr('reset')}")
        except Exception as e:
            print(f"{fg('red')}[PolyVirt] Error deleting {env_path}: {e}{attr('reset')}")

