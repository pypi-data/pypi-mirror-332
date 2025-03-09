# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessagePostParams"]


class MessagePostParams(TypedDict, total=False):
    content: Required[str]

    data: Optional[object]

    meta: Optional[object]

    parent_id: Optional[str]
