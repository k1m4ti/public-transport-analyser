"""Configuration module for loading project settings from pyproject.toml

This module provides utility functions to dynamically locate the project root directory 
and parse application-specific settings from the pyproject.toml configuration file. 
"""
from pathlib import Path
import sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


def get_root_dir() -> Path:
    """Dynamically find the project root directory by searching upward for pyproject.toml

    Returns:
        Path: The absolute path to the project root directory.
    """
    return next(p for p in Path(__file__).resolve().parents if (p / "pyproject.toml").exists())


def load_app_config() -> dict:
    """Load and return the app-specific configuration from pyproject.toml

    Returns:
        dict: A directory containing configuration values under the [tool.transport-analyser] section.
    """
    root_dir = get_root_dir()
    pyproject_path = root_dir / "pyproject.toml"

    with open(pyproject_path, "rb") as f:
        config = tomllib.load(f)

    return config.get("tool", {}).get("transport-analyser", {})


ROOT_DIR = get_root_dir()
APP_CONFIG = load_app_config()
