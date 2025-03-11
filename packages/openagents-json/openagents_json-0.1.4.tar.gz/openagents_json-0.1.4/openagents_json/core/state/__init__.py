"""
State management for OpenAgents JSON.

This package provides a comprehensive state management system for persisting
agent state across workflow steps and processes.
"""

from openagents_json.core.state.base import (
    StateManager,
    StateError,
    StateSerializationError,
    StateDeserializationError,
    StateCorruptionError,
    StateLockError,
)
from openagents_json.core.state.decorators import stateful, StatefulBase
from openagents_json.core.state.manager import get_state_manager, set_state_manager, configure_state_manager
from openagents_json.core.state.serialization import (
    Serializer,
    JsonSerializer,
    get_serializer,
    register_serializer,
)
from openagents_json.core.state.managers import (
    MemoryStateManager,
    FileStateManager,
    DatabaseStateManager,
    RedisStateManager,
)

__all__ = [
    # Base classes and interfaces
    "StateManager",
    "Serializer",
    
    # Error classes
    "StateError",
    "StateSerializationError",
    "StateDeserializationError",
    "StateCorruptionError",
    "StateLockError",
    
    # Decorators and mixins
    "stateful",
    "StatefulBase",
    
    # Manager factory functions
    "get_state_manager",
    "set_state_manager",
    "configure_state_manager",
    
    # Serialization utilities
    "JsonSerializer",
    "get_serializer",
    "register_serializer",
    
    # State manager implementations
    "MemoryStateManager",
    "FileStateManager",
    "DatabaseStateManager",
    "RedisStateManager",
] 