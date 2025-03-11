"""
Configuration system for OpenAgents JSON agents.

This module provides utilities for configuring agents, including loading
configuration from various sources, validation, and management.
"""

import json
import logging
import os
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Type, Union, get_type_hints

import yaml
from pydantic import BaseModel, Field, ValidationError

logger = logging.getLogger(__name__)


class AgentConfigError(Exception):
    """Exception raised for agent configuration errors."""
    pass


class AgentConfigModel(BaseModel):
    """Base Pydantic model for agent configuration."""
    
    name: str = Field(..., description="The name of the agent")
    description: str = Field("", description="Description of the agent")
    version: str = Field("0.1.0", description="Version of the agent")
    agent_type: str = Field(..., description="Type of agent (e.g., llm, tool, workflow)")
    enabled: bool = Field(True, description="Whether the agent is enabled")
    
    class Config:
        """Configuration for the Pydantic model."""
        extra = "allow"  # Allow extra fields


class LLMAgentConfigModel(AgentConfigModel):
    """Configuration model for LLM-based agents."""
    
    agent_type: str = Field("llm", const=True, description="Type must be 'llm'")
    model: str = Field(..., description="Language model identifier")
    temperature: float = Field(0.7, description="Temperature for generation")
    max_tokens: Optional[int] = Field(None, description="Maximum tokens to generate")
    prompt_templates: Dict[str, str] = Field(default_factory=dict, description="Prompt templates")
    stop_sequences: List[str] = Field(default_factory=list, description="Sequences that stop generation")


class ToolAgentConfigModel(AgentConfigModel):
    """Configuration model for tool-based agents."""
    
    agent_type: str = Field("tool", const=True, description="Type must be 'tool'")
    tools: List[str] = Field(default_factory=list, description="List of tool names to use")
    default_tool: Optional[str] = Field(None, description="Default tool to use if not specified")


class WorkflowAgentConfigModel(AgentConfigModel):
    """Configuration model for workflow-based agents."""
    
    agent_type: str = Field("workflow", const=True, description="Type must be 'workflow'")
    workflow_id: str = Field(..., description="ID of the workflow to execute")
    steps: List[Dict[str, Any]] = Field(default_factory=list, description="Workflow steps")


@dataclass
class AgentConfig:
    """
    Configuration for agents.
    
    This class provides methods for loading, validating, and accessing
    agent configuration from various sources.
    """
    
    name: str
    description: str = ""
    version: str = "0.1.0"
    agent_type: str = "generic"
    enabled: bool = True
    settings: Dict[str, Any] = field(default_factory=dict)
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> "AgentConfig":
        """
        Create an agent configuration from a dictionary.
        
        Args:
            config_dict: Dictionary containing the configuration
            
        Returns:
            Agent configuration object
            
        Raises:
            AgentConfigError: If the configuration is invalid
        """
        # Validate the configuration using the appropriate model
        agent_type = config_dict.get("agent_type", "generic")
        
        try:
            if agent_type == "llm":
                model = LLMAgentConfigModel(**config_dict)
            elif agent_type == "tool":
                model = ToolAgentConfigModel(**config_dict)
            elif agent_type == "workflow":
                model = WorkflowAgentConfigModel(**config_dict)
            else:
                model = AgentConfigModel(**config_dict)
                
            # Convert to dictionary
            validated_dict = model.dict()
            
            # Extract basic fields
            name = validated_dict.pop("name")
            description = validated_dict.pop("description", "")
            version = validated_dict.pop("version", "0.1.0")
            agent_type = validated_dict.pop("agent_type", "generic")
            enabled = validated_dict.pop("enabled", True)
            
            # Everything else goes into settings
            return cls(
                name=name,
                description=description,
                version=version,
                agent_type=agent_type,
                enabled=enabled,
                settings=validated_dict
            )
            
        except ValidationError as e:
            raise AgentConfigError(f"Invalid agent configuration: {str(e)}")
    
    @classmethod
    def from_file(cls, file_path: Union[str, Path]) -> "AgentConfig":
        """
        Load agent configuration from a file.
        
        Supports JSON and YAML files based on file extension.
        
        Args:
            file_path: Path to the configuration file
            
        Returns:
            Agent configuration object
            
        Raises:
            AgentConfigError: If the file cannot be loaded or the configuration is invalid
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            raise AgentConfigError(f"Configuration file not found: {file_path}")
        
        try:
            # Load based on file extension
            if file_path.suffix.lower() in (".yaml", ".yml"):
                with open(file_path, "r") as f:
                    config_dict = yaml.safe_load(f)
            elif file_path.suffix.lower() == ".json":
                with open(file_path, "r") as f:
                    config_dict = json.load(f)
            else:
                raise AgentConfigError(f"Unsupported file type: {file_path.suffix}")
            
            return cls.from_dict(config_dict)
            
        except Exception as e:
            raise AgentConfigError(f"Error loading configuration from {file_path}: {str(e)}")
    
    @classmethod
    def from_env(cls, prefix: str = "AGENT_") -> "AgentConfig":
        """
        Load agent configuration from environment variables.
        
        Environment variables should be prefixed with the specified prefix
        and use underscores. For example, AGENT_NAME, AGENT_DESCRIPTION, etc.
        
        Args:
            prefix: Prefix for environment variables
            
        Returns:
            Agent configuration object
            
        Raises:
            AgentConfigError: If required variables are missing or invalid
        """
        # Build configuration dictionary from environment variables
        config_dict = {}
        
        # Required fields
        name = os.environ.get(f"{prefix}NAME")
        if not name:
            raise AgentConfigError(f"Required environment variable {prefix}NAME not found")
        
        config_dict["name"] = name
        
        # Optional fields
        if f"{prefix}DESCRIPTION" in os.environ:
            config_dict["description"] = os.environ[f"{prefix}DESCRIPTION"]
        
        if f"{prefix}VERSION" in os.environ:
            config_dict["version"] = os.environ[f"{prefix}VERSION"]
        
        if f"{prefix}AGENT_TYPE" in os.environ:
            config_dict["agent_type"] = os.environ[f"{prefix}AGENT_TYPE"]
        
        if f"{prefix}ENABLED" in os.environ:
            config_dict["enabled"] = os.environ[f"{prefix}ENABLED"].lower() in ("true", "1", "yes")
        
        # Get all environment variables with prefix and add to settings
        for key, value in os.environ.items():
            if key.startswith(prefix) and key not in (
                f"{prefix}NAME",
                f"{prefix}DESCRIPTION",
                f"{prefix}VERSION",
                f"{prefix}AGENT_TYPE",
                f"{prefix}ENABLED"
            ):
                # Remove prefix and convert to lowercase for settings
                setting_key = key[len(prefix):].lower()
                config_dict[setting_key] = value
        
        return cls.from_dict(config_dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the configuration to a dictionary.
        
        Returns:
            Dictionary representation of the configuration
        """
        config_dict = asdict(self)
        
        # Move settings to top level
        result = {
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "agent_type": self.agent_type,
            "enabled": self.enabled,
            **self.settings
        }
        
        return result
    
    def save(self, file_path: Union[str, Path], format: str = "auto") -> None:
        """
        Save the configuration to a file.
        
        Args:
            file_path: Path to save the configuration to
            format: Format to save as (auto, json, yaml)
            
        Raises:
            AgentConfigError: If the file cannot be saved
        """
        file_path = Path(file_path)
        
        # Determine format from file extension if auto
        if format == "auto":
            if file_path.suffix.lower() in (".yaml", ".yml"):
                format = "yaml"
            elif file_path.suffix.lower() == ".json":
                format = "json"
            else:
                format = "json"  # Default to JSON
        
        try:
            # Convert to dictionary
            config_dict = self.to_dict()
            
            # Save based on format
            if format == "yaml":
                with open(file_path, "w") as f:
                    yaml.dump(config_dict, f, default_flow_style=False)
            elif format == "json":
                with open(file_path, "w") as f:
                    json.dump(config_dict, f, indent=2)
            else:
                raise AgentConfigError(f"Unsupported format: {format}")
                
        except Exception as e:
            raise AgentConfigError(f"Error saving configuration to {file_path}: {str(e)}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value by key.
        
        Checks both basic fields and settings.
        
        Args:
            key: The key to look up
            default: Default value if the key is not found
            
        Returns:
            The configuration value if found, default otherwise
        """
        if key in ("name", "description", "version", "agent_type", "enabled"):
            return getattr(self, key)
        else:
            return self.settings.get(key, default)
    
    def update(self, **kwargs) -> None:
        """
        Update the configuration with new values.
        
        Args:
            **kwargs: Key-value pairs to update
        """
        for key, value in kwargs.items():
            if key in ("name", "description", "version", "agent_type", "enabled"):
                setattr(self, key, value)
            else:
                self.settings[key] = value 