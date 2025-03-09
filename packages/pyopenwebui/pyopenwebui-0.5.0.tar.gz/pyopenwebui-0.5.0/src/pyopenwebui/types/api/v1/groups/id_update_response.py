# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["IDUpdateResponse"]


class IDUpdateResponse(BaseModel):
    id: str

    created_at: int

    description: str

    name: str

    updated_at: int

    user_id: str

    data: Optional[object] = None

    meta: Optional[object] = None

    permissions: Optional[object] = None

    user_ids: Optional[List[str]] = None
