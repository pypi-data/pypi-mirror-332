# CI/CD Pipeline

This document describes the Continuous Integration and Continuous Deployment (CI/CD) pipeline for the OpenAgents JSON project.

## Overview

The CI/CD pipeline automates the testing, building, and deployment processes using GitHub Actions. The pipeline includes:

1. **Code Quality Checks**: Linting, formatting, and type checking
2. **Automated Testing**: Unit and integration tests with coverage reporting
3. **Security Scanning**: Dependency vulnerability scanning and code security analysis
4. **Documentation Building**: Automatic documentation generation and publishing
5. **PyPI Release**: Automated package publishing to PyPI

## Workflow Files

The CI/CD pipeline is defined in several GitHub Actions workflow files in the `.github/workflows/` directory:

- `python-tests.yml`: Runs tests, linting, type checking, and security scanning
- `docs.yml`: Builds and publishes documentation
- `pypi-release.yml`: Builds and publishes the package to PyPI
- `dependency-review.yml`: Reviews dependencies for security vulnerabilities

## Workflow Details

### Python Tests and Security

The `python-tests.yml` workflow runs on pushes to the main branch, pull requests to the main branch, and on a weekly schedule for security updates. It includes the following jobs:

#### Test Job

This job runs on multiple Python versions (3.9, 3.10, 3.11) and includes:

1. **Dependency Installation**: Installs the package and development dependencies
2. **Code Formatting Checks**: Verifies code formatting with Black and isort
3. **Type Checking**: Validates type hints with mypy
4. **Testing**: Runs unit and integration tests with pytest
5. **Coverage Reporting**: Generates coverage reports and uploads them to Codecov

#### Security Job

This job performs security scanning:

1. **Bandit**: Scans Python code for common security issues
2. **Safety**: Checks package dependencies for known vulnerabilities

### Documentation

The `docs.yml` workflow runs on pushes to the main branch and pull requests to the main branch. It:

1. Builds the documentation using MkDocs
2. Publishes the documentation to GitHub Pages when pushed to the main branch

### PyPI Release

The `pypi-release.yml` workflow runs when a new GitHub release is created. It:

1. Builds the Python package using the build package
2. Verifies the package with twine
3. Uploads the package to PyPI

### Dependency Review

The `dependency-review.yml` workflow runs on pull requests to review dependencies for security vulnerabilities.

## Setting Up Secrets

The CI/CD pipeline requires the following secrets:

1. `PYPI_USERNAME`: Your PyPI username for package publishing
2. `PYPI_PASSWORD`: Your PyPI password or token for package publishing

To add these secrets:

1. Go to your GitHub repository
2. Navigate to Settings > Secrets and variables > Actions
3. Click "New repository secret"
4. Add each secret with its appropriate value

## Branch Protection Rules

To ensure code quality, we recommend configuring branch protection rules for the main branch:

1. Navigate to Settings > Branches
2. Click "Add rule" next to "Branch protection rules"
3. Enter "main" as the branch name pattern
4. Enable the following settings:
   - Require status checks to pass before merging
   - Require branches to be up to date before merging
   - Select status checks: "test", "security", "docs"
   - Require pull request reviews before merging
   - Dismiss stale pull request approvals when new commits are pushed
   - Require review from Code Owners

## Manual Deployments

While the CI/CD pipeline automates most processes, manual steps are sometimes necessary:

### Creating a Release

To create a new release and trigger the PyPI publishing workflow:

1. Navigate to the Releases page on GitHub
2. Click "Draft a new release"
3. Choose or create a tag following semantic versioning (e.g., v0.1.0)
4. Set the release title and description
5. Add release notes detailing changes
6. Click "Publish release"

### Updating Documentation

Documentation is automatically published when changes are pushed to the main branch. To manually update:

```bash
# Build documentation locally
mkdocs build

# Serve documentation locally for review
mkdocs serve
```

## Troubleshooting

If a workflow fails, you can:

1. View the detailed error logs in the Actions tab of your GitHub repository
2. Re-run a failed workflow by clicking the "Re-run jobs" button
3. Make necessary fixes and commit them to trigger the workflow again

For security scanning failures:
- Review the bandit and safety reports
- Address identified vulnerabilities
- Update dependencies as needed

## Adding Custom Workflows

To add a custom workflow:

1. Create a new YAML file in the `.github/workflows/` directory
2. Define the workflow following the GitHub Actions syntax
3. Commit and push the file to your repository

Example structure for a custom workflow:

```yaml
name: Custom Workflow

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  custom_job:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run custom step
        run: |
          echo "Running custom workflow"
          # Add your commands here
``` 