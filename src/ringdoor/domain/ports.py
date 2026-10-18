"""Ports. Application code depends on these, not on Ring, macOS, or FastAPI."""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Protocol, Tuple


class DoorError(Exception):
    """A door operation failed. Adapters translate vendor errors into this."""

    def __init__(self, status: int, detail: str) -> None:
        self.status = status
        self.detail = detail
        super().__init__(detail)


class DoorGateway(Protocol):
    async def list_devices(self, include: str = ...) -> List[Dict[str, Any]]: ...

    async def event_history(self, device_id: str, event_types: Optional[str] = None) -> List[Dict[str, Any]]: ...

    async def open_whep(self, device_id: str, sdp_offer: str) -> Tuple[str, Optional[str]]: ...

    async def close_whep(self, session_url: str) -> None: ...

    async def download_snapshot(self, device_id: str, start_ms: Optional[int] = None) -> bytes: ...

    async def aclose(self) -> None: ...


class SpeechPort(Protocol):
    def transcribe(self, wav: bytes) -> str: ...


class VisionPort(Protocol):
    def describe(self, image: bytes) -> str: ...
