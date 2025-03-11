"""
Pytest configuration for OpenAgents JSON tests.

This module configures the test environment before any tests run.
"""

import pytest

# We'll configure settings in individual test modules as needed
# from openagents_json import configure_from_dict


# Configure test settings before any tests run
def pytest_configure(config):
    """Configure the test environment."""
    # Configure minimal test settings
    test_settings = {
        "app__name": "test-app",
        "app__debug": True,
        "app__api_prefix": "/api",
        "registry__auto_discover": False,
        "registry__modules": [],
        "workflow__validation_mode": "strict",
        "job__store_type": "memory",
        "job__store_file_dir": "/tmp",
        "job__retention_days": 7,
        "db__dialect": "sqlite",
        "db__path": ":memory:",
        "db__host": "localhost",
        "db__port": 5432,
        "db__username": "test",
        "db__password": "test",
        "db__name": "test",
        "db__connection_string": "sqlite:///:memory:",
    }
    # configure_from_dict(test_settings)
