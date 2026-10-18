"""Wire ports to adapters. This is the only module that knows every concrete type."""
from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from typing import List, Optional

from .adapters.http.routes import build_app
from .adapters.mac.speech import MacSpeech
from .adapters.mac.vision import MacVision
from .adapters.memory.bus import EventBus
from .adapters.mock.source import mock_event
from .adapters.ring.client import RingClient
from .adapters.ring.poll import poll_history
from .application.ingest import Ingest
from .application.live import LiveSessions
from .application.reading import Reading
from .config import API_BASE, Settings
from .domain.alerts import Stage, default_stages
from .domain.ports import DoorGateway, SpeechPort, VisionPort


class _FnSpeech:
    def __init__(self, fn) -> None:
        self._fn = fn

    def transcribe(self, wav: bytes) -> str:
        return self._fn(wav)


class _FnVision:
    def __init__(self, fn) -> None:
        self._fn = fn

    def describe(self, image: bytes) -> str:
        return self._fn(image)


def create_app(
    settings: Optional[Settings] = None,
    stages: Optional[List[Stage]] = None,
    client: Optional[DoorGateway] = None,
    describe=None,
    transcribe=None,
):
    settings = settings or Settings.from_env()
    stages = stages if stages is not None else default_stages()
    bus = EventBus()
    owns_client = client is None
    if client is None and (settings.access_token or settings.refresh_token):
        client = RingClient(settings)
    speech: SpeechPort = _FnSpeech(transcribe) if transcribe is not None else MacSpeech()
    vision: VisionPort = _FnVision(describe) if describe is not None else MacVision()
    ingest = Ingest(bus, stages)
    live = LiveSessions(client, settings.device_id, API_BASE)
    reading = Reading(bus, speech, vision, live)
    tasks: List["asyncio.Task[None]"] = []

    def emit_sync(event) -> None:
        tasks.append(asyncio.ensure_future(ingest(event)))

    @asynccontextmanager
    async def lifespan(_app):
        if settings.source == "poll":
            if not (client and settings.device_id):
                raise RuntimeError("RINGDOOR_SOURCE=poll needs a Ring token and RINGDOOR_DEVICE_ID")
            tasks.append(asyncio.create_task(poll_history(client, settings.device_id, settings.poll_seconds, emit_sync)))
        yield
        for task in tasks:
            task.cancel()
        if owns_client and client is not None:
            await client.aclose()

    simulate = None
    if settings.source != "webhook":
        async def simulate(kind: str, sub_type: Optional[str] = None):
            await ingest(mock_event(kind, sub_type))

    return build_app(settings, bus, ingest, live, reading, lifespan, simulate)
