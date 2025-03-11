#!/usr/bin/env python
"""
Script to set up Git hooks for the OpenAgents JSON project.
"""

import os
import sys
import shutil
import logging
import subprocess
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Define paths
ROOT_DIR = Path(__file__).parent.parent
HOOKS_DIR = ROOT_DIR / ".git" / "hooks"
PRE_COMMIT_HOOK = HOOKS_DIR / "pre-commit"

# Pre-commit hook content
PRE_COMMIT_CONTENT = """#!/bin/bash
# Pre-commit hook to generate TypeScript types from Pydantic models

set -e

# Get the root directory of the repository
ROOT_DIR=$(git rev-parse --show-toplevel)

# Check if datamodel-code-generator is installed
if ! pip show datamodel-code-generator > /dev/null 2>&1; then
  echo "Error: datamodel-code-generator is not installed."
  echo "Please install it with: pip install datamodel-code-generator"
  exit 1
fi

# Run the type generation script
echo "Running TypeScript type generation..."
python "$ROOT_DIR/scripts/generate_types.py"

# Check if there are any changes to the generated types
if git diff --name-only | grep -q "openagents_json/ui/src/types/generated"; then
  echo "Warning: Generated TypeScript types have changed."
  echo "Please review and add the changes to your commit."
  echo "You may need to run: git add openagents_json/ui/src/types/generated/*.ts"
  exit 1
fi

echo "TypeScript type generation check passed."
exit 0
"""

def setup_pre_commit_hook():
    """Set up the pre-commit hook."""
    logger.info("Setting up pre-commit hook...")
    
    if not HOOKS_DIR.exists():
        logger.error(f"Git hooks directory not found: {HOOKS_DIR}")
        logger.error("Are you in a git repository?")
        return False
    
    with open(PRE_COMMIT_HOOK, "w") as f:
        f.write(PRE_COMMIT_CONTENT)
    
    # Make the hook executable
    os.chmod(PRE_COMMIT_HOOK, 0o755)
    logger.info(f"Pre-commit hook installed at: {PRE_COMMIT_HOOK}")
    return True

def install_dependencies():
    """Install required dependencies."""
    logger.info("Installing datamodel-code-generator...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "datamodel-code-generator"],
            check=True,
            capture_output=True,
            text=True
        )
        logger.info("Successfully installed datamodel-code-generator")
        return True
    except subprocess.CalledProcessError as e:
        logger.error("Failed to install datamodel-code-generator:")
        logger.error(e.stderr)
        return False

def main():
    """Main function."""
    logger.info("Setting up Git hooks for OpenAgents JSON project...")
    
    if not install_dependencies():
        logger.error("Failed to install dependencies. Aborting.")
        sys.exit(1)
    
    if not setup_pre_commit_hook():
        logger.error("Failed to set up pre-commit hook. Aborting.")
        sys.exit(1)
    
    logger.info("Git hooks setup completed successfully.")

if __name__ == "__main__":
    main() 