# GitHub Issue Management Scripts

Scripts for automated GitHub issue updates and task management.

## Overview

These scripts automate the process of updating GitHub issues with progress information, including:

- Adding detailed comments with formatted progress updates
- Updating task lists in issue descriptions (checking off completed items)
- Maintaining consistent reporting through structured JSON files

## Requirements

- Python 3.6+
- `requests` library
- GitHub Personal Access Token with repo permissions

## Setup

1. Install the required Python package:

```bash
pip install requests
```

2. Set up your GitHub token:

```bash
export GITHUB_TOKEN=your_personal_access_token
```

You can generate a token at https://github.com/settings/tokens with `repo` scope permissions.

## File Structure

- `github_issue_updater.py` - Main Python script for updating issues
- `update_issue.sh` - Shell script wrapper for easier usage
- `completed_tasks.json` - List of completed tasks with details
- `pending_tasks.json` - List of remaining tasks with details
- `additional_notes.txt` - Additional notes to include in updates

## Basic Usage

### Update an Issue with Current Progress

```bash
./update_issue.sh --issue 22 --update-tasks
```

Options:
- `--repo owner/repo` - Specify repository (default from environment)
- `--issue NUMBER` - Issue number to update (required)
- `--update-tasks` - Flag to update task list in issue description

## Task Lists

The task lists use this JSON format:

```json
[
  {
    "name": "Task Name",
    "details": [
      "Detail 1",
      "Detail 2"
    ]
  }
]
```

To mark a task as completed:
1. Cut the task from `pending_tasks.json`
2. Paste it into `completed_tasks.json`
3. Update the details as needed
4. Run the update script

## Advanced Usage

For more flexibility, use the Python script directly:

```bash
python github_issue_updater.py \
  --issue 22 \
  --completed completed_tasks.json \
  --pending pending_tasks.json \
  --notes "Additional notes here" \
  --update-tasks
```

## See Also

For more detailed instructions, see the `cursor.rules` file in the repository root. 