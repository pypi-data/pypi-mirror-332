# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ......_models import BaseModel
from .....user_model import UserModel

__all__ = ["AllGetResponse", "AllGetResponseItem"]


class AllGetResponseItem(BaseModel):
    id: str

    created_at: int

    type: str

    updated_at: int

    user_id: str

    version: int

    data: Optional[object] = None

    meta: Optional[object] = None

    user: Optional[UserModel] = None


AllGetResponse: TypeAlias = List[AllGetResponseItem]
