"""Captions and the scene sentence. Speech and vision are ports."""
from __future__ import annotations

import asyncio
from typing import Protocol

from ..domain.ports import DoorError
from .live import LiveSessions


class _Speech(Protocol):
    def transcribe(self, wav: bytes) -> str: ...


class _Vision(Protocol):
    def describe(self, image: bytes) -> str: ...


class _Bus(Protocol):
    def publish(self, message: dict) -> None: ...


class Reading:
    def __init__(self, bus: _Bus, speech: _Speech, vision: _Vision, live: LiveSessions) -> None:
        self._bus = bus
        self._speech = speech
        self._vision = vision
        self._live = live

    async def caption(self, wav: bytes) -> str:
        text = await self._call(self._speech.transcribe, wav)
        if text:
            self._bus.publish({"kind": "caption", "text": text})
        return text

    async def scene_from_image(self, image: bytes) -> str:
        if not image:
            raise DoorError(400, "Expected an image body")
        sentence = await self._call(self._vision.describe, image)
        self._bus.publish({"kind": "scene", "text": sentence})
        return sentence

    async def scene_from_door(self) -> str:
        image = await self._live.snapshot()
        return await self.scene_from_image(image)

    async def _call(self, fn, payload: bytes) -> str:
        try:
            return await asyncio.to_thread(fn, payload)
        except DoorError:
            raise
        except Exception as exc:
            raise DoorError(502, str(exc)) from exc
