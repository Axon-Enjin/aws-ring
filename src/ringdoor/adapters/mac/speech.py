from __future__ import annotations

from .runner import run_script


class MacSpeech:
    def transcribe(self, wav: bytes) -> str:
        if len(wav) < 44:
            return ""
        return " ".join(run_script("transcribe.js", wav, ".wav", timeout=30).split())


def transcribe_wav(wav: bytes) -> str:
    return MacSpeech().transcribe(wav)
