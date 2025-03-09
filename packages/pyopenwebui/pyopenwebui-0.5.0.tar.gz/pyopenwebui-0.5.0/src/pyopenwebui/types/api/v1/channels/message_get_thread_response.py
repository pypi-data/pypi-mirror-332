# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ....._models import BaseModel

__all__ = [
    "MessageGetThreadResponse",
    "MessageGetThreadResponseItem",
    "MessageGetThreadResponseItemReaction",
    "MessageGetThreadResponseItemUser",
]


class MessageGetThreadResponseItemReaction(BaseModel):
    count: int

    name: str

    user_ids: List[str]


class MessageGetThreadResponseItemUser(BaseModel):
    id: str

    name: str

    profile_image_url: str

    role: str


class MessageGetThreadResponseItem(BaseModel):
    id: str

    content: str

    created_at: int

    latest_reply_at: Optional[int] = None

    reactions: List[MessageGetThreadResponseItemReaction]

    reply_count: int

    updated_at: int

    user: MessageGetThreadResponseItemUser

    user_id: str

    channel_id: Optional[str] = None

    data: Optional[object] = None

    meta: Optional[object] = None

    parent_id: Optional[str] = None


MessageGetThreadResponse: TypeAlias = List[MessageGetThreadResponseItem]
