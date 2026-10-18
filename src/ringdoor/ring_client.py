"""Compatibility imports. The Ring client is an adapter behind DoorGateway."""
from .adapters.ring.client import RingClient, TokenProvider

__all__ = ["RingClient", "TokenProvider"]
