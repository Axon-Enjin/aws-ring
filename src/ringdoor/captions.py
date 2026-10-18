"""Compatibility imports. Speech recognition is the macOS adapter."""
from .adapters.mac.speech import transcribe_wav

__all__ = ["transcribe_wav"]
