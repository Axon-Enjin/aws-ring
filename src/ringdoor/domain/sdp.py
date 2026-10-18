"""Pure checks for a live-view offer and a session URL. No network."""
from __future__ import annotations

from typing import Optional
from urllib.parse import urlparse


def offer_error(sdp: str) -> Optional[str]:
    """Ring's doorbell answers H264 only, and every track must be receive-only. VP8 gets a 500."""
    if "a=recvonly" not in sdp:
        return "Offer must be receive-only"
    if "h264/90000" not in sdp.lower():
        return "Offer must include H264. This doorbell rejects other video codecs."
    return None


def session_url_allowed(url: str, api_base: str) -> bool:
    parsed = urlparse(url)
    base = urlparse(api_base)
    return parsed.scheme == "https" and parsed.netloc == base.netloc and parsed.path.startswith("/v1/")
