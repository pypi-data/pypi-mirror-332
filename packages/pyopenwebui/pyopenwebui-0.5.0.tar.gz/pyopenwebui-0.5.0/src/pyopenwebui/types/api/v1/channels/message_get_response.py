# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ....._models import BaseModel

__all__ = [
    "MessageGetResponse",
    "MessageGetResponseItem",
    "MessageGetResponseItemReaction",
    "MessageGetResponseItemUser",
]


class MessageGetResponseItemReaction(BaseModel):
    count: int

    name: str

    user_ids: List[str]


class MessageGetResponseItemUser(BaseModel):
    id: str

    name: str

    profile_image_url: str

    role: str


class MessageGetResponseItem(BaseModel):
    id: str

    content: str

    created_at: int

    latest_reply_at: Optional[int] = None

    reactions: List[MessageGetResponseItemReaction]

    reply_count: int

    updated_at: int

    user: MessageGetResponseItemUser

    user_id: str

    channel_id: Optional[str] = None

    data: Optional[object] = None

    meta: Optional[object] = None

    parent_id: Optional[str] = None


MessageGetResponse: TypeAlias = List[MessageGetResponseItem]
