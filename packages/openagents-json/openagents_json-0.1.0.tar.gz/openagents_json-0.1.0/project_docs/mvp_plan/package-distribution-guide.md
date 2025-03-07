# OpenAgents JSON: Package Distribution Guide

This document provides comprehensive guidance on creating and distributing the OpenAgents JSON package via PyPI, following Python packaging best practices.

## Package Structure

The OpenAgents JSON package follows a modern Python package structure:

```
openagents_json/
├── pyproject.toml          # Modern project configuration
├── setup.cfg               # Package metadata and configuration
├── README.md               # Project documentation
├── LICENSE                 # MIT License
├── CHANGELOG.md            # Version history
├── CONTRIBUTING.md         # Contribution guidelines
├── docs/                   # Documentation
│   ├── index.md            # Documentation home
│   ├── getting-started.md  # Getting started guide
│   ├── api/                # API documentation
│   ├── examples/           # Example documentation
│   └── mkdocs.yml          # MkDocs configuration
├── tests/                  # Test suite
│   ├── __init__.py         # Test package init
│   ├── conftest.py         # pytest configuration
│   ├── unit/               # Unit tests
│   └── integration/        # Integration tests
├── examples/               # Example applications
│   ├── simple_app.py       # Simple example
│   └── complex_app.py      # Complex example
└── openagents_json/        # Source code
    ├── __init__.py         # Package initialization
    ├── py.typed            # Type hints marker
    ├── core/               # Core functionality
    │   ├── __init__.py     # Core package init
    │   ├── workflow.py     # Workflow definitions
    │   ├── orchestrator.py # Workflow orchestration
    │   └── validation.py   # Validation utilities
    ├── fastapi/            # FastAPI integration
    │   ├── __init__.py     # FastAPI package init
    │   ├── app.py          # OpenAgentsApp class
    │   ├── middleware.py   # FastAPI middleware
    │   └── routers.py      # FastAPI routers
    ├── registries/         # Component registries
    │   ├── __init__.py     # Registries package init
    │   └── registry.py     # Registry implementation
    ├── adapters/           # Component adapters
    │   ├── __init__.py     # Adapters package init
    │   ├── llm.py          # LLM adapters
    │   └── tools.py        # Tool adapters
    └── utils/              # Utility functions
        ├── __init__.py     # Utils package init
        └── helpers.py      # Helper functions
```

## Configuration Files

### pyproject.toml

The `pyproject.toml` file is the primary configuration file for modern Python packages:

```toml
[build-system]
requires = ["setuptools>=45", "wheel", "setuptools_scm>=6.2"]
build-backend = "setuptools.build_meta"

[project]
name = "openagents-json"
description = "A FastAPI extension for building AI agent workflows"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Framework :: FastAPI",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "Intended Audience :: Developers",
]
dependencies = [
    "fastapi>=0.68.0",
    "pydantic>=1.8.0",
    "uvicorn>=0.15.0",
    "jinja2>=3.0.0",
    "python-dotenv>=0.19.0",
]
dynamic = ["version"]

[project.urls]
"Homepage" = "https://github.com/yourusername/openagents-json"
"Bug Tracker" = "https://github.com/yourusername/openagents-json/issues"
"Documentation" = "https://openagents-json.readthedocs.io/"

[project.optional-dependencies]
dev = [
    "pytest>=6.0",
    "pytest-cov>=2.12.0",
    "black>=21.5b2",
    "isort>=5.9.1",
    "mypy>=0.910",
    "flake8>=3.9.2",
    "pre-commit>=2.13.0",
]
docs = [
    "mkdocs>=1.2.0",
    "mkdocs-material>=7.1.0",
    "mkdocstrings>=0.15.0",
]
all = [
    "openagents-json[dev,docs]"
]

[tool.setuptools_scm]
write_to = "openagents_json/_version.py"

[tool.black]
line-length = 88
target-version = ['py38']

[tool.isort]
profile = "black"
line_length = 88

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_functions = "test_*"
python_classes = "Test*"
```

### setup.cfg (Alternative to pyproject.toml for some metadata)

```ini
[metadata]
name = openagents-json
author = Your Name
author_email = your.email@example.com
description = A FastAPI extension for building AI agent workflows
long_description = file: README.md
long_description_content_type = text/markdown
keywords = fastapi, agents, workflows, ai
```

## Versioning

Use semantic versioning (SemVer) for version management:

- **Major version (X.0.0)**: Breaking changes that require code modifications
- **Minor version (0.X.0)**: New features in a backward-compatible manner
- **Patch version (0.0.X)**: Backward-compatible bug fixes

During development and early releases, use these guidelines:

- **Alpha releases (0.1.0a1)**: Early development, expect breaking changes
- **Beta releases (0.5.0b1)**: Feature complete but not fully tested
- **Release candidates (1.0.0rc1)**: Potential stable release, testing for bugs

Setup automatic versioning using `setuptools_scm`:

```python
# openagents_json/__init__.py
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "0.1.0.dev0+unknown"

# Export key classes for a clean API
from .core import Workflow
from .fastapi import OpenAgentsApp
from .registries import Registry

__all__ = ["Workflow", "OpenAgentsApp", "Registry", "__version__"]
```

## Package Building

Build the package using modern build tools:

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Check the built distribution files
ls dist/

# Validate the package
twine check dist/*
```

## Distribution Workflow

### Local Testing

Before publishing to PyPI, test the package locally:

```bash
# Install in development mode
pip install -e .

# Install with test dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

### TestPyPI

Before releasing to PyPI, test on TestPyPI:

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ openagents-json
```

### PyPI

Once tested, release to PyPI:

```bash
# Upload to PyPI
twine upload dist/*

# Install from PyPI
pip install openagents-json
```

## CI/CD for Package Distribution

Use GitHub Actions for automated testing and publishing:

```yaml
# .github/workflows/python-publish.yml
name: Upload Python Package

on:
  release:
    types: [created]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
      with:
        fetch-depth: 0  # Required for setuptools_scm

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine

    - name: Build and publish
      env:
        TWINE_USERNAME: ${{ secrets.PYPI_USERNAME }}
        TWINE_PASSWORD: ${{ secrets.PYPI_PASSWORD }}
      run: |
        python -m build
        twine upload dist/*
```

## Documentation Publishing

Set up automatic documentation publishing with ReadTheDocs:

1. Create an account on ReadTheDocs
2. Connect your GitHub repository
3. Configure the documentation settings

```yaml
# .readthedocs.yml
version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "3.10"

python:
  install:
    - method: pip
      path: .
      extra_requirements:
        - docs

mkdocs:
  configuration: docs/mkdocs.yml
```

## Best Practices for Package Maintenance

### Changelog Management

Maintain a detailed changelog:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Feature X

### Fixed
- Bug Y

## [0.1.0] - 2023-03-01

### Added
- Initial release
- Basic workflow engine
- FastAPI integration
```

### Deprecation Policy

Follow a clear deprecation policy:

1. Mark features as deprecated with warnings
2. Keep deprecated features for at least one minor version cycle
3. Remove deprecated features only in major version upgrades

```python
import warnings

def deprecated_function():
    warnings.warn(
        "This function is deprecated and will be removed in version 2.0.0.",
        DeprecationWarning,
        stacklevel=2
    )
    # Function implementation
```

### Release Process

Follow a structured release process:

1. Update the changelog
2. Create a release branch
3. Update version if not using automatic versioning
4. Run all tests
5. Build and verify the package
6. Create a GitHub release
7. Let CI/CD publish to PyPI

## FastAPI Integration Specifics

Since OpenAgents JSON is a FastAPI extension, pay special attention to:

1. **FastAPI Version Compatibility**: Test with multiple FastAPI versions
2. **Extension Patterns**: Follow established FastAPI extension patterns
3. **Middleware Integration**: Ensure proper middleware integration
4. **Starlette Compatibility**: Test with the underlying Starlette framework
5. **ASGI Standards**: Adhere to ASGI standards for compatibility

## Conclusion

Following these Python packaging best practices ensures that OpenAgents JSON will be:

- Easy to install via pip
- Well-documented for users
- Properly versioned for dependency management
- Ready for integration with FastAPI applications
- Maintainable over the long term 