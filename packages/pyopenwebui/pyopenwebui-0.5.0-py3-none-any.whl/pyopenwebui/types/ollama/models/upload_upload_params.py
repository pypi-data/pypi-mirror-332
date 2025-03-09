# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ...._types import FileTypes

__all__ = ["UploadUploadParams"]


class UploadUploadParams(TypedDict, total=False):
    file: Required[FileTypes]

    url_idx: Optional[int]
