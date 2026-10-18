"""Alert rules. A failing stage is skipped so the baseline alert still publishes."""
from __future__ import annotations

import time
from typing import List, Protocol

from pydantic import BaseModel

from .models import DoorEvent


class Alert(BaseModel):
    id: str
    level: str  # visitor | motion | info
    headline: str
    detail: str = ""
    event_id: str
    created_ms: int


class Stage(Protocol):
    async def handle(self, event: DoorEvent) -> List[Alert]: ...


_SUBTYPE_TEXT = {
    "human": "A person is at your door",
    "package_delivery": "A package delivery is at your door",
    "vehicle": "A vehicle is near your door",
    "other_motion": "Motion at your door",
    "motion": "Motion at your door",
}


class RuleStage:
    async def handle(self, event: DoorEvent) -> List[Alert]:
        now = int(time.time() * 1000)
        if event.type == "button_press":
            return [Alert(id=f"a_{event.id}", level="visitor", headline="Someone rang your doorbell", detail="Check the door.", event_id=event.id, created_ms=now)]
        if event.type == "motion_detected":
            text = _SUBTYPE_TEXT.get(event.sub_type or "motion", "Motion at your door")
            return [Alert(id=f"a_{event.id}", level="motion", headline=text, event_id=event.id, created_ms=now)]
        return []


def default_stages() -> List[Stage]:
    return [RuleStage()]


async def run_stages(stages: List[Stage], event: DoorEvent) -> List[Alert]:
    alerts: List[Alert] = []
    for stage in stages:
        try:
            alerts.extend(await stage.handle(event))
        except Exception as exc:
            print(f"[pipeline] {type(stage).__name__} failed: {exc}")
    return alerts
