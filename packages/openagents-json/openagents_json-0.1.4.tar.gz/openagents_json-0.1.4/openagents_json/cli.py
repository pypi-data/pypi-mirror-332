#!/usr/bin/env python
"""
Command-line interface for OpenAgents JSON.

This module provides the CLI entry points for the package,
allowing users to run common operations from the command line.
"""

import argparse
import sys
from typing import List, Optional

from openagents_json import __version__


def main(args: Optional[List[str]] = None) -> int:
    """
    Main entry point for the CLI.

    Args:
        args: Command line arguments (defaults to sys.argv[1:])

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="openagents-json",
        description="OpenAgents JSON - A framework for building AI agent workflows",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Init command
    init_parser = subparsers.add_parser("init", help="Initialize a new project")
    init_parser.add_argument(
        "--name", default="openagents-project", help="Project name"
    )
    init_parser.add_argument("--directory", default=".", help="Directory to initialize")

    # Run command
    run_parser = subparsers.add_parser("run", help="Run a workflow")
    run_parser.add_argument("workflow", help="Workflow ID to run")
    run_parser.add_argument(
        "--inputs", help="JSON string or file path containing inputs"
    )

    # Parse args
    parsed_args = parser.parse_args(args)

    # If no command was provided, show help and exit
    if not parsed_args.command:
        parser.print_help()
        return 0

    # Handle commands
    if parsed_args.command == "init":
        return handle_init(parsed_args)
    elif parsed_args.command == "run":
        return handle_run(parsed_args)

    return 0


def handle_init(args: argparse.Namespace) -> int:
    """
    Handle the 'init' command.

    Args:
        args: Parsed command line arguments

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    print(f"Initializing new project '{args.name}' in directory '{args.directory}'")
    print("This functionality is not yet implemented.")
    return 0


def handle_run(args: argparse.Namespace) -> int:
    """
    Handle the 'run' command.

    Args:
        args: Parsed command line arguments

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    print(f"Running workflow '{args.workflow}'")
    print("This functionality is not yet implemented.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
