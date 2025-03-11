from setuptools import setup
import os
import re
from pathlib import Path


# Read version from VERSION file
base_dir = os.path.dirname(os.path.abspath(__file__))
version_path = os.path.join(base_dir, "VERSION")
try:
    with open(version_path) as version_file:
        version = version_file.read().strip()
except FileNotFoundError:  # can't find VERSION when building in isolated environment?
    expr = re.compile(r"tspmetrics-(\d+\.\d+(\.\d+)?)")
    vmatch = expr.match(Path(base_dir).name)
    if vmatch:
        version = vmatch.group(1)
    else:
        version = "0.0.0"

# Write version to __meta__.py (if needed)
meta_path = os.path.join(base_dir, "tspmetrics", "__meta__.py")
with open(meta_path, "w") as meta_file:
    data = (
f'''# Automatically created. Please do not edit.
__version__ = '{version}'
__author__ = 'Nick Brown'
'''
    )
    meta_file.write(data)

# Call the setup function
setup(version=version)