# Database Storage Backend

The OpenAgents JSON framework provides a robust database storage backend for persisting jobs and related data. This document explains how to use the SQLAlchemyJobStore, configure different database backends, and optimize database performance.

## Overview

SQLAlchemyJobStore is a production-ready implementation of the JobStore interface that uses SQLAlchemy to persist jobs in a relational database. It supports multiple database backends:

- SQLite (simple file-based database, ideal for development)
- PostgreSQL (robust, enterprise-grade database for production)
- MySQL (popular, widely-used database with good performance)

## Basic Usage

To use SQLAlchemyJobStore with the JobManager:

```python
from openagents_json.job.manager import JobManager
from openagents_json.job.storage import SQLAlchemyJobStore

# Create a SQLAlchemyJobStore
job_store = SQLAlchemyJobStore(
    dialect="sqlite",  # or "postgresql" or "mysql"
    path="jobs.db"     # for SQLite
)

# Initialize JobManager with the job store
job_manager = JobManager(job_store=job_store)
```

## Configuration Options

### SQLite Configuration

SQLite is ideal for development, testing, or small applications:

```python
job_store = SQLAlchemyJobStore(
    dialect="sqlite",
    path="path/to/database.db"  # Optional, defaults to "openagents.db"
)
```

### PostgreSQL Configuration

PostgreSQL is recommended for production environments:

```python
job_store = SQLAlchemyJobStore(
    dialect="postgresql",
    host="localhost",         # Database host
    port=5432,                # Database port
    username="user",          # Database username
    password="password",      # Database password
    database="openagents"     # Database name
)
```

### MySQL Configuration

MySQL provides another production-ready option:

```python
job_store = SQLAlchemyJobStore(
    dialect="mysql",
    host="localhost",         # Database host
    port=3306,                # Database port (default for MySQL)
    username="user",          # Database username
    password="password",      # Database password
    database="openagents"     # Database name
)
```

### Direct Connection String

You can also provide a direct SQLAlchemy connection string:

```python
job_store = SQLAlchemyJobStore(
    connection_string="postgresql://user:password@localhost:5432/openagents"
)
```

## Connection Pooling

SQLAlchemyJobStore supports connection pooling to improve performance by reusing database connections. This is particularly important for production applications with many concurrent operations.

```python
job_store = SQLAlchemyJobStore(
    dialect="postgresql",
    host="localhost",
    username="user",
    password="password",
    database="openagents",
    
    # Connection pooling settings
    pooling=True,              # Enable connection pooling
    pool_size=5,               # Number of connections to keep open
    max_overflow=10,           # Maximum number of connections above pool_size
    pool_timeout=30,           # Seconds to wait for a connection from the pool
    pool_recycle=3600          # Seconds after which connections are recycled
)
```

Connection pooling is automatically configured based on the database dialect:
- For SQLite, the default SQLite connection handling is used (SQLite has its own connection mechanism)
- For PostgreSQL and MySQL, QueuePool is used for efficient connection management

## Performance Optimization

### Index Optimization

SQLAlchemyJobStore automatically creates indexes on common query fields:
- `status`: For querying jobs by status
- `priority`: For ordering jobs by priority
- `batch_id`: For grouping related jobs
- `created_at`: For time-based filtering and sorting
- `updated_at`: For time-based filtering and sorting

### Resource Management

It's important to properly close database resources when they're no longer needed:

```python
# When you're done with the job store
job_store.close()
```

This releases database connections and other resources.

### Query Optimization

When querying for jobs, use specific filters to reduce the result set:

```python
# Retrieve a limited set of jobs with specific filters
jobs = job_store.list(
    status=JobStatus.COMPLETED,
    workflow_id="my-workflow",
    created_after="2023-01-01T00:00:00",
    limit=100,
    sort_by="created_at",
    sort_order="desc"
)
```

### Batch Operations

For handling multiple jobs, use batch operations:

```python
# Create multiple jobs in a single batch
batch_id = job_store.create_job_batch(jobs_list)

# Retrieve all jobs in a batch
batch_jobs = job_store.get_batch_jobs(batch_id)
```

## Configuration via Environment Variables

You can configure the database connection through environment variables:

```python
import os
from openagents_json.job.storage import SQLAlchemyJobStore

job_store = SQLAlchemyJobStore(
    dialect=os.getenv("DB_DIALECT", "sqlite"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", "5432")),
    username=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    path=os.getenv("DB_PATH")
)
```

## Database Cleanup

To prevent the database from growing indefinitely, you can clean up old jobs:

```python
# Delete jobs older than 30 days
deleted_count = job_store.cleanup_old_jobs(days=30)
print(f"Deleted {deleted_count} old jobs")
```

## Troubleshooting

### Connection Issues

If you encounter connection issues:

1. Verify database credentials
2. Check that the database server is running and accessible
3. Ensure the database exists and the user has proper permissions
4. Review firewall settings that might block connections

### Performance Issues

If you experience performance problems:

1. Increase connection pool size for high-concurrency applications
2. Ensure queries are using appropriate filters
3. Add indexes for frequently queried fields
4. Consider using batch operations for multiple jobs
5. Set appropriate timeouts for long-running operations

## Example: Complete Production Configuration

Here's an example of a production-ready PostgreSQL configuration:

```python
job_store = SQLAlchemyJobStore(
    dialect="postgresql",
    host="db.example.com",
    port=5432,
    username="app_user",
    password="secure_password",
    database="openagents_prod",
    pooling=True,
    pool_size=10,
    max_overflow=20,
    pool_timeout=60,
    pool_recycle=1800  # Recycle connections every 30 minutes
)

# Initialize with proper resource cleanup
try:
    # Use the job store...
    job_manager = JobManager(job_store=job_store)
    
    # ...application code...
    
finally:
    # Always close connections when done
    job_store.close()
``` 