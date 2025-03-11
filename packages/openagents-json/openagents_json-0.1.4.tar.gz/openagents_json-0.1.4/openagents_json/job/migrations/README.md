# Database Migrations for JobStore

This directory contains database migration scripts for the SQLAlchemyJobStore implementation.

## Creating Database Tables

To create the necessary database tables for the SQLAlchemyJobStore, you can use the `create_tables.py` script:

```bash
# Using environment variables from .env file
python -m openagents_json.job.migrations.create_tables --use-env

# Using SQLite with a specific path
python -m openagents_json.job.migrations.create_tables --dialect sqlite --path /path/to/database.db

# Using PostgreSQL
python -m openagents_json.job.migrations.create_tables \
    --dialect postgresql \
    --host localhost \
    --port 5432 \
    --username postgres \
    --password secret \
    --database openagents

# Using a direct connection string
python -m openagents_json.job.migrations.create_tables \
    --connection-string "postgresql://username:password@localhost:5432/dbname"
```

## Environment Variables

When using the `--use-env` flag, the script will use the following environment variables:

- `OPENAGENTS_DB_DIALECT`: Database dialect (sqlite, postgresql, mysql)
- `OPENAGENTS_DB_PATH`: Path for SQLite database
- `OPENAGENTS_DB_HOST`: Database host
- `OPENAGENTS_DB_PORT`: Database port
- `OPENAGENTS_DB_USERNAME`: Database username
- `OPENAGENTS_DB_PASSWORD`: Database password
- `OPENAGENTS_DB_NAME`: Database name
- `OPENAGENTS_DB_CONNECTION_STRING`: Direct SQLAlchemy connection string (overrides other settings)

These can be set in your `.env` file or directly in your environment.

## Automatic Schema Creation

The SQLAlchemyJobStore will automatically create the necessary tables if they don't exist when it's initialized. However, for production environments, it's recommended to run the migration script explicitly before starting your application. 