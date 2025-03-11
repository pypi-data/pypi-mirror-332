"""
Serialization utilities for OpenAgents JSON agents.

This module provides utilities for serializing and deserializing agents,
including saving and loading agent definitions and state.
"""

import json
import logging
import pickle
import os
from pathlib import Path
from typing import Any, Dict, Optional, Type, Union

from openagents_json.agent.base import BaseAgent

logger = logging.getLogger(__name__)


def serialize_agent(
    agent: BaseAgent,
    output_dir: Union[str, Path],
    include_state: bool = True,
    format: str = "json",
) -> Dict[str, str]:
    """
    Serialize an agent to disk.
    
    Args:
        agent: The agent to serialize
        output_dir: Directory to save serialized agent
        include_state: Whether to include agent state
        format: Serialization format (json or pickle)
        
    Returns:
        Dictionary with paths to serialized files
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    result = {}
    
    # Store agent definition
    definition = {
        "name": agent.name,
        "agent_id": agent.agent_id,
        "type": agent.__class__.__name__,
        "metadata": {
            "description": agent.metadata.description,
            "version": agent.metadata.version,
            "author": agent.metadata.author,
            "tags": list(agent.metadata.tags)
        }
    }
    
    # Add class-specific attributes
    if hasattr(agent, "model"):
        definition["model"] = agent.model
    
    if hasattr(agent, "tools") and agent.tools:
        definition["tools"] = list(agent.tools.keys())
    
    if hasattr(agent, "workflow_id") and agent.workflow_id:
        definition["workflow_id"] = agent.workflow_id
    
    # Capabilities
    if agent.capabilities:
        definition["capabilities"] = list(agent.capabilities.keys())
    
    # Serialize definition to JSON
    definition_path = output_dir / f"{agent.name}_definition.json"
    with open(definition_path, "w") as f:
        json.dump(definition, f, indent=2)
    
    result["definition"] = str(definition_path)
    
    # Serialize state if requested
    if include_state:
        state_dict = {
            "agent_id": agent.state.agent_id,
            "session_id": agent.state.session_id,
            "created_at": agent.state.created_at.isoformat(),
            "updated_at": agent.state.updated_at.isoformat(),
            "memory": agent.state.memory,
            "context": agent.state.context,
            "metadata": agent.state.metadata
        }
        
        state_path = output_dir / f"{agent.name}_state.json"
        with open(state_path, "w") as f:
            json.dump(state_dict, f, indent=2)
        
        result["state"] = str(state_path)
    
    # If format is pickle, serialize the full agent
    if format == "pickle":
        try:
            pickle_path = output_dir / f"{agent.name}.pkl"
            with open(pickle_path, "wb") as f:
                pickle.dump(agent, f)
            result["pickle"] = str(pickle_path)
        except Exception as e:
            logger.warning(f"Failed to pickle agent: {str(e)}")
    
    return result


def deserialize_agent(
    definition_path: Union[str, Path],
    agent_class: Optional[Type[BaseAgent]] = None,
    state_path: Optional[Union[str, Path]] = None,
    pickle_path: Optional[Union[str, Path]] = None,
) -> Optional[BaseAgent]:
    """
    Deserialize an agent from disk.
    
    Args:
        definition_path: Path to the agent definition JSON
        agent_class: Optional agent class (required unless pickle_path is provided)
        state_path: Optional path to the agent state JSON
        pickle_path: Optional path to a pickled agent
        
    Returns:
        The deserialized agent, or None if deserialization failed
    """
    # Try loading from pickle first if path is provided
    if pickle_path:
        try:
            with open(pickle_path, "rb") as f:
                agent = pickle.load(f)
            
            logger.info(f"Loaded agent from pickle: {agent.name}")
            return agent
        except Exception as e:
            logger.warning(f"Failed to load agent from pickle: {str(e)}")
    
    # If we don't have an agent class and pickle failed, we can't deserialize
    if not agent_class:
        logger.error("Cannot deserialize agent: no agent_class provided and pickle failed")
        return None
    
    # Load agent definition
    try:
        with open(definition_path, "r") as f:
            definition = json.load(f)
    except Exception as e:
        logger.error(f"Failed to load agent definition: {str(e)}")
        return None
    
    # Create agent with basic parameters
    try:
        # Get the required parameters for the agent class
        required_params = {}
        if hasattr(agent_class, "__init__"):
            import inspect
            sig = inspect.signature(agent_class.__init__)
            for param_name, param in sig.parameters.items():
                if param_name == "self":
                    continue
                    
                if param.default == inspect.Parameter.empty:
                    if param_name == "name":
                        required_params["name"] = definition.get("name", "unnamed_agent")
                    elif param_name == "model" and "model" in definition:
                        required_params["model"] = definition["model"]
                    elif param_name == "workflow_id" and "workflow_id" in definition:
                        required_params["workflow_id"] = definition["workflow_id"]
        
        # Create the agent
        agent = agent_class(**required_params)
        
        # Restore basic attributes
        agent.agent_id = definition.get("agent_id", agent.agent_id)
        agent.name = definition.get("name", agent.name)
        
        # Restore tools if applicable
        if hasattr(agent, "tools") and "tools" in definition:
            for tool_name in definition["tools"]:
                # Note: This only restores the tool names, not the implementation
                # The actual tool functions would need to be registered separately
                logger.info(f"Tool {tool_name} needs to be registered separately")
        
        # Restore capabilities if applicable
        if "capabilities" in definition:
            for capability_name in definition["capabilities"]:
                # Note: This only restores the capability names, not the implementation
                # The actual capability functions would need to be registered separately
                logger.info(f"Capability {capability_name} needs to be registered separately")
        
        # Restore state if provided
        if state_path:
            try:
                with open(state_path, "r") as f:
                    state_dict = json.load(f)
                
                # Update basic state attributes
                agent.state.agent_id = state_dict.get("agent_id", agent.state.agent_id)
                agent.state.session_id = state_dict.get("session_id", agent.state.session_id)
                
                # Update memory and context
                if "memory" in state_dict:
                    agent.state.memory = state_dict["memory"]
                if "context" in state_dict:
                    agent.state.context = state_dict["context"]
                if "metadata" in state_dict:
                    agent.state.metadata = state_dict["metadata"]
            except Exception as e:
                logger.warning(f"Failed to restore agent state: {str(e)}")
        
        return agent
        
    except Exception as e:
        logger.error(f"Failed to create agent: {str(e)}")
        return None


def agent_to_dict(agent: BaseAgent) -> Dict[str, Any]:
    """
    Convert an agent to a dictionary representation.
    
    Args:
        agent: The agent to convert
        
    Returns:
        Dictionary representation of the agent
    """
    result = {
        "name": agent.name,
        "agent_id": agent.agent_id,
        "type": agent.__class__.__name__,
        "metadata": {
            "description": agent.metadata.description,
            "version": agent.metadata.version,
            "author": agent.metadata.author,
            "tags": list(agent.metadata.tags)
        },
        "capabilities": list(agent.capabilities.keys())
    }
    
    # Add class-specific attributes
    if hasattr(agent, "model"):
        result["model"] = agent.model
    
    if hasattr(agent, "tools") and agent.tools:
        result["tools"] = list(agent.tools.keys())
    
    if hasattr(agent, "workflow_id") and agent.workflow_id:
        result["workflow_id"] = agent.workflow_id
    
    return result 