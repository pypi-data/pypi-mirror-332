# End of Cycle Review Process

This document outlines the comprehensive process for conducting end-of-cycle reviews in the OpenAgents JSON project, integrating repository documentation, code quality assessment, and GitHub issue management.

## Overview

The end-of-cycle review process helps ensure:
- Code quality and consistency
- Comprehensive documentation
- Up-to-date GitHub issue tracking
- Clear progress assessments for stakeholders
- Developer-friendly codebase maintenance
- Scalable AI agentic workload framework

## Setup

Before your first review, run the setup script to install necessary dependencies:

```bash
.scripts/setup_review_tools.sh
```

This script installs:
- `tree` command for repository structure documentation
- Python code quality tools (`flake8`, `interrogate`)
- `jq` for JSON processing

## Running a Review

### Complete Review Process

To run a full end-of-cycle review connected to a GitHub issue:

```bash
.scripts/end_of_cycle_review.sh <issue_number>
```

For example:

```bash
.scripts/end_of_cycle_review.sh 42
```

This will:
1. Generate repository structure documentation
2. Run code quality analysis
3. Check for documentation that needs to be updated
4. Prompt you to update completed/pending tasks
5. Generate a summary report
6. Update the GitHub issue (after confirmation)

### Options

The review script supports the following options:

- `--skip-code-analysis`: Skip running code quality tools
- `--skip-tree-gen`: Skip generating repository structure documentation
- `--skip-doc-check`: Skip documentation checking process

Example:

```bash
.scripts/end_of_cycle_review.sh 42 --skip-code-analysis
```

### Repository Structure Only

If you just want to generate the repository structure documentation:

```bash
.scripts/generate_repo_tree.sh
```

This creates a timestamped file in `project_docs/repo_structure/`.

## Managing GitHub Issues

The review process integrates with the GitHub issue management tools. For each review:

1. Update `.scripts/gh_issue_management/completed_tasks.json` with tasks completed in this cycle
2. Update `.scripts/gh_issue_management/pending_tasks.json` with tasks still pending
3. Update `.scripts/gh_issue_management/additional_notes.txt` with context and explanations

The review script will use these files to generate a summary report and update the GitHub issue.

## Documentation Management

The end-of-cycle review process includes automated assistance for managing both project documentation and user/developer documentation.

### Project Documentation

The review includes checks for project documentation in the `project_docs` directory, focusing on:

- Build strategy documents in `project_docs/mvp_plan/`
- Implementation strategy and technical decisions
- Package distribution guidelines
- Scaling path documentation

### User/Developer Documentation

The review also checks user-facing documentation in the `docs` directory:

- User guides and tutorials in `docs/getting-started/`
- API documentation
- Installation and configuration guides

### Documentation Check Process

The script will:
1. Generate a documentation checklist in the review artifacts directory
2. List recently modified documentation files that may need review
3. Offer to open key documentation files for immediate review
4. Include documentation updates in the GitHub issue summary

## Review Artifacts

Each review generates artifacts in the `project_docs/cycle_reviews/` directory, including:

- Review summary (markdown)
- Repository structure documentation
- Code quality reports
- Documentation checklist

These artifacts provide a historical record of project progress and can be referenced in future planning.

## Code Review Standards

During the review process, assess code against these standards:

### Code Quality
- Consistent formatting and style
- Comprehensive docstrings
- No unnecessary commented code
- No debug statements in production code

### Developer Experience
- Intuitive APIs with clear documentation
- Helpful error messages
- Comments explaining complex logic
- Up-to-date dependency documentation

### AI Agent Framework Considerations
- Consistent agent interfaces
- Modular and reusable components
- Well-documented stateful operations
- Proper error handling
- Clear configuration documentation

## Documentation Review Standards

When reviewing documentation, ensure:

### Project Documentation Standards
- Technical accuracy and completeness
- Consistency with implemented features
- Clear explanation of architectural decisions
- Up-to-date build strategies and scaling paths

### User/Developer Documentation Standards
- Easy-to-follow tutorials and guides
- Comprehensive API documentation
- Accurate installation instructions
- Clear configuration guidance
- Helpful troubleshooting information

## Integration with Development Workflow

The end-of-cycle review process should be integrated into your development workflow:

1. Complete a development cycle ("yolo")
2. Run the end-of-cycle review
3. Update documentation as needed
4. Address any issues identified in the review
5. Update GitHub issue with progress
6. Begin the next development cycle

## Expanding the Review Process

The review process can be expanded by:

1. Adding additional code quality tools to `.scripts/setup_review_tools.sh`
2. Extending the cursor rule at `.cursor/rules/end-of-routine-process.mdc`
3. Adding custom checks to `.scripts/end_of_cycle_review.sh`

## Related Documentation

- [GitHub Issue Integration](../.cursor/rules/github-issue-integration.mdc)
- [End of Cycle Review Rule](../.cursor/rules/end-of-routine-process.mdc) 