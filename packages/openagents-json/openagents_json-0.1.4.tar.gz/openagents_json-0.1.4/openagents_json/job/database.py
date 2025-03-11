"""
Database models for job storage in the OpenAgents JSON framework.

This module provides SQLAlchemy ORM models for persisting jobs in a database,
with support for different database backends.
"""

import logging
import os
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Union

from sqlalchemy import (
    JSON,
    Column,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.pool import NullPool, QueuePool

from openagents_json.job.model import Job, JobPriority, JobStatus
from openagents_json.job.retry import RetryPolicy

# Create SQLAlchemy base
Base = declarative_base()

# Define association table for many-to-many relationship between jobs and tags
job_tags = Table(
    "job_tags",
    Base.metadata,
    Column("job_id", String(36), ForeignKey("jobs.job_id"), primary_key=True),
    Column("tag", String(255), primary_key=True),
)

# Define association table for job dependencies
job_dependencies = Table(
    "job_dependencies",
    Base.metadata,
    Column("job_id", String(36), ForeignKey("jobs.job_id"), primary_key=True),
    Column("dependency_id", String(36), ForeignKey("jobs.job_id"), primary_key=True),
)


class JobModel(Base):
    """SQLAlchemy model for job storage."""

    __tablename__ = "jobs"

    # Core attributes
    job_id = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False, default="")
    description = Column(Text, nullable=True)
    payload = Column(JSON, nullable=True)
    status = Column(Enum(JobStatus), nullable=False, default=JobStatus.PENDING)
    priority = Column(Enum(JobPriority), nullable=False, default=JobPriority.MEDIUM)
    max_retries = Column(Integer, nullable=False, default=0)
    retry_delay = Column(Integer, nullable=False, default=0)
    retry_policy = Column(JSON, nullable=True)
    timeout = Column(Integer, nullable=True)
    metadata = Column(JSON, nullable=True)
    created_at = Column(Float, nullable=False)
    updated_at = Column(Float, nullable=False)
    started_at = Column(Float, nullable=True)
    completed_at = Column(Float, nullable=True)
    result = Column(JSON, nullable=True)
    error = Column(JSON, nullable=True)
    retry_count = Column(Integer, default=0)
    batch_id = Column(String(36), nullable=True, index=True)
    worker_id = Column(String(255), nullable=True, index=True)

    # Relationships
    tags = relationship("TagModel", secondary=job_tags, backref="jobs")
    dependencies = relationship(
        "JobModel",
        secondary=job_dependencies,
        primaryjoin=job_id == job_dependencies.c.job_id,
        secondaryjoin=job_id == job_dependencies.c.dependency_id,
        backref="dependent_jobs",
    )

    def to_job(self) -> Job:
        """
        Convert SQLAlchemy model to Job object.

        Returns:
            Job: The converted Job object.
        """
        job = Job(
            job_id=self.job_id,
            name=self.name,
            description=self.description,
            payload=self.payload,
            status=self.status,
            priority=self.priority,
            max_retries=self.max_retries,
            retry_delay=self.retry_delay,
            retry_policy=self.retry_policy,
            timeout=self.timeout,
            tags=[tag.name for tag in self.tags],
            metadata=self.metadata,
            created_at=(
                datetime.fromtimestamp(self.created_at) if self.created_at else None
            ),
            updated_at=(
                datetime.fromtimestamp(self.updated_at) if self.updated_at else None
            ),
            started_at=(
                datetime.fromtimestamp(self.started_at) if self.started_at else None
            ),
            completed_at=(
                datetime.fromtimestamp(self.completed_at) if self.completed_at else None
            ),
            result=self.result,
            error=self.error,
            dependencies=[dep.job_id for dep in self.dependencies],
            batch_id=self.batch_id,
            worker_id=self.worker_id,
        )
        job.retry_count = self.retry_count
        return job

    @classmethod
    def from_job(cls, job: Job) -> "JobModel":
        """
        Convert Job object to SQLAlchemy model.

        Args:
            job: The Job object to convert.

        Returns:
            JobModel: The converted model instance.
        """
        # Extract retry policy if available
        retry_policy_dict = None
        if hasattr(job, "retry_policy") and job.retry_policy:
            retry_policy_dict = job.retry_policy.to_dict()

        model = cls(
            job_id=job.job_id,
            name=job.name,
            description=job.description,
            payload=job.payload,
            status=job.status,
            priority=job.priority,
            max_retries=job.max_retries,
            retry_delay=job.retry_delay,
            retry_policy=retry_policy_dict,
            timeout=job.timeout,
            metadata=job.metadata,
            created_at=(
                job.created_at.timestamp()
                if job.created_at
                else datetime.now().timestamp()
            ),
            updated_at=(
                job.updated_at.timestamp()
                if job.updated_at
                else datetime.now().timestamp()
            ),
            started_at=job.started_at.timestamp() if job.started_at else None,
            completed_at=job.completed_at.timestamp() if job.completed_at else None,
            result=job.result,
            error=job.error,
            retry_count=job.retry_count,
            batch_id=job.batch_id,
            worker_id=getattr(job, "worker_id", None),
        )
        return model


class TagModel(Base):
    """SQLAlchemy model for job tags."""

    __tablename__ = "tags"

    name = Column(String(255), primary_key=True)
    description = Column(Text, nullable=True)

    def __repr__(self):
        return f"<Tag {self.name}>"


def get_engine(
    connection_string: str,
    pooling: bool = True,
    pool_size: int = 5,
    max_overflow: int = 10,
    pool_timeout: int = 30,
    pool_recycle: int = 3600,
    echo: bool = False,
):
    """
    Get SQLAlchemy engine for the given connection string with connection pooling.

    Args:
        connection_string: SQLAlchemy connection string.
        pooling: Whether to enable connection pooling.
        pool_size: The size of the connection pool.
        max_overflow: The maximum overflow size of the pool.
        pool_timeout: The number of seconds to wait before giving up on getting a connection from the pool.
        pool_recycle: The number of seconds after which a connection is automatically recycled.
        echo: Whether to echo SQL queries (useful for debugging).

    Returns:
        SQLAlchemy engine.
    """
    if pooling:
        if "sqlite" in connection_string:
            # SQLite connections are already pooled in a different way,
            # and don't benefit from QueuePool
            logging.info("SQLite detected - using default SQLite pooling")
            return create_engine(connection_string, echo=echo)
        else:
            logging.info(
                f"Creating database engine with connection pooling (pool_size={pool_size}, max_overflow={max_overflow})"
            )
            return create_engine(
                connection_string,
                poolclass=QueuePool,
                pool_size=pool_size,
                max_overflow=max_overflow,
                pool_timeout=pool_timeout,
                pool_recycle=pool_recycle,
                echo=echo,
            )
    else:
        logging.info("Creating database engine without connection pooling")
        return create_engine(connection_string, poolclass=NullPool, echo=echo)


def get_session_factory(engine):
    """
    Get SQLAlchemy session factory for the given engine.

    Args:
        engine: SQLAlchemy engine.

    Returns:
        SQLAlchemy session factory.
    """
    return scoped_session(sessionmaker(bind=engine))


def build_connection_string(
    dialect: str,
    host: Optional[str] = None,
    port: Optional[int] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    database: Optional[str] = None,
    path: Optional[str] = None,
) -> str:
    """
    Build SQLAlchemy connection string from components.

    Args:
        dialect: Database dialect (sqlite, postgresql, mysql).
        host: Database host (for postgresql, mysql).
        port: Database port (for postgresql, mysql).
        username: Database username (for postgresql, mysql).
        password: Database password (for postgresql, mysql).
        database: Database name (for postgresql, mysql).
        path: Database file path (for sqlite).

    Returns:
        SQLAlchemy connection string.
    """
    if dialect == "sqlite":
        path = path or "openagents.db"
        return f"sqlite:///{path}"
    elif dialect == "postgresql":
        host = host or "localhost"
        port = port or 5432
        auth = f"{username}:{password}@" if username and password else ""
        return f"postgresql://{auth}{host}:{port}/{database}"
    elif dialect == "mysql":
        host = host or "localhost"
        port = port or 3306
        auth = f"{username}:{password}@" if username and password else ""
        return f"mysql+pymysql://{auth}{host}:{port}/{database}"
    else:
        raise ValueError(f"Unsupported dialect: {dialect}")


def init_db(engine, create_tables=True):
    """
    Initialize database schema.

    Args:
        engine: SQLAlchemy engine.
        create_tables: Whether to create tables if they don't exist.
    """
    if create_tables:
        Base.metadata.create_all(engine)

    # Create indexes that might be helpful for performance
    try:
        with engine.connect() as connection:
            # Create indexes
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_jobs_status ON jobs (status)"
            )
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_jobs_priority ON jobs (priority)"
            )
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_jobs_batch_id ON jobs (batch_id)"
            )
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_jobs_created_at ON jobs (created_at)"
            )
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_jobs_updated_at ON jobs (updated_at)"
            )
    except Exception as e:
        logging.warning(f"Could not create all indexes: {str(e)}")


class WorkerModel(Base):
    """SQLAlchemy model for worker registration."""

    __tablename__ = "workers"

    worker_id = Column(String(255), primary_key=True)
    hostname = Column(String(255), nullable=True)
    pid = Column(Integer, nullable=True)
    tags = Column(JSON, nullable=True)
    max_concurrent_jobs = Column(Integer, nullable=False, default=5)
    started_at = Column(Float, nullable=False)
    last_heartbeat = Column(Float, nullable=False)
    status = Column(String(50), nullable=False, default="active")
    running_jobs = Column(JSON, nullable=True)
    metadata = Column(JSON, nullable=True)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "WorkerModel":
        """
        Create worker model from dictionary.

        Args:
            data: Worker information dictionary

        Returns:
            WorkerModel instance
        """
        # Convert string timestamps to float
        for ts_field in ["started_at", "last_heartbeat"]:
            if isinstance(data.get(ts_field), str):
                try:
                    dt = datetime.fromisoformat(data[ts_field])
                    data[ts_field] = dt.timestamp()
                except (ValueError, TypeError):
                    data[ts_field] = datetime.now().timestamp()

        return cls(
            worker_id=data.get("worker_id"),
            hostname=data.get("hostname"),
            pid=data.get("pid"),
            tags=data.get("tags"),
            max_concurrent_jobs=data.get("max_concurrent_jobs", 5),
            started_at=data.get("started_at", datetime.now().timestamp()),
            last_heartbeat=data.get("last_heartbeat", datetime.now().timestamp()),
            status=data.get("status", "active"),
            running_jobs=data.get("running_jobs"),
            metadata=data.get("metadata"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert worker model to dictionary.

        Returns:
            Dictionary representation of worker
        """
        return {
            "worker_id": self.worker_id,
            "hostname": self.hostname,
            "pid": self.pid,
            "tags": self.tags,
            "max_concurrent_jobs": self.max_concurrent_jobs,
            "started_at": (
                datetime.fromtimestamp(self.started_at).isoformat()
                if self.started_at
                else None
            ),
            "last_heartbeat": (
                datetime.fromtimestamp(self.last_heartbeat).isoformat()
                if self.last_heartbeat
                else None
            ),
            "status": self.status,
            "running_jobs": self.running_jobs,
            "metadata": self.metadata,
        }
