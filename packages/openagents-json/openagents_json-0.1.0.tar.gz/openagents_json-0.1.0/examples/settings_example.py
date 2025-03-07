#!/usr/bin/env python
"""
Example demonstrating the OpenAgents JSON settings system.

This example shows how to access and configure settings in different ways.
"""

import os
from pprint import pprint

from openagents_json import settings, configure_from_dict


def print_section(title):
    """Print a section title."""
    print("\n" + "=" * 50)
    print(f" {title} ".center(50, "="))
    print("=" * 50)


def main():
    """Run the settings example."""
    print_section("Default Settings")
    
    # Print default settings
    print("App Settings:")
    print(f"  app_name: {settings.app.app_name}")
    print(f"  debug: {settings.app.debug}")
    print(f"  environment: {settings.app.environment}")
    
    print("\nAgent Settings:")
    print(f"  default_llm_provider: {settings.agent.default_llm_provider}")
    print(f"  default_model: {settings.agent.default_model}")
    
    print("\nStorage Settings:")
    print(f"  storage_type: {settings.storage.storage_type}")
    print(f"  database.dialect: {settings.storage.database.dialect}")
    
    # Demonstrate legacy field access
    print("\nLegacy Field Access:")
    print(f"  DEBUG: {settings.DEBUG}")
    print(f"  DEFAULT_MODEL: {settings.DEFAULT_MODEL}")
    print(f"  DB_DIALECT: {settings.DB_DIALECT}")
    
    # Modify settings programmatically
    print_section("Programmatic Configuration")
    
    configure_from_dict({
        "app__debug": True,
        "app__log_level": "DEBUG",
        "agent__default_model": "gpt-4o",
        "storage__storage_type": "file",
        "storage__file_storage_path": "/tmp/openagents",
    })
    
    print("Updated Settings:")
    print(f"  app.debug: {settings.app.debug}")
    print(f"  app.log_level: {settings.app.log_level}")
    print(f"  agent.default_model: {settings.agent.default_model}")
    print(f"  storage.storage_type: {settings.storage.storage_type}")
    print(f"  storage.file_storage_path: {settings.storage.file_storage_path}")
    
    # Verify legacy fields are synchronized
    print("\nVerify Legacy Fields Sync:")
    print(f"  DEBUG: {settings.DEBUG}")
    print(f"  DEFAULT_MODEL: {settings.DEFAULT_MODEL}")
    
    # Demonstrate environment variable configuration
    print_section("Environment Variable Configuration")
    
    # Set environment variables
    os.environ["OPENAGENTS_APP__ENVIRONMENT"] = "production"
    os.environ["OPENAGENTS_AGENT__MAX_RETRIES"] = "5"
    
    # Create a new settings instance to pick up environment variables
    # (In a real application, you would use get_settings() to refresh)
    from openagents_json.settings import Settings
    new_settings = Settings()
    
    print("Settings from Environment Variables:")
    print(f"  app.environment: {new_settings.app.environment}")
    print(f"  agent.max_retries: {new_settings.agent.max_retries}")
    
    # Custom settings
    print_section("Custom Settings")
    
    settings.custom_settings["my_custom_setting"] = "custom value"
    settings.custom_settings["feature_flags"] = {
        "enable_experimental": True,
        "beta_features": ["feature1", "feature2"],
    }
    
    print("Custom Settings:")
    pprint(settings.custom_settings)


if __name__ == "__main__":
    main() 