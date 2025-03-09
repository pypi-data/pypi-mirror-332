"""Edger: Reclaim your browser choice by redirecting Microsoft Edge."""

# Instead of importing main directly, we should import the module
# This avoids a circular import issue
import importlib.util
import sys

__version__ = "0.1.2"

# Don't import directly to avoid circular imports
def main():
    """Entry point for the package."""
    from .edger import main as edger_main
    edger_main()