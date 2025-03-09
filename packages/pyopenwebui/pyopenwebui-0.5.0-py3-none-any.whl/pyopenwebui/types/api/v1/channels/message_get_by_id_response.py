# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["MessageGetByIDResponse", "Reaction", "User"]


class Reaction(BaseModel):
    count: int

    name: str

    user_ids: List[str]


class User(BaseModel):
    id: str

    name: str

    profile_image_url: str

    role: str


class MessageGetByIDResponse(BaseModel):
    id: str

    content: str

    created_at: int

    latest_reply_at: Optional[int] = None

    reactions: List[Reaction]

    reply_count: int

    updated_at: int

    user: User

    user_id: str

    channel_id: Optional[str] = None

    data: Optional[object] = None

    meta: Optional[object] = None

    parent_id: Optional[str] = None
