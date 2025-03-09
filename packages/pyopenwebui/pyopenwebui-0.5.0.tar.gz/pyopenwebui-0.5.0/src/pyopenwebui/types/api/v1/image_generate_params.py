# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ImageGenerateParams"]


class ImageGenerateParams(TypedDict, total=False):
    prompt: Required[str]

    model: Optional[str]

    n: int

    negative_prompt: Optional[str]

    size: Optional[str]
