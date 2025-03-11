"""
Base state management classes and exceptions.

This module defines the core abstractions for state management, including the
StateManager interface and common exception types.
"""

import abc
import contextlib
import logging
from typing import Any, Dict, List, Optional, Type

logger = logging.getLogger(__name__)


class StateError(Exception):
    """Base class for state management errors."""
    pass


class StateSerializationError(StateError):
    """Error during state serialization."""
    pass


class StateDeserializationError(StateError):
    """Error during state deserialization."""
    pass


class StateCorruptionError(StateError):
    """State corruption detected."""
    pass


class StateLockError(StateError):
    """Error acquiring state lock."""
    pass


class StateManager(abc.ABC):
    """
    Abstract base class for state management.
    
    StateManager provides an interface for persisting agent state between
    workflow steps and across processes.
    """
    
    @abc.abstractmethod
    def get_state(self, agent_id: str, key: str, default: Any = None) -> Any:
        """
        Retrieve state by key.
        
        Args:
            agent_id: The ID of the agent
            key: State key to retrieve
            default: Default value if key doesn't exist
            
        Returns:
            The state value if found, otherwise the default value
        """
        pass
        
    @abc.abstractmethod
    def set_state(self, agent_id: str, key: str, value: Any) -> None:
        """
        Store state by key.
        
        Args:
            agent_id: The ID of the agent
            key: State key to set
            value: Value to store
        """
        pass
        
    @abc.abstractmethod
    def delete_state(self, agent_id: str, key: str) -> None:
        """
        Remove state by key.
        
        Args:
            agent_id: The ID of the agent
            key: State key to delete
        """
        pass
        
    @abc.abstractmethod
    def clear_state(self, agent_id: str) -> None:
        """
        Remove all state for an agent.
        
        Args:
            agent_id: The ID of the agent
        """
        pass
        
    @abc.abstractmethod
    def exists(self, agent_id: str, key: str) -> bool:
        """
        Check if state exists.
        
        Args:
            agent_id: The ID of the agent
            key: State key to check
            
        Returns:
            True if the key exists, False otherwise
        """
        pass
        
    @abc.abstractmethod
    def keys(self, agent_id: str) -> List[str]:
        """
        List all keys for an agent (for introspection).
        
        Args:
            agent_id: The ID of the agent
            
        Returns:
            List of state keys for the agent
        """
        pass
        
    @abc.abstractmethod
    def get_bulk_state(self, agent_id: str, keys: List[str]) -> Dict[str, Any]:
        """
        Bulk retrieve multiple state keys.
        
        Args:
            agent_id: The ID of the agent
            keys: List of state keys to retrieve
            
        Returns:
            Dictionary of key/value pairs
        """
        pass
        
    @abc.abstractmethod
    def set_bulk_state(self, agent_id: str, key_values: Dict[str, Any]) -> None:
        """
        Bulk store multiple state keys/values.
        
        Args:
            agent_id: The ID of the agent
            key_values: Dictionary of key/value pairs to store
        """
        pass
        
    @abc.abstractmethod
    def begin_transaction(self) -> Any:
        """
        Start a transaction context.
        
        Returns:
            Transaction object or identifier
        """
        pass
        
    @abc.abstractmethod
    def commit_transaction(self) -> None:
        """Commit a transaction."""
        pass
        
    @abc.abstractmethod
    def rollback_transaction(self) -> None:
        """Rollback a transaction."""
        pass
        
    @contextlib.contextmanager
    def transaction(self):
        """
        Context manager for transaction handling.
        
        Example:
            ```python
            with state_manager.transaction():
                state_manager.set_state(agent_id, "key", value)
                state_manager.set_state(agent_id, "other_key", other_value)
            # Transaction is automatically committed or rolled back
            ```
            
        Yields:
            Transaction context
            
        Raises:
            StateError: If transaction operations fail
        """
        self.begin_transaction()
        try:
            yield
            self.commit_transaction()
        except Exception as e:
            logger.exception("Error during state transaction, rolling back")
            self.rollback_transaction()
            if isinstance(e, StateError):
                raise
            raise StateError(f"Transaction failed: {e}") from e
            
    @abc.abstractmethod
    def validate_state(self, agent_id: str) -> bool:
        """
        Validate that the state is not corrupted.
        
        Args:
            agent_id: The ID of the agent
            
        Returns:
            True if state is valid, False otherwise
        """
        pass
    
    @abc.abstractmethod
    def create_backup(self, agent_id: str) -> str:
        """
        Create a backup of the current state.
        
        Args:
            agent_id: The ID of the agent
            
        Returns:
            Backup identifier
        """
        pass
    
    @abc.abstractmethod
    def restore_backup(self, agent_id: str, backup_id: str) -> bool:
        """
        Restore from a backup.
        
        Args:
            agent_id: The ID of the agent
            backup_id: Backup identifier from create_backup
            
        Returns:
            True if restore was successful, False otherwise
        """
        pass
    
    def backup_policy(self, policy: str = "manual"):
        """
        Set the backup policy.
        
        Args:
            policy: One of "manual", "before_execution", "after_execution", "on_error"
        """
        self._backup_policy = policy
    
    def maybe_create_backup(self, agent_id: str, event: str) -> Optional[str]:
        """
        Create a backup if the policy dictates it.
        
        Args:
            agent_id: Agent ID
            event: Event triggering potential backup ("before_execution", "after_execution", "on_error")
            
        Returns:
            Backup ID if created, None otherwise
        """
        if hasattr(self, "_backup_policy") and (self._backup_policy == event or self._backup_policy == "always"):
            return self.create_backup(agent_id)
        return None 