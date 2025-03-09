# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FileModel"]


class FileModel(BaseModel):
    id: str

    created_at: Optional[int] = None

    filename: str

    updated_at: Optional[int] = None

    user_id: str

    access_control: Optional[object] = None

    data: Optional[object] = None

    hash: Optional[str] = None

    meta: Optional[object] = None

    path: Optional[str] = None
