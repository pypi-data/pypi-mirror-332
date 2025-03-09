# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["FileListResponse", "FileListResponseItem", "FileListResponseItemMeta"]


class FileListResponseItemMeta(BaseModel):
    content_type: Optional[str] = None

    name: Optional[str] = None

    size: Optional[int] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class FileListResponseItem(BaseModel):
    id: str

    created_at: int

    filename: str

    meta: FileListResponseItemMeta

    updated_at: int

    user_id: str

    data: Optional[object] = None

    hash: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


FileListResponse: TypeAlias = List[FileListResponseItem]
