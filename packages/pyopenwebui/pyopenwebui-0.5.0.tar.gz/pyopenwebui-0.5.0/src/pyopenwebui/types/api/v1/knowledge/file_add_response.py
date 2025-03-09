# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from ....shared.file_model import FileModel

__all__ = ["FileAddResponse"]


class FileAddResponse(BaseModel):
    id: str

    created_at: int

    description: str

    files: List[FileModel]

    name: str

    updated_at: int

    user_id: str

    access_control: Optional[object] = None

    data: Optional[object] = None

    meta: Optional[object] = None
