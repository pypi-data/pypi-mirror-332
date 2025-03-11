"""
Test that demonstrates using direct configuration to configure settings.

This test shows how to use direct configuration to configure settings
before importing OpenAgentsApp.
"""

import os

import pytest

# Configure settings directly
os.environ["APP_NAME"] = "test-app"
os.environ["DEBUG"] = "true"
os.environ["API_PREFIX"] = "/api"
os.environ["REGISTRY_AUTO_DISCOVER"] = "false"
os.environ["REGISTRY_MODULES"] = "[]"
os.environ["WORKFLOW_VALIDATION_MODE"] = "strict"
os.environ["JOB_STORE_TYPE"] = "memory"
os.environ["JOB_STORE_FILE_DIR"] = "/tmp"
os.environ["JOB_RETENTION_DAYS"] = "7"
os.environ["DB_DIALECT"] = "sqlite"
os.environ["DB_PATH"] = ":memory:"
os.environ["DB_HOST"] = "localhost"
os.environ["DB_PORT"] = "5432"
os.environ["DB_USERNAME"] = "test"
os.environ["DB_PASSWORD"] = "test"
os.environ["DB_NAME"] = "test"
os.environ["DB_CONNECTION_STRING"] = "sqlite:///:memory:"

# Now we can import OpenAgentsApp
from openagents_json import OpenAgentsApp


def test_app_with_env_settings():
    """Test creating an OpenAgentsApp instance with settings from environment variables."""
    app = OpenAgentsApp()

    # Verify that the settings were loaded correctly
    assert app.settings.app.name == "test-app"
    assert app.settings.app.debug is True
    assert app.settings.app.api_prefix == "/api"
    assert app.settings.workflow.validation_mode == "strict"
    assert app.settings.job.store_type == "memory"
