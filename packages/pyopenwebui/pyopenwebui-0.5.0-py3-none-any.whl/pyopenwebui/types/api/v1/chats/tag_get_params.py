# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TagGetParams"]


class TagGetParams(TypedDict, total=False):
    name: Required[str]

    limit: Optional[int]

    skip: Optional[int]
