# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["FolderGetResponse", "FolderGetResponseItem"]


class FolderGetResponseItem(BaseModel):
    id: str

    created_at: int

    name: str

    updated_at: int

    user_id: str

    is_expanded: Optional[bool] = None

    items: Optional[object] = None

    meta: Optional[object] = None

    parent_id: Optional[str] = None


FolderGetResponse: TypeAlias = List[FolderGetResponseItem]
