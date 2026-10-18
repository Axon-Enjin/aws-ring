"""Compatibility imports. osascript lives in the macOS adapter."""
from .adapters.mac.runner import run_script

__all__ = ["run_script"]
