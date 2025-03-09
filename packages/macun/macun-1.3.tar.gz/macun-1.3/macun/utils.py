import sys

try: import tomllib as toml # 3.11+
except ImportError: import toml #<3.11 #type:ignore

def check_command():
    if sys.argv[1] in ("--version", "version", "-V"):
        output = f"macun-{get_version()}"

        
    else: return None
    return output

def get_version(): # macun --version
    with open("pyproject.toml","rb") as f:
        config = toml.load(f)
    return config["project"]["version"]