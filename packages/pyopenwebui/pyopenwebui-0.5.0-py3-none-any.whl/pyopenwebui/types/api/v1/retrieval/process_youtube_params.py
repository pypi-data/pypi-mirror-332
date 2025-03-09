# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProcessYoutubeParams"]


class ProcessYoutubeParams(TypedDict, total=False):
    url: Required[str]

    collection_name: Optional[str]
