"""
Memory-based state manager implementation.

This module provides a state manager that keeps state in memory. It is suitable
for development and testing, but does not persist state across process restarts.
"""

import copy
import logging
import time
from typing import Any, Dict, List, Optional

from openagents_json.core.state.base import StateManager, StateError

logger = logging.getLogger(__name__)


class MemoryStateManager(StateManager):
    """
    In-memory storage for development and testing.
    
    This state manager keeps agent state in memory. It is suitable for 
    development and testing, but does not persist state across process restarts.
    
    Example:
        ```python
        manager = MemoryStateManager()
        manager.set_state("agent-123", "counter", 42)
        value = manager.get_state("agent-123", "counter")  # 42
        ```
    """
    
    def __init__(self):
        """Initialize the memory state manager."""
        self._state = {}  # agent_id -> {key: value}
        self._transaction = None
        self._backup_policy = "manual"
        self._backups = {}  # backup_id -> {agent_id: {key: value}}
        
    def get_state(self, agent_id: str, key: str, default: Any = None) -> Any:
        """Retrieve state by key."""
        if self._transaction is not None and agent_id in self._transaction:
            # Check if the key is in the transaction
            if key in self._transaction[agent_id]:
                return self._transaction[agent_id][key]
                
        if agent_id not in self._state or key not in self._state[agent_id]:
            return default
            
        return copy.deepcopy(self._state[agent_id][key])
        
    def set_state(self, agent_id: str, key: str, value: Any) -> None:
        """Store state by key."""
        if self._transaction is not None:
            # If in a transaction, just store in memory
            if agent_id not in self._transaction:
                self._transaction[agent_id] = {}
            self._transaction[agent_id][key] = copy.deepcopy(value)
            return
            
        if agent_id not in self._state:
            self._state[agent_id] = {}
            
        self._state[agent_id][key] = copy.deepcopy(value)
        
    def delete_state(self, agent_id: str, key: str) -> None:
        """Remove state by key."""
        if self._transaction is not None:
            # If in a transaction, mark for deletion
            if agent_id not in self._transaction:
                self._transaction[agent_id] = {}
            self._transaction[agent_id][key] = None  # Use None as a marker for deletion
            return
            
        if agent_id in self._state and key in self._state[agent_id]:
            del self._state[agent_id][key]
            
    def clear_state(self, agent_id: str) -> None:
        """Remove all state for an agent."""
        if self._transaction is not None:
            # If in a transaction, mark all keys for deletion
            self._transaction[agent_id] = {}  # Empty dict means delete all
            return
            
        if agent_id in self._state:
            del self._state[agent_id]
            
    def exists(self, agent_id: str, key: str) -> bool:
        """Check if state exists."""
        if self._transaction is not None and agent_id in self._transaction:
            # Check if the key is in the transaction
            if key in self._transaction[agent_id]:
                return self._transaction[agent_id][key] is not None
                
        return agent_id in self._state and key in self._state[agent_id]
        
    def keys(self, agent_id: str) -> List[str]:
        """List all keys for an agent (for introspection)."""
        result = []
        
        # Add keys from transaction if in transaction
        if self._transaction is not None and agent_id in self._transaction:
            for key, value in self._transaction[agent_id].items():
                if value is not None:  # Skip keys marked for deletion
                    result.append(key)
                    
        # Add keys from state
        if agent_id in self._state:
            for key in self._state[agent_id]:
                if key not in result:
                    result.append(key)
                    
        return result
        
    def get_bulk_state(self, agent_id: str, keys: List[str]) -> Dict[str, Any]:
        """Bulk retrieve multiple state keys."""
        result = {}
        for key in keys:
            result[key] = self.get_state(agent_id, key)
        return result
        
    def set_bulk_state(self, agent_id: str, key_values: Dict[str, Any]) -> None:
        """Bulk store multiple state keys/values."""
        for key, value in key_values.items():
            self.set_state(agent_id, key, value)
            
    def begin_transaction(self) -> Dict:
        """Start a transaction context."""
        if self._transaction is not None:
            raise StateError("Transaction already in progress")
            
        self._transaction = {}
        return self._transaction
        
    def commit_transaction(self) -> None:
        """Commit a transaction."""
        if self._transaction is None:
            raise StateError("No transaction in progress")
            
        try:
            # Apply all changes in the transaction
            for agent_id, keys in self._transaction.items():
                if not keys:
                    # Empty dict means delete all
                    if agent_id in self._state:
                        del self._state[agent_id]
                    continue
                    
                if agent_id not in self._state:
                    self._state[agent_id] = {}
                    
                for key, value in keys.items():
                    if value is None:
                        # None means delete
                        if key in self._state[agent_id]:
                            del self._state[agent_id][key]
                    else:
                        # Otherwise set the value
                        self._state[agent_id][key] = copy.deepcopy(value)
        finally:
            # Clear the transaction
            self._transaction = None
            
    def rollback_transaction(self) -> None:
        """Rollback a transaction."""
        if self._transaction is None:
            raise StateError("No transaction in progress")
            
        # Just discard the transaction
        self._transaction = None
        
    def validate_state(self, agent_id: str) -> bool:
        """Validate that the state is not corrupted."""
        # In-memory state can't be corrupted
        return True
    
    def create_backup(self, agent_id: str) -> str:
        """Create a backup of the current state."""
        if agent_id not in self._state:
            return ""  # No state to backup
            
        backup_id = f"{agent_id}_{int(time.time())}"
        
        # Make a deep copy of the agent's state
        self._backups[backup_id] = {
            agent_id: copy.deepcopy(self._state[agent_id])
        }
        
        return backup_id
    
    def restore_backup(self, agent_id: str, backup_id: str) -> bool:
        """Restore from a backup."""
        if backup_id not in self._backups or agent_id not in self._backups[backup_id]:
            logger.error(f"Backup {backup_id} not found for agent {agent_id}")
            return False
            
        # Restore the agent's state from the backup
        self._state[agent_id] = copy.deepcopy(self._backups[backup_id][agent_id])
        return True 