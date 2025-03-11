"""
Database state manager implementation using SQLAlchemy.

This module provides a database-backed implementation of the StateManager interface
for persistent state storage in production environments.
"""

import json
import logging
import uuid
from contextlib import contextmanager
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Union

import sqlalchemy as sa
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

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

# Define the base model class
Base = declarative_base()


class StateEntry(Base):
    """Database model for state entries."""
    
    __tablename__ = "agent_state"
    
    id = sa.Column(sa.String(255), primary_key=True)
    agent_id = sa.Column(sa.String(255), index=True, nullable=False)
    key = sa.Column(sa.String(255), index=True, nullable=False)
    value = sa.Column(sa.Text, nullable=True)
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now)
    version = sa.Column(sa.Integer, default=1)
    
    __table_args__ = (
        sa.UniqueConstraint('agent_id', 'key', name='uix_agent_key'),
    )


class StateBackup(Base):
    """Database model for state backups."""
    
    __tablename__ = "agent_state_backup"
    
    id = sa.Column(sa.String(255), primary_key=True)
    agent_id = sa.Column(sa.String(255), index=True, nullable=False)
    backup_id = sa.Column(sa.String(255), index=True, nullable=False)
    data = sa.Column(sa.Text, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    
    __table_args__ = (
        sa.UniqueConstraint('agent_id', 'backup_id', name='uix_agent_backup'),
    )


class DatabaseStateManager(StateManager):
    """
    Database implementation of the StateManager interface.
    
    This class provides a persistent state manager backed by a SQL database
    through SQLAlchemy. It supports all state operations with transaction support.
    """
    
    def __init__(
        self,
        database_url: Optional[str] = None,
        serializer_name: str = "json",
        use_locking: bool = True,
        create_tables: bool = True,
    ):
        """
        Initialize the database state manager.
        
        Args:
            database_url: Database connection URL (defaults to settings)
            serializer_name: Name of the serializer to use
            use_locking: Whether to use row-level locking for concurrency control
            create_tables: Whether to automatically create tables if they don't exist
        """
        settings = get_settings()
        
        # Use provided database_url or get from settings
        if database_url is None:
            if settings.state.database_url:
                database_url = settings.state.database_url
            else:
                # Construct from database settings
                db = settings.storage.database
                if db.connection_string:
                    database_url = db.connection_string
                elif db.dialect == "sqlite":
                    database_url = f"sqlite:///{db.path}"
                else:
                    port = f":{db.port}" if db.port else ""
                    password = f":{db.password.get_secret_value()}" if db.password else ""
                    database_url = (
                        f"{db.dialect}://{db.username}{password}@{db.host}{port}/{db.name}"
                    )
        
        # Initialize SQLAlchemy engine and session factory
        self.engine = sa.create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)
        
        # Create tables if needed
        if create_tables:
            Base.metadata.create_all(self.engine)
        
        # Get the specified serializer
        self.serializer = get_serializer(serializer_name)
        self.use_locking = use_locking
        
        # Thread-local storage for transactions
        self._transaction = None
    
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
            session = self._get_session()
            
            # Get the state entry
            entry = self._get_entry(session, agent_id, key)
            if entry is None:
                return default
            
            # Deserialize the value
            return self.serializer.deserialize(entry.value)
            
        except StateDeserializationError as e:
            logger.error(f"Error deserializing state for agent {agent_id}, key {key}: {e}")
            raise
        except SQLAlchemyError as e:
            logger.error(f"Database error getting state for agent {agent_id}, key {key}: {e}")
            raise StateError(f"Database error: {e}") from e
        finally:
            if self._transaction is None:
                session.close()
    
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
            session = self._get_session()
            
            # Serialize the value
            serialized_value = self.serializer.serialize(value)
            
            # Check if entry exists
            entry = self._get_entry(session, agent_id, key)
            
            if entry:
                # Update existing entry
                entry.value = serialized_value
                entry.updated_at = datetime.now()
                entry.version += 1
            else:
                # Create new entry
                entry = StateEntry(
                    id=str(uuid.uuid4()),
                    agent_id=agent_id,
                    key=key,
                    value=serialized_value,
                )
                session.add(entry)
            
            if self._transaction is None:
                session.commit()
                
        except StateSerializationError as e:
            logger.error(f"Error serializing state for agent {agent_id}, key {key}: {e}")
            if self._transaction is None:
                session.rollback()
            raise
        except SQLAlchemyError as e:
            logger.error(f"Database error setting state for agent {agent_id}, key {key}: {e}")
            if self._transaction is None:
                session.rollback()
            raise StateError(f"Database error: {e}") from e
        finally:
            if self._transaction is None:
                session.close()
    
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
            session = self._get_session()
            
            # Delete the entry
            entry = self._get_entry(session, agent_id, key)
            if entry:
                session.delete(entry)
                
                if self._transaction is None:
                    session.commit()
                
        except SQLAlchemyError as e:
            logger.error(f"Database error deleting state for agent {agent_id}, key {key}: {e}")
            if self._transaction is None:
                session.rollback()
            raise StateError(f"Database error: {e}") from e
        finally:
            if self._transaction is None:
                session.close()
    
    def clear_state(self, agent_id: str) -> None:
        """
        Clear all state for an agent.
        
        Args:
            agent_id: Agent identifier
            
        Raises:
            StateError: If there's an error accessing the state
        """
        try:
            session = self._get_session()
            
            # Delete all entries for the agent
            session.query(StateEntry).filter(StateEntry.agent_id == agent_id).delete()
            
            if self._transaction is None:
                session.commit()
                
        except SQLAlchemyError as e:
            logger.error(f"Database error clearing state for agent {agent_id}: {e}")
            if self._transaction is None:
                session.rollback()
            raise StateError(f"Database error: {e}") from e
        finally:
            if self._transaction is None:
                session.close()
    
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
            session = self._get_session()
            
            # Query for the entry
            exists = session.query(sa.exists().where(
                sa.and_(
                    StateEntry.agent_id == agent_id,
                    StateEntry.key == key
                )
            )).scalar()
            
            return exists
            
        except SQLAlchemyError as e:
            logger.error(f"Database error checking state for agent {agent_id}, key {key}: {e}")
            raise StateError(f"Database error: {e}") from e
        finally:
            if self._transaction is None:
                session.close()
    
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
            session = self._get_session()
            
            # Query for all keys
            keys = session.query(StateEntry.key).filter(
                StateEntry.agent_id == agent_id
            ).all()
            
            return [key[0] for key in keys]
            
        except SQLAlchemyError as e:
            logger.error(f"Database error listing keys for agent {agent_id}: {e}")
            raise StateError(f"Database error: {e}") from e
        finally:
            if self._transaction is None:
                session.close()
    
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
        try:
            session = self._get_session()
            
            # Query for entries
            entries = session.query(StateEntry).filter(
                sa.and_(
                    StateEntry.agent_id == agent_id,
                    StateEntry.key.in_(keys)
                )
            ).all()
            
            # Deserialize values
            result = {}
            for entry in entries:
                try:
                    result[entry.key] = self.serializer.deserialize(entry.value)
                except StateDeserializationError as e:
                    logger.error(f"Error deserializing state for agent {agent_id}, key {entry.key}: {e}")
                    raise
            
            return result
            
        except SQLAlchemyError as e:
            logger.error(f"Database error bulk getting state for agent {agent_id}: {e}")
            raise StateError(f"Database error: {e}") from e
        finally:
            if self._transaction is None:
                session.close()
    
    def set_bulk_state(self, agent_id: str, key_values: Dict[str, Any]) -> None:
        """
        Set multiple state values.
        
        Args:
            agent_id: Agent identifier
            key_values: Dictionary of key-value pairs
            
        Raises:
            StateError: If there's an error accessing the state
        """
        try:
            session = self._get_session()
            
            # Get existing entries
            existing_keys = [key for key, _ in key_values.items()]
            existing_entries = session.query(StateEntry).filter(
                sa.and_(
                    StateEntry.agent_id == agent_id,
                    StateEntry.key.in_(existing_keys)
                )
            ).all()
            
            # Create a map of existing entries
            entry_map = {entry.key: entry for entry in existing_entries}
            
            # Update or create entries
            for key, value in key_values.items():
                serialized_value = self.serializer.serialize(value)
                
                if key in entry_map:
                    # Update existing entry
                    entry = entry_map[key]
                    entry.value = serialized_value
                    entry.updated_at = datetime.now()
                    entry.version += 1
                else:
                    # Create new entry
                    entry = StateEntry(
                        id=str(uuid.uuid4()),
                        agent_id=agent_id,
                        key=key,
                        value=serialized_value,
                    )
                    session.add(entry)
            
            if self._transaction is None:
                session.commit()
                
        except StateSerializationError as e:
            logger.error(f"Error serializing state for agent {agent_id}: {e}")
            if self._transaction is None:
                session.rollback()
            raise
        except SQLAlchemyError as e:
            logger.error(f"Database error bulk setting state for agent {agent_id}: {e}")
            if self._transaction is None:
                session.rollback()
            raise StateError(f"Database error: {e}") from e
        finally:
            if self._transaction is None:
                session.close()
    
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
        
        try:
            # Create a new session
            session = self.Session()
            
            # Start a transaction
            self._transaction = {
                'session': session,
                'operations': [],
            }
            
            return self._transaction
            
        except SQLAlchemyError as e:
            logger.error(f"Database error beginning transaction: {e}")
            raise StateError(f"Database error: {e}") from e
    
    def commit_transaction(self) -> None:
        """
        Commit the current transaction.
        
        Raises:
            StateError: If there's no transaction in progress or an error committing
        """
        if self._transaction is None:
            raise StateError("No transaction in progress")
        
        try:
            # Commit the transaction
            self._transaction['session'].commit()
            
        except SQLAlchemyError as e:
            logger.error(f"Database error committing transaction: {e}")
            self._transaction['session'].rollback()
            raise StateError(f"Database error: {e}") from e
        finally:
            # Close the session and clear the transaction
            self._transaction['session'].close()
            self._transaction = None
    
    def rollback_transaction(self) -> None:
        """
        Rollback the current transaction.
        
        Raises:
            StateError: If there's no transaction in progress or an error rolling back
        """
        if self._transaction is None:
            raise StateError("No transaction in progress")
        
        try:
            # Rollback the transaction
            self._transaction['session'].rollback()
            
        except SQLAlchemyError as e:
            logger.error(f"Database error rolling back transaction: {e}")
            raise StateError(f"Database error: {e}") from e
        finally:
            # Close the session and clear the transaction
            self._transaction['session'].close()
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
            session = self._get_session()
            
            # Query for entries
            entries = session.query(StateEntry).filter(
                StateEntry.agent_id == agent_id
            ).all()
            
            # Try to deserialize each entry
            for entry in entries:
                try:
                    self.serializer.deserialize(entry.value)
                except StateDeserializationError:
                    return False
            
            return True
            
        except SQLAlchemyError:
            return False
        finally:
            if self._transaction is None:
                session.close()
    
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
            session = self._get_session()
            
            # Generate backup ID
            backup_id = f"backup_{agent_id}_{int(datetime.now().timestamp())}"
            
            # Get all entries for the agent
            entries = session.query(StateEntry).filter(
                StateEntry.agent_id == agent_id
            ).all()
            
            # Prepare backup data
            backup_data = {
                entry.key: self.serializer.deserialize(entry.value)
                for entry in entries
            }
            
            # Serialize the backup data
            serialized_backup = json.dumps(backup_data)
            
            # Create backup entry
            backup = StateBackup(
                id=str(uuid.uuid4()),
                agent_id=agent_id,
                backup_id=backup_id,
                data=serialized_backup,
            )
            session.add(backup)
            
            if self._transaction is None:
                session.commit()
            
            return backup_id
            
        except (StateSerializationError, StateDeserializationError) as e:
            logger.error(f"Error serializing backup for agent {agent_id}: {e}")
            if self._transaction is None:
                session.rollback()
            raise
        except SQLAlchemyError as e:
            logger.error(f"Database error creating backup for agent {agent_id}: {e}")
            if self._transaction is None:
                session.rollback()
            raise StateError(f"Database error: {e}") from e
        finally:
            if self._transaction is None:
                session.close()
    
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
            session = self._get_session()
            
            # Get the backup
            backup = session.query(StateBackup).filter(
                sa.and_(
                    StateBackup.agent_id == agent_id,
                    StateBackup.backup_id == backup_id
                )
            ).first()
            
            if not backup:
                return False
            
            # Parse the backup data
            backup_data = json.loads(backup.data)
            
            # Start a nested transaction for the restore
            with session.begin_nested():
                # Clear existing state
                session.query(StateEntry).filter(
                    StateEntry.agent_id == agent_id
                ).delete()
                
                # Restore state from backup
                for key, value in backup_data.items():
                    serialized_value = self.serializer.serialize(value)
                    entry = StateEntry(
                        id=str(uuid.uuid4()),
                        agent_id=agent_id,
                        key=key,
                        value=serialized_value,
                    )
                    session.add(entry)
            
            if self._transaction is None:
                session.commit()
            
            return True
            
        except (json.JSONDecodeError, StateSerializationError) as e:
            logger.error(f"Error deserializing backup for agent {agent_id}: {e}")
            if self._transaction is None:
                session.rollback()
            raise StateError(f"Backup data error: {e}") from e
        except SQLAlchemyError as e:
            logger.error(f"Database error restoring backup for agent {agent_id}: {e}")
            if self._transaction is None:
                session.rollback()
            raise StateError(f"Database error: {e}") from e
        finally:
            if self._transaction is None:
                session.close()
    
    def _get_session(self) -> Session:
        """
        Get the current session or create a new one.
        
        Returns:
            SQLAlchemy session
        """
        if self._transaction is not None:
            return self._transaction['session']
        else:
            return self.Session()
    
    def _get_entry(self, session: Session, agent_id: str, key: str) -> Optional[StateEntry]:
        """
        Get a state entry by agent and key.
        
        Args:
            session: SQLAlchemy session
            agent_id: Agent identifier
            key: State key
            
        Returns:
            StateEntry object or None if not found
        """
        query = session.query(StateEntry).filter(
            sa.and_(
                StateEntry.agent_id == agent_id,
                StateEntry.key == key
            )
        )
        
        # Apply locking if enabled
        if self.use_locking and self._transaction is not None:
            query = query.with_for_update()
        
        return query.first() 