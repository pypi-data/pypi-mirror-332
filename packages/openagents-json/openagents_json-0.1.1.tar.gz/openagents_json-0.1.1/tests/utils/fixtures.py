"""
Test fixtures for OpenAgents JSON.

This module provides common pytest fixtures that can be used across
different test modules to set up test environments.
"""

import os
import tempfile

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from openagents_json import OpenAgentsApp
from openagents_json.job.storage import SQLAlchemyJobStore


@pytest.fixture
def app_fixture():
    """Fixture that provides a fresh OpenAgentsApp instance for testing."""
    # Create the app with test settings (configured in conftest.py)
    app = OpenAgentsApp()
    yield app


@pytest.fixture
def test_client(app_fixture):
    """Fixture that provides a FastAPI test client for API testing."""
    fastapi_app = FastAPI()
    fastapi_app.include_router(app_fixture.router, prefix="/agents", tags=["agents"])
    client = TestClient(fastapi_app)
    yield client


@pytest.fixture
def in_memory_db():
    """
    Fixture that provides an in-memory SQLite database for testing.

    This is useful for testing database integration without affecting
    a real database.
    """
    # Create an in-memory SQLite database
    engine = create_engine("sqlite:///:memory:")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

    # Create tables
    Base.metadata.create_all(bind=engine)

    # Create a session
    db = SessionLocal()

    yield db

    # Clean up
    db.close()


@pytest.fixture
def mock_job_store():
    """Fixture that provides an in-memory job store for testing."""
    # Create an in-memory SQLite database for job storage
    job_store = SQLAlchemyJobStore(dialect="sqlite", path=":memory:")
    yield job_store


@pytest.fixture
def mock_agent(app_fixture):
    """Fixture that provides a mock agent for testing."""

    @app_fixture.agent("test_agent", description="A test agent")
    class TestAgent:
        def __init__(self, config=None):
            self.config = config or {}

        @app_fixture.capability("echo", description="Echo the input")
        async def echo(self, text: str) -> str:
            """Echo the input text."""
            return text

        @app_fixture.capability("reverse", description="Reverse the input")
        async def reverse(self, text: str) -> str:
            """Reverse the input text."""
            return text[::-1]

    yield app_fixture.agent_registry.agents["test_agent"]


@pytest.fixture
def mock_workflow(app_fixture, mock_agent):
    """Fixture that provides a mock workflow for testing."""
    workflow_def = {
        "id": "test_workflow",
        "description": "A test workflow",
        "steps": [
            {
                "id": "step1",
                "component": "test_agent.echo",
                "inputs": {"text": "{{input.text}}"},
            },
            {
                "id": "step2",
                "component": "test_agent.reverse",
                "inputs": {"text": "{{step1.output}}"},
            },
        ],
        "output": {"original": "{{step1.output}}", "reversed": "{{step2.output}}"},
    }

    app_fixture.workflow_registry.register(workflow_def)
    yield workflow_def
