# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["EmbedEmbedByIndexParams"]


class EmbedEmbedByIndexParams(TypedDict, total=False):
    input: Required[Union[List[str], str]]

    model: Required[str]

    keep_alive: Union[int, str, None]

    options: Optional[object]

    truncate: Optional[bool]
