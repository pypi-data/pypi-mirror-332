# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = [
    "KnowledgeGetListResponse",
    "KnowledgeGetListResponseItem",
    "KnowledgeGetListResponseItemFile",
    "KnowledgeGetListResponseItemFileFileMetadataResponse",
    "KnowledgeGetListResponseItemUser",
]


class KnowledgeGetListResponseItemFileFileMetadataResponse(BaseModel):
    id: str

    created_at: int

    meta: object

    updated_at: int


KnowledgeGetListResponseItemFile: TypeAlias = Union[KnowledgeGetListResponseItemFileFileMetadataResponse, object]


class KnowledgeGetListResponseItemUser(BaseModel):
    id: str

    email: str

    name: str

    profile_image_url: str

    role: str


class KnowledgeGetListResponseItem(BaseModel):
    id: str

    created_at: int

    description: str

    name: str

    updated_at: int

    user_id: str

    access_control: Optional[object] = None

    data: Optional[object] = None

    files: Optional[List[KnowledgeGetListResponseItemFile]] = None

    meta: Optional[object] = None

    user: Optional[KnowledgeGetListResponseItemUser] = None


KnowledgeGetListResponse: TypeAlias = List[KnowledgeGetListResponseItem]
