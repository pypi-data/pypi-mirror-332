"""
Decorators for state management.

This module provides decorators for creating stateful properties.
"""

import functools
import inspect
import logging
from typing import Any, Callable, Dict, Optional, Type

from openagents_json.core.state.manager import get_state_manager

logger = logging.getLogger(__name__)


def stateful(
    key: Optional[str] = None,
    serializer: Optional[str] = None,
    persistent: bool = True,
    cached: bool = True
):
    """
    Decorator for creating stateful properties.
    
    Stateful properties are automatically persisted using the configured
    state manager.
    
    Args:
        key: Custom state key (defaults to property name)
        serializer: Serializer to use (default based on type)
        persistent: Whether to persist across sessions
        cached: Whether to cache the value in memory
        
    Example:
        ```python
        class MyAgent(BaseAgent):
            @stateful(key="my_counter", persistent=True, cached=True)
            def counter(self) -> int:
                return 0  # Default value when not set
                
            def increment(self):
                self.counter += 1  # Automatically persisted
        ```
        
    Returns:
        Property descriptor that handles state management
    """
    def decorator(func):
        prop_name = func.__name__
        state_key = key or prop_name
        
        @functools.wraps(func)
        def getter(self):
            # Get from cache if available
            if cached and hasattr(self, f"_cached_{prop_name}"):
                return getattr(self, f"_cached_{prop_name}")
                
            # Get from state manager
            if hasattr(self, "_state_manager") and persistent:
                # Check if key exists in state manager
                if self._state_manager.exists(self.agent_id, state_key):
                    value = self._state_manager.get_state(
                        self.agent_id, state_key, None
                    )
                    if value is not None or self._state_manager.exists(self.agent_id, state_key):
                        if cached:
                            setattr(self, f"_cached_{prop_name}", value)
                        return value
                    
            # Get default value from decorated function
            value = func(self)
            
            # Store in state manager
            if hasattr(self, "_state_manager") and persistent:
                self._state_manager.set_state(self.agent_id, state_key, value)
                
            # Cache the value
            if cached:
                setattr(self, f"_cached_{prop_name}", value)
                
            return value
            
        def setter(self, value):
            # Update cache
            if cached:
                setattr(self, f"_cached_{prop_name}", value)
                
            # Update state manager
            if hasattr(self, "_state_manager") and persistent:
                self._state_manager.set_state(self.agent_id, state_key, value)
                
        # Create property with getter and setter
        prop = property(getter, setter)
        
        # Mark the property as stateful for introspection
        prop._stateful = True
        prop._stateful_key = state_key
        prop._stateful_serializer = serializer
        prop._stateful_persistent = persistent
        prop._stateful_cached = cached
        
        return prop
    
    return decorator


class StatefulBase:
    """
    Mixin for adding state management to any class.
    
    This mixin provides methods for loading and saving state, and can be used
    with the `@stateful` decorator to add state persistence to any class.
    
    Example:
        ```python
        class MyAgent(StatefulBase):
            def __init__(self, agent_id, name):
                super().__init__()
                self.agent_id = agent_id
                self.name = name
                
            @stateful
            def counter(self) -> int:
                return 0
        ```
    """
    
    def __init__(self, state_manager=None, *args, **kwargs):
        """
        Initialize the stateful base.
        
        Args:
            state_manager: Optional custom state manager
            *args: Positional arguments for the parent class
            **kwargs: Keyword arguments for the parent class
        """
        self._state_manager = state_manager or get_state_manager()
        super().__init__(*args, **kwargs)
        
    def save_state(self) -> None:
        """
        Force save all stateful properties.
        
        This method saves all stateful properties to the state manager.
        """
        if not hasattr(self, "_state_manager"):
            return
            
        # Find all stateful properties
        for name, prop in inspect.getmembers(self.__class__, lambda x: isinstance(x, property)):
            if hasattr(prop, "_stateful") and prop._stateful:
                try:
                    value = getattr(self, name)
                    self._state_manager.set_state(self.agent_id, prop._stateful_key, value)
                except Exception as e:
                    logger.warning(f"Error saving stateful property {name}: {e}")
                
    def load_state(self) -> None:
        """
        Force load all stateful properties.
        
        This method loads all stateful properties from the state manager.
        """
        if not hasattr(self, "_state_manager"):
            return
            
        # Find all stateful properties
        for name, prop in inspect.getmembers(self.__class__, lambda x: isinstance(x, property)):
            if hasattr(prop, "_stateful") and prop._stateful:
                try:
                    # This will trigger the getter which loads from state
                    getattr(self, name)
                except Exception as e:
                    logger.warning(f"Error loading stateful property {name}: {e}")
                    
    def clear_state(self) -> None:
        """
        Clear all state for this instance.
        
        This method removes all state for this instance from the state manager.
        """
        if not hasattr(self, "_state_manager"):
            return
            
        self._state_manager.clear_state(self.agent_id)
        
        # Clear cached values
        for name, prop in inspect.getmembers(self.__class__, lambda x: isinstance(x, property)):
            if hasattr(prop, "_stateful") and prop._stateful and prop._stateful_cached:
                if hasattr(self, f"_cached_{name}"):
                    delattr(self, f"_cached_{name}")
                    
    def get_state_snapshot(self) -> Dict[str, Any]:
        """
        Get a serializable snapshot of the agent's state.
        
        Returns:
            Dictionary containing the agent's state
        """
        if not hasattr(self, "_state_manager"):
            return {}
            
        # Get all keys
        keys = self._state_manager.keys(self.agent_id)
        
        # Return bulk state
        return self._state_manager.get_bulk_state(self.agent_id, keys)
    
    def restore_from_snapshot(self, snapshot: Dict[str, Any]) -> None:
        """
        Restore agent state from a snapshot.
        
        Args:
            snapshot: Snapshot dictionary from get_state_snapshot
        """
        if not hasattr(self, "_state_manager"):
            return
            
        # Set all values from snapshot
        self._state_manager.set_bulk_state(self.agent_id, snapshot)
        
        # Reload state
        self.load_state() 