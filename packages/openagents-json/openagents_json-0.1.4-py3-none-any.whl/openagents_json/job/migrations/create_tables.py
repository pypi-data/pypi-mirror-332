#!/usr/bin/env python
"""
Database migration script for creating job tables.

This script creates the necessary database tables for the SQLAlchemyJobStore.
It can be run directly to set up the schema for a new database.
"""

import argparse
import logging
import os
import sys

# Add parent directory to path to allow imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from openagents_json.job.database import Base, create_engine
from openagents_json.settings import settings

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def create_tables(
    connection_string=None,
    dialect=None,
    host=None,
    port=None,
    username=None,
    password=None,
    database=None,
    path=None,
):
    """
    Create database tables for the job store.

    Args:
        connection_string: Direct SQLAlchemy connection string
        dialect: Database dialect (sqlite, postgresql, mysql)
        host: Database host
        port: Database port
        username: Database username
        password: Database password
        database: Database name
        path: Path for SQLite database

    Returns:
        True if tables were created successfully, False otherwise
    """
    try:
        # Create engine with provided parameters
        engine = create_engine(
            connection_string=connection_string,
            dialect=dialect,
            host=host,
            port=port,
            username=username,
            password=password,
            database=database,
            path=path,
        )

        # Create all tables
        logger.info(
            f"Creating database tables for dialect: {dialect or 'from connection string'}"
        )
        Base.metadata.create_all(engine)
        logger.info("Database tables created successfully")
        return True

    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}")
        return False


def main():
    """Parse command line arguments and create tables."""
    parser = argparse.ArgumentParser(
        description="Create database tables for the job store"
    )

    # Connection options
    parser.add_argument("--connection-string", help="SQLAlchemy connection string")
    parser.add_argument(
        "--dialect", choices=["sqlite", "postgresql", "mysql"], help="Database dialect"
    )
    parser.add_argument("--host", help="Database host")
    parser.add_argument("--port", type=int, help="Database port")
    parser.add_argument("--username", help="Database username")
    parser.add_argument("--password", help="Database password")
    parser.add_argument("--database", help="Database name")
    parser.add_argument("--path", help="Path for SQLite database")
    parser.add_argument(
        "--use-env",
        action="store_true",
        help="Use connection settings from environment variables",
    )

    args = parser.parse_args()

    # If use-env flag is set, use settings from environment
    if args.use_env:
        logger.info("Using database connection settings from environment variables")
        success = create_tables(
            connection_string=settings.db_connection_string,
            dialect=settings.db_dialect,
            host=settings.db_host,
            port=settings.db_port,
            username=settings.db_username,
            password=settings.db_password,
            database=settings.db_name,
            path=settings.db_path,
        )
    else:
        # Use command line arguments
        success = create_tables(
            connection_string=args.connection_string,
            dialect=args.dialect,
            host=args.host,
            port=args.port,
            username=args.username,
            password=args.password,
            database=args.database,
            path=args.path,
        )

    if success:
        logger.info("Migration completed successfully")
        return 0
    else:
        logger.error("Migration failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
