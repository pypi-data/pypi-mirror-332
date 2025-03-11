"""
OpenAgents JSON: A FastAPI extension for building AI agent workflows
-------------------------------------------------------------------

OpenAgents JSON provides a structured framework for building intelligent workflows
using a three-stage model:
1. Agent & Asset Definition - Define and register AI components like agents, tools, and assets
2. Workflow Definition - Compose agents into reusable workflows with validation and templating
3. Job Management - Execute, monitor, and control workflow instances as jobs
"""

__version__ = "0.1.0"

from openagents_json.core.app import OpenAgentsApp
from openagents_json.settings import configure_from_dict, get_settings, settings

__all__ = ["OpenAgentsApp", "settings", "get_settings", "configure_from_dict"]
