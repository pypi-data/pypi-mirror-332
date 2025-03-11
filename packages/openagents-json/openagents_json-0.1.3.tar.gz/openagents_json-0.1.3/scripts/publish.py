#!/usr/bin/env python3
"""
Build and publish the package to PyPI.

Usage:
    python scripts/publish.py [--test] [--dry-run]

Options:
    --test     Publish to TestPyPI instead of PyPI
    --dry-run  Build the package but don't publish it
"""

import os
import subprocess
import sys
from pathlib import Path

# Get the project root directory
ROOT_DIR = Path(__file__).parent.parent.absolute()


def clean_build_dirs():
    """Clean build directories."""
    print("Cleaning build directories...")
    dirs_to_clean = [
        ROOT_DIR / "dist",
        ROOT_DIR / "build",
        ROOT_DIR / "openagents_json.egg-info",
    ]
    
    for dir_path in dirs_to_clean:
        if dir_path.exists():
            print(f"Removing {dir_path}")
            subprocess.run(["rm", "-rf", str(dir_path)], check=True)


def build_package():
    """Build the package."""
    print("Building package...")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--upgrade", "build", "twine"],
        check=True,
    )
    subprocess.run([sys.executable, "-m", "build"], cwd=ROOT_DIR, check=True)


def publish_package(test=False):
    """Publish the package to PyPI or TestPyPI."""
    if test:
        print("Publishing to TestPyPI...")
        repo_url = "https://test.pypi.org/legacy/"
    else:
        print("Publishing to PyPI...")
        repo_url = "https://upload.pypi.org/legacy/"

    subprocess.run(
        [
            sys.executable,
            "-m",
            "twine",
            "upload",
            "--repository-url",
            repo_url,
            "dist/*",
        ],
        cwd=ROOT_DIR,
        check=True,
    )


def main():
    """Main function."""
    test_mode = "--test" in sys.argv
    dry_run = "--dry-run" in sys.argv
    
    # Ensure we're in a clean state
    clean_build_dirs()
    
    # Build the package
    build_package()
    
    # Publish the package if not in dry-run mode
    if not dry_run:
        publish_package(test=test_mode)
        print("Package published successfully!")
    else:
        print("Dry run completed. Package built but not published.")
    
    print("Done!")


if __name__ == "__main__":
    main()