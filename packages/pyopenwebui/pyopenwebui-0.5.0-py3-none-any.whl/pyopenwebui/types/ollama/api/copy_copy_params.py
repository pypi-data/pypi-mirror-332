# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CopyCopyParams"]


class CopyCopyParams(TypedDict, total=False):
    destination: Required[str]

    source: Required[str]

    url_idx: Optional[int]
