# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["KnowledgeResetByIDResponse", "File", "FileFileMetadataResponse"]


class FileFileMetadataResponse(BaseModel):
    id: str

    created_at: int

    meta: object

    updated_at: int


File: TypeAlias = Union[FileFileMetadataResponse, object]


class KnowledgeResetByIDResponse(BaseModel):
    id: str

    created_at: int

    description: str

    name: str

    updated_at: int

    user_id: str

    access_control: Optional[object] = None

    data: Optional[object] = None

    files: Optional[List[File]] = None

    meta: Optional[object] = None
