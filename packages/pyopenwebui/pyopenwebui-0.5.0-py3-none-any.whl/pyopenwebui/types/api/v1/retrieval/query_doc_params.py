# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["QueryDocParams"]


class QueryDocParams(TypedDict, total=False):
    collection_name: Required[str]

    query: Required[str]

    hybrid: Optional[bool]

    k: Optional[int]

    r: Optional[float]
