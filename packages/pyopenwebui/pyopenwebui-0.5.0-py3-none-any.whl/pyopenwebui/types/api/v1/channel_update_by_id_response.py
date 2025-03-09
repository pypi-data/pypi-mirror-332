# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ChannelUpdateByIDResponse"]


class ChannelUpdateByIDResponse(BaseModel):
    id: str

    created_at: int

    name: str

    updated_at: int

    user_id: str

    access_control: Optional[object] = None

    data: Optional[object] = None

    description: Optional[str] = None

    meta: Optional[object] = None

    type: Optional[str] = None
