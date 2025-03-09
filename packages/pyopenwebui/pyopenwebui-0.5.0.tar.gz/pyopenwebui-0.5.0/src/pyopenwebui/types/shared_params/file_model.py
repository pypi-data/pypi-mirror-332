# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FileModel"]


class FileModel(TypedDict, total=False):
    id: Required[str]

    created_at: Required[Optional[int]]

    filename: Required[str]

    updated_at: Required[Optional[int]]

    user_id: Required[str]

    access_control: Optional[object]

    data: Optional[object]

    hash: Optional[str]

    meta: Optional[object]

    path: Optional[str]
