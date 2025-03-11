"""
Tests for the settings module.

This module tests the settings module's functionality, including:
- Environment variable loading
- Default values
- Validation
- Nested settings access
- Secure handling of sensitive values
"""

import os
import unittest
from pathlib import Path
from unittest.mock import patch

from openagents_json.settings import Settings, configure_from_dict, get_settings


class TestSettings(unittest.TestCase):
    """Test the settings module."""

    def setUp(self):
        """Set up the test environment."""
        # Save the original environment variables
        self.original_env = os.environ.copy()

    def tearDown(self):
        """Clean up the test environment."""
        # Restore the original environment variables
        os.environ.clear()
        os.environ.update(self.original_env)

    def test_default_values(self):
        """Test that default values are set correctly."""
        settings = Settings()

        # Check app settings defaults
        self.assertFalse(settings.app.debug)
        self.assertEqual(settings.app.log_level, "INFO")
        self.assertEqual(settings.app.environment, "development")

        # Check job settings defaults
        self.assertEqual(settings.job.job_retention_days, 30)
        self.assertEqual(settings.job.max_concurrent_jobs, 100)

        # Check storage settings defaults
        self.assertEqual(settings.storage.storage_type, "memory")

    def test_environment_variable_loading(self):
        """Test loading settings from environment variables."""
        # Set environment variables
        os.environ["OPENAGENTS_APP__DEBUG"] = "true"
        os.environ["OPENAGENTS_APP__LOG_LEVEL"] = "DEBUG"
        os.environ["OPENAGENTS_JOB__MAX_CONCURRENT_JOBS"] = "50"
        os.environ["OPENAGENTS_STORAGE__STORAGE_TYPE"] = "file"
        os.environ["OPENAGENTS_STORAGE__FILE_STORAGE_PATH"] = "/tmp/storage"

        # Create new settings instance
        settings = Settings()

        # Check that environment variables were loaded
        self.assertTrue(settings.app.debug)
        self.assertEqual(settings.app.log_level, "DEBUG")
        self.assertEqual(settings.job.max_concurrent_jobs, 50)
        self.assertEqual(settings.storage.storage_type, "file")
        self.assertEqual(str(settings.storage.file_storage_path), "/tmp/storage")

    def test_environment_variable_validation(self):
        """Test validation of environment variables."""
        # Set invalid environment variables
        os.environ["OPENAGENTS_APP__LOG_LEVEL"] = "INVALID"
        os.environ["OPENAGENTS_JOB__MAX_CONCURRENT_JOBS"] = "-10"
        os.environ["OPENAGENTS_STORAGE__STORAGE_TYPE"] = "invalid_storage"

        # Check that validation errors are raised
        with self.assertRaises(ValueError):
            Settings()

    def test_secure_values(self):
        """Test that sensitive values are handled securely."""
        # Set sensitive environment variables
        os.environ["OPENAGENTS_APP__SECRET_KEY"] = "test-secret-key"
        os.environ["OPENAGENTS_AGENT__OPENAI_API_KEY"] = "sk-test-api-key"

        # Create new settings instance
        settings = Settings()

        # Check that values are stored as SecretStr
        self.assertEqual(settings.app.secret_key.get_secret_value(), "test-secret-key")
        self.assertEqual(
            settings.agent.openai_api_key.get_secret_value(), "sk-test-api-key"
        )

        # Check that repr does not expose the values
        self.assertNotIn("test-secret-key", repr(settings.app.secret_key))
        self.assertNotIn("sk-test-api-key", repr(settings.agent.openai_api_key))

    def test_storage_validation(self):
        """Test storage configuration validation."""
        # Test file storage without path
        os.environ["OPENAGENTS_STORAGE__STORAGE_TYPE"] = "file"
        with self.assertRaises(ValueError):
            Settings()

        # Test file storage with path
        os.environ["OPENAGENTS_STORAGE__FILE_STORAGE_PATH"] = "/tmp/storage"
        settings = Settings()
        self.assertEqual(settings.storage.storage_type, "file")

        # Test redis without URL
        os.environ.clear()
        os.environ.update(self.original_env)
        os.environ["OPENAGENTS_STORAGE__STORAGE_TYPE"] = "redis"
        with self.assertRaises(ValueError):
            Settings()

        # Test redis with URL
        os.environ["OPENAGENTS_STORAGE__REDIS_URL"] = "redis://localhost:6379/0"
        settings = Settings()
        self.assertEqual(settings.storage.storage_type, "redis")

        # Test postgres without credentials
        os.environ.clear()
        os.environ.update(self.original_env)
        os.environ["OPENAGENTS_STORAGE__STORAGE_TYPE"] = "postgres"
        with self.assertRaises(ValueError):
            Settings()

        # Test postgres with database_url
        os.environ["OPENAGENTS_STORAGE__DATABASE_URL"] = (
            "postgresql://user:pass@localhost:5432/db"
        )
        settings = Settings()
        self.assertEqual(settings.storage.storage_type, "postgres")

        # Test postgres with individual params
        os.environ.clear()
        os.environ.update(self.original_env)
        os.environ["OPENAGENTS_STORAGE__STORAGE_TYPE"] = "postgres"
        os.environ["OPENAGENTS_STORAGE__DB_HOST"] = "localhost"
        os.environ["OPENAGENTS_STORAGE__DB_NAME"] = "openagents"
        settings = Settings()
        self.assertEqual(settings.storage.storage_type, "postgres")

    def test_get_settings(self):
        """Test the get_settings function."""
        settings = get_settings()

        # Check that it returns the global settings instance
        self.assertEqual(settings.app.environment, "development")

        # Check that modification of the environment updates the settings
        os.environ["OPENAGENTS_APP__ENVIRONMENT"] = "production"
        settings = get_settings()
        self.assertEqual(settings.app.environment, "production")

    def test_configure_from_dict(self):
        """Test configuring settings from a dictionary."""
        config_dict = {
            "app__debug": True,
            "app__log_level": "WARNING",
            "job__max_concurrent_jobs": 42,
            "storage__storage_type": "file",
            "storage__file_storage_path": "/custom/path",
        }

        # Configure settings from dictionary
        configure_from_dict(config_dict)
        settings = get_settings()

        # Check that settings were updated
        self.assertTrue(settings.app.debug)
        self.assertEqual(settings.app.log_level, "WARNING")
        self.assertEqual(settings.job.max_concurrent_jobs, 42)
        self.assertEqual(settings.storage.storage_type, "file")
        self.assertEqual(str(settings.storage.file_storage_path), "/custom/path")


if __name__ == "__main__":
    unittest.main()
