"""
State manager factory and utilities.

This module provides functions for getting and configuring state managers.
"""

import logging
from typing import Any, Dict, Optional

from openagents_json.core.state.base import StateManager
from openagents_json.core.state.managers import (
    MemoryStateManager,
    FileStateManager,
    DatabaseStateManager,
    RedisStateManager,
)
from openagents_json.settings import get_settings

logger = logging.getLogger(__name__)

# Global state manager instance
_state_manager = None


def get_state_manager(name: Optional[str] = None) -> StateManager:
    """
    Get a state manager instance.
    
    Args:
        name: Name of the state manager to get (defaults to settings)
        
    Returns:
        StateManager instance
        
    Raises:
        ValueError: If the specified state manager is not supported
    """
    global _state_manager
    
    # Return existing instance if available
    if _state_manager is not None:
        return _state_manager
    
    # Get settings
    settings = get_settings()
    
    # Use provided name or get from settings
    if name is None:
        name = settings.state.manager
    
    # Create state manager based on name
    if name == "memory":
        _state_manager = MemoryStateManager()
    elif name == "file":
        _state_manager = FileStateManager(
            base_path=settings.state.file_path,
            serializer_name=settings.state.serializer,
        )
    elif name == "database":
        _state_manager = DatabaseStateManager(
            database_url=settings.state.database_url,
            serializer_name=settings.state.serializer,
        )
    elif name == "redis":
        _state_manager = RedisStateManager(
            redis_url=settings.state.redis_url,
            serializer_name=settings.state.serializer,
        )
    else:
        raise ValueError(f"Unsupported state manager: {name}")
    
    logger.info(f"Initialized state manager: {name}")
    return _state_manager


def set_state_manager(manager: StateManager) -> None:
    """
    Set the global state manager instance.
    
    Args:
        manager: StateManager instance to set
    """
    global _state_manager
    _state_manager = manager
    logger.info(f"Set custom state manager: {manager.__class__.__name__}")


def configure_state_manager(config: Dict[str, Any]) -> StateManager:
    """
    Configure and get a state manager from a configuration dictionary.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        StateManager instance
        
    Raises:
        ValueError: If the specified state manager is not supported
    """
    manager_type = config.get("type", "memory")
    
    if manager_type == "memory":
        return MemoryStateManager()
    elif manager_type == "file":
        return FileStateManager(
            base_path=config.get("file_path", "~/.openagents/state"),
            serializer_name=config.get("serializer", "json"),
        )
    elif manager_type == "database":
        return DatabaseStateManager(
            database_url=config.get("database_url"),
            serializer_name=config.get("serializer", "json"),
            create_tables=config.get("create_tables", True),
        )
    elif manager_type == "redis":
        return RedisStateManager(
            redis_url=config.get("redis_url"),
            serializer_name=config.get("serializer", "json"),
            key_prefix=config.get("key_prefix", "openagents:state:"),
        )
    else:
        raise ValueError(f"Unsupported state manager type: {manager_type}") 