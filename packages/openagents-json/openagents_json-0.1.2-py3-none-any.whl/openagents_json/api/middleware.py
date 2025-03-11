"""
Middleware for integrating OpenAgents JSON with existing FastAPI applications.
"""

from typing import Any, Callable, Dict, Optional

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from openagents_json.core.app import OpenAgentsApp
from openagents_json.settings import settings


class OpenAgentsMiddleware(BaseHTTPMiddleware):
    """
    Middleware for integrating OpenAgents JSON with existing FastAPI applications.

    This middleware provides access to OpenAgents JSON capabilities in request handlers,
    exposing the OpenAgentsApp instance via request.state.openagents_app.
    It also provides context for job and workflow operations.

    Examples:
        ```python
        from fastapi import FastAPI, Request
        from openagents_json.api import OpenAgentsMiddleware
        from openagents_json.core.app import OpenAgentsApp

        app = FastAPI()
        openagents_app = OpenAgentsApp()

        app.add_middleware(OpenAgentsMiddleware, app=openagents_app)

        @app.get("/custom-workflow")
        async def create_custom_job(request: Request, workflow_id: str):
            # Access OpenAgentsApp from the request
            openagents_app = request.state.openagents_app

            # Create a job
            job = await openagents_app.create_job(workflow_id, inputs={})
            return job
        ```
    """

    def __init__(
        self,
        app: ASGIApp,
        openagents_app: Optional[OpenAgentsApp] = None,
        request_callback: Optional[Callable[[Request], Any]] = None,
        response_callback: Optional[Callable[[Request, Response], Any]] = None,
    ):
        """
        Initialize the OpenAgents middleware.

        Args:
            app: The ASGI application
            openagents_app: An instance of OpenAgentsApp
            request_callback: Optional callback that will be executed on each request
            response_callback: Optional callback that will be executed on each response
        """
        super().__init__(app)
        self.openagents_app = openagents_app or OpenAgentsApp()
        self.request_callback = request_callback
        self.response_callback = response_callback

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Process the request and response.

        Args:
            request: The incoming request
            call_next: The next middleware or route handler

        Returns:
            The response
        """
        # Attach OpenAgentsApp to the request state
        request.state.openagents_app = self.openagents_app

        # Execute request callback if provided
        if self.request_callback:
            await self.request_callback(request)

        # Extract request information for logging
        if settings.app.debug:
            method = request.method
            url = str(request.url)
            headers = dict(request.headers)
            print(f"OpenAgents: {method} {url}")

        # Process the request
        response = await call_next(request)

        # Execute response callback if provided
        if self.response_callback:
            await self.response_callback(request, response)

        return response
