"""
Script to register example workflows with the OpenAgents application.

This script can be run to preload example workflows into the registry.
"""

import asyncio
import logging
from typing import Any, Dict, List

from openagents_json.core.app import OpenAgentsApp
from openagents_json.workflow.examples.simple_workflow import simple_workflow

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def register_examples(app: OpenAgentsApp) -> List[Dict[str, Any]]:
    """
    Register example workflows with the application.

    Args:
        app: OpenAgentsApp instance

    Returns:
        List of registered workflow IDs
    """
    registered = []

    # Register simple workflow
    logger.info(f"Registering simple workflow: {simple_workflow['id']}")
    if app.register_workflow(simple_workflow):
        registered.append(simple_workflow)
        logger.info(f"Successfully registered workflow: {simple_workflow['id']}")
    else:
        logger.error(f"Failed to register workflow: {simple_workflow['id']}")

    # Add more example workflows here as needed

    return registered


async def main():
    """Main entry point for the script."""
    # Create a new OpenAgentsApp instance
    app = OpenAgentsApp()

    # Register example workflows
    registered = await register_examples(app)

    # Print summary
    logger.info(f"Registered {len(registered)} example workflows")
    for workflow in registered:
        logger.info(f"  - {workflow['id']}: {workflow['name']}")


if __name__ == "__main__":
    asyncio.run(main())
