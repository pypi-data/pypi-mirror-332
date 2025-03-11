import sys
from importlib.metadata import version

def check_command():
    if sys.argv[1] in ("--version", "version", "-V"):
        output = f"macun-{get_version()}"

    elif sys.argv[1] in ("--help", "help", "-H"):
        output = show_help()
        
    else: return None
    return output

def get_version(): # macun --version
    try: return version("macun")
    except: return "Unknown"



def show_help(): #macun --help 
    return """usage: macun <command>

commands:

--version, version, -V
    displays current macun version

--help, help, -H
    display commands

Any terminal command
    runs the command with macun
"""
