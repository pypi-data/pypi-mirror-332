# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ChatChatByIndexParams"]


class ChatChatByIndexParams(TypedDict, total=False):
    body: Required[object]

    bypass_filter: Optional[bool]
