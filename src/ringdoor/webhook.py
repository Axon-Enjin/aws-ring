"""Compatibility imports. HMAC verification lives in the HTTP adapter."""
from .adapters.http.hmac import sign, verify_signature

__all__ = ["sign", "verify_signature"]
