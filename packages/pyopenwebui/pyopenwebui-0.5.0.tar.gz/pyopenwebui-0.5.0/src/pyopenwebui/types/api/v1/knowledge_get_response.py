# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = [
    "KnowledgeGetResponse",
    "KnowledgeGetResponseItem",
    "KnowledgeGetResponseItemFile",
    "KnowledgeGetResponseItemFileFileMetadataResponse",
    "KnowledgeGetResponseItemUser",
]


class KnowledgeGetResponseItemFileFileMetadataResponse(BaseModel):
    id: str

    created_at: int

    meta: object

    updated_at: int


KnowledgeGetResponseItemFile: TypeAlias = Union[KnowledgeGetResponseItemFileFileMetadataResponse, object]


class KnowledgeGetResponseItemUser(BaseModel):
    id: str

    email: str

    name: str

    profile_image_url: str

    role: str


class KnowledgeGetResponseItem(BaseModel):
    id: str

    created_at: int

    description: str

    name: str

    updated_at: int

    user_id: str

    access_control: Optional[object] = None

    data: Optional[object] = None

    files: Optional[List[KnowledgeGetResponseItemFile]] = None

    meta: Optional[object] = None

    user: Optional[KnowledgeGetResponseItemUser] = None


KnowledgeGetResponse: TypeAlias = List[KnowledgeGetResponseItem]
