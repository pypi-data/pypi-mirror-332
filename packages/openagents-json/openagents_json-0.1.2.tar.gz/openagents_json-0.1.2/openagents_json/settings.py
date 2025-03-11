"""
Centralized settings management for the OpenAgents JSON framework.

This module provides a unified settings interface using Pydantic Settings v2,
allowing configuration through environment variables, .env files, and code.
All settings are strongly typed, validated, and categorized for ease of use.

Environment variables are supported with the prefix OPENAGENTS_.
Examples:
    OPENAGENTS_APP__DEBUG=true
    OPENAGENTS_APP__LOG_LEVEL=INFO
    OPENAGENTS_OPENAI_API_KEY=sk-...

For sensitive values like API keys, SecretStr is used to prevent accidental exposure.
"""

import os
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional, Union

from dotenv import load_dotenv
from pydantic import (
    AnyHttpUrl,
    Field,
    SecretStr,
    field_validator,
    model_validator,
)
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

# Load .env file if it exists
load_dotenv()


class AppSettings(BaseSettings):
    """Application-wide settings."""

    app_name: str = Field(
        default="OpenAgents JSON", description="Name of the application"
    )

    debug: bool = Field(
        default=False,
        description="Enable debug mode with detailed logging and error messages.",
    )

    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO", description="Logging level for the application."
    )

    secret_key: Optional[SecretStr] = Field(
        default=None,
        description="Secret key for cryptographic signing. Must be set in production.",
    )

    environment: Literal["development", "testing", "production"] = Field(
        default="development", description="Application environment."
    )

    api_prefix: str = Field(default="/api", description="Prefix for API routes")

    @field_validator("secret_key", mode="before")
    @classmethod
    def validate_secret_key(cls, v: Any) -> Any:
        """Generate a random secret key if not provided in development mode."""
        if v is None:
            # For development only, generate a random key
            import secrets

            return SecretStr(secrets.token_hex(32))
        return v


class RegistrySettings(BaseSettings):
    """Settings for component registry."""

    auto_discover: bool = Field(
        default=True,
        description="Automatically discover agents in the specified modules",
    )

    modules: List[str] = Field(
        default_factory=list, description="Modules to scan for agent registrations"
    )


class WorkflowSettings(BaseSettings):
    """Settings for workflow management."""

    validation_mode: Literal["strict", "lenient", "none"] = Field(
        default="strict",
        description="Validation mode for workflows: strict, lenient, or none",
    )


class AgentSettings(BaseSettings):
    """Settings for AI agents and models."""

    default_llm_provider: Literal["openai", "anthropic", "local"] = Field(
        default="openai",
        description="Default LLM provider to use when not specified explicitly.",
    )

    openai_api_key: Optional[SecretStr] = Field(
        default=None,
        description="OpenAI API key for accessing OpenAI models. Required if using OpenAI.",
    )

    anthropic_api_key: Optional[SecretStr] = Field(
        default=None,
        description="Anthropic API key for accessing Claude models. Required if using Anthropic.",
    )

    default_model: str = Field(
        default="gpt-3.5-turbo",
        description="Default model identifier to use when not specified explicitly.",
    )

    timeout_seconds: int = Field(
        default=30,
        description="Default timeout in seconds for agent operations.",
        ge=1,
        le=300,
    )

    max_retries: int = Field(
        default=3,
        description="Maximum number of retries for agent operations.",
        ge=0,
        le=10,
    )


class JobSettings(BaseSettings):
    """Settings for job management and execution."""

    job_retention_days: int = Field(
        default=30,
        description="Number of days to retain completed jobs before cleanup.",
        ge=1,
    )

    max_concurrent_jobs: int = Field(
        default=100,
        description="Maximum number of concurrent jobs to execute.",
        ge=1,
    )

    default_job_timeout_seconds: int = Field(
        default=3600,
        description="Default timeout in seconds for job execution.",
        ge=1,
    )

    default_max_retries: int = Field(
        default=3,
        description="Default maximum number of retries for failed jobs.",
        ge=0,
    )

    default_retry_delay_seconds: int = Field(
        default=30,
        description="Default delay in seconds between job retries.",
        ge=1,
    )

    job_recovery_timeout_minutes: int = Field(
        default=5,
        description="Number of minutes after which a running job with no updates is considered interrupted.",
        ge=1,
        le=1440,  # maximum of 24 hours
    )

    # Storage settings
    store_type: str = Field(
        default="memory",
        description="""
        Storage type for job persistence. Options:
        - 'memory': Volatile in-memory storage (fastest, no persistence)
        - 'file': JSON file-based storage (good for development/simple deployments)
        - 'database': SQL database storage via SQLAlchemy (recommended for production)
        """,
    )

    store_path: Optional[str] = Field(
        default=None,
        description="Path for file-based job storage. Only used when store_type='file'.",
    )

    @field_validator("store_type")
    def validate_store_type(cls, v):
        """Validate the store_type against allowed values."""
        allowed_types = ["memory", "file", "database", "sqlalchemy"]
        if v.lower() not in allowed_types:
            raise ValueError(
                f"Invalid store type '{v}'. Must be one of: {', '.join(allowed_types)}"
            )
        return v.lower()


class DatabaseSettings(BaseSettings):
    """
    Settings for database connections.

    These settings are used for database job storage when job.store_type = 'database',
    and can also be used by other database-connected components.
    """

    dialect: str = Field(
        default="sqlite", description="Database dialect: sqlite, postgresql, mysql"
    )

    path: Optional[str] = Field(
        default="./openagents.db",
        description="Path for SQLite database (only used with dialect='sqlite')",
    )

    host: Optional[str] = Field(
        default="localhost", description="Database host (for PostgreSQL/MySQL)"
    )

    port: Optional[int] = Field(
        default=None, description="Database port (for PostgreSQL/MySQL)"
    )

    username: Optional[str] = Field(
        default=None, description="Database username (for PostgreSQL/MySQL)"
    )

    password: Optional[SecretStr] = Field(
        default=None, description="Database password (for PostgreSQL/MySQL)"
    )

    name: Optional[str] = Field(
        default="openagents", description="Database name (for PostgreSQL/MySQL)"
    )

    connection_string: Optional[str] = Field(
        default=None,
        description="Direct SQLAlchemy connection string (overrides other database settings)",
    )

    connection_pool_size: int = Field(
        default=5, description="Size of the database connection pool", ge=1
    )

    connection_max_overflow: int = Field(
        default=10,
        description="Maximum number of connections allowed beyond the pool size",
        ge=0,
    )

    connection_timeout: int = Field(
        default=30,
        description="Timeout in seconds for acquiring a connection from the pool",
        ge=1,
    )

    connection_recycle: int = Field(
        default=3600,
        description="Number of seconds after which a connection is recycled",
        ge=1,
    )

    @model_validator(mode="after")
    def validate_db_configuration(self) -> "DatabaseSettings":
        """Validate database configuration."""
        # For SQLite, we need a path
        if self.dialect == "sqlite" and not self.path:
            raise ValueError("Path must be provided for SQLite database")

        # For other databases, we need either a connection string or host/name
        if self.dialect in ("postgresql", "mysql") and not self.connection_string:
            if not (self.host and self.name):
                raise ValueError(
                    f"Either connection_string or host and name must be provided for {self.dialect}"
                )

        return self


class StorageSettings(BaseSettings):
    """Settings for data storage and persistence."""

    storage_type: Literal["memory", "file", "redis", "postgres", "sqlite", "mysql"] = (
        Field(
            default="memory",
            description="Type of storage backend to use for job and state persistence.",
        )
    )

    # File storage settings
    file_storage_path: Optional[Path] = Field(
        default=None,
        description="Path to directory for file storage. Required if storage_type is 'file'.",
    )

    # Redis settings
    redis_url: Optional[str] = Field(
        default=None,
        description="Redis connection URL. Required if storage_type is 'redis'.",
    )

    # Database is configured through the database section
    database: DatabaseSettings = Field(default_factory=DatabaseSettings)

    @model_validator(mode="after")
    def validate_storage_configuration(self) -> "StorageSettings":
        """Validate that necessary settings are provided based on storage_type."""
        if self.storage_type == "file" and not self.file_storage_path:
            raise ValueError(
                "file_storage_path must be set when storage_type is 'file'"
            )

        if self.storage_type == "redis" and not self.redis_url:
            raise ValueError("redis_url must be set when storage_type is 'redis'")

        db_types = {"postgres", "mysql", "sqlite"}
        if self.storage_type in db_types:
            # Validation happens in the DatabaseSettings class
            pass

        return self


class Settings(BaseSettings):
    """
    Main settings class that combines all sub-settings.

    This is the main entry point for accessing application settings.
    """

    model_config = SettingsConfigDict(
        env_prefix="OPENAGENTS_",
        env_nested_delimiter="__",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    app: AppSettings = Field(default_factory=AppSettings)
    registry: RegistrySettings = Field(default_factory=RegistrySettings)
    workflow: WorkflowSettings = Field(default_factory=WorkflowSettings)
    agent: AgentSettings = Field(default_factory=AgentSettings)
    job: JobSettings = Field(default_factory=JobSettings)
    storage: StorageSettings = Field(default_factory=StorageSettings)

    # Legacy fields for backward compatibility - these will redirect to the nested settings
    # to maintain compatibility with existing code
    APP_NAME: Optional[str] = Field(
        default=None, description="DEPRECATED: Use app.app_name instead"
    )
    DEBUG: Optional[bool] = Field(
        default=None, description="DEPRECATED: Use app.debug instead"
    )
    API_PREFIX: Optional[str] = Field(
        default=None, description="DEPRECATED: Use app.api_prefix instead"
    )
    REGISTRY_AUTO_DISCOVER: Optional[bool] = Field(
        default=None, description="DEPRECATED: Use registry.auto_discover instead"
    )
    REGISTRY_MODULES: Optional[List[str]] = Field(
        default=None, description="DEPRECATED: Use registry.modules instead"
    )
    WORKFLOW_VALIDATION_MODE: Optional[str] = Field(
        default=None, description="DEPRECATED: Use workflow.validation_mode instead"
    )
    JOB_STORE_TYPE: Optional[str] = Field(
        default=None, description="DEPRECATED: Use job.store_type instead"
    )
    JOB_STORE_FILE_DIR: Optional[str] = Field(
        default=None, description="DEPRECATED: Use job.store_path instead"
    )
    JOB_RETENTION_DAYS: Optional[int] = Field(
        default=None, description="DEPRECATED: Use job.job_retention_days instead"
    )
    DB_DIALECT: Optional[str] = Field(
        default=None, description="DEPRECATED: Use storage.database.dialect instead"
    )
    DB_PATH: Optional[str] = Field(
        default=None, description="DEPRECATED: Use storage.database.path instead"
    )
    DB_HOST: Optional[str] = Field(
        default=None, description="DEPRECATED: Use storage.database.host instead"
    )
    DB_PORT: Optional[int] = Field(
        default=None, description="DEPRECATED: Use storage.database.port instead"
    )
    DB_USERNAME: Optional[str] = Field(
        default=None, description="DEPRECATED: Use storage.database.username instead"
    )
    DB_PASSWORD: Optional[str] = Field(
        default=None, description="DEPRECATED: Use storage.database.password instead"
    )
    DB_NAME: Optional[str] = Field(
        default=None, description="DEPRECATED: Use storage.database.name instead"
    )
    DB_CONNECTION_STRING: Optional[str] = Field(
        default=None,
        description="DEPRECATED: Use storage.database.connection_string instead",
    )

    # Custom settings
    custom_settings: Dict[str, Any] = Field(
        default_factory=dict, description="Custom settings for extensions"
    )

    # Version information
    version: str = Field(default="0.1.0", description="OpenAgents JSON version.")

    @model_validator(mode="after")
    def sync_legacy_fields(self) -> "Settings":
        """
        Synchronize legacy fields with nested settings.

        This ensures that both the new nested settings and old flat settings
        remain in sync regardless of which is used in code.
        """
        # Two-way sync for app settings
        if self.APP_NAME is not None and self.app.app_name != self.APP_NAME:
            self.app.app_name = self.APP_NAME
        elif (
            self.app.app_name != "OpenAgents JSON"
            and self.APP_NAME != self.app.app_name
        ):
            self.APP_NAME = self.app.app_name

        if self.DEBUG is not None and self.app.debug != self.DEBUG:
            self.app.debug = self.DEBUG
        elif self.app.debug is not False and self.DEBUG != self.app.debug:
            self.DEBUG = self.app.debug

        if self.API_PREFIX is not None and self.app.api_prefix != self.API_PREFIX:
            self.app.api_prefix = self.API_PREFIX
        elif self.app.api_prefix != "/api" and self.API_PREFIX != self.app.api_prefix:
            self.API_PREFIX = self.app.api_prefix

        # Two-way sync for registry settings
        if (
            self.REGISTRY_AUTO_DISCOVER is not None
            and self.registry.auto_discover != self.REGISTRY_AUTO_DISCOVER
        ):
            self.registry.auto_discover = self.REGISTRY_AUTO_DISCOVER
        elif (
            self.registry.auto_discover is not True
            and self.REGISTRY_AUTO_DISCOVER != self.registry.auto_discover
        ):
            self.REGISTRY_AUTO_DISCOVER = self.registry.auto_discover

        if (
            self.REGISTRY_MODULES is not None
            and self.registry.modules != self.REGISTRY_MODULES
        ):
            self.registry.modules = self.REGISTRY_MODULES
        elif self.registry.modules and self.REGISTRY_MODULES != self.registry.modules:
            self.REGISTRY_MODULES = self.registry.modules

        # Two-way sync for workflow settings
        if (
            self.WORKFLOW_VALIDATION_MODE is not None
            and self.workflow.validation_mode != self.WORKFLOW_VALIDATION_MODE
        ):
            self.workflow.validation_mode = self.WORKFLOW_VALIDATION_MODE
        elif (
            self.workflow.validation_mode != "strict"
            and self.WORKFLOW_VALIDATION_MODE != self.workflow.validation_mode
        ):
            self.WORKFLOW_VALIDATION_MODE = self.workflow.validation_mode

        # Two-way sync for job settings
        if (
            self.JOB_STORE_TYPE is not None
            and self.job.store_type != self.JOB_STORE_TYPE
        ):
            self.job.store_type = self.JOB_STORE_TYPE
        elif (
            self.job.store_type != "memory"
            and self.JOB_STORE_TYPE != self.job.store_type
        ):
            self.JOB_STORE_TYPE = self.job.store_type

        if (
            self.JOB_STORE_FILE_DIR is not None
            and self.job.store_path != self.JOB_STORE_FILE_DIR
        ):
            self.job.store_path = self.JOB_STORE_FILE_DIR
        elif self.job.store_path and self.JOB_STORE_FILE_DIR != self.job.store_path:
            self.JOB_STORE_FILE_DIR = self.job.store_path

        if (
            self.JOB_RETENTION_DAYS is not None
            and self.job.job_retention_days != self.JOB_RETENTION_DAYS
        ):
            self.job.job_retention_days = self.JOB_RETENTION_DAYS
        elif (
            self.job.job_retention_days != 30
            and self.JOB_RETENTION_DAYS != self.job.job_retention_days
        ):
            self.JOB_RETENTION_DAYS = self.job.job_retention_days

        # Two-way sync for database settings
        if (
            self.DB_DIALECT is not None
            and self.storage.database.dialect != self.DB_DIALECT
        ):
            self.storage.database.dialect = self.DB_DIALECT
        elif (
            self.storage.database.dialect != "sqlite"
            and self.DB_DIALECT != self.storage.database.dialect
        ):
            self.DB_DIALECT = self.storage.database.dialect

        if self.DB_PATH is not None and self.storage.database.path != self.DB_PATH:
            self.storage.database.path = self.DB_PATH
        elif (
            self.storage.database.path != "./openagents.db"
            and self.DB_PATH != self.storage.database.path
        ):
            self.DB_PATH = self.storage.database.path

        if self.DB_HOST is not None and self.storage.database.host != self.DB_HOST:
            self.storage.database.host = self.DB_HOST
        elif (
            self.storage.database.host != "localhost"
            and self.DB_HOST != self.storage.database.host
        ):
            self.DB_HOST = self.storage.database.host

        if self.DB_PORT is not None and self.storage.database.port != self.DB_PORT:
            self.storage.database.port = self.DB_PORT
        elif (
            self.storage.database.port is not None
            and self.DB_PORT != self.storage.database.port
        ):
            self.DB_PORT = self.storage.database.port

        if (
            self.DB_USERNAME is not None
            and self.storage.database.username != self.DB_USERNAME
        ):
            self.storage.database.username = self.DB_USERNAME
        elif (
            self.storage.database.username
            and self.DB_USERNAME != self.storage.database.username
        ):
            self.DB_USERNAME = self.storage.database.username

        if self.DB_PASSWORD is not None:
            if self.storage.database.password is None:
                self.storage.database.password = SecretStr(self.DB_PASSWORD)
            elif self.storage.database.password.get_secret_value() != self.DB_PASSWORD:
                self.storage.database.password = SecretStr(self.DB_PASSWORD)
        elif self.storage.database.password and not hasattr(self, "DB_PASSWORD"):
            self.DB_PASSWORD = self.storage.database.password.get_secret_value()

        if self.DB_NAME is not None and self.storage.database.name != self.DB_NAME:
            self.storage.database.name = self.DB_NAME
        elif (
            self.storage.database.name != "openagents"
            and self.DB_NAME != self.storage.database.name
        ):
            self.DB_NAME = self.storage.database.name

        if (
            self.DB_CONNECTION_STRING is not None
            and self.storage.database.connection_string != self.DB_CONNECTION_STRING
        ):
            self.storage.database.connection_string = self.DB_CONNECTION_STRING
        elif (
            self.storage.database.connection_string
            and self.DB_CONNECTION_STRING != self.storage.database.connection_string
        ):
            self.DB_CONNECTION_STRING = self.storage.database.connection_string

        return self

    def __getattr__(self, name: str) -> Any:
        """
        Allow accessing settings using both legacy and new styles.

        This dynamic method handles the case when an attribute is accessed
        that doesn't exist directly on the Settings object.
        """
        # Check if it's a legacy all-uppercase field
        if name.isupper():
            legacy_field_map = {
                # Map from legacy field name to nested path
                "APP_NAME": ("app", "app_name"),
                "DEBUG": ("app", "debug"),
                "LOG_LEVEL": ("app", "log_level"),
                "SECRET_KEY": ("app", "secret_key"),
                "ENVIRONMENT": ("app", "environment"),
                "API_PREFIX": ("app", "api_prefix"),
                "REGISTRY_AUTO_DISCOVER": ("registry", "auto_discover"),
                "REGISTRY_MODULES": ("registry", "modules"),
                "WORKFLOW_VALIDATION_MODE": ("workflow", "validation_mode"),
                "DEFAULT_LLM_PROVIDER": ("agent", "default_llm_provider"),
                "OPENAI_API_KEY": ("agent", "openai_api_key"),
                "ANTHROPIC_API_KEY": ("agent", "anthropic_api_key"),
                "DEFAULT_MODEL": ("agent", "default_model"),
                "TIMEOUT_SECONDS": ("agent", "timeout_seconds"),
                "MAX_RETRIES": ("agent", "max_retries"),
                "JOB_RETENTION_DAYS": ("job", "job_retention_days"),
                "MAX_CONCURRENT_JOBS": ("job", "max_concurrent_jobs"),
                "DEFAULT_JOB_TIMEOUT_SECONDS": ("job", "default_job_timeout_seconds"),
                "DEFAULT_MAX_RETRIES": ("job", "default_max_retries"),
                "DEFAULT_RETRY_DELAY_SECONDS": ("job", "default_retry_delay_seconds"),
                "JOB_STORE_TYPE": ("job", "store_type"),
                "JOB_STORE_FILE_DIR": ("job", "store_path"),
                "STORAGE_TYPE": ("storage", "storage_type"),
                "FILE_STORAGE_PATH": ("storage", "file_storage_path"),
                "REDIS_URL": ("storage", "redis_url"),
                "DB_DIALECT": ("storage", "database", "dialect"),
                "DB_PATH": ("storage", "database", "path"),
                "DB_HOST": ("storage", "database", "host"),
                "DB_PORT": ("storage", "database", "port"),
                "DB_USERNAME": ("storage", "database", "username"),
                "DB_PASSWORD": ("storage", "database", "password"),
                "DB_NAME": ("storage", "database", "name"),
                "DB_CONNECTION_STRING": ("storage", "database", "connection_string"),
            }

            if name in legacy_field_map:
                # Get the path to the nested attribute
                path = legacy_field_map[name]

                # Navigate to the attribute following the path
                value = self
                for attr in path:
                    value = getattr(value, attr)

                return value

        # Attribute doesn't exist
        raise AttributeError(f"'Settings' object has no attribute '{name}'")


# Create a global settings instance
settings = Settings()


def get_settings() -> Settings:
    """
    Get the global settings instance.

    This function returns the global settings instance, reloading any
    environment variables that may have changed since the last time
    it was accessed.

    Returns:
        The global Settings instance
    """
    return settings


def configure_from_dict(config_dict: Dict[str, Any]) -> None:
    """
    Configure settings from a dictionary.

    This allows programmatic configuration of settings, which can be useful
    for testing, initialization from config files, etc.

    Args:
        config_dict: Dictionary of configuration values, in the format
                     "section__key": value
    """
    # Split the keys into section and key parts
    for key, value in config_dict.items():
        if "__" in key:
            section, key = key.split("__", 1)

            # Update the appropriate section
            if hasattr(settings, section):
                section_obj = getattr(settings, section)
                if hasattr(section_obj, key):
                    setattr(section_obj, key, value)
                else:
                    raise ValueError(f"Unknown setting: {section}.{key}")
            else:
                raise ValueError(f"Unknown settings section: {section}")
        else:
            # Direct attribute on the settings object
            if hasattr(settings, key):
                setattr(settings, key, value)
            else:
                settings.custom_settings[key] = value
