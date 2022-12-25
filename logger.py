import sys

def warn(message):
    print(f"WARNING: {message}")

def fatal(message):
    print(f"FATAL: {message}")
    sys.exit(1)