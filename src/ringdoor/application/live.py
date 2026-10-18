"""Live view and snapshots through a DoorGateway. SDP rules stay in the domain."""
from __future__ import annotations

from typing import List, Optional, Tuple

from ..domain.ports import DoorError, DoorGateway
from ..domain.sdp import offer_error, session_url_allowed

_NO_DOOR = "No Ring credentials configured"


class LiveSessions:
    def __init__(self, door: Optional[DoorGateway], device_id: Optional[str], api_base: str) -> None:
        self._door = door
        self._device_id = device_id
        self._api_base = api_base

    async def open(self, sdp: str) -> Tuple[str, Optional[str]]:
        self._require_door()
        problem = offer_error(sdp)
        if problem:
            raise DoorError(400, problem)
        return await self._door.open_whep(await self._device(), sdp)  # type: ignore[union-attr]

    async def close(self, session_url: str) -> None:
        self._require_door()
        if not session_url_allowed(session_url, self._api_base):
            raise DoorError(400, "Session URL is not a Ring media session")
        await self._door.close_whep(session_url)  # type: ignore[union-attr]

    async def snapshot(self) -> bytes:
        self._require_door()
        return await self._door.download_snapshot(await self._device())  # type: ignore[union-attr]

    async def devices(self) -> List[dict]:
        self._require_door()
        return await self._door.list_devices()  # type: ignore[union-attr]

    def _require_door(self) -> None:
        if self._door is None:
            raise DoorError(503, _NO_DOOR)

    async def _device(self) -> str:
        if self._device_id:
            return self._device_id
        found = await self._door.list_devices()  # type: ignore[union-attr]
        if not found:
            raise DoorError(404, "No Ring devices on this token")
        return found[0]["id"]
