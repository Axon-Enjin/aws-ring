"""HTTP adapter. Translates DoorError into status codes and does not call Ring or macOS."""
from __future__ import annotations

import asyncio
import json
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from pydantic import BaseModel

from ...domain.models import normalize_webhook
from ...domain.ports import DoorError
from .hmac import verify_signature

STATIC = Path(__file__).resolve().parents[2] / "static"


class CloseLive(BaseModel):
    session_url: str


def build_app(settings, bus, ingest, live, reading, lifespan, simulate=None) -> FastAPI:
    app = FastAPI(title="ringdoor", lifespan=lifespan)
    app.state.bus = bus

    def http_error(exc: DoorError) -> HTTPException:
        return HTTPException(exc.status, exc.detail)

    @app.get("/health")
    async def health():
        return {"status": "ok", "source": settings.source}

    @app.post("/webhook/ring")
    async def ring_webhook(request: Request):
        raw = await request.body()
        if not verify_signature(raw, request.headers.get("X-Signature"), settings.hmac_key):
            return JSONResponse({"error": "bad signature"}, status_code=401)
        try:
            body = json.loads(raw)
        except ValueError:
            return JSONResponse({"error": "invalid json"}, status_code=400)
        ev = normalize_webhook(body)
        if bus.is_duplicate(ev.request_id or ev.id):
            return {"status": "duplicate"}
        # Ring requires a 200 within 5s; do the work after responding.
        asyncio.ensure_future(ingest(ev))
        return {"status": "accepted"}

    @app.get("/api/recent")
    async def recent():
        return bus.history

    @app.post("/api/log/clear")
    async def clear_log():
        bus.clear()
        return {"status": "cleared"}

    @app.get("/stream")
    async def stream():
        q = bus.subscribe()

        async def gen():
            try:
                for message in bus.history:
                    yield f"data: {json.dumps(message)}\n\n"
                while True:
                    try:
                        message = await asyncio.wait_for(q.get(), timeout=20)
                        yield f"data: {json.dumps(message)}\n\n"
                    except asyncio.TimeoutError:
                        yield ": ping\n\n"
            finally:
                bus.unsubscribe(q)

        return StreamingResponse(gen(), media_type="text/event-stream", headers={"Cache-Control": "no-cache"})

    @app.post("/api/live/offer")
    async def live_offer(request: Request):
        sdp = (await request.body()).decode("utf-8", errors="replace")
        try:
            answer, session_url = await live.open(sdp)
        except DoorError as exc:
            raise http_error(exc) from exc
        return {"sdp": answer, "session_url": session_url}

    @app.post("/api/live/close")
    async def live_close(body: CloseLive):
        try:
            await live.close(body.session_url)
        except DoorError as exc:
            raise http_error(exc) from exc
        return {"status": "closed"}

    @app.post("/api/captions")
    async def captions(request: Request):
        try:
            text = await reading.caption(await request.body())
        except DoorError as exc:
            raise http_error(exc) from exc
        return {"text": text}

    @app.post("/api/scene")
    async def scene(request: Request):
        try:
            sentence = await reading.scene_from_image(await request.body())
        except DoorError as exc:
            raise http_error(exc) from exc
        return {"sentence": sentence}

    @app.post("/api/scene/ring")
    async def scene_ring():
        try:
            sentence = await reading.scene_from_door()
        except DoorError as exc:
            raise http_error(exc) from exc
        return {"sentence": sentence}

    @app.get("/api/devices")
    async def devices():
        try:
            return await live.devices()
        except DoorError as exc:
            raise http_error(exc) from exc

    if simulate is not None:
        @app.post("/dev/mock/{kind}")
        async def dev_mock(kind: str, sub_type: Optional[str] = None):
            if kind not in ("button_press", "motion_detected"):
                raise HTTPException(400, "kind must be button_press or motion_detected")
            await simulate(kind, sub_type)
            return {"status": "ok"}

    @app.get("/")
    async def index():
        return FileResponse(STATIC / "index.html")

    return app
