# Contributing to OpenAgents JSON

First off, thank you for considering contributing to OpenAgents JSON! It's people like you that make this project such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by the [OpenAgents JSON Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [project@openagents.org](mailto:project@openagents.org).

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers understand your report, reproduce the behavior, and find related reports.

**Before Submitting A Bug Report:**

* Check the [issues](https://github.com/username/openagents-json/issues) for a list of existing issues.
* Perform a cursory search to see if the problem has already been reported.

**How Do I Submit A (Good) Bug Report?**

Bugs are tracked as GitHub issues. Create an issue and provide the following information:

* Use a clear and descriptive title.
* Describe the exact steps to reproduce the problem with as much detail as possible.
* Provide specific examples to demonstrate the steps.
* Describe the behavior you observed and point out what exactly is the problem with that behavior.
* Explain which behavior you expected to see instead and why.
* Include screenshots or animated GIFs if applicable.
* If the problem is related to performance or memory, include a CPU profile capture.
* If the problem wasn't triggered by a specific action, describe what you were doing before the problem happened.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion, including completely new features and minor improvements to existing functionality.

**How Do I Submit A (Good) Enhancement Suggestion?**

Enhancement suggestions are tracked as GitHub issues. Create an issue and provide the following information:

* Use a clear and descriptive title.
* Provide a step-by-step description of the suggested enhancement with as much detail as possible.
* Provide specific examples to demonstrate the steps or point to similar existing features.
* Describe the current behavior and explain which behavior you expected to see instead and why.
* Explain why this enhancement would be useful to most users.
* List some other applications where this enhancement exists if applicable.

### Pull Requests

The process described here has several goals:

- Maintain code quality
- Fix problems that are important to users
- Engage the community in working toward the best possible solution
- Enable a sustainable system for maintainers to review contributions

Please follow these steps to have your contribution considered by the maintainers:

1. Fork the repository and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Format your code according to the project guidelines.
7. Submit your pull request!

### Pull Request Process

1. Update the README.md or documentation with details of changes if applicable.
2. Update the CHANGELOG.md with your changes under the "Unreleased" section.
3. The PR will be merged once you have the sign-off of two maintainers.

## Development Environment

### Setting Up

1. Fork the repository.
2. Clone your fork locally.

```bash
git clone https://github.com/your-username/openagents-json.git
cd openagents-json
```

3. Install development dependencies:

```bash
make install-dev
```

4. Set up pre-commit hooks:

```bash
pre-commit install
```

### Running Tests

```bash
make test
```

### Code Style

This project uses:

- [Black](https://github.com/psf/black) for code formatting
- [isort](https://github.com/pycqa/isort) for import sorting
- [Flake8](https://github.com/pycqa/flake8) for linting
- [mypy](https://github.com/python/mypy) for static type checking

You can run all code quality checks with:

```bash
make lint
```

Format code with:

```bash
make format
```

## Git Workflow

1. Create a branch from `main` for your changes.
2. Make your changes in the branch.
3. Run tests and code quality checks.
4. Commit your changes with a meaningful commit message.
5. Push your branch and create a pull request.

### Commit Messages

Our commit messages follow the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
type(scope): short summary
```

Types include:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

Examples:
- `feat(workflow): add parallel execution support`
- `fix(agent): resolve deadlock in agent registration`
- `docs(api): update API documentation`

## Documentation

Documentation is crucial for this project. Please update the documentation when adding new features or changing existing ones. The documentation is built using [MkDocs](https://www.mkdocs.org/).

To build and preview the documentation locally:

```bash
make docs-serve
```

## License

By contributing, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).

## Questions?

Feel free to contact the project maintainers if you have any questions or need further guidance.

Happy contributing!

## Git Branching Strategy

We follow a modified GitFlow workflow with the following branches:

### Core Branches

- **main** - Production-ready code only. This branch should always be deployable.
  - Protected branch - cannot be pushed to directly
  - Changes must go through pull requests with code review
  - Represents the official release history

- **develop** - Integration branch for features.
  - Base branch for feature development
  - Contains all completed features that are awaiting release
  - Should be reasonably stable

### Supporting Branches

- **feature/[name]** - For developing new features.
  - Branch from: `develop`
  - Merge back into: `develop`
  - Naming: `feature/issue-number-brief-description` (e.g., `feature/42-user-authentication`)

- **bugfix/[name]** - For fixing bugs in development.
  - Branch from: `develop`
  - Merge back into: `develop`
  - Naming: `bugfix/issue-number-brief-description` (e.g., `bugfix/57-login-error`)

- **hotfix/[name]** - For critical production fixes.
  - Branch from: `main`
  - Merge back into: `main` AND `develop`
  - Naming: `hotfix/issue-number-brief-description` (e.g., `hotfix/65-security-patch`)

- **release/[version]** - For preparing releases.
  - Branch from: `develop`
  - Merge back into: `main` AND `develop`
  - Naming: `release/x.y.z` (e.g., `release/1.2.0`)

## Workflow

### Feature Development

1. Create a new issue in the issue tracker
2. Create a new feature branch from `develop`:
   ```
   git checkout develop
   git pull
   git checkout -b feature/issue-number-description
   ```
3. Work on your feature, committing changes with meaningful messages
4. Push your changes to the remote repository:
   ```
   git push -u origin feature/issue-number-description
   ```
5. Open a pull request to merge your feature into `develop`
6. After review and approval, the feature branch will be merged into `develop`
7. Delete the feature branch after successful merge

### Hotfix Process

1. Create a hotfix branch from `main`:
   ```
   git checkout main
   git pull
   git checkout -b hotfix/issue-number-description
   ```
2. Fix the issue with minimal changes
3. Open a pull request to merge into `main`
4. After merge to `main`, ensure the fix is also merged to `develop`

### Release Process

1. Create a release branch from `develop`:
   ```
   git checkout develop
   git pull
   git checkout -b release/x.y.z
   ```
2. Make any final adjustments and version updates
3. Open a pull request to merge into `main`
4. After merge to `main`, tag the release:
   ```
   git tag -a vx.y.z -m "Release x.y.z"
   git push origin vx.y.z
   ```
5. Merge the release changes back into `develop`

## Commit Message Guidelines

We follow conventional commits format:

- `feat:` - A new feature
- `fix:` - A bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc)
- `refactor:` - Code changes that neither fix bugs nor add features
- `test:` - Adding or updating tests
- `chore:` - Changes to build process or auxiliary tools

Example: `feat: Add user authentication API`

## Pull Request Guidelines

- Provide a clear, descriptive title and description
- Reference any related issues using the GitHub issue linking format (e.g., "Fixes #42")
- Update documentation for any changed functionality
- Include tests for new features or bug fixes
- Ensure all tests pass before requesting review
- Keep PRs focused on a single concern

Thank you for contributing! 