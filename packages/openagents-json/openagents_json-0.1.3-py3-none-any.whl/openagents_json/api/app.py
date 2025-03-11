"""
OpenAgentsAPI class that extends FastAPI with OpenAgents JSON capabilities.
"""

import os
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Union

from fastapi import APIRouter, Depends, FastAPI, Request, Response
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.base import BaseHTTPMiddleware

from openagents_json.api.middleware import OpenAgentsMiddleware
from openagents_json.api.router import create_api_router
from openagents_json.core.app import OpenAgentsApp
from openagents_json.settings import Settings, settings


class OpenAgentsAPI(FastAPI):
    """
    FastAPI application with integrated OpenAgents JSON capabilities.

    This class extends FastAPI to provide a seamless integration with
    OpenAgents JSON framework, allowing for agent registration, workflow
    management, and job execution directly through the API.

    Examples:
        ```python
        from openagents_json.api import OpenAgentsAPI

        app = OpenAgentsAPI(
            title="My Agent App",
            description="An application with AI agents"
        )

        @app.agent("my_agent")
        class MyAgent:
            @app.capability("analyze")
            def analyze_text(self, text: str) -> str:
                return f"Analysis of: {text}"

        # Define a workflow
        my_workflow = {
            "id": "text_analysis",
            "name": "Text Analysis",
            "steps": [...]
        }
        app.register_workflow(my_workflow)
        ```
    """

    def __init__(
        self,
        *args,
        openagents_app: Optional[OpenAgentsApp] = None,
        custom_settings: Optional[Dict[str, Any]] = None,
        api_prefix: Optional[str] = None,
        include_middleware: bool = True,
        serve_ui: bool = True,
        **kwargs,
    ):
        """
        Initialize the OpenAgentsAPI application.

        Args:
            *args: Arguments passed to FastAPI
            openagents_app: Existing OpenAgentsApp instance (optional)
            custom_settings: Custom settings for OpenAgents JSON
            api_prefix: Prefix for API routes
            include_middleware: Whether to include OpenAgents middleware
            serve_ui: Whether to serve the UI
            **kwargs: Keyword arguments passed to FastAPI
        """
        super().__init__(*args, **kwargs)

        # Initialize settings if provided
        if custom_settings:
            from openagents_json.settings import configure_from_dict

            configure_from_dict(custom_settings)

        # Create or use the existing OpenAgentsApp
        self.openagents_app = openagents_app or OpenAgentsApp()

        # Set up the prefix
        self.api_prefix = api_prefix or settings.app.api_prefix

        # Add the router to the app
        router = create_api_router(self.openagents_app)
        self.include_router(router, prefix=self.api_prefix)

        # Add middleware if requested
        if include_middleware:
            self.add_middleware(OpenAgentsMiddleware, app=self.openagents_app)

        # Add exception handler for OpenAgents exceptions
        self.add_exception_handler(Exception, self._exception_handler)

        # Serve UI if requested
        if serve_ui:
            self._setup_ui_routes()

    def _setup_ui_routes(self):
        """Set up routes for serving the UI."""
        # Get the package directory
        package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        static_dir = os.path.join(package_dir, "static")
        ui_dir = os.path.join(static_dir, "ui")

        # Check if the UI build exists
        if os.path.exists(ui_dir) and os.path.isdir(ui_dir):
            # Mount static assets (JS, CSS, images)
            self.mount("/static", StaticFiles(directory=static_dir), name="static")

            # Serve the SPA for all frontend routes
            @self.get("/ui/{full_path:path}")
            async def serve_spa(full_path: str):
                """Serve the SPA for any UI route."""
                spa_path = os.path.join(ui_dir, "index.html")
                return FileResponse(spa_path)

    def _exception_handler(self, request: Request, exc: Exception) -> JSONResponse:
        """Handle exceptions in API requests."""
        # If this is a development environment, include the traceback
        if settings.app.environment == "development":
            import traceback

            tb = traceback.format_exc()
            return JSONResponse(
                status_code=500,
                content={
                    "error": str(exc),
                    "traceback": tb,
                    "type": exc.__class__.__name__,
                },
            )

        # For production, just return a simple message
        return JSONResponse(status_code=500, content={"error": "Internal server error"})

    def agent(self, name: str, **metadata):
        """
        Decorator to register an agent class.

        Args:
            name: Name of the agent
            **metadata: Additional metadata for the agent

        Returns:
            Decorator function
        """
        return self.openagents_app.agent(name, **metadata)

    def capability(self, name: str, **metadata):
        """
        Decorator to register an agent capability.

        Args:
            name: Name of the capability
            **metadata: Additional metadata for the capability

        Returns:
            Decorator function
        """
        return self.openagents_app.capability(name, **metadata)

    def tool(self, name: str, **metadata):
        """
        Decorator to register a standalone tool.

        Args:
            name: Name of the tool
            **metadata: Additional metadata for the tool

        Returns:
            Decorator function
        """
        return self.openagents_app.tool(name, **metadata)

    def register_workflow(self, workflow_def: Dict[str, Any]) -> bool:
        """
        Register a workflow definition.

        Args:
            workflow_def: Workflow definition as a dictionary

        Returns:
            True if registration was successful
        """
        return self.openagents_app.register_workflow(workflow_def)

    async def create_job(
        self, workflow_id: str, inputs: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Create a new job from a workflow definition.

        Args:
            workflow_id: ID of the workflow to execute
            inputs: Input values for the workflow

        Returns:
            Created job as a dictionary
        """
        return await self.openagents_app.create_job(workflow_id, inputs)

    async def get_job_status(self, job_id: str) -> Dict[str, Any]:
        """
        Get the status of a job.

        Args:
            job_id: ID of the job

        Returns:
            Job status as a dictionary
        """
        return await self.openagents_app.get_job_status(job_id)

    async def get_job_results(self, job_id: str) -> Dict[str, Any]:
        """
        Get the results of a completed job.

        Args:
            job_id: ID of the job

        Returns:
            Job results as a dictionary
        """
        return await self.openagents_app.get_job_results(job_id)
