# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ModelSetParams"]


class ModelSetParams(TypedDict, total=False):
    default_models: Required[Annotated[Optional[str], PropertyInfo(alias="DEFAULT_MODELS")]]

    model_order_list: Required[Annotated[Optional[List[str]], PropertyInfo(alias="MODEL_ORDER_LIST")]]
