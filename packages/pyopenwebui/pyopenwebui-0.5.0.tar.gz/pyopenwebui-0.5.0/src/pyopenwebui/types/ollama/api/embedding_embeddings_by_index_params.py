# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["EmbeddingEmbeddingsByIndexParams"]


class EmbeddingEmbeddingsByIndexParams(TypedDict, total=False):
    model: Required[str]

    prompt: Required[str]

    keep_alive: Union[int, str, None]

    options: Optional[object]
