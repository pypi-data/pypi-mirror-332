# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ConfigUpdateParams"]


class ConfigUpdateParams(TypedDict, total=False):
    enable_evaluation_arena_models: Annotated[Optional[bool], PropertyInfo(alias="ENABLE_EVALUATION_ARENA_MODELS")]

    evaluation_arena_models: Annotated[Optional[Iterable[object]], PropertyInfo(alias="EVALUATION_ARENA_MODELS")]
