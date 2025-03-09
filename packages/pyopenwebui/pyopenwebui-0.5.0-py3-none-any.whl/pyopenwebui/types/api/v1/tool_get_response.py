# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["ToolGetResponse", "ToolGetResponseItem", "ToolGetResponseItemMeta", "ToolGetResponseItemUser"]


class ToolGetResponseItemMeta(BaseModel):
    description: Optional[str] = None

    manifest: Optional[object] = None


class ToolGetResponseItemUser(BaseModel):
    id: str

    email: str

    name: str

    profile_image_url: str

    role: str


class ToolGetResponseItem(BaseModel):
    id: str

    created_at: int

    meta: ToolGetResponseItemMeta

    name: str

    updated_at: int

    user_id: str

    access_control: Optional[object] = None

    user: Optional[ToolGetResponseItemUser] = None


ToolGetResponse: TypeAlias = List[ToolGetResponseItem]
