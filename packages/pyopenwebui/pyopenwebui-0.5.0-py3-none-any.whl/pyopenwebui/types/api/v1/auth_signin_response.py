# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["AuthSigninResponse"]


class AuthSigninResponse(BaseModel):
    id: str

    token: str

    email: str

    name: str

    profile_image_url: str

    role: str

    token_type: str

    expires_at: Optional[int] = None

    permissions: Optional[object] = None
