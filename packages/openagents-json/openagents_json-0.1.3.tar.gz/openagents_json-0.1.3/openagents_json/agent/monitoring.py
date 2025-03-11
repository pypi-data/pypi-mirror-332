"""
Monitoring and telemetry system for OpenAgents JSON agents.

This module provides utilities for monitoring agent execution, collecting
metrics, and tracking performance and errors.
"""

import functools
import logging
import time
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Set, Type, TypeVar, Union

logger = logging.getLogger(__name__)


class EventType(Enum):
    """Types of events that can be monitored."""
    
    AGENT_INITIALIZED = "agent_initialized"
    AGENT_EXECUTED = "agent_executed"
    AGENT_ERROR = "agent_error"
    CAPABILITY_CALLED = "capability_called"
    CAPABILITY_ERROR = "capability_error"
    TOOL_CALLED = "tool_called"
    TOOL_ERROR = "tool_error"
    WORKFLOW_STEP_EXECUTED = "workflow_step_executed"
    WORKFLOW_STEP_ERROR = "workflow_step_error"
    CUSTOM = "custom"


@dataclass
class Event:
    """Base class for monitoring events."""
    
    event_type: EventType
    timestamp: datetime = field(default_factory=datetime.now)
    agent_id: Optional[str] = None
    session_id: Optional[str] = None
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentEvent(Event):
    """Event for agent operations."""
    
    agent_name: str = ""
    agent_type: str = ""
    execution_time_ms: Optional[float] = None


@dataclass
class CapabilityEvent(Event):
    """Event for capability operations."""
    
    agent_id: str = ""
    capability_name: str = ""
    execution_time_ms: Optional[float] = None
    inputs: Dict[str, Any] = field(default_factory=dict)
    output: Any = None


@dataclass
class ToolEvent(Event):
    """Event for tool operations."""
    
    tool_name: str = ""
    execution_time_ms: Optional[float] = None
    inputs: Dict[str, Any] = field(default_factory=dict)
    output: Any = None


@dataclass
class WorkflowStepEvent(Event):
    """Event for workflow step operations."""
    
    workflow_id: str = ""
    step_id: str = ""
    step_type: str = ""
    execution_time_ms: Optional[float] = None
    inputs: Dict[str, Any] = field(default_factory=dict)
    outputs: Dict[str, Any] = field(default_factory=dict)


class EventHandler:
    """Base class for event handlers."""
    
    def handle_event(self, event: Event) -> None:
        """
        Handle an event.
        
        Args:
            event: The event to handle
        """
        raise NotImplementedError("Event handlers must implement handle_event")


class LoggingEventHandler(EventHandler):
    """Event handler that logs events."""
    
    def __init__(self, log_level: int = logging.INFO):
        """
        Initialize the logging event handler.
        
        Args:
            log_level: Logging level to use
        """
        self.log_level = log_level
    
    def handle_event(self, event: Event) -> None:
        """
        Log the event.
        
        Args:
            event: The event to log
        """
        # Format the log message based on event type
        if isinstance(event, AgentEvent):
            message = f"Agent {event.agent_name} ({event.event_type.value})"
            if event.execution_time_ms is not None:
                message += f" took {event.execution_time_ms:.2f}ms"
                
        elif isinstance(event, CapabilityEvent):
            message = f"Capability {event.capability_name} ({event.event_type.value})"
            if event.execution_time_ms is not None:
                message += f" took {event.execution_time_ms:.2f}ms"
                
        elif isinstance(event, ToolEvent):
            message = f"Tool {event.tool_name} ({event.event_type.value})"
            if event.execution_time_ms is not None:
                message += f" took {event.execution_time_ms:.2f}ms"
                
        elif isinstance(event, WorkflowStepEvent):
            message = f"Workflow step {event.step_id} in {event.workflow_id} ({event.event_type.value})"
            if event.execution_time_ms is not None:
                message += f" took {event.execution_time_ms:.2f}ms"
                
        else:
            message = f"Event: {event.event_type.value}"
        
        # Add agent and session IDs if available
        if event.agent_id:
            message += f" | Agent ID: {event.agent_id}"
        if event.session_id:
            message += f" | Session ID: {event.session_id}"
        
        # Log the message
        logger.log(self.log_level, message)


class AgentMonitor:
    """
    Monitoring system for agents.
    
    This class provides methods for tracking agent execution, collecting
    metrics, and handling monitoring events.
    """
    
    def __init__(self):
        """Initialize the agent monitor."""
        self.event_handlers: List[EventHandler] = []
        self.metrics: Dict[str, Dict[str, Any]] = {}
        
        # Add default event handler
        self.add_event_handler(LoggingEventHandler())
    
    def add_event_handler(self, handler: EventHandler) -> None:
        """
        Add an event handler.
        
        Args:
            handler: The event handler to add
        """
        self.event_handlers.append(handler)
    
    def emit_event(self, event: Event) -> None:
        """
        Emit an event to all handlers.
        
        Args:
            event: The event to emit
        """
        for handler in self.event_handlers:
            try:
                handler.handle_event(event)
            except Exception as e:
                logger.error(f"Error in event handler: {str(e)}")
    
    def track_agent_execution(self, agent_id: str, agent_name: str, agent_type: str, 
                             session_id: Optional[str] = None) -> Callable:
        """
        Decorator to track agent execution.
        
        Args:
            agent_id: ID of the agent
            agent_name: Name of the agent
            agent_type: Type of the agent
            session_id: Optional session ID
            
        Returns:
            Decorator function
        """
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                start_time = time.time()
                
                try:
                    # Emit initialization event
                    self.emit_event(AgentEvent(
                        event_type=EventType.AGENT_INITIALIZED,
                        agent_id=agent_id,
                        agent_name=agent_name,
                        agent_type=agent_type,
                        session_id=session_id
                    ))
                    
                    # Execute the function
                    result = await func(*args, **kwargs)
                    
                    # Calculate execution time
                    execution_time_ms = (time.time() - start_time) * 1000
                    
                    # Emit execution event
                    self.emit_event(AgentEvent(
                        event_type=EventType.AGENT_EXECUTED,
                        agent_id=agent_id,
                        agent_name=agent_name,
                        agent_type=agent_type,
                        session_id=session_id,
                        execution_time_ms=execution_time_ms,
                        details={"success": True}
                    ))
                    
                    # Update metrics
                    self._update_agent_metrics(agent_id, execution_time_ms, True)
                    
                    return result
                    
                except Exception as e:
                    # Calculate execution time
                    execution_time_ms = (time.time() - start_time) * 1000
                    
                    # Emit error event
                    self.emit_event(AgentEvent(
                        event_type=EventType.AGENT_ERROR,
                        agent_id=agent_id,
                        agent_name=agent_name,
                        agent_type=agent_type,
                        session_id=session_id,
                        execution_time_ms=execution_time_ms,
                        details={"error": str(e), "error_type": type(e).__name__}
                    ))
                    
                    # Update metrics
                    self._update_agent_metrics(agent_id, execution_time_ms, False)
                    
                    # Re-raise the exception
                    raise
            
            return wrapper
        
        return decorator
    
    def track_capability(self, agent_id: str, capability_name: str, 
                        session_id: Optional[str] = None) -> Callable:
        """
        Decorator to track capability execution.
        
        Args:
            agent_id: ID of the agent
            capability_name: Name of the capability
            session_id: Optional session ID
            
        Returns:
            Decorator function
        """
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                start_time = time.time()
                
                try:
                    # Execute the function
                    result = await func(*args, **kwargs)
                    
                    # Calculate execution time
                    execution_time_ms = (time.time() - start_time) * 1000
                    
                    # Emit event
                    self.emit_event(CapabilityEvent(
                        event_type=EventType.CAPABILITY_CALLED,
                        agent_id=agent_id,
                        capability_name=capability_name,
                        session_id=session_id,
                        execution_time_ms=execution_time_ms,
                        inputs=kwargs,
                        output=result
                    ))
                    
                    return result
                    
                except Exception as e:
                    # Calculate execution time
                    execution_time_ms = (time.time() - start_time) * 1000
                    
                    # Emit error event
                    self.emit_event(CapabilityEvent(
                        event_type=EventType.CAPABILITY_ERROR,
                        agent_id=agent_id,
                        capability_name=capability_name,
                        session_id=session_id,
                        execution_time_ms=execution_time_ms,
                        inputs=kwargs,
                        details={"error": str(e), "error_type": type(e).__name__}
                    ))
                    
                    # Re-raise the exception
                    raise
            
            return wrapper
        
        return decorator
    
    def track_tool(self, tool_name: str, session_id: Optional[str] = None) -> Callable:
        """
        Decorator to track tool execution.
        
        Args:
            tool_name: Name of the tool
            session_id: Optional session ID
            
        Returns:
            Decorator function
        """
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                start_time = time.time()
                
                try:
                    # Execute the function
                    result = await func(*args, **kwargs)
                    
                    # Calculate execution time
                    execution_time_ms = (time.time() - start_time) * 1000
                    
                    # Emit event
                    self.emit_event(ToolEvent(
                        event_type=EventType.TOOL_CALLED,
                        tool_name=tool_name,
                        session_id=session_id,
                        execution_time_ms=execution_time_ms,
                        inputs=kwargs,
                        output=result
                    ))
                    
                    return result
                    
                except Exception as e:
                    # Calculate execution time
                    execution_time_ms = (time.time() - start_time) * 1000
                    
                    # Emit error event
                    self.emit_event(ToolEvent(
                        event_type=EventType.TOOL_ERROR,
                        tool_name=tool_name,
                        session_id=session_id,
                        execution_time_ms=execution_time_ms,
                        inputs=kwargs,
                        details={"error": str(e), "error_type": type(e).__name__}
                    ))
                    
                    # Re-raise the exception
                    raise
            
            return wrapper
        
        return decorator
    
    def track_workflow_step(self, workflow_id: str, step_id: str, step_type: str,
                           session_id: Optional[str] = None) -> Callable:
        """
        Decorator to track workflow step execution.
        
        Args:
            workflow_id: ID of the workflow
            step_id: ID of the step
            step_type: Type of the step
            session_id: Optional session ID
            
        Returns:
            Decorator function
        """
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                start_time = time.time()
                
                try:
                    # Execute the function
                    result = await func(*args, **kwargs)
                    
                    # Calculate execution time
                    execution_time_ms = (time.time() - start_time) * 1000
                    
                    # Emit event
                    self.emit_event(WorkflowStepEvent(
                        event_type=EventType.WORKFLOW_STEP_EXECUTED,
                        workflow_id=workflow_id,
                        step_id=step_id,
                        step_type=step_type,
                        session_id=session_id,
                        execution_time_ms=execution_time_ms,
                        inputs=kwargs,
                        outputs=result if isinstance(result, dict) else {"result": result}
                    ))
                    
                    return result
                    
                except Exception as e:
                    # Calculate execution time
                    execution_time_ms = (time.time() - start_time) * 1000
                    
                    # Emit error event
                    self.emit_event(WorkflowStepEvent(
                        event_type=EventType.WORKFLOW_STEP_ERROR,
                        workflow_id=workflow_id,
                        step_id=step_id,
                        step_type=step_type,
                        session_id=session_id,
                        execution_time_ms=execution_time_ms,
                        inputs=kwargs,
                        details={"error": str(e), "error_type": type(e).__name__}
                    ))
                    
                    # Re-raise the exception
                    raise
            
            return wrapper
        
        return decorator
    
    def _update_agent_metrics(self, agent_id: str, execution_time_ms: float, success: bool) -> None:
        """
        Update metrics for an agent.
        
        Args:
            agent_id: ID of the agent
            execution_time_ms: Execution time in milliseconds
            success: Whether the execution was successful
        """
        if agent_id not in self.metrics:
            self.metrics[agent_id] = {
                "total_executions": 0,
                "successful_executions": 0,
                "failed_executions": 0,
                "total_execution_time_ms": 0,
                "average_execution_time_ms": 0,
                "last_execution_time": datetime.now().isoformat(),
                "last_execution_success": success
            }
        
        metrics = self.metrics[agent_id]
        metrics["total_executions"] += 1
        metrics["total_execution_time_ms"] += execution_time_ms
        metrics["average_execution_time_ms"] = metrics["total_execution_time_ms"] / metrics["total_executions"]
        metrics["last_execution_time"] = datetime.now().isoformat()
        metrics["last_execution_success"] = success
        
        if success:
            metrics["successful_executions"] += 1
        else:
            metrics["failed_executions"] += 1
    
    def get_metrics(self, agent_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get metrics for an agent or all agents.
        
        Args:
            agent_id: Optional ID of the agent to get metrics for
            
        Returns:
            Dictionary with metrics
        """
        if agent_id:
            return self.metrics.get(agent_id, {})
        else:
            return self.metrics


# Create a global agent monitor
agent_monitor = AgentMonitor() 