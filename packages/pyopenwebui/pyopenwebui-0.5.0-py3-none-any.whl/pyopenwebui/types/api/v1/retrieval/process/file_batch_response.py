# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ......_models import BaseModel

__all__ = ["FileBatchResponse", "Error", "Result"]


class Error(BaseModel):
    file_id: str

    status: str

    error: Optional[str] = None


class Result(BaseModel):
    file_id: str

    status: str

    error: Optional[str] = None


class FileBatchResponse(BaseModel):
    errors: List[Error]

    results: List[Result]
