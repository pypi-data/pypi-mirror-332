# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["QueryCollectionParams"]


class QueryCollectionParams(TypedDict, total=False):
    collection_names: Required[List[str]]

    query: Required[str]

    hybrid: Optional[bool]

    k: Optional[int]

    r: Optional[float]
