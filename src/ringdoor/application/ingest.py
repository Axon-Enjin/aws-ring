"""Turn a DoorEvent into bus messages. Knows rules and the bus, not HTTP or Ring."""
from __future__ import annotations

from typing import Any, List, Protocol

from ..domain.alerts import Alert, Stage, run_stages
from ..domain.models import DoorEvent


class Publisher(Protocol):
    def publish(self, message: dict) -> None: ...


class Ingest:
    def __init__(self, bus: Publisher, stages: List[Stage]) -> None:
        self._bus = bus
        self._stages = stages

    async def __call__(self, event: DoorEvent) -> None:
        self._bus.publish({"kind": "event", **event.model_dump(exclude={"raw"})})
        for alert in await run_stages(self._stages, event):
            self._bus.publish({"kind": "alert", **_alert(alert)})


def _alert(alert: Alert) -> dict:
    body: dict[str, Any] = alert.model_dump()
    return body
