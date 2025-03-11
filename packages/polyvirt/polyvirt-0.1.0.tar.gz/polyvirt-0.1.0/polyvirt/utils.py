import os
from colored import fg, attr

def get_activation_command(env_path, manager):
    """
    Return a shell-appropriate command for activating a given environment.
    This is a best-effort approach; real activation can differ by shell and OS.
    """
    if os.name == "nt":
        # Windows
        if manager == "conda":
            return f"conda activate {env_path}"
        else:
            return f"{env_path}\\Scripts\\activate.bat"
    else:
        # Unix-like
        if manager == "conda":
            return f"conda activate {env_path}"
        else:
            return f"source {env_path}/bin/activate"

def print_activation_instructions(env_record):
    manager = env_record["manager"]
    env_path = env_record["path"]
    command = get_activation_command(env_path, manager)
    print(f"{fg('green')}To activate '{env_record['name']}' ({manager}), run:\n  {command}{attr('reset')}")

