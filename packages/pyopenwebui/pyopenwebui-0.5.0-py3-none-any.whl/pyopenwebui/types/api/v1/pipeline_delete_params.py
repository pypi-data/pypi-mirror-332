# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PipelineDeleteParams"]


class PipelineDeleteParams(TypedDict, total=False):
    id: Required[str]

    url_idx: Required[Annotated[int, PropertyInfo(alias="urlIdx")]]
