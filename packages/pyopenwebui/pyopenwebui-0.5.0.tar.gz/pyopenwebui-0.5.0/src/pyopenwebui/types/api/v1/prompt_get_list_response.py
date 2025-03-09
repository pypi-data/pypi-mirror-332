# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["PromptGetListResponse", "PromptGetListResponseItem", "PromptGetListResponseItemUser"]


class PromptGetListResponseItemUser(BaseModel):
    id: str

    email: str

    name: str

    profile_image_url: str

    role: str


class PromptGetListResponseItem(BaseModel):
    command: str

    content: str

    timestamp: int

    title: str

    user_id: str

    access_control: Optional[object] = None

    user: Optional[PromptGetListResponseItemUser] = None


PromptGetListResponse: TypeAlias = List[PromptGetListResponseItem]
