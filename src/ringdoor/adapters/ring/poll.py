"""Playground tokens cannot register a webhook URL, so history is polled instead."""
from __future__ import annotations

import asyncio

from ...domain.models import normalize_history_item
from ...domain.ports import DoorGateway


async def poll_history(door: DoorGateway, device_id: str, interval: float, emit) -> None:
    """First pass only records what already exists (no replay of old events as new alerts)."""
    seen = set()
    primed = False
    while True:
        try:
            for item in await door.event_history(device_id):
                ev = normalize_history_item(item, device_id)
                if ev.id in seen:
                    continue
                seen.add(ev.id)
                if primed:
                    emit(ev)
            primed = True
        except Exception as exc:
            print(f"[poll] {type(exc).__name__}: {exc}")
        await asyncio.sleep(interval)
