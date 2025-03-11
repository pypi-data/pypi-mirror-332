"""
File-based state manager implementation.

This module provides a state manager that persists state to the file system.
"""

import json
import logging
import os
import shutil
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from openagents_json.core.state.base import StateManager, StateError
from openagents_json.core.state.serialization import get_serializer

logger = logging.getLogger(__name__)


class FileStateManager(StateManager):
    """
    File-based storage for simple deployments.
    
    This state manager persists agent state to the file system. It is suitable 
    for single-node deployments and development environments.
    
    Example:
        ```python
        manager = FileStateManager("~/.openagents/state")
        manager.set_state("agent-123", "counter", 42)
        value = manager.get_state("agent-123", "counter")  # 42
        ```
    """
    
    def __init__(
        self, 
        base_path: Union[str, Path],
        serializer_name: str = "json",
        use_locking: bool = True
    ):
        """
        Initialize the file state manager.
        
        Args:
            base_path: Base directory for state storage
            serializer_name: Name of the serializer to use
            use_locking: Whether to use file locking for concurrency control
        """
        self._base_path = Path(os.path.expanduser(base_path))
        self._base_path.mkdir(parents=True, exist_ok=True)
        self._serializer = get_serializer(serializer_name)
        self._use_locking = use_locking
        self._cache = {}  # Optional cache for performance
        self._transaction = None
        self._backup_policy = "manual"
        
    def get_state(self, agent_id: str, key: str, default: Any = None) -> Any:
        """Retrieve state by key."""
        if self._transaction is not None and agent_id in self._transaction:
            # Check if the key is in the transaction
            if key in self._transaction[agent_id]:
                return self._transaction[agent_id][key]
                
        file_path = self._get_state_file(agent_id, key)
        if not file_path.exists():
            return default
            
        try:
            with open(file_path, "r") as f:
                serialized_data = f.read()
            return self._serializer.deserialize(serialized_data)
        except Exception as e:
            logger.warning(f"Error reading state file {file_path}: {e}")
            return default
            
    def set_state(self, agent_id: str, key: str, value: Any) -> None:
        """Store state by key."""
        if self._transaction is not None:
            # If in a transaction, just store in memory
            if agent_id not in self._transaction:
                self._transaction[agent_id] = {}
            self._transaction[agent_id][key] = value
            return
            
        file_path = self._get_state_file(agent_id, key)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            serialized_data = self._serializer.serialize(value)
            
            # Use atomic file write to prevent corruption
            with tempfile.NamedTemporaryFile(mode="w", dir=file_path.parent, delete=False) as temp_file:
                temp_file.write(serialized_data)
                temp_file_path = temp_file.name
                
            os.replace(temp_file_path, file_path)
        except Exception as e:
            logger.error(f"Error writing state file {file_path}: {e}")
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
            raise StateError(f"Failed to write state: {e}")
            
    def delete_state(self, agent_id: str, key: str) -> None:
        """Remove state by key."""
        if self._transaction is not None:
            # If in a transaction, mark for deletion
            if agent_id not in self._transaction:
                self._transaction[agent_id] = {}
            self._transaction[agent_id][key] = None  # Use None as a marker for deletion
            return
            
        file_path = self._get_state_file(agent_id, key)
        if file_path.exists():
            try:
                os.unlink(file_path)
            except Exception as e:
                logger.error(f"Error deleting state file {file_path}: {e}")
                raise StateError(f"Failed to delete state: {e}")
                
    def clear_state(self, agent_id: str) -> None:
        """Remove all state for an agent."""
        if self._transaction is not None:
            # If in a transaction, mark all keys for deletion
            self._transaction[agent_id] = {}  # Empty dict means delete all
            return
            
        agent_dir = self._base_path / agent_id
        if agent_dir.exists():
            try:
                shutil.rmtree(agent_dir)
            except Exception as e:
                logger.error(f"Error clearing state for agent {agent_id}: {e}")
                raise StateError(f"Failed to clear state: {e}")
                
    def exists(self, agent_id: str, key: str) -> bool:
        """Check if state exists."""
        if self._transaction is not None and agent_id in self._transaction:
            # Check if the key is in the transaction
            if key in self._transaction[agent_id]:
                return self._transaction[agent_id][key] is not None
                
        file_path = self._get_state_file(agent_id, key)
        return file_path.exists()
        
    def keys(self, agent_id: str) -> List[str]:
        """List all keys for an agent (for introspection)."""
        result = []
        
        # Add keys from transaction if in transaction
        if self._transaction is not None and agent_id in self._transaction:
            for key, value in self._transaction[agent_id].items():
                if value is not None:  # Skip keys marked for deletion
                    result.append(key)
        
        # Add keys from file system
        agent_dir = self._base_path / agent_id
        if agent_dir.exists():
            for path in agent_dir.glob("*.json"):
                key = path.stem
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
                    self.clear_state(agent_id)
                    continue
                    
                for key, value in keys.items():
                    if value is None:
                        # None means delete
                        file_path = self._get_state_file(agent_id, key)
                        if file_path.exists():
                            os.unlink(file_path)
                    else:
                        # Otherwise set the value
                        file_path = self._get_state_file(agent_id, key)
                        file_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        serialized_data = self._serializer.serialize(value)
                        
                        # Use atomic file write
                        with tempfile.NamedTemporaryFile(mode="w", dir=file_path.parent, delete=False) as temp_file:
                            temp_file.write(serialized_data)
                            temp_file_path = temp_file.name
                            
                        os.replace(temp_file_path, file_path)
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
        agent_dir = self._base_path / agent_id
        if not agent_dir.exists():
            return True  # No state to validate
            
        valid = True
        for path in agent_dir.glob("*.json"):
            try:
                with open(path, "r") as f:
                    serialized_data = f.read()
                self._serializer.deserialize(serialized_data)
            except Exception as e:
                logger.error(f"Validation error for state file {path}: {e}")
                valid = False
                
        return valid
    
    def create_backup(self, agent_id: str) -> str:
        """Create a backup of the current state."""
        agent_dir = self._base_path / agent_id
        if not agent_dir.exists():
            return ""  # No state to backup
            
        backup_id = f"{agent_id}_{int(time.time())}"
        backup_dir = self._base_path / "_backups" / backup_id
        
        try:
            backup_dir.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(agent_dir, backup_dir)
            return backup_id
        except Exception as e:
            logger.error(f"Error creating backup for agent {agent_id}: {e}")
            return ""
    
    def restore_backup(self, agent_id: str, backup_id: str) -> bool:
        """Restore from a backup."""
        backup_dir = self._base_path / "_backups" / backup_id
        if not backup_dir.exists():
            logger.error(f"Backup {backup_id} not found")
            return False
            
        agent_dir = self._base_path / agent_id
        if agent_dir.exists():
            try:
                shutil.rmtree(agent_dir)
            except Exception as e:
                logger.error(f"Error removing existing state for agent {agent_id}: {e}")
                return False
                
        try:
            shutil.copytree(backup_dir, agent_dir)
            return True
        except Exception as e:
            logger.error(f"Error restoring backup {backup_id} for agent {agent_id}: {e}")
            return False
            
    def _get_state_file(self, agent_id: str, key: str) -> Path:
        """Get the path to a state file."""
        return self._base_path / agent_id / f"{key}.json" 