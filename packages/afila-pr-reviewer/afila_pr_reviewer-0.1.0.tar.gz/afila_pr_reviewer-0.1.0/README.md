# AFILALABS PR Reviewer

A command-line tool developed by AFILALABS (Chicago) that reviews GitHub pull requests using OpenAI's GPT-4 API.

## Features

- Automatically analyzes pull requests from a GitHub URL
- Reviews each file in the PR individually
- Provides overall assessment of the PR
- Can add comments directly to GitHub (optional)
- Configurable through environment variables or config file

## Installation

```bash
pip install afila-pr-reviewer
```

## Requirements

- Python 3.7+
- GitHub personal access token with repo scope
- OpenAI API key

## Usage

### Quick Start

First time setup:
```bash
pr-reviewer --setup
```

Review a PR:
```bash
pr-reviewer https://github.com/owner/repo/pull/123
```

### Command line options

```bash
pr-reviewer https://github.com/owner/repo/pull/123 \
  --github-token your-github-token \
  --openai-key your-openai-api-key \
  --comment \  # Add comments to the PR
  --output review.md  # Save the review to a file
```

### Environment Variables

You can use environment variables instead of passing tokens as arguments:

```bash
export GITHUB_TOKEN=your-github-token
export OPENAI_API_KEY=your-openai-api-key
pr-reviewer https://github.com/owner/repo/pull/123
```

## License

MIT