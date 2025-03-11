import os
import platform
import pathlib

def get_private_key_path():
    """
    Detects the runtime environment and returns the appropriate private key path.
    """
    # Detect if running in a Docker container
    in_docker = False
    if os.path.exists("/proc/self/cgroup"):
        with open("/proc/self/cgroup", "r") as f:
            in_docker = any("docker" in line or "kubepod" in line for line in f)

    # Check the OS type
    os_name = platform.system()

    # Use your custom key filename
    key_filename = "vastai"

    # Determine the path based on environment
    if in_docker:
        private_key_path = f"/root/.ssh/{key_filename}"
    elif os_name == "Darwin":  # macOS
        print("macOS detected.")
        private_key_path = str(pathlib.Path.home() / ".ssh" / key_filename)
    else:
        private_key_path = str(pathlib.Path.home() / ".ssh" / key_filename)

    return private_key_path



# Example usage in your script
PRIVATE_KEY_PATH = get_private_key_path()