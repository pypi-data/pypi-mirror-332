# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = [
    "ToolGetListResponse",
    "ToolGetListResponseItem",
    "ToolGetListResponseItemMeta",
    "ToolGetListResponseItemUser",
]


class ToolGetListResponseItemMeta(BaseModel):
    description: Optional[str] = None

    manifest: Optional[object] = None


class ToolGetListResponseItemUser(BaseModel):
    id: str

    email: str

    name: str

    profile_image_url: str

    role: str


class ToolGetListResponseItem(BaseModel):
    id: str

    created_at: int

    meta: ToolGetListResponseItemMeta

    name: str

    updated_at: int

    user_id: str

    access_control: Optional[object] = None

    user: Optional[ToolGetListResponseItemUser] = None


ToolGetListResponse: TypeAlias = List[ToolGetListResponseItem]
