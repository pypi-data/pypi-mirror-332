"""
Core functionality for OpenAgents JSON.

This module contains the core components of the OpenAgents JSON framework,
including the main application class, configuration, and utility functions.
"""

from openagents_json.core.app import OpenAgentsApp
from openagents_json.core.registry import (
    BaseComponentRegistry,
    ComponentMetadata,
    InMemoryComponentRegistry,
    component_registry,
)
from openagents_json.settings import Settings

__all__ = [
    "OpenAgentsApp",
    "Settings",
    "BaseComponentRegistry",
    "InMemoryComponentRegistry",
    "ComponentMetadata",
    "component_registry",
]
