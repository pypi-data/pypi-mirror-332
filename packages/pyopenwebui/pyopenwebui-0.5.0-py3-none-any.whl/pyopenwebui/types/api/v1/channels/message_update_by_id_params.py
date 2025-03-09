# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageUpdateByIDParams"]


class MessageUpdateByIDParams(TypedDict, total=False):
    id: Required[str]

    content: Required[str]

    data: Optional[object]

    meta: Optional[object]

    parent_id: Optional[str]
