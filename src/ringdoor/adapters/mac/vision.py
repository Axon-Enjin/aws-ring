from __future__ import annotations

from ...domain.scene_policy import parse_labels, sentence_from_labels
from .runner import run_script


class MacVision:
    def describe(self, image: bytes) -> str:
        text = run_script("describe.js", image, ".jpg", timeout=90)
        return sentence_from_labels(parse_labels(text))


def describe_image(image: bytes) -> str:
    return MacVision().describe(image)
