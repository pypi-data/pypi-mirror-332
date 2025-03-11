# Settings System

The OpenAgents JSON framework provides a robust and flexible settings system based on Pydantic Settings v2. This system allows you to configure all aspects of the framework through environment variables, `.env` files, or programmatically.

## Basic Usage

The settings can be accessed through the global `settings` instance:

```python
from openagents_json import settings

# Access nested settings
if settings.app.debug:
    print("Debug mode is enabled")
    
# Access agent settings
openai_key = settings.agent.openai_api_key.get_secret_value()
```

## Configuration Methods

There are several ways to configure the settings:

### 1. Environment Variables

All settings can be configured using environment variables with the `OPENAGENTS_` prefix and double underscore (`__`) as a separator for nested settings:

```bash
# Set debug mode
export OPENAGENTS_APP__DEBUG=true

# Set OpenAI API key
export OPENAGENTS_AGENT__OPENAI_API_KEY=sk-your-api-key

# Set database configuration
export OPENAGENTS_STORAGE__DATABASE__HOST=localhost
export OPENAGENTS_STORAGE__DATABASE__NAME=openagents
```

### 2. .env File

You can also use a `.env` file in your project root to set environment variables:

```ini
# Application settings
OPENAGENTS_APP__DEBUG=true
OPENAGENTS_APP__LOG_LEVEL=DEBUG

# Agent settings
OPENAGENTS_AGENT__OPENAI_API_KEY=sk-your-api-key
OPENAGENTS_AGENT__DEFAULT_MODEL=gpt-4o

# Storage settings
OPENAGENTS_STORAGE__STORAGE_TYPE=postgres
OPENAGENTS_STORAGE__DATABASE__HOST=localhost
OPENAGENTS_STORAGE__DATABASE__NAME=openagents
OPENAGENTS_STORAGE__DATABASE__USERNAME=postgres
OPENAGENTS_STORAGE__DATABASE__PASSWORD=your-password
```

### 3. Programmatic Configuration

You can configure settings programmatically using the `configure_from_dict` function:

```python
from openagents_json import configure_from_dict

configure_from_dict({
    "app__debug": True,
    "app__log_level": "DEBUG",
    "agent__openai_api_key": "sk-your-api-key",
    "storage__storage_type": "postgres",
    "storage__database__host": "localhost",
    "storage__database__name": "openagents",
})
```

## Settings Categories

The settings are organized into several categories to make them easier to manage:

### App Settings

General application-wide settings:

```python
settings.app.app_name        # Application name
settings.app.debug           # Debug mode
settings.app.log_level       # Logging level
settings.app.secret_key      # Secret key for cryptographic signing
settings.app.environment     # Environment (development, testing, production)
settings.app.api_prefix      # Prefix for API routes
```

### Registry Settings

Settings for the component registry:

```python
settings.registry.auto_discover    # Whether to automatically discover agents
settings.registry.modules          # Modules to scan for agent registrations
```

### Workflow Settings

Settings for workflow management:

```python
settings.workflow.validation_mode  # Validation mode (strict, lenient, none)
```

### Agent Settings

Settings for AI agents and LLMs:

```python
settings.agent.default_llm_provider    # Default LLM provider
settings.agent.openai_api_key          # OpenAI API key
settings.agent.anthropic_api_key       # Anthropic API key
settings.agent.default_model           # Default model identifier
settings.agent.timeout_seconds         # Default timeout for agent operations
settings.agent.max_retries             # Maximum number of retries for agent operations
```

### Job Settings

Settings for job management and execution:

```python
settings.job.job_retention_days            # Days to retain completed jobs
settings.job.max_concurrent_jobs           # Maximum concurrent jobs
settings.job.default_job_timeout_seconds   # Default timeout for job execution
settings.job.default_max_retries           # Default max retries for failed jobs
settings.job.default_retry_delay_seconds   # Default delay between retries
settings.job.store_type                    # Job storage type
settings.job.store_path                    # Path for file-based job storage
```

### Storage Settings

Settings for data storage and persistence:

```python
settings.storage.storage_type          # Storage backend type
settings.storage.file_storage_path     # Path for file storage
settings.storage.redis_url             # Redis connection URL
settings.storage.database.dialect      # Database dialect
settings.storage.database.path         # Path for SQLite database
settings.storage.database.host         # Database host
settings.storage.database.port         # Database port
settings.storage.database.username     # Database username
settings.storage.database.password     # Database password
settings.storage.database.name         # Database name
settings.storage.database.connection_string  # Direct database connection string
```

## FastAPI Integration

The settings can be used with FastAPI dependency injection:

```python
from fastapi import Depends, FastAPI
from openagents_json import settings, get_settings
from openagents_json.settings import Settings

app = FastAPI()

@app.get("/settings")
async def read_settings(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app.app_name,
        "debug": settings.app.debug,
        "environment": settings.app.environment
    }
```

## Adding Custom Settings

You can add custom settings using the `custom_settings` dictionary:

```python
settings.custom_settings["my_custom_setting"] = "custom value"
```

Or by configuring them through environment variables or the `.env` file:

```ini
OPENAGENTS_MY_CUSTOM_SETTING=custom value
```

## Legacy Field Support

For backward compatibility, the settings system supports legacy-style uppercase field names:

```python
# Legacy usage pattern (not recommended for new code)
settings.JOB_STORE_TYPE         # Same as settings.job.store_type
settings.DB_HOST                # Same as settings.storage.database.host
settings.MAX_CONCURRENT_JOBS    # Same as settings.job.max_concurrent_jobs
```

This legacy support ensures that existing code continues to work while transitioning to the new nested structure.

## Validation

The settings system includes validation to ensure that:

1. Settings have appropriate types
2. Required settings are provided
3. Settings with constraints (e.g., minimum values) are valid
4. Dependent settings are consistent (e.g., file storage path is provided when using file storage)

If validation fails, an error will be raised with a helpful message.

## Sensitive Values

Sensitive values like API keys and passwords are handled using Pydantic's `SecretStr` type, which prevents accidental exposure in logs or error messages:

```python
# This will not expose the key in logs or repr()
api_key = settings.agent.openai_api_key

# To access the actual value:
api_key_value = api_key.get_secret_value()
```

## Testing

For testing, you can override settings temporarily using `configure_from_dict`:

```python
import pytest
from openagents_json import configure_from_dict, settings

@pytest.fixture
def test_settings():
    # Original settings
    original_debug = settings.app.debug
    
    # Override settings for test
    configure_from_dict({
        "app__debug": True,
        "job__max_concurrent_jobs": 2,
    })
    
    yield
    
    # Restore original settings
    configure_from_dict({
        "app__debug": original_debug,
    })
```

## Best Practices

1. Use the nested structure (`settings.app.debug`) for new code
2. Avoid using legacy uppercase fields (`settings.DEBUG`) in new code
3. Use environment variables or `.env` files for configuration
4. Always validate sensitive information
5. Handle missing optional settings gracefully 