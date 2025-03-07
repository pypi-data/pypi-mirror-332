"""Configuration utilities for PR Reviewer."""

import os
import json
from pathlib import Path

def get_config_dir():
    """Get the configuration directory."""
    return Path.home() / ".pr-reviewer"

def get_config_path():
    """Get the path to the configuration file."""
    return get_config_dir() / "config.json"

def ensure_config_dir():
    """Ensure the configuration directory exists."""
    config_dir = get_config_dir()
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
    return config_dir

def load_config():
    """Load the configuration file or return default config."""
    config_path = get_config_path()
    if config_path.exists():
        with open(config_path, "r") as f:
            return json.load(f)

    # Default configuration
    return {
        "github": {
            "use_keyring": True,
            "token": ""
        },
        "openai": {
            "use_keyring": True,
            "api_key": "",
            "model": "gpt-4"
        },
        "review": {
            "add_comments": False,
            "skip_files": ["package-lock.json", "yarn.lock"],
            "file_size_limit_kb": 100
        },
        "team": {
            "shared_key_path": "",
            "use_shared_keys": False
        }
    }

def save_config(config):
    """Save the configuration to the config file."""
    ensure_config_dir()
    config_path = get_config_path()
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
    return config_path