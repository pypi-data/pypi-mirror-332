"""
Test helper functions for OpenAgents JSON.

This module provides utility functions that make it easier to test
various aspects of the OpenAgents JSON framework.
"""

import asyncio
import time
from typing import Any, Callable, Dict, List, Optional, Union


def assert_json_structure(
    actual: Dict[str, Any], expected: Dict[str, Any], path: str = "$"
):
    """
    Assert that the actual JSON structure contains all the keys and value types
    expected in the expected structure.

    Args:
        actual: The actual JSON structure to check
        expected: The expected structure to compare against
        path: The current path in the JSON structure (for error reporting)
    """
    # Check type match at the current level
    assert isinstance(
        actual, type(expected)
    ), f"Type mismatch at {path}: expected {type(expected)}, got {type(actual)}"

    # If this is a dict, check keys recursively
    if isinstance(expected, dict):
        for key, expected_value in expected.items():
            assert key in actual, f"Missing key '{key}' at {path}"
            assert_json_structure(actual[key], expected_value, f"{path}.{key}")


def compare_dict_paths(
    dict1: Dict[str, Any], dict2: Dict[str, Any], paths: List[str]
) -> bool:
    """
    Compare specific paths in two dictionaries.

    Args:
        dict1: The first dictionary
        dict2: The second dictionary
        paths: A list of dot-separated paths to compare

    Returns:
        True if all paths match, False otherwise
    """
    for path in paths:
        keys = path.split(".")
        val1 = dict1
        val2 = dict2

        try:
            for key in keys:
                val1 = val1[key]
                val2 = val2[key]

            if val1 != val2:
                return False

        except (KeyError, TypeError):
            return False

    return True


async def wait_for_job_completion(job_manager, job_id, timeout=10, check_interval=0.1):
    """
    Wait for a job to complete or until a timeout is reached.

    Args:
        job_manager: The job manager instance
        job_id: The ID of the job to wait for
        timeout: Maximum time to wait in seconds
        check_interval: How often to check job status in seconds

    Returns:
        The final job status
    """
    start_time = time.time()
    while True:
        status = await job_manager.get_job_status(job_id)

        if status.state in ["COMPLETED", "FAILED", "CANCELLED"]:
            return status

        if time.time() - start_time > timeout:
            raise TimeoutError(
                f"Job {job_id} did not complete within {timeout} seconds"
            )

        await asyncio.sleep(check_interval)


def create_test_workflow(
    workflow_id: str = "test_workflow",
    description: str = "Test workflow for testing",
    steps: Optional[List[Dict[str, Any]]] = None,
    output: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Create a test workflow definition with sensible defaults.

    Args:
        workflow_id: ID for the workflow
        description: Description of the workflow
        steps: List of step definitions (defaults to a simple one-step workflow)
        output: Output mapping (defaults to the output of the first step)

    Returns:
        A complete workflow definition dictionary
    """
    if steps is None:
        steps = [
            {
                "id": "step1",
                "component": "test_agent.echo",
                "inputs": {"text": "{{input.text}}"},
            }
        ]

    if output is None:
        output = {"result": "{{step1.output}}"}

    return {
        "id": workflow_id,
        "description": description,
        "steps": steps,
        "output": output,
    }


def create_test_agent(app, agent_id: str = "test_agent") -> None:
    """
    Register a test agent with the provided OpenAgentsApp instance.

    Args:
        app: The OpenAgentsApp instance
        agent_id: ID for the agent
    """

    @app.agent(agent_id, description=f"Test agent '{agent_id}'")
    class TestAgent:
        def __init__(self, config=None):
            self.config = config or {}

        @app.capability("echo", description="Echo the input")
        async def echo(self, text: str) -> str:
            return text

        @app.capability("reverse", description="Reverse the input")
        async def reverse(self, text: str) -> str:
            return text[::-1]

        @app.capability("transform", description="Apply a transformation")
        async def transform(self, text: str, transform_fn: Callable[[str], str]) -> str:
            return transform_fn(text)
