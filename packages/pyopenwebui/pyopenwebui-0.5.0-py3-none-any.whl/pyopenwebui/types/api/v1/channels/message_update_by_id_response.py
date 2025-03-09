# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["MessageUpdateByIDResponse"]


class MessageUpdateByIDResponse(BaseModel):
    id: str

    content: str

    created_at: int

    updated_at: int

    user_id: str

    channel_id: Optional[str] = None

    data: Optional[object] = None

    meta: Optional[object] = None

    parent_id: Optional[str] = None
