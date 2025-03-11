"""
Event system for job state notifications in the OpenAgents JSON framework.

This module provides an event emitter and subscriber system for job lifecycle events,
enabling components to publish and subscribe to job state changes and other relevant events.
The event system serves as the foundation for monitoring, observability, and inter-component
communication.
"""

import asyncio
import enum
import logging
import time
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Set, Union

from openagents_json.job.model import Job, JobStatus

logger = logging.getLogger(__name__)


class EventType(str, enum.Enum):
    """Enumeration of possible event types."""

    # Job lifecycle events
    JOB_CREATED = "job.created"
    JOB_QUEUED = "job.queued"
    JOB_STARTED = "job.started"
    JOB_PAUSED = "job.paused"
    JOB_RESUMED = "job.resumed"
    JOB_COMPLETED = "job.completed"
    JOB_FAILED = "job.failed"
    JOB_CANCELLED = "job.cancelled"
    JOB_RETRYING = "job.retrying"

    # Job progress events
    JOB_PROGRESS_UPDATED = "job.progress.updated"

    # Worker events
    WORKER_REGISTERED = "worker.registered"
    WORKER_HEARTBEAT = "worker.heartbeat"
    WORKER_CLAIMED_JOB = "worker.claimed_job"
    WORKER_OFFLINE = "worker.offline"

    # System events
    SYSTEM_STARTUP = "system.startup"
    SYSTEM_SHUTDOWN = "system.shutdown"
    SYSTEM_ERROR = "system.error"


@dataclass
class Event:
    """
    Event data structure for the event system.

    Contains information about an event, including its type, timestamp,
    and associated data.
    """

    event_type: EventType
    timestamp: datetime = field(default_factory=datetime.now)
    job_id: Optional[str] = None
    worker_id: Optional[str] = None
    data: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_job(cls, event_type: EventType, job: Job, **extra_data) -> "Event":
        """
        Create an event from a job instance.

        Args:
            event_type: Type of the event
            job: Job instance related to the event
            extra_data: Additional data to include in the event

        Returns:
            Event instance with job data
        """
        data = job.to_dict()
        data.update(extra_data)
        return cls(
            event_type=event_type, job_id=job.job_id, worker_id=job.worker_id, data=data
        )


# Type definition for event handlers
EventHandler = Callable[[Event], None]
AsyncEventHandler = Callable[[Event], asyncio.coroutine]


class EventEmitter:
    """
    Event emitter for publishing and subscribing to events.

    Implements the observer pattern for event-based communication
    between components.
    """

    def __init__(self):
        """Initialize the event emitter."""
        self._handlers: Dict[EventType, List[EventHandler]] = {}
        self._async_handlers: Dict[EventType, List[AsyncEventHandler]] = {}
        self._global_handlers: List[EventHandler] = []
        self._async_global_handlers: List[AsyncEventHandler] = []
        self._is_emitting: bool = False
        self._pending_events: List[Event] = []

    def on(self, event_type: EventType, handler: EventHandler) -> None:
        """
        Register a synchronous event handler for a specific event type.

        Args:
            event_type: Type of event to listen for
            handler: Function to call when the event is emitted
        """
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    def off(self, event_type: EventType, handler: EventHandler) -> None:
        """
        Remove a synchronous event handler for a specific event type.

        Args:
            event_type: Type of event the handler is registered for
            handler: Handler function to remove
        """
        if event_type in self._handlers:
            if handler in self._handlers[event_type]:
                self._handlers[event_type].remove(handler)

    def on_any(self, handler: EventHandler) -> None:
        """
        Register a synchronous handler for all event types.

        Args:
            handler: Function to call for any emitted event
        """
        self._global_handlers.append(handler)

    def off_any(self, handler: EventHandler) -> None:
        """
        Remove a global synchronous event handler.

        Args:
            handler: Global handler function to remove
        """
        if handler in self._global_handlers:
            self._global_handlers.remove(handler)

    async def on_async(self, event_type: EventType, handler: AsyncEventHandler) -> None:
        """
        Register an asynchronous event handler for a specific event type.

        Args:
            event_type: Type of event to listen for
            handler: Async function to call when the event is emitted
        """
        if event_type not in self._async_handlers:
            self._async_handlers[event_type] = []
        self._async_handlers[event_type].append(handler)

    async def off_async(
        self, event_type: EventType, handler: AsyncEventHandler
    ) -> None:
        """
        Remove an asynchronous event handler for a specific event type.

        Args:
            event_type: Type of event the handler is registered for
            handler: Async handler function to remove
        """
        if event_type in self._async_handlers:
            if handler in self._async_handlers[event_type]:
                self._async_handlers[event_type].remove(handler)

    async def on_any_async(self, handler: AsyncEventHandler) -> None:
        """
        Register an asynchronous handler for all event types.

        Args:
            handler: Async function to call for any emitted event
        """
        self._async_global_handlers.append(handler)

    async def off_any_async(self, handler: AsyncEventHandler) -> None:
        """
        Remove a global asynchronous event handler.

        Args:
            handler: Global async handler function to remove
        """
        if handler in self._async_global_handlers:
            self._async_global_handlers.remove(handler)

    def emit(self, event: Event) -> None:
        """
        Emit a synchronous event to all registered handlers.

        Args:
            event: Event to emit
        """
        if self._is_emitting:
            # Queue event if already emitting to prevent recursion issues
            self._pending_events.append(event)
            return

        self._is_emitting = True
        try:
            # Call type-specific handlers
            for handler in self._handlers.get(event.event_type, []):
                try:
                    handler(event)
                except Exception as e:
                    logger.error(f"Error in event handler for {event.event_type}: {e}")

            # Call global handlers
            for handler in self._global_handlers:
                try:
                    handler(event)
                except Exception as e:
                    logger.error(
                        f"Error in global event handler for {event.event_type}: {e}"
                    )
        finally:
            self._is_emitting = False

            # Process any events that were queued during emission
            pending = self._pending_events.copy()
            self._pending_events.clear()
            for pending_event in pending:
                self.emit(pending_event)

    async def emit_async(self, event: Event) -> None:
        """
        Emit an asynchronous event to all registered handlers.

        Args:
            event: Event to emit
        """
        # First emit to synchronous handlers
        self.emit(event)

        # Then emit to async handlers
        tasks = []

        # Call type-specific async handlers
        for handler in self._async_handlers.get(event.event_type, []):
            tasks.append(asyncio.create_task(handler(event)))

        # Call global async handlers
        for handler in self._async_global_handlers:
            tasks.append(asyncio.create_task(handler(event)))

        # Await all handler tasks
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)


# Global event emitter instance
event_emitter = EventEmitter()
