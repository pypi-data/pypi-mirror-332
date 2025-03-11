.PHONY: install format lint test docs clean build build-test publish publish-test setup

# Default target
all: format lint test

# Set up the development environment
setup:
	pip install -e ".[dev,docs,test]"
	cp -n .env.dev .env || true
	pre-commit install

# Install the package in development mode
install:
	pip install -e ".[dev,docs]"

# Format code with black and isort
format:
	black openagents_json tests examples
	isort openagents_json tests examples

# Run linting with black, isort, and mypy
lint:
	black --check openagents_json tests examples
	isort --check openagents_json tests examples
	mypy openagents_json

# Run tests with pytest
test:
	pytest

# Generate documentation with mkdocs
docs:
	mkdocs build

# Build the package distribution
build: clean
	python -m build

# Build the package distribution and verify it without publishing
build-test: clean
	python scripts/publish.py --dry-run

# Clean build artifacts
clean:
	rm -rf build dist *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Publish the package to PyPI
publish: build
	python scripts/publish.py

# Publish the package to TestPyPI
publish-test: build
	python scripts/publish.py --test

# Serve the documentation locally
serve-docs:
	mkdocs serve 