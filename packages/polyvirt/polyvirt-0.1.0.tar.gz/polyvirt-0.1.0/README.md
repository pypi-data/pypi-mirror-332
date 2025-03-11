# PolyVirt

**PolyVirt** is a Python CLI tool to create, track, and manage virtual environments across different environment managers (such as `venv`, `virtualenv`, and `conda`). It maintains a simple JSON-based registry and can optionally search your filesystem for untracked environments. It also allows for removing environments from the registry or completely deleting them from disk.

## Features

1. **Create a Virtual Environment**  
   - Choose the manager (`venv`, `virtualenv`, or `conda`).  
   - Specify the environment name and location.  
   - PolyVirt automatically records it in its registry.

2. **List and Search**  
   - Lists all tracked environments, grouped by manager.  
   - Offers a filesystem scan mode to find untracked environments.

3. **Activate and Switch**  
   - You can select/activate a virtual environment from your tracked list.  
   - On Unix-like shells, you’ll see instructions for `source path/bin/activate`; on Windows, instructions for `path\Scripts\activate.bat`.

4. **Remove Environments**  
   - Remove environments from the registry only, or remove them from disk entirely (`--purge`).

5. **Automatic Manager Detection**  
   - If a selected manager (`venv`, `virtualenv`, `conda`) is not available, PolyVirt will exit gracefully with an informative message.

6. **Custom Decorators**  
   - Demonstrates usage of decorators (`decorators.py`) to display environment usage info.

7. **Future GUI**  
   - Currently, PolyVirt is a CLI tool (via `argparse`). A future GUI can be built on top of the same modules.

## Requirements

- Python 3.7+  
- `colored`  
- `tqdm`

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Installation

Install PolyVirt locally in editable mode:
```bash
cd polyvirt
pip install -e .
```

To install from PyPI (after it is published):
```bash
pip install polyvirt
```

Run it:
```bash
polyvirt --help
```

## Usage

### Create a new environment
```bash
polyvirt create --manager venv --name myenv --path /home/user/myenv
```

### Create a Conda environment
```bash
polyvirt create --manager conda --name condaenv --path /home/user/condaenv
```

### List tracked environments
```bash
polyvirt list
```

### Scan filesystem for untracked environments
```bash
polyvirt scan --start /home/user --max-depth 4
```

### Show activation instructions for an environment
```bash
polyvirt activate --name myenv
```

### Remove environment from registry only
```bash
polyvirt remove --name myenv
```

### Remove environment from registry AND delete from disk
```bash
polyvirt remove --name myenv --purge
```

## License

PolyVirt is licensed under the **MIT License**. See `LICENSE` for details.

---
