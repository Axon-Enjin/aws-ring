"""Compatibility imports. Policy lives in domain.scene_policy; macOS vision is an adapter."""
from .adapters.mac.vision import describe_image
from .domain.scene_policy import parse_labels, sentence_from_labels

__all__ = ["describe_image", "parse_labels", "sentence_from_labels"]
