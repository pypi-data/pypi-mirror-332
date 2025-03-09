# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["GenerateGenerateByIndexParams"]


class GenerateGenerateByIndexParams(TypedDict, total=False):
    model: Required[str]

    prompt: Required[str]

    context: Optional[Iterable[int]]

    format: Optional[str]

    images: Optional[List[str]]

    keep_alive: Union[int, str, None]

    options: Optional[object]

    raw: Optional[bool]

    stream: Optional[bool]

    suffix: Optional[str]

    system: Optional[str]

    template: Optional[str]
