"""
Tests for the FastAPI integration.
"""

import json

import pytest
from fastapi.testclient import TestClient

from openagents_json.api import OpenAgentsAPI, OpenAgentsMiddleware, create_api_router
from openagents_json.core.app import OpenAgentsApp
from openagents_json.workflow import Connection, Parameter, Step, Workflow


# Example agent class for testing
class TestAgent:
    """Test agent for testing purposes."""

    def test_capability(self, input_value: str) -> str:
        """Example capability."""
        return f"Processed: {input_value}"


# Test workflow definition
TEST_WORKFLOW = {
    "id": "test_workflow",
    "name": "Test Workflow",
    "description": "A test workflow for unit tests",
    "version": "1.0.0",
    "steps": [
        {
            "id": "step1",
            "type": "input",
            "name": "Input Step",
            "description": "Test input step",
            "outputs": [
                {
                    "name": "value",
                    "type": "string",
                    "description": "Test value",
                    "required": True,
                }
            ],
        },
        {
            "id": "step2",
            "type": "output",
            "name": "Output Step",
            "description": "Test output step",
            "inputs": [
                {
                    "name": "value",
                    "type": "string",
                    "description": "Test value",
                    "required": True,
                }
            ],
        },
    ],
    "connections": [
        {
            "from_step": "step1",
            "from_output": "value",
            "to_step": "step2",
            "to_input": "value",
        }
    ],
    "inputs": [],
    "outputs": [],
    "metadata": {
        "author": "Test Author",
        "tags": ["test", "example"],
        "category": "test",
    },
}


class TestOpenAgentsAPI:
    """Tests for the OpenAgentsAPI extension."""

    @pytest.fixture
    def app(self):
        """Create a test app for testing."""
        app = OpenAgentsAPI(
            title="Test API", description="Test API for unit tests", version="0.1.0"
        )

        # Register a test agent
        @app.agent("test_agent")
        class MyTestAgent(TestAgent):
            @app.capability("test")
            def test_capability(self, input_value: str) -> str:
                return super().test_capability(input_value)

        # Register a test workflow
        app.register_workflow(TEST_WORKFLOW)

        # Add a custom endpoint
        @app.get("/test")
        async def test_endpoint():
            return {"message": "Test endpoint"}

        return app

    @pytest.fixture
    def client(self, app):
        """Create a test client for testing."""
        return TestClient(app)

    def test_health_endpoint(self, client):
        """Test the health endpoint."""
        response = client.get("/api/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    def test_agents_endpoint(self, client):
        """Test the agents endpoint."""
        response = client.get("/api/agents")
        assert response.status_code == 200
        agents = response.json()
        assert len(agents) == 1
        assert agents[0]["name"] == "test_agent"
        assert "test" in agents[0]["capabilities"]

    def test_workflows_endpoint(self, client):
        """Test the workflows endpoint."""
        response = client.get("/api/workflows")
        assert response.status_code == 200
        workflows = response.json()
        assert len(workflows) == 1
        assert workflows[0]["id"] == "test_workflow"
        assert workflows[0]["name"] == "Test Workflow"

    def test_custom_endpoint(self, client):
        """Test a custom endpoint."""
        response = client.get("/test")
        assert response.status_code == 200
        assert response.json() == {"message": "Test endpoint"}


class TestOpenAgentsMiddleware:
    """Tests for the OpenAgentsMiddleware."""

    @pytest.fixture
    def app(self):
        """Create a test app with middleware for testing."""
        from fastapi import FastAPI, Request

        app = FastAPI()

        # Create the OpenAgentsApp instance
        openagents_app = OpenAgentsApp()

        # Register a test agent
        @openagents_app.agent("test_agent")
        class MyTestAgent(TestAgent):
            @openagents_app.capability("test")
            def test_capability(self, input_value: str) -> str:
                return super().test_capability(input_value)

        # Register a test workflow
        openagents_app.register_workflow(TEST_WORKFLOW)

        # Add the middleware
        app.add_middleware(OpenAgentsMiddleware, openagents_app=openagents_app)

        # Mount the API router
        router = create_api_router(openagents_app)
        app.include_router(router, prefix="/api")

        # Add a custom endpoint that uses the OpenAgentsApp
        @app.get("/test")
        async def test_endpoint(request: Request):
            oa_app = request.state.openagents_app
            agents = await oa_app._get_agents()
            return {"message": "Test endpoint", "agent_count": len(agents)}

        return app

    @pytest.fixture
    def client(self, app):
        """Create a test client for testing."""
        return TestClient(app)

    def test_health_endpoint(self, client):
        """Test the health endpoint."""
        response = client.get("/api/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    def test_agents_endpoint(self, client):
        """Test the agents endpoint."""
        response = client.get("/api/agents")
        assert response.status_code == 200
        agents = response.json()
        assert len(agents) == 1
        assert agents[0]["name"] == "test_agent"
        assert "test" in agents[0]["capabilities"]

    def test_workflows_endpoint(self, client):
        """Test the workflows endpoint."""
        response = client.get("/api/workflows")
        assert response.status_code == 200
        workflows = response.json()
        assert len(workflows) == 1
        assert workflows[0]["id"] == "test_workflow"
        assert workflows[0]["name"] == "Test Workflow"

    def test_custom_endpoint(self, client):
        """Test a custom endpoint using middleware."""
        response = client.get("/test")
        assert response.status_code == 200
        assert response.json() == {"message": "Test endpoint", "agent_count": 1}


class TestAPIRouter:
    """Tests for the API router."""

    @pytest.fixture
    def app(self):
        """Create a test app with API router for testing."""
        from fastapi import FastAPI

        app = FastAPI()

        # Create the OpenAgentsApp instance
        openagents_app = OpenAgentsApp()

        # Register a test agent
        @openagents_app.agent("test_agent")
        class MyTestAgent(TestAgent):
            @openagents_app.capability("test")
            def test_capability(self, input_value: str) -> str:
                return super().test_capability(input_value)

        # Register a test workflow
        openagents_app.register_workflow(TEST_WORKFLOW)

        # Mount the API router
        router = create_api_router(openagents_app)
        app.include_router(router, prefix="/api")

        # Add a custom endpoint
        @app.get("/test")
        async def test_endpoint():
            return {"message": "Test endpoint"}

        return app

    @pytest.fixture
    def client(self, app):
        """Create a test client for testing."""
        return TestClient(app)

    def test_health_endpoint(self, client):
        """Test the health endpoint."""
        response = client.get("/api/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    def test_agents_endpoint(self, client):
        """Test the agents endpoint."""
        response = client.get("/api/agents")
        assert response.status_code == 200
        agents = response.json()
        assert len(agents) == 1
        assert agents[0]["name"] == "test_agent"
        assert "test" in agents[0]["capabilities"]

    def test_workflows_endpoint(self, client):
        """Test the workflows endpoint."""
        response = client.get("/api/workflows")
        assert response.status_code == 200
        workflows = response.json()
        assert len(workflows) == 1
        assert workflows[0]["id"] == "test_workflow"
        assert workflows[0]["name"] == "Test Workflow"

    def test_custom_endpoint(self, client):
        """Test a custom endpoint."""
        response = client.get("/test")
        assert response.status_code == 200
        assert response.json() == {"message": "Test endpoint"}
