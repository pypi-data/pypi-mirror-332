# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional

from ...._models import BaseModel

__all__ = ["FileUploadResponse", "Meta"]


class Meta(BaseModel):
    content_type: Optional[str] = None

    name: Optional[str] = None

    size: Optional[int] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class FileUploadResponse(BaseModel):
    id: str

    created_at: int

    filename: str

    meta: Meta

    updated_at: int

    user_id: str

    data: Optional[object] = None

    hash: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
