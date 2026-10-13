"""Verify Ring webhooks and turn hand landmarks into a doorbell event.

The inputs are the raw webhook body and hand points. Faces, images, and video
never enter this module.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import math
from collections import deque
from dataclasses import dataclass

__all__ = [
    "HandEvent",
    "RingEvent",
    "Seen",
    "hand_event",
    "handle",
    "parse_event",
    "should_translate",
    "sign",
    "verify_signature",
]

_LIVE = frozenset({"button_press", "motion_detected"})


def _key_bytes(signing_key: str | bytes) -> bytes:
    if isinstance(signing_key, str):
        return signing_key.encode()
    if isinstance(signing_key, (bytes, bytearray)):
        return bytes(signing_key)
    raise TypeError("signing key must be str or bytes")


def _body_bytes(raw_body: bytes) -> bytes:
    if isinstance(raw_body, str) or not isinstance(raw_body, (bytes, bytearray)):
        raise TypeError("raw_body must be the request bytes, not str")
    return bytes(raw_body)


def sign(signing_key: str | bytes, raw_body: bytes) -> str:
    """Return the X-Signature value Ring would send for this exact body."""
    digest = hmac.new(_key_bytes(signing_key), _body_bytes(raw_body), hashlib.sha256).hexdigest()
    return "sha256=" + digest


def verify_signature(signing_key: str | bytes, raw_body: bytes, signature: str | bytes) -> bool:
    """True when signature is HMAC-SHA256 of the raw body, hex, optional sha256= prefix.

    Compare the header to the bytes Ring sent. Re-serializing the JSON changes
    the digest, so a payload that looks right will still fail.
    """
    body = _body_bytes(raw_body)
    if isinstance(signature, bytes):
        signature = signature.decode()
    if not isinstance(signature, str):
        return False
    received = signature.strip()
    if received.startswith("sha256="):
        received = received[7:]
    expected = hmac.new(_key_bytes(signing_key), body, hashlib.sha256).hexdigest()
    if len(received) != len(expected):
        return False
    return hmac.compare_digest(expected, received)


@dataclass(frozen=True)
class RingEvent:
    request_id: str
    account_id: str
    event_type: str
    event_id: str
    device_id: str
    timestamp_ms: int | None
    sub_type: str | None
    component_ids: tuple[str, ...]


def parse_event(payload: dict) -> RingEvent:
    """Read a Ring webhook v1.1 object. Call this only after the signature checks out."""
    if not isinstance(payload, dict):
        raise ValueError("not a Ring webhook v1.1 payload")
    try:
        meta = payload["meta"]
        data = payload["data"]
        attrs = data.get("attributes") or {}
        if not isinstance(meta, dict) or not isinstance(data, dict) or not isinstance(attrs, dict):
            raise TypeError
        components = attrs.get("component_ids") or ()
        if components and not isinstance(components, (list, tuple)):
            raise TypeError
        timestamp = attrs.get("timestamp")
        return RingEvent(
            request_id=str(meta["request_id"]),
            account_id=str(meta["account_id"]),
            event_type=str(data["type"]),
            event_id=str(data.get("id") or ""),
            device_id=str(attrs.get("source") or attrs.get("source_id") or ""),
            timestamp_ms=None if timestamp is None else int(timestamp),
            sub_type=None if attrs.get("sub_type") is None else str(attrs["sub_type"]),
            component_ids=tuple(str(item) for item in components),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("not a Ring webhook v1.1 payload") from exc


class Seen:
    """Remember request ids so a retried webhook is handled once.

    ponytail: process-local set, cap 1024. Use a shared store if more than one process handles deliveries.
    """

    def __init__(self, cap: int = 1024):
        if cap < 1:
            raise ValueError("cap must be >= 1")
        self.cap = cap
        self._order: deque[str] = deque()
        self._ids: set[str] = set()

    def first(self, request_id: str) -> bool:
        if request_id in self._ids:
            return False
        self._ids.add(request_id)
        self._order.append(request_id)
        if len(self._order) > self.cap:
            self._ids.discard(self._order.popleft())
        return True


def _event_body(event: RingEvent, status: str) -> dict:
    body = {
        "status": status,
        "request_id": event.request_id,
        "account_id": event.account_id,
        "type": event.event_type,
        "event_id": event.event_id,
        "device_id": event.device_id,
        "timestamp_ms": event.timestamp_ms,
        "sub_type": event.sub_type,
        "component_ids": list(event.component_ids),
    }
    return body


def handle(
    raw_body: bytes,
    signature: str | bytes | None,
    signing_key: str | bytes,
    seen: Seen | None = None,
) -> tuple[int, dict]:
    """Verify, parse, and dedupe one delivery.

    401 rejects a bad signature (do not parse it). 400 is a permanent reject for
    a body that is not v1.1. 200 with status duplicate means Ring already got
    this request_id, so it must not retry. The work here is local and returns
    inside Ring's five-second window.
    """
    if not verify_signature(signing_key, raw_body, "" if signature is None else signature):
        return 401, {"error": "invalid signature"}
    try:
        event = parse_event(json.loads(_body_bytes(raw_body)))
    except (json.JSONDecodeError, ValueError, UnicodeError):
        return 400, {"error": "bad payload"}
    if seen is not None and not seen.first(event.request_id):
        return 200, {"status": "duplicate", "request_id": event.request_id}
    return 200, _event_body(event, "ok")


def _xy(point: object) -> tuple[float, float]:
    if isinstance(point, (list, tuple)):
        if len(point) < 2:
            raise ValueError("landmark needs x and y")
        x, y = float(point[0]), float(point[1])
    else:
        try:
            x, y = float(point.x), float(point.y)  # type: ignore[attr-defined]
        except AttributeError:
            raise ValueError("landmark needs x and y") from None
    if not math.isfinite(x) or not math.isfinite(y):
        raise ValueError("landmark is not a finite number")
    return x, y


def _frame(frame: object) -> list[list[tuple[float, float]]]:
    if isinstance(frame, dict):
        raise ValueError("pass hand landmarks only; face data is not accepted")
    hands: list[list[tuple[float, float]]] = []
    try:
        for hand in frame:  # type: ignore[union-attr]
            if isinstance(hand, dict):
                raise ValueError("pass hand landmarks only; face data is not accepted")
            hands.append([_xy(point) for point in hand])
    except TypeError as exc:
        raise ValueError("a frame is a list of hands") from exc
    return hands


@dataclass(frozen=True)
class HandEvent:
    """How many hands are in the latest frame, and whether they moved.

    signing is a gate for a translator. It is not a recognized sign.
    """

    hands: int
    moving: bool
    bbox: tuple[float, float, float, float] | None

    @property
    def signing(self) -> bool:
        return self.hands > 0 and self.moving


def _moved(prev: list, curr: list) -> tuple[float, int]:
    total = 0.0
    count = 0
    for before, after in zip(prev, curr):
        for (ax, ay), (bx, by) in zip(before, after):
            total += math.hypot(bx - ax, by - ay)
            count += 1
    return total, count


def hand_event(frames: object, move: float = 0.02) -> HandEvent:
    """Summarize the last frame of hand landmarks.

    Each frame is a list of hands. Each hand is a list of (x, y) points, or
    objects with .x and .y, in normalized image space. Extra axes are ignored.
    Pass at least two frames to detect movement.

    ponytail: movement is the mean point shift between the last two frames, hands aligned by index. Tune `move` if the camera is far from the signer. A hand entering the frame counts as movement.
    """
    if move < 0:
        raise ValueError("move threshold must be >= 0")
    if isinstance(frames, dict):
        raise ValueError("pass hand landmarks only; face data is not accepted")
    parsed = [_frame(frame) for frame in frames]  # type: ignore[union-attr]
    if not parsed:
        return HandEvent(0, False, None)
    latest = parsed[-1]
    points = [point for hand in latest for point in hand]
    if not points:
        return HandEvent(0, False, None)
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    bbox = (min(xs), min(ys), max(xs), max(ys))
    moving = False
    if len(parsed) >= 2:
        previous = parsed[-2]
        if len(previous) != len(latest):
            moving = True
        else:
            total, count = _moved(previous, latest)
            moving = count > 0 and (total / count) >= move
    return HandEvent(len(latest), moving, bbox)


def should_translate(event: RingEvent, hands: HandEvent) -> bool:
    """True for a doorbell press or a motion event when the hands are moving.

    A vehicle motion event is skipped. This does not read the video.
    """
    if event.event_type not in _LIVE or event.sub_type == "vehicle":
        return False
    return hands.signing
