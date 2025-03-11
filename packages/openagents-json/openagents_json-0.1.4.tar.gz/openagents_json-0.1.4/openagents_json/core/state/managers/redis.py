"""
Redis state manager implementation.

This module provides a Redis-backed implementation of the StateManager interface
for distributed state storage in production environments.
"""

import json
import logging
import time
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Union

import redis
from redis.exceptions import RedisError

from openagents_json.core.state.base import (
    StateManager, 
    StateError, 
    StateSerializationError,
    StateDeserializationError,
    StateLockError,
)
from openagents_json.core.state.serialization import get_serializer
from openagents_json.settings import get_settings

logger = logging.getLogger(__name__)


class RedisStateManager(StateManager):
    """
    Redis implementation of the StateManager interface.
    
    This class provides a persistent state manager backed by Redis for
    distributed state storage with transaction support.
    """
    
    def __init__(
        self,
        redis_url: Optional[str] = None,
        serializer_name: str = "json",
        key_prefix: str = "openagents:state:",
        lock_timeout: int = 30,
    ):
        """
        Initialize the Redis state manager.
        
        Args:
            redis_url: Redis connection URL (defaults to settings)
            serializer_name: Name of the serializer to use
            key_prefix: Prefix for Redis keys
            lock_timeout: Timeout in seconds for locks
        """
        settings = get_settings()
        
        # Use provided redis_url or get from settings
        if redis_url is None:
            if settings.state.redis_url:
                redis_url = settings.state.redis_url
            elif settings.storage.redis_url:
                redis_url = settings.storage.redis_url
            else:
                raise ValueError("Redis URL not provided and not found in settings")
        
        # Initialize Redis client
        self.redis = redis.from_url(redis_url)
        
        # Get the specified serializer
        self.serializer = get_serializer(serializer_name)
        
        # Set key prefix and lock timeout
        self.key_prefix = key_prefix
        self.lock_timeout = lock_timeout
        
        # Thread-local storage for transactions
        self._transaction = None
        
        # Test connection
        try:
            self.redis.ping()
        except RedisError as e:
            raise StateError(f"Redis connection error: {e}") from e
    
    def get_state(self, agent_id: str, key: str, default: Any = None) -> Any:
        """
        Get a state value by key.
        
        Args:
            agent_id: Agent identifier
            key: State key
            default: Default value if key doesn't exist
            
        Returns:
            The state value or default if not found
            
        Raises:
            StateError: If there's an error accessing the state
        """
        try:
            # Get the value from Redis
            redis_key = self._make_key(agent_id, key)
            value = self.redis.get(redis_key)
            
            if value is None:
                return default
            
            # Deserialize the value
            return self.serializer.deserialize(value)
            
        except StateDeserializationError as e:
            logger.error(f"Error deserializing state for agent {agent_id}, key {key}: {e}")
            raise
        except RedisError as e:
            logger.error(f"Redis error getting state for agent {agent_id}, key {key}: {e}")
            raise StateError(f"Redis error: {e}") from e
    
    def set_state(self, agent_id: str, key: str, value: Any) -> None:
        """
        Set a state value by key.
        
        Args:
            agent_id: Agent identifier
            key: State key
            value: State value to set
            
        Raises:
            StateError: If there's an error accessing the state
        """
        try:
            # Serialize the value
            serialized_value = self.serializer.serialize(value)
            
            # Set the value in Redis
            redis_key = self._make_key(agent_id, key)
            
            if self._transaction is not None:
                # Add to transaction
                self._transaction['operations'].append(
                    ('set', redis_key, serialized_value)
                )
            else:
                # Execute immediately
                self.redis.set(redis_key, serialized_value)
                
        except StateSerializationError as e:
            logger.error(f"Error serializing state for agent {agent_id}, key {key}: {e}")
            raise
        except RedisError as e:
            logger.error(f"Redis error setting state for agent {agent_id}, key {key}: {e}")
            raise StateError(f"Redis error: {e}") from e
    
    def delete_state(self, agent_id: str, key: str) -> None:
        """
        Delete a state value by key.
        
        Args:
            agent_id: Agent identifier
            key: State key
            
        Raises:
            StateError: If there's an error accessing the state
        """
        try:
            # Delete the key from Redis
            redis_key = self._make_key(agent_id, key)
            
            if self._transaction is not None:
                # Add to transaction
                self._transaction['operations'].append(
                    ('delete', redis_key)
                )
            else:
                # Execute immediately
                self.redis.delete(redis_key)
                
        except RedisError as e:
            logger.error(f"Redis error deleting state for agent {agent_id}, key {key}: {e}")
            raise StateError(f"Redis error: {e}") from e
    
    def clear_state(self, agent_id: str) -> None:
        """
        Clear all state for an agent.
        
        Args:
            agent_id: Agent identifier
            
        Raises:
            StateError: If there's an error accessing the state
        """
        try:
            # Get all keys for the agent
            pattern = self._make_key(agent_id, "*")
            keys = self.redis.keys(pattern)
            
            if not keys:
                return
            
            if self._transaction is not None:
                # Add to transaction
                for key in keys:
                    self._transaction['operations'].append(
                        ('delete', key)
                    )
            else:
                # Execute immediately
                self.redis.delete(*keys)
                
        except RedisError as e:
            logger.error(f"Redis error clearing state for agent {agent_id}: {e}")
            raise StateError(f"Redis error: {e}") from e
    
    def exists(self, agent_id: str, key: str) -> bool:
        """
        Check if a state key exists.
        
        Args:
            agent_id: Agent identifier
            key: State key
            
        Returns:
            True if the key exists, False otherwise
            
        Raises:
            StateError: If there's an error accessing the state
        """
        try:
            # Check if the key exists in Redis
            redis_key = self._make_key(agent_id, key)
            return bool(self.redis.exists(redis_key))
            
        except RedisError as e:
            logger.error(f"Redis error checking state for agent {agent_id}, key {key}: {e}")
            raise StateError(f"Redis error: {e}") from e
    
    def keys(self, agent_id: str) -> List[str]:
        """
        Get all state keys for an agent.
        
        Args:
            agent_id: Agent identifier
            
        Returns:
            List of state keys
            
        Raises:
            StateError: If there's an error accessing the state
        """
        try:
            # Get all keys for the agent
            pattern = self._make_key(agent_id, "*")
            redis_keys = self.redis.keys(pattern)
            
            # Extract the key part from the Redis keys
            prefix_len = len(self._make_key(agent_id, ""))
            return [key.decode('utf-8')[prefix_len:] for key in redis_keys]
            
        except RedisError as e:
            logger.error(f"Redis error listing keys for agent {agent_id}: {e}")
            raise StateError(f"Redis error: {e}") from e
    
    def get_bulk_state(self, agent_id: str, keys: List[str]) -> Dict[str, Any]:
        """
        Get multiple state values by keys.
        
        Args:
            agent_id: Agent identifier
            keys: List of state keys
            
        Returns:
            Dictionary of key-value pairs
            
        Raises:
            StateError: If there's an error accessing the state
        """
        if not keys:
            return {}
            
        try:
            # Get all values in a single operation
            redis_keys = [self._make_key(agent_id, key) for key in keys]
            values = self.redis.mget(redis_keys)
            
            # Deserialize values
            result = {}
            for i, value in enumerate(values):
                if value is not None:
                    try:
                        result[keys[i]] = self.serializer.deserialize(value)
                    except StateDeserializationError as e:
                        logger.error(f"Error deserializing state for agent {agent_id}, key {keys[i]}: {e}")
                        raise
            
            return result
            
        except RedisError as e:
            logger.error(f"Redis error bulk getting state for agent {agent_id}: {e}")
            raise StateError(f"Redis error: {e}") from e
    
    def set_bulk_state(self, agent_id: str, key_values: Dict[str, Any]) -> None:
        """
        Set multiple state values.
        
        Args:
            agent_id: Agent identifier
            key_values: Dictionary of key-value pairs
            
        Raises:
            StateError: If there's an error accessing the state
        """
        if not key_values:
            return
            
        try:
            # Prepare key-value pairs for Redis
            redis_key_values = {}
            for key, value in key_values.items():
                serialized_value = self.serializer.serialize(value)
                redis_key = self._make_key(agent_id, key)
                redis_key_values[redis_key] = serialized_value
            
            if self._transaction is not None:
                # Add to transaction
                for redis_key, serialized_value in redis_key_values.items():
                    self._transaction['operations'].append(
                        ('set', redis_key, serialized_value)
                    )
            else:
                # Execute immediately
                self.redis.mset(redis_key_values)
                
        except StateSerializationError as e:
            logger.error(f"Error serializing state for agent {agent_id}: {e}")
            raise
        except RedisError as e:
            logger.error(f"Redis error bulk setting state for agent {agent_id}: {e}")
            raise StateError(f"Redis error: {e}") from e
    
    def begin_transaction(self) -> Dict:
        """
        Begin a new transaction.
        
        Returns:
            Transaction context object
            
        Raises:
            StateError: If there's an error starting the transaction
        """
        if self._transaction is not None:
            raise StateError("Transaction already in progress")
        
        # Create a new transaction
        self._transaction = {
            'operations': [],
            'watch_keys': set(),
        }
        
        return self._transaction
    
    def commit_transaction(self) -> None:
        """
        Commit the current transaction.
        
        Raises:
            StateError: If there's no transaction in progress or an error committing
        """
        if self._transaction is None:
            raise StateError("No transaction in progress")
        
        try:
            # Start a pipeline
            pipeline = self.redis.pipeline(transaction=True)
            
            # Watch keys if any
            if self._transaction['watch_keys']:
                pipeline.watch(*self._transaction['watch_keys'])
            
            # Add operations to the pipeline
            for operation in self._transaction['operations']:
                if operation[0] == 'set':
                    pipeline.set(operation[1], operation[2])
                elif operation[0] == 'delete':
                    pipeline.delete(operation[1])
            
            # Execute the pipeline
            pipeline.execute()
            
        except RedisError as e:
            logger.error(f"Redis error committing transaction: {e}")
            raise StateError(f"Redis error: {e}") from e
        finally:
            # Clear the transaction
            self._transaction = None
    
    def rollback_transaction(self) -> None:
        """
        Rollback the current transaction.
        
        Raises:
            StateError: If there's no transaction in progress
        """
        if self._transaction is None:
            raise StateError("No transaction in progress")
        
        # Just clear the transaction
        self._transaction = None
    
    def validate_state(self, agent_id: str) -> bool:
        """
        Validate the state for an agent.
        
        Args:
            agent_id: Agent identifier
            
        Returns:
            True if the state is valid, False otherwise
        """
        try:
            # Get all keys for the agent
            pattern = self._make_key(agent_id, "*")
            keys = self.redis.keys(pattern)
            
            # Try to deserialize each value
            for key in keys:
                value = self.redis.get(key)
                try:
                    self.serializer.deserialize(value)
                except StateDeserializationError:
                    return False
            
            return True
            
        except RedisError:
            return False
    
    def create_backup(self, agent_id: str) -> str:
        """
        Create a backup of the agent's state.
        
        Args:
            agent_id: Agent identifier
            
        Returns:
            Backup identifier
            
        Raises:
            StateError: If there's an error creating the backup
        """
        try:
            # Generate backup ID
            backup_id = f"backup_{agent_id}_{int(datetime.now().timestamp())}"
            
            # Get all keys for the agent
            pattern = self._make_key(agent_id, "*")
            keys = self.redis.keys(pattern)
            
            if not keys:
                # No state to backup
                return backup_id
            
            # Get all values
            values = self.redis.mget(keys)
            
            # Prepare backup data
            backup_data = {}
            for i, key in enumerate(keys):
                if values[i] is not None:
                    # Extract the key part from the Redis key
                    prefix_len = len(self._make_key(agent_id, ""))
                    state_key = key.decode('utf-8')[prefix_len:]
                    
                    try:
                        backup_data[state_key] = self.serializer.deserialize(values[i])
                    except StateDeserializationError as e:
                        logger.error(f"Error deserializing state for backup, key {key}: {e}")
                        raise
            
            # Serialize the backup data
            serialized_backup = json.dumps(backup_data)
            
            # Store the backup
            backup_key = f"{self.key_prefix}backup:{agent_id}:{backup_id}"
            self.redis.set(backup_key, serialized_backup)
            
            # Set expiration if configured
            if hasattr(self, 'backup_expiration') and self.backup_expiration > 0:
                self.redis.expire(backup_key, self.backup_expiration)
            
            return backup_id
            
        except (StateSerializationError, StateDeserializationError) as e:
            logger.error(f"Error serializing backup for agent {agent_id}: {e}")
            raise
        except RedisError as e:
            logger.error(f"Redis error creating backup for agent {agent_id}: {e}")
            raise StateError(f"Redis error: {e}") from e
    
    def restore_backup(self, agent_id: str, backup_id: str) -> bool:
        """
        Restore a backup of the agent's state.
        
        Args:
            agent_id: Agent identifier
            backup_id: Backup identifier
            
        Returns:
            True if the backup was restored, False otherwise
            
        Raises:
            StateError: If there's an error restoring the backup
        """
        try:
            # Get the backup
            backup_key = f"{self.key_prefix}backup:{agent_id}:{backup_id}"
            serialized_backup = self.redis.get(backup_key)
            
            if serialized_backup is None:
                return False
            
            # Parse the backup data
            backup_data = json.loads(serialized_backup)
            
            # Start a pipeline for atomic restore
            pipeline = self.redis.pipeline(transaction=True)
            
            # Clear existing state
            pattern = self._make_key(agent_id, "*")
            keys = self.redis.keys(pattern)
            if keys:
                pipeline.delete(*keys)
            
            # Restore state from backup
            for key, value in backup_data.items():
                redis_key = self._make_key(agent_id, key)
                serialized_value = self.serializer.serialize(value)
                pipeline.set(redis_key, serialized_value)
            
            # Execute the pipeline
            pipeline.execute()
            
            return True
            
        except (json.JSONDecodeError, StateSerializationError) as e:
            logger.error(f"Error deserializing backup for agent {agent_id}: {e}")
            raise StateError(f"Backup data error: {e}") from e
        except RedisError as e:
            logger.error(f"Redis error restoring backup for agent {agent_id}: {e}")
            raise StateError(f"Redis error: {e}") from e
    
    def _make_key(self, agent_id: str, key: str) -> str:
        """
        Create a Redis key from agent ID and state key.
        
        Args:
            agent_id: Agent identifier
            key: State key
            
        Returns:
            Redis key
        """
        return f"{self.key_prefix}{agent_id}:{key}"
    
    def acquire_lock(self, lock_name: str, timeout: Optional[int] = None) -> bool:
        """
        Acquire a distributed lock.
        
        Args:
            lock_name: Name of the lock
            timeout: Lock timeout in seconds (defaults to self.lock_timeout)
            
        Returns:
            True if the lock was acquired, False otherwise
        """
        if timeout is None:
            timeout = self.lock_timeout
            
        lock_key = f"{self.key_prefix}lock:{lock_name}"
        lock_value = str(uuid.uuid4())
        
        # Store the lock value for release
        if not hasattr(self, '_locks'):
            self._locks = {}
        self._locks[lock_name] = lock_value
        
        # Try to acquire the lock with NX (only set if not exists)
        return bool(self.redis.set(
            lock_key, 
            lock_value, 
            ex=timeout, 
            nx=True
        ))
    
    def release_lock(self, lock_name: str) -> bool:
        """
        Release a distributed lock.
        
        Args:
            lock_name: Name of the lock
            
        Returns:
            True if the lock was released, False otherwise
        """
        if not hasattr(self, '_locks') or lock_name not in self._locks:
            return False
            
        lock_key = f"{self.key_prefix}lock:{lock_name}"
        lock_value = self._locks[lock_name]
        
        # Use Lua script to ensure we only delete our own lock
        script = """
        if redis.call('get', KEYS[1]) == ARGV[1] then
            return redis.call('del', KEYS[1])
        else
            return 0
        end
        """
        
        result = self.redis.eval(script, 1, lock_key, lock_value)
        
        # Clean up
        if lock_name in self._locks:
            del self._locks[lock_name]
            
        return bool(result)
    
    def set_backup_expiration(self, days: int) -> None:
        """
        Set expiration time for backups.
        
        Args:
            days: Number of days to keep backups
        """
        self.backup_expiration = days * 24 * 60 * 60  # Convert to seconds 