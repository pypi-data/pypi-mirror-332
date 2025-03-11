#!/usr/bin/env python
"""
Script to generate TypeScript types from Pydantic models.
This script will generate TypeScript interfaces from Pydantic models used in the OpenAgents JSON project.
"""

import os
import sys
import subprocess
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Define paths
ROOT_DIR = Path(__file__).parent.parent
WORKFLOW_MODELS_PATH = ROOT_DIR / "openagents_json" / "workflow" / "models.py"
VALIDATOR_BASE_PATH = ROOT_DIR / "openagents_json" / "workflow" / "validator" / "base.py"
UI_TYPES_DIR = ROOT_DIR / "openagents_json" / "ui" / "src" / "types" / "generated"

# Type generation targets
TARGETS = [
    {
        "input": WORKFLOW_MODELS_PATH,
        "output": UI_TYPES_DIR / "workflow.ts",
        "description": "Workflow models"
    },
    {
        "input": VALIDATOR_BASE_PATH,
        "output": UI_TYPES_DIR / "validation.ts",
        "description": "Validation models"
    }
]

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import datamodel_code_generator
        logger.info("datamodel-code-generator is installed.")
    except ImportError:
        logger.error("datamodel-code-generator is not installed. Please install it with: pip install datamodel-code-generator")
        sys.exit(1)

def ensure_output_dir():
    """Ensure the output directory exists."""
    os.makedirs(UI_TYPES_DIR, exist_ok=True)
    logger.info(f"Ensured output directory exists: {UI_TYPES_DIR}")

def generate_types():
    """Generate TypeScript types from Pydantic models."""
    check_dependencies()
    ensure_output_dir()
    
    success = True
    for target in TARGETS:
        input_path = target["input"]
        output_path = target["output"]
        description = target["description"]
        
        if not input_path.exists():
            logger.error(f"Input file not found: {input_path}")
            success = False
            continue
            
        logger.info(f"Generating TypeScript types for {description}...")
        cmd = [
            "datamodel-codegen",
            "--input", str(input_path),
            "--output", str(output_path),
            "--target-python-version", "3.9",
            "--output-model-type", "typescript"
        ]
        
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            logger.info(f"Successfully generated types for {description}: {output_path}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Error generating types for {description}:")
            logger.error(f"Command: {' '.join(cmd)}")
            logger.error(f"Error: {e.stderr}")
            success = False
    
    return success

def validate_generated_types():
    """Validate that all expected TypeScript type files exist."""
    missing_files = []
    for target in TARGETS:
        output_path = target["output"]
        if not output_path.exists():
            missing_files.append(output_path)
    
    if missing_files:
        logger.error("The following type files were not generated:")
        for file in missing_files:
            logger.error(f"  - {file}")
        return False
    
    logger.info("All type files were successfully generated.")
    return True

def main():
    """Main function."""
    logger.info("Starting TypeScript type generation from Pydantic models...")
    
    if not generate_types():
        logger.error("Type generation failed.")
        sys.exit(1)
        
    if not validate_generated_types():
        logger.error("Type validation failed.")
        sys.exit(1)
        
    logger.info("TypeScript type generation completed successfully.")

if __name__ == "__main__":
    main() 