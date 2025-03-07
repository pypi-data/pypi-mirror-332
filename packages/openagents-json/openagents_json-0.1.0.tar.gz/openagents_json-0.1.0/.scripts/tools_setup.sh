#!/bin/bash
# Script to set up the environment for the project

# Set the script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Load environment variables from .env.scripts
if [ -f "$SCRIPT_DIR/.env.scripts" ]; then
    echo "Loading environment variables from .env.scripts..."
    set -a
    source "$SCRIPT_DIR/.env.scripts"
    set +a
else
    echo "Warning: .env.scripts file not found. Using default environment variables."
    if [ -f "$SCRIPT_DIR/.env.scripts.example" ]; then
        echo "Consider copying .env.scripts.example to .env.scripts and updating the values."
    fi
fi

# Create virtual environment if it doesn't exist
VENV_DIR="$PROJECT_ROOT/.venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists in $VENV_DIR"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Install requirements
REQUIREMENTS_FILE="$SCRIPT_DIR/requirements.agents.txt"
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing requirements from $REQUIREMENTS_FILE..."
    pip install -r "$REQUIREMENTS_FILE"
else
    echo "Error: Requirements file not found at $REQUIREMENTS_FILE"
    exit 1
fi

echo "Setup complete! Virtual environment is activated and requirements are installed."
echo "To deactivate the virtual environment, run 'deactivate'"
