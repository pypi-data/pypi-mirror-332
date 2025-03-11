# Installation

This guide covers the installation of the OpenAgents JSON framework and its dependencies.

## Requirements

OpenAgents JSON requires:

- Python 3.9 or higher
- FastAPI 0.100.0 or higher
- Pydantic 2.0.0 or higher

## Standard Installation

To install OpenAgents JSON with its standard dependencies:

```bash
pip install openagents-json
```

This will install the core package along with the necessary dependencies.

## Development Installation

For development, you can install the package in editable mode with additional development and documentation dependencies:

```bash
# Clone the repository
git clone https://github.com/nznking/openagents-json.git
cd openagents-json

# Install in editable mode with development dependencies
pip install -e ".[dev,docs]"
```

This includes:

- Testing tools (pytest, pytest-cov, pytest-asyncio)
- Code formatting tools (black, isort)
- Type checking (mypy)
- Documentation tools (mkdocs, mkdocs-material, mkdocstrings)

## Using the Makefile

If you're developing OpenAgents JSON, you can use the included Makefile for common tasks:

```bash
# Install development dependencies
make install

# Run tests
make test

# Format code
make format

# Run linters
make lint

# Build documentation
make docs

# Serve documentation locally
make serve-docs
```

## Environment Variables

OpenAgents JSON uses environment variables for configuration. You can set these in a `.env` file in your project root:

```
OPENAGENTS_DEBUG=True
OPENAGENTS_API_PREFIX=/api/v1
OPENAGENTS_JOB_STORE_TYPE=file
OPENAGENTS_JOB_STORE_PATH=/path/to/job/store
```

All configuration options are documented in the [Configuration Guide](../user-guide/configuration.md).

## Verifying Installation

To verify that OpenAgents JSON is installed correctly, you can run:

```python
import openagents_json

print(f"OpenAgents JSON version: {openagents_json.__version__}")
```

## Next Steps

Once you have installed OpenAgents JSON, you can proceed to the [Quick Start](quick-start.md) guide to learn how to use it. 