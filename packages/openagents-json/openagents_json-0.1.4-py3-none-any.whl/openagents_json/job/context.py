"""
Job context for OpenAgents JSON.

This module provides the JobContext class for tracking job execution context,
including state checkpoints for agent state persistence.
"""

import json
import logging
import time
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

logger = logging.getLogger(__name__)


@dataclass
class JobContext:
    """
    Context information for job execution.
    
    JobContext tracks information about a job execution, including state
    checkpoints for agent state persistence across workflow steps.
    """
    
    job_id: str
    step_id: Optional[str] = None
    agent_id: Optional[str] = None
    workflow_id: Optional[str] = None
    parent_job_id: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)
    state_checkpoint: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert to dictionary for serialization.
        
        Returns:
            Dictionary representation of the context
        """
        return {
            "job_id": self.job_id,
            "step_id": self.step_id,
            "agent_id": self.agent_id,
            "workflow_id": self.workflow_id,
            "parent_job_id": self.parent_job_id,
            "created_at": self.created_at.isoformat(),
            "metadata": self.metadata,
            "state_checkpoint": self.state_checkpoint,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "JobContext":
        """
        Create from dictionary after deserialization.
        
        Args:
            data: Dictionary representation of the context
            
        Returns:
            JobContext instance
        """
        # Handle datetime conversion
        if "created_at" in data and isinstance(data["created_at"], str):
            data["created_at"] = datetime.fromisoformat(data["created_at"])
        
        return cls(**data)
    
    def __str__(self) -> str:
        """Return a string representation of the context."""
        return f"JobContext(job_id={self.job_id}, step_id={self.step_id}, agent_id={self.agent_id})"
    
    def update(self, **kwargs) -> None:
        """
        Update context attributes.
        
        Args:
            **kwargs: Key-value pairs to update
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                self.metadata[key] = value
    
    def create_checkpoint(self) -> str:
        """
        Create a new state checkpoint ID.
        
        Returns:
            Checkpoint ID
        """
        checkpoint_id = f"{self.job_id}_{self.step_id}_{int(time.time())}"
        self.state_checkpoint = checkpoint_id
        return checkpoint_id 