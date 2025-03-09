# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PipelineGetParams"]


class PipelineGetParams(TypedDict, total=False):
    url_idx: Annotated[Optional[int], PropertyInfo(alias="urlIdx")]
