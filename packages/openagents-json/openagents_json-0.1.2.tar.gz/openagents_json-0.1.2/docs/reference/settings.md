# OpenAgents JSON Settings Reference

This document provides a comprehensive reference for all settings available in the OpenAgents JSON framework.

## Environment Variables

All settings can be configured using environment variables with the prefix `OPENAGENTS_` and nested delimiter `__`. For example:

```
OPENAGENTS_APP__DEBUG=true
OPENAGENTS_AGENT__OPENAI_API_KEY=sk-your-api-key
OPENAGENTS_STORAGE__DATABASE__HOST=localhost
```

## App Settings

Application-wide settings.

| Name | Type | Default | Description |
| ---- | ---- | ------- | ----------- |
| app_name | str | OpenAgents JSON | Name of the application |
| debug | bool | False | Enable debug mode with detailed logging and error messages |
| log_level | str | INFO | Logging level for the application |
| secret_key | SecretStr | *auto-generated* | Secret key for cryptographic signing. Must be set in production |
| environment | str | development | Application environment |
| api_prefix | str | /api | Prefix for API routes |

## Registry Settings

Settings for component registry.

| Name | Type | Default | Description |
| ---- | ---- | ------- | ----------- |
| auto_discover | bool | True | Automatically discover agents in the specified modules |
| modules | List[str] | [] | Modules to scan for agent registrations |

## Workflow Settings

Settings for workflow management.

| Name | Type | Default | Description |
| ---- | ---- | ------- | ----------- |
| validation_mode | str | strict | Validation mode for workflows: strict, lenient, or none |

## Agent Settings

Settings for AI agents and models.

| Name | Type | Default | Description |
| ---- | ---- | ------- | ----------- |
| default_llm_provider | str | openai | Default LLM provider to use when not specified explicitly |
| openai_api_key | SecretStr | None | OpenAI API key for accessing OpenAI models. Required if using OpenAI |
| anthropic_api_key | SecretStr | None | Anthropic API key for accessing Claude models. Required if using Anthropic |
| default_model | str | gpt-3.5-turbo | Default model identifier to use when not specified explicitly |
| timeout_seconds | int | 30 | Default timeout in seconds for agent operations |
| max_retries | int | 3 | Maximum number of retries for agent operations |

## Job Settings

Settings for job management and execution.

| Name | Type | Default | Description |
| ---- | ---- | ------- | ----------- |
| job_retention_days | int | 30 | Number of days to retain completed jobs before cleanup |
| max_concurrent_jobs | int | 100 | Maximum number of concurrent jobs to execute |
| default_job_timeout_seconds | int | 3600 | Default timeout in seconds for job execution |
| default_max_retries | int | 3 | Default maximum number of retries for failed jobs |
| default_retry_delay_seconds | int | 30 | Default delay in seconds between job retries |
| store_type | str | memory | Storage type for jobs: memory, file, database |
| store_path | str | None | Path for file-based job storage |

## Storage Settings

Settings for data storage and persistence.

| Name | Type | Default | Description |
| ---- | ---- | ------- | ----------- |
| storage_type | str | memory | Type of storage backend to use for job and state persistence |
| file_storage_path | Path | None | Path to directory for file storage. Required if storage_type is 'file' |
| redis_url | str | None | Redis connection URL. Required if storage_type is 'redis' |
| **database** | DatabaseSettings | - | Database connection settings |
| database.dialect | str | sqlite | Database dialect: sqlite, postgresql, mysql |
| database.path | str | ./openagents.db | Path for SQLite database |
| database.host | str | localhost | Database host |
| database.port | int | None | Database port |
| database.username | str | None | Database username |
| database.password | SecretStr | None | Database password |
| database.name | str | openagents | Database name |
| database.connection_string | str | None | Direct database connection string (overrides other settings) |

## Legacy Field Support

For backward compatibility, the settings system supports legacy-style uppercase field names:

```python
# Legacy usage pattern (not recommended for new code)
settings.JOB_STORE_TYPE         # Same as settings.job.store_type
settings.DB_HOST                # Same as settings.storage.database.host
settings.MAX_CONCURRENT_JOBS    # Same as settings.job.max_concurrent_jobs
```

This legacy support ensures that existing code continues to work while transitioning to the new nested structure. 