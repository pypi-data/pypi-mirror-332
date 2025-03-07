#!/usr/bin/env python3
"""
GitHub Issue Updater

A script to update GitHub issues with progress information, add comments, and update task lists.
"""

import os
import sys
import json
import argparse
import requests
from typing import Dict, List, Optional, Union, Any
from datetime import datetime

class GitHubIssueUpdater:
    """A class to update GitHub issues with progress information."""
    
    def __init__(self, token: str = None, repo: str = None):
        """Initialize the GitHubIssueUpdater with authentication token and repo information.
        
        Args:
            token: GitHub Personal Access Token with repo permissions
            repo: Repository name in format "owner/repo"
        """
        self.token = token or os.environ.get("GITHUB_TOKEN")
        if not self.token:
            raise ValueError("GitHub token is required. Set GITHUB_TOKEN environment variable or pass token parameter.")
        
        self.repo = repo or os.environ.get("GITHUB_REPOSITORY")
        if not self.repo:
            raise ValueError("GitHub repository is required. Set GITHUB_REPOSITORY environment variable or pass repo parameter.")
        
        self.api_base_url = f"https://api.github.com/repos/{self.repo}"
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def get_issue(self, issue_number: int) -> Dict[str, Any]:
        """Get information about a specific issue.
        
        Args:
            issue_number: The issue number
            
        Returns:
            Dict containing issue information
        """
        url = f"{self.api_base_url}/issues/{issue_number}"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code != 200:
            error_msg = f"Failed to get issue #{issue_number}: {response.status_code} - {response.text}"
            raise Exception(error_msg)
            
        return response.json()
    
    def add_comment(self, issue_number: int, comment_text: str) -> Dict[str, Any]:
        """Add a comment to an issue.
        
        Args:
            issue_number: The issue number
            comment_text: The text of the comment to add
            
        Returns:
            Dict containing the created comment information
        """
        url = f"{self.api_base_url}/issues/{issue_number}/comments"
        data = {"body": comment_text}
        
        response = requests.post(url, headers=self.headers, json=data)
        
        if response.status_code != 201:
            error_msg = f"Failed to add comment to issue #{issue_number}: {response.status_code} - {response.text}"
            raise Exception(error_msg)
            
        return response.json()
    
    def update_issue(self, issue_number: int, updates: Dict[str, str]) -> Dict[str, Any]:
        """Update an issue with new information.
        
        Args:
            issue_number: The issue number
            updates: Dict containing fields to update (title, body, state, etc.)
            
        Returns:
            Dict containing the updated issue information
        """
        url = f"{self.api_base_url}/issues/{issue_number}"
        
        response = requests.patch(url, headers=self.headers, json=updates)
        
        if response.status_code != 200:
            error_msg = f"Failed to update issue #{issue_number}: {response.status_code} - {response.text}"
            raise Exception(error_msg)
            
        return response.json()
    
    def update_task_list(self, issue_number: int, completed_tasks: List[str]) -> Dict[str, Any]:
        """Update the task list in an issue description based on task names.
        
        Args:
            issue_number: The issue number
            completed_tasks: List of task descriptions to mark as completed
            
        Returns:
            Dict containing the updated issue information
        """
        issue = self.get_issue(issue_number)
        body = issue["body"]
        
        # Task items look like "- [ ] Task description" (incomplete) or "- [x] Task description" (complete)
        for task in completed_tasks:
            # Escape special regex characters
            escaped_task = task.replace("[", r"\[").replace("]", r"\]").replace("(", r"\(").replace(")", r"\)")
            unchecked_pattern = f"- [ ] {escaped_task}"
            checked_pattern = f"- [x] {escaped_task}"
            
            # Only update if it's not already checked
            if unchecked_pattern in body:
                body = body.replace(unchecked_pattern, checked_pattern)
        
        # Update the issue with the new body
        updates = {"body": body}
        return self.update_issue(issue_number, updates)
    
    def generate_progress_comment(self, completed_tasks: List[Dict[str, str]], 
                                 pending_tasks: List[Dict[str, str]], 
                                 additional_notes: str = "") -> str:
        """Generate a formatted comment with task progress information.
        
        Args:
            completed_tasks: List of dicts with keys 'name' and 'details'
            pending_tasks: List of dicts with keys 'name' and 'details'
            additional_notes: Optional additional notes to include
            
        Returns:
            Formatted markdown comment text
        """
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comment = f"## Progress Update - {now}\n\n"
        
        if completed_tasks:
            comment += "### Completed Tasks ✅\n\n"
            for task in completed_tasks:
                comment += f"- [x] **{task['name']}**\n"
                if task.get('details'):
                    for detail in task['details']:
                        comment += f"  - {detail}\n"
                comment += "\n"
        
        if pending_tasks:
            comment += "### Remaining Tasks ⏳\n\n"
            for task in pending_tasks:
                comment += f"- [ ] **{task['name']}**\n"
                if task.get('details'):
                    for detail in task['details']:
                        comment += f"  - {detail}\n"
                comment += "\n"
        
        if additional_notes:
            comment += f"### Additional Notes\n\n{additional_notes}\n"
        
        return comment

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description="Update GitHub issues with progress information")
    parser.add_argument("--token", help="GitHub Personal Access Token (or set GITHUB_TOKEN env var)")
    parser.add_argument("--repo", help="Repository in format owner/repo (or set GITHUB_REPOSITORY env var)")
    parser.add_argument("--issue", type=int, required=True, help="Issue number to update")
    parser.add_argument("--completed", help="JSON file with completed tasks")
    parser.add_argument("--pending", help="JSON file with pending tasks")
    parser.add_argument("--notes", help="Additional notes to include in the comment")
    parser.add_argument("--update-tasks", action="store_true", help="Update task list in issue description")
    
    args = parser.parse_args()
    
    try:
        updater = GitHubIssueUpdater(args.token, args.repo)
        
        # Load completed and pending tasks from JSON files
        completed_tasks = []
        if args.completed:
            with open(args.completed, 'r') as f:
                completed_tasks = json.load(f)
        
        pending_tasks = []
        if args.pending:
            with open(args.pending, 'r') as f:
                pending_tasks = json.load(f)
        
        # Generate and post comment
        if completed_tasks or pending_tasks or args.notes:
            comment = updater.generate_progress_comment(
                completed_tasks, 
                pending_tasks,
                args.notes
            )
            result = updater.add_comment(args.issue, comment)
            print(f"Comment added to issue #{args.issue}: {result['html_url']}")
        
        # Update task list in issue description if requested
        if args.update_tasks and completed_tasks:
            task_names = [task['name'] for task in completed_tasks]
            updater.update_task_list(args.issue, task_names)
            print(f"Updated task list in issue #{args.issue}")
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 