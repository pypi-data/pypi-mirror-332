import functools
from colored import fg, attr

def current_env_info(func):
    """
    A custom decorator that prints environment usage info
    before running the decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Example: If we tracked the currently active environment, we could show it here.
        # For demo, just prints a line indicating an environment might be active.
        print(f"{fg('blue')}[PolyVirt] Currently using environment (if any is active)...{attr('reset')}")
        return func(*args, **kwargs)
    return wrapper

