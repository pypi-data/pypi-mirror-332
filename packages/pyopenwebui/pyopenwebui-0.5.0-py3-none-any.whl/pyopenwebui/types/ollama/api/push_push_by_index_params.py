# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PushPushByIndexParams"]


class PushPushByIndexParams(TypedDict, total=False):
    name: Required[str]

    insecure: Optional[bool]

    stream: Optional[bool]
