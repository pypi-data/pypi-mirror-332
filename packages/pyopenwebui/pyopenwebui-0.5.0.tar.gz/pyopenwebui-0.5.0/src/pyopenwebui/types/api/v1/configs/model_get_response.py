# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ModelGetResponse"]


class ModelGetResponse(BaseModel):
    default_models: Optional[str] = FieldInfo(alias="DEFAULT_MODELS", default=None)

    api_model_order_list: Optional[List[str]] = FieldInfo(alias="MODEL_ORDER_LIST", default=None)
