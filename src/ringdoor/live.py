"""Compatibility imports. SDP checks live in ringdoor.domain.sdp."""
from .config import API_BASE
from .domain.sdp import offer_error, session_url_allowed


def allowed_session_url(url: str) -> bool:
    return session_url_allowed(url, API_BASE)


__all__ = ["allowed_session_url", "offer_error"]
