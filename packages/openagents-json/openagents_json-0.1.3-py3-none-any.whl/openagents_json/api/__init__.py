"""
FastAPI integration for OpenAgents JSON.

This module provides integration options for FastAPI applications:
1. Extension: OpenAgentsApp class that extends FastAPI
2. Middleware: Middleware for existing FastAPI applications
3. Router: Enhanced router for FastAPI applications
"""

from openagents_json.api.app import OpenAgentsAPI
from openagents_json.api.middleware import OpenAgentsMiddleware
from openagents_json.api.router import create_api_router

__all__ = [
    "OpenAgentsAPI",
    "OpenAgentsMiddleware",
    "create_api_router",
]
