"""Process entry. Wiring lives in composition; routes live in the HTTP adapter."""
from __future__ import annotations

from .composition import create_app

__all__ = ["create_app", "app_factory"]


def app_factory():  # uvicorn --factory ringdoor.main:app_factory
    return create_app()
