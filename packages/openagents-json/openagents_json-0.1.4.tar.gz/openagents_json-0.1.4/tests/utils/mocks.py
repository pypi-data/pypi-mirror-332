"""
Mock objects for OpenAgents JSON testing.

This module provides mock implementations of external systems and services
that can be used for testing without requiring actual external dependencies.
"""

from typing import Any, Callable, Dict, List, Optional


class MockAgentClient:
    """
    A mock implementation of an AI agent client for testing.

    This can be used to simulate responses from AI agents without
    requiring actual API calls or external services.
    """

    def __init__(self, responses=None):
        """
        Initialize the mock agent client.

        Args:
            responses: A dictionary mapping request patterns to responses
        """
        self.responses = responses or {}
        self.calls = []

    async def call(self, prompt: str, **kwargs) -> str:
        """
        Simulate a call to an AI agent.

        Args:
            prompt: The input prompt
            **kwargs: Additional arguments

        Returns:
            A mocked response based on the prompt
        """
        self.calls.append({"prompt": prompt, "kwargs": kwargs})

        # Try to find a matching response pattern
        for pattern, response in self.responses.items():
            if pattern in prompt:
                return response

        # Default response if no pattern matches
        return f"Mock response to: {prompt}"

    def add_response(self, pattern: str, response: str) -> None:
        """
        Add a response pattern to the mock.

        Args:
            pattern: The pattern to match in prompts
            response: The response to return
        """
        self.responses[pattern] = response

    def get_call_count(self) -> int:
        """
        Get the number of calls made to this mock.

        Returns:
            The number of calls
        """
        return len(self.calls)

    def reset(self) -> None:
        """Reset the call history."""
        self.calls = []


class MockJobCallback:
    """
    A mock job callback for testing job execution flows.

    This can be used to test job execution flows by capturing
    callback events without requiring actual callback handlers.
    """

    def __init__(self):
        """Initialize the mock job callback."""
        self.events = []

    async def on_status_change(
        self, job_id: str, status: str, metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Record a job status change event.

        Args:
            job_id: The ID of the job
            status: The new status
            metadata: Additional metadata about the status change
        """
        self.events.append(
            {
                "type": "status_change",
                "job_id": job_id,
                "status": status,
                "metadata": metadata or {},
            }
        )

    async def on_progress(
        self, job_id: str, progress: float, message: Optional[str] = None
    ) -> None:
        """
        Record a job progress event.

        Args:
            job_id: The ID of the job
            progress: The progress value (0.0 to 1.0)
            message: An optional progress message
        """
        self.events.append(
            {
                "type": "progress",
                "job_id": job_id,
                "progress": progress,
                "message": message,
            }
        )

    async def on_error(
        self, job_id: str, error: str, details: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Record a job error event.

        Args:
            job_id: The ID of the job
            error: The error message
            details: Additional error details
        """
        self.events.append(
            {
                "type": "error",
                "job_id": job_id,
                "error": error,
                "details": details or {},
            }
        )

    def get_events(self, event_type: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Get all recorded events, optionally filtered by type.

        Args:
            event_type: If provided, only return events of this type

        Returns:
            A list of event dictionaries
        """
        if event_type is None:
            return self.events

        return [event for event in self.events if event["type"] == event_type]

    def reset(self) -> None:
        """Reset the event history."""
        self.events = []
