"""
State management utilities for OpenAgents JSON agents.

This module provides utilities for managing agent state, including
state persistence, retrieval, and manipulation.
"""

import json
import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Union

logger = logging.getLogger(__name__)


class AgentStateManager:
    """
    Manages state for agents.
    
    This class provides methods for saving, loading, and manipulating
    agent state across executions.
    """
    
    def __init__(self, storage_dir: Optional[Union[str, Path]] = None):
        """
        Initialize the state manager.
        
        Args:
            storage_dir: Optional directory for storing state files
        """
        self.storage_dir = Path(storage_dir or os.environ.get("AGENT_STATE_DIR", ".agent_states"))
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        
        self.states: Dict[str, Dict[str, Any]] = {}
    
    def get_state(self, agent_id: str, session_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get the state for an agent.
        
        Args:
            agent_id: ID of the agent
            session_id: Optional session ID
            
        Returns:
            The agent state
        """
        key = self._get_key(agent_id, session_id)
        
        # Check if state is in memory
        if key in self.states:
            return self.states[key]
        
        # Try to load from disk
        state_file = self._get_state_file(agent_id, session_id)
        if state_file.exists():
            try:
                with open(state_file, "r") as f:
                    state = json.load(f)
                self.states[key] = state
                return state
            except Exception as e:
                logger.warning(f"Error loading state for {key}: {str(e)}")
        
        # Return empty state if not found
        self.states[key] = {
            "agent_id": agent_id,
            "session_id": session_id,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "memory": {},
            "context": {}
        }
        
        return self.states[key]
    
    def update_state(
        self,
        agent_id: str,
        updates: Dict[str, Any],
        session_id: Optional[str] = None,
        save: bool = True
    ) -> Dict[str, Any]:
        """
        Update the state for an agent.
        
        Args:
            agent_id: ID of the agent
            updates: Dictionary of updates to apply
            session_id: Optional session ID
            save: Whether to save the state to disk
            
        Returns:
            The updated state
        """
        state = self.get_state(agent_id, session_id)
        
        # Apply updates
        for key, value in updates.items():
            if key in ("memory", "context") and isinstance(value, dict):
                # Merge dictionaries for memory and context
                state[key] = {**state.get(key, {}), **value}
            else:
                state[key] = value
        
        # Update timestamp
        state["updated_at"] = datetime.now().isoformat()
        
        # Save to disk if requested
        if save:
            self.save_state(agent_id, session_id)
        
        return state
    
    def save_state(self, agent_id: str, session_id: Optional[str] = None) -> bool:
        """
        Save the state for an agent to disk.
        
        Args:
            agent_id: ID of the agent
            session_id: Optional session ID
            
        Returns:
            True if the state was saved successfully, False otherwise
        """
        key = self._get_key(agent_id, session_id)
        
        if key not in self.states:
            logger.warning(f"No state found for {key}")
            return False
        
        state_file = self._get_state_file(agent_id, session_id)
        
        try:
            with open(state_file, "w") as f:
                json.dump(self.states[key], f, indent=2)
            return True
        except Exception as e:
            logger.error(f"Error saving state for {key}: {str(e)}")
            return False
    
    def clear_state(self, agent_id: str, session_id: Optional[str] = None) -> bool:
        """
        Clear the state for an agent.
        
        Args:
            agent_id: ID of the agent
            session_id: Optional session ID
            
        Returns:
            True if the state was cleared successfully, False otherwise
        """
        key = self._get_key(agent_id, session_id)
        
        # Remove from memory
        if key in self.states:
            del self.states[key]
        
        # Remove from disk
        state_file = self._get_state_file(agent_id, session_id)
        if state_file.exists():
            try:
                state_file.unlink()
                return True
            except Exception as e:
                logger.error(f"Error deleting state file for {key}: {str(e)}")
                return False
        
        return True
    
    def list_agent_sessions(self, agent_id: str) -> List[str]:
        """
        List all session IDs for an agent.
        
        Args:
            agent_id: ID of the agent
            
        Returns:
            List of session IDs
        """
        prefix = f"{agent_id}_"
        sessions = []
        
        for key in self.states:
            if key.startswith(prefix) and "_" in key:
                sessions.append(key.split("_", 1)[1])
        
        # Also check disk
        for file in self.storage_dir.glob(f"{prefix}*.json"):
            session_id = file.stem.split("_", 1)[1] if "_" in file.stem else None
            if session_id and session_id not in sessions:
                sessions.append(session_id)
        
        return sessions
    
    def _get_key(self, agent_id: str, session_id: Optional[str] = None) -> str:
        """
        Get the key for an agent state.
        
        Args:
            agent_id: ID of the agent
            session_id: Optional session ID
            
        Returns:
            The state key
        """
        return f"{agent_id}_{session_id}" if session_id else agent_id
    
    def _get_state_file(self, agent_id: str, session_id: Optional[str] = None) -> Path:
        """
        Get the file path for an agent state.
        
        Args:
            agent_id: ID of the agent
            session_id: Optional session ID
            
        Returns:
            The state file path
        """
        key = self._get_key(agent_id, session_id)
        return self.storage_dir / f"{key}.json" 