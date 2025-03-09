# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["ModelGetResponse", "ModelGetResponseItem", "ModelGetResponseItemMeta", "ModelGetResponseItemUser"]


class ModelGetResponseItemMeta(BaseModel):
    capabilities: Optional[object] = None

    description: Optional[str] = None

    profile_image_url: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ModelGetResponseItemUser(BaseModel):
    id: str

    email: str

    name: str

    profile_image_url: str

    role: str


class ModelGetResponseItem(BaseModel):
    id: str

    created_at: int

    is_active: bool

    meta: ModelGetResponseItemMeta

    name: str

    params: Dict[str, object]

    updated_at: int

    user_id: str

    access_control: Optional[object] = None

    base_model_id: Optional[str] = None

    user: Optional[ModelGetResponseItemUser] = None


ModelGetResponse: TypeAlias = List[ModelGetResponseItem]
