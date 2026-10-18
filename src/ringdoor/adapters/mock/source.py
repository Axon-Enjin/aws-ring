"""Synthetic doorbell events in the documented v1.1 envelope."""
from __future__ import annotations

import time
import uuid
from typing import Any, Dict, Optional

from ...domain.models import DoorEvent, normalize_webhook


def mock_webhook_body(kind: str = "button_press", device_id: str = "mock.ring.device.front-door", sub_type: Optional[str] = None) -> Dict[str, Any]:
    ts = int(time.time() * 1000)
    attrs: Dict[str, Any] = {"source": device_id, "source_type": "devices", "timestamp": ts}
    if kind == "motion_detected":
        attrs["sub_type"] = sub_type or "human"
    return {
        "meta": {"version": "1.1", "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "request_id": str(uuid.uuid4()), "account_id": "mock-account"},
        "data": {
            "id": f"{device_id}_{'motion' if kind == 'motion_detected' else 'button_press'}_{ts}",
            "type": kind,
            "attributes": attrs,
            "relationships": {"devices": {"links": {"self": f"/v1/devices/{device_id}"}}},
        },
    }


def mock_event(kind: str = "button_press", sub_type: Optional[str] = None) -> DoorEvent:
    return normalize_webhook(mock_webhook_body(kind, sub_type=sub_type), source="mock")
