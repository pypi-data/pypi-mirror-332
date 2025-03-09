# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ChatImportParams"]


class ChatImportParams(TypedDict, total=False):
    chat: Required[object]

    folder_id: Optional[str]

    meta: Optional[object]

    pinned: Optional[bool]
