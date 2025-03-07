#!/usr/bin/env python3
"""
PR Reviewer - A command-line tool that reviews GitHub pull requests using OpenAI APIs.
"""

import os
import sys
import argparse
import json
import logging
from typing import Dict, List, Optional, Tuple, Any
import re
import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('pr-reviewer')

class GitHubClient:
    """Client for interacting with GitHub API."""

    def __init__(self, token: str, base_url: str = "https://api.github.com"):
        self.token = token
        self.base_url = base_url
        self.session = self._create_session()
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def _create_session(self) -> requests.Session:
        """Create session with retry logic."""
        session = requests.Session()
        retry = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('https://', adapter)
        session.mount('http://', adapter)
        return session

    def get_pr_details(self, owner: str, repo: str, pr_number: int) -> Dict[str, Any]:
        """Get pull request details."""
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls/{pr_number}"
        response = self.session.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_pr_files(self, owner: str, repo: str, pr_number: int) -> List[Dict[str, Any]]:
        """Get files changed in the pull request."""
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls/{pr_number}/files"
        response = self.session.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_file_content(self, owner: str, repo: str, path: str, ref: str) -> str:
        """Get content of a file at a specific commit."""
        url = f"{self.base_url}/repos/{owner}/{repo}/contents/{path}"
        response = self.session.get(url, headers=self.headers, params={"ref": ref})
        response.raise_for_status()
        content = response.json()

        if content.get('type') != 'file':
            raise ValueError(f"Path does not point to a file: {path}")

        import base64
        return base64.b64decode(content['content']).decode('utf-8')

    def add_comment(self, owner: str, repo: str, pr_number: int, body: str) -> Dict[str, Any]:
        """Add a comment to a pull request."""
        url = f"{self.base_url}/repos/{owner}/{repo}/issues/{pr_number}/comments"
        response = self.session.post(url, headers=self.headers, json={"body": body})
        response.raise_for_status()
        return response.json()

    def add_review_comment(self, owner: str, repo: str, pr_number: int,
                         commit_id: str, path: str, position: int, body: str) -> Dict[str, Any]:
        """Add a review comment to a specific line in a file."""
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls/{pr_number}/comments"
        payload = {
            "commit_id": commit_id,
            "path": path,
            "position": position,
            "body": body
        }
        response = self.session.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()


class OpenAIClient:
    """Client for interacting with OpenAI API."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.base_url = "https://api.openai.com/v1"

    def analyze_code(self, code: str, prompt: str = None) -> str:
        """Analyze code using OpenAI API."""
        if prompt is None:
            prompt = "Review this code for bugs, security issues, and suggestions for improvement:"

        messages = [
            {"role": "system", "content": "You are a code review assistant that provides concise, actionable feedback."},
            {"role": "user", "content": f"{prompt}\n\n```\n{code}\n```"}
        ]

        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": "gpt-4",  # Can be configurable
            "messages": messages,
            "max_tokens": 1000,
            "temperature": 0.2
        }

        response = self.session.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        result = response.json()

        return result["choices"][0]["message"]["content"]

    def analyze_pr(self, pr_description: str, files_summary: str) -> str:
        """Analyze a PR description and files changed to provide overall feedback."""
        messages = [
            {"role": "system", "content": "You are a helpful code review assistant. Provide a concise summary of the pull request, focusing on its purpose, scope, and potential issues."},
            {"role": "user", "content": f"PR Description:\n{pr_description}\n\nFiles changed:\n{files_summary}"}
        ]

        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": "gpt-4",
            "messages": messages,
            "max_tokens": 1000,
            "temperature": 0.2
        }

        response = self.session.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        result = response.json()

        return result["choices"][0]["message"]["content"]


class PRReviewer:
    """Main class for reviewing pull requests."""

    def __init__(self, github_token: str, openai_api_key: str):
        self.github_client = GitHubClient(github_token)
        self.openai_client = OpenAIClient(openai_api_key)

    def parse_pr_url(self, pr_url: str) -> Tuple[str, str, int]:
        """Parse PR URL to extract owner, repo, and PR number."""
        # Match pattern like https://github.com/owner/repo/pull/123
        pattern = r"https?://github\.com/([^/]+)/([^/]+)/pull/(\d+)"
        match = re.match(pattern, pr_url)

        if not match:
            raise ValueError(f"Invalid GitHub PR URL: {pr_url}")

        owner, repo, pr_number = match.groups()
        return owner, repo, int(pr_number)

    def review_pr(self, pr_url: str, comment: bool = False) -> str:
        """Review a pull request and optionally add comments."""
        owner, repo, pr_number = self.parse_pr_url(pr_url)
        logger.info(f"Reviewing PR #{pr_number} in {owner}/{repo}")

        # Get PR details
        pr_details = self.github_client.get_pr_details(owner, repo, pr_number)
        pr_title = pr_details["title"]
        pr_description = pr_details.get("body", "")
        commit_id = pr_details["head"]["sha"]

        logger.info(f"PR Title: {pr_title}")
        logger.info(f"Commit ID: {commit_id}")

        # Get files changed
        files = self.github_client.get_pr_files(owner, repo, pr_number)
        logger.info(f"Found {len(files)} changed files")

        files_summary = "\n".join([f"- {f['filename']} (+{f['additions']}/-{f['deletions']})" for f in files])

        # Analyze PR overall
        logger.info("Analyzing PR overall...")
        overall_review = self.openai_client.analyze_pr(pr_description, files_summary)

        # Review each file individually
        file_reviews = []
        for file in files:
            filename = file["filename"]
            # Skip binary files or very large files
            if file.get("status") == "removed" or file.get("size", 0) > 100000:
                logger.info(f"Skipping {filename} (removed or too large)")
                continue

            logger.info(f"Reviewing file: {filename}")

            try:
                content = self.github_client.get_file_content(owner, repo, filename, commit_id)
                review = self.openai_client.analyze_code(content, f"Review this {filename} file:")
                file_reviews.append((filename, review))

                # Add comment to the PR if requested
                if comment:
                    logger.info(f"Adding review comment for {filename}")
                    self.github_client.add_review_comment(
                        owner, repo, pr_number, commit_id, filename, 1, review
                    )
            except Exception as e:
                logger.error(f"Error reviewing {filename}: {str(e)}")
                file_reviews.append((filename, f"Error reviewing file: {str(e)}"))

        # Compile the full review
        full_review = f"# PR Review: {pr_title}\n\n"
        full_review += "## Overall Assessment\n\n"
        full_review += overall_review
        full_review += "\n\n## File Reviews\n\n"

        for filename, review in file_reviews:
            full_review += f"### {filename}\n\n{review}\n\n"

        # Add the full review as a comment if requested
        if comment:
            logger.info("Adding overall review comment")
            self.github_client.add_comment(owner, repo, pr_number, full_review)

        return full_review


def main():
    """Main entry point for the tool."""
    parser = argparse.ArgumentParser(description="Review GitHub PRs using OpenAI")
    parser.add_argument("pr_url", help="URL of the GitHub PR to review")
    parser.add_argument("--github-token", help="GitHub access token")
    parser.add_argument("--openai-key", help="OpenAI API key")
    parser.add_argument("--comment", action="store_true", help="Add comments to the PR")
    parser.add_argument("--output", help="Save review to output file")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")

    args = parser.parse_args()

    # Setup logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    # Get credentials from args, env vars, or config file
    github_token = args.github_token or os.environ.get("GITHUB_TOKEN")
    openai_key = args.openai_key or os.environ.get("OPENAI_API_KEY")

    if not github_token:
        sys.exit("Error: GitHub token not provided. Use --github-token or set GITHUB_TOKEN environment variable.")

    if not openai_key:
        sys.exit("Error: OpenAI API key not provided. Use --openai-key or set OPENAI_API_KEY environment variable.")

    try:
        reviewer = PRReviewer(github_token, openai_key)
        review = reviewer.review_pr(args.pr_url, comment=args.comment)

        if args.output:
            with open(args.output, "w") as f:
                f.write(review)
            logger.info(f"Review saved to {args.output}")
        else:
            print(review)

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()