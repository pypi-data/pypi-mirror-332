# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["FeedbackGetByIDResponse"]


class FeedbackGetByIDResponse(BaseModel):
    id: str

    created_at: int

    type: str

    updated_at: int

    user_id: str

    version: int

    data: Optional[object] = None

    meta: Optional[object] = None

    snapshot: Optional[object] = None
