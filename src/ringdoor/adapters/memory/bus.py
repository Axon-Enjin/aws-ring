"""In-memory fan-out with replay and idempotency."""
from __future__ import annotations

import asyncio
from typing import Any, Dict, List, Optional, Set


class EventBus:
    """Messages are dicts: {kind: event|alert|caption|scene, ...}."""

    def __init__(self, max_history: int = 200) -> None:
        self.history: List[Dict[str, Any]] = []
        self._subs: Set["asyncio.Queue[Dict[str, Any]]"] = set()
        self._seen: Set[str] = set()
        self._max = max_history

    def is_duplicate(self, key: Optional[str]) -> bool:
        """Ring retries deliveries; request_id (or event id) makes handling idempotent."""
        if not key:
            return False
        if key in self._seen:
            return True
        self._seen.add(key)
        if len(self._seen) > 5000:
            self._seen = set(list(self._seen)[-2500:])
        return False

    def clear(self) -> None:
        self.history.clear()

    def publish(self, message: Dict[str, Any]) -> None:
        self.history.append(message)
        del self.history[: -self._max]
        for q in list(self._subs):
            q.put_nowait(message)

    def subscribe(self) -> "asyncio.Queue[Dict[str, Any]]":
        q: "asyncio.Queue[Dict[str, Any]]" = asyncio.Queue()
        self._subs.add(q)
        return q

    def unsubscribe(self, q: "asyncio.Queue[Dict[str, Any]]") -> None:
        self._subs.discard(q)
