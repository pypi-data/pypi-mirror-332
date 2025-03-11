"""
Basic tests for the testing utilities that don't depend on OpenAgentsApp.

These tests verify that the basic testing utilities work correctly.
"""

import pytest

from tests.utils.helpers import assert_json_structure, compare_dict_paths
from tests.utils.mocks import MockAgentClient, MockJobCallback


def test_assert_json_structure():
    """Test the assert_json_structure helper function."""
    # Test with matching structures
    actual = {"id": "test", "nested": {"key": "value"}, "list": [1, 2, 3]}

    expected = {"id": "any_string", "nested": {"key": "any_string"}, "list": []}

    # This should not raise an exception
    assert_json_structure(actual, expected)

    # Test with missing key
    try:
        assert_json_structure({"id": "test"}, {"id": "test", "missing": "value"})
        assert False, "Should have raised an AssertionError"
    except AssertionError:
        pass


def test_compare_dict_paths():
    """Test the compare_dict_paths helper function."""
    dict1 = {"a": {"b": {"c": "value1"}}, "x": "y"}

    dict2 = {"a": {"b": {"c": "value1"}}, "x": "z"}

    # Test matching paths
    assert compare_dict_paths(dict1, dict2, ["a.b.c"])

    # Test non-matching paths
    assert not compare_dict_paths(dict1, dict2, ["x"])

    # Test multiple paths
    assert not compare_dict_paths(dict1, dict2, ["a.b.c", "x"])


@pytest.mark.asyncio
async def test_mock_agent_client():
    """Test the MockAgentClient class."""
    client = MockAgentClient(
        {"hello": "Hello, world!", "weather": "The weather is sunny today."}
    )

    # Test a matching pattern
    response = await client.call("Tell me hello")
    assert response == "Hello, world!"

    # Test another matching pattern
    response = await client.call("What's the weather like?")
    assert response == "The weather is sunny today."

    # Test a non-matching pattern
    response = await client.call("Something else")
    assert "Mock response to:" in response

    # Verify call count
    assert client.get_call_count() == 3

    # Test adding a response
    client.add_response("new", "New response")
    response = await client.call("This is new")
    assert response == "New response"

    # Test reset
    client.reset()
    assert client.get_call_count() == 0


@pytest.mark.asyncio
async def test_mock_job_callback():
    """Test the MockJobCallback class."""
    callback = MockJobCallback()

    # Simulate job lifecycle events
    await callback.on_status_change("job-123", "QUEUED")
    await callback.on_status_change("job-123", "RUNNING")
    await callback.on_progress("job-123", 0.5, "Halfway done")
    await callback.on_status_change("job-123", "COMPLETED")

    # Check the recorded events
    events = callback.get_events()
    assert len(events) == 4

    # Check specific event types
    status_events = callback.get_events("status_change")
    assert len(status_events) == 3

    progress_events = callback.get_events("progress")
    assert len(progress_events) == 1
    assert progress_events[0]["progress"] == 0.5

    # Test reset
    callback.reset()
    assert len(callback.get_events()) == 0
