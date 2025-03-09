#!/usr/bin/env python3
"""
Script for publishing the package to PyPI.
This script builds the package and uploads it to PyPI.
"""

import os
import subprocess
import sys
from typing import List

def run_command(cmd: List[str]) -> None:
    """Run a command and exit if it fails."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, check=False)
    if result.returncode != 0:
        print(f"Command failed with exit code {result.returncode}")
        sys.exit(result.returncode)

def main() -> None:
    """Main entry point."""
    # Ensure we're in the right directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print("Starting package publishing process...")
    
    # Clean build artifacts
    print("Cleaning previous build artifacts...")
    for directory in ["build", "dist", "ollama_toolkit.egg-info"]:
        if os.path.exists(directory):
            run_command(["rm", "-rf", directory])
    
    # Run tests
    print("Running tests...")
    run_command(["python", "-m", "pytest", "tests"])  # Updated path
    
    # Build the package
    print("Building the package...")
    run_command(["python", "-m", "build"])
    
    # Upload to PyPI
    print("Uploading to PyPI...")
    run_command(["python", "-m", "twine", "upload", "dist/*"])
    
    print("Package published successfully!")

if __name__ == "__main__":
    main()
