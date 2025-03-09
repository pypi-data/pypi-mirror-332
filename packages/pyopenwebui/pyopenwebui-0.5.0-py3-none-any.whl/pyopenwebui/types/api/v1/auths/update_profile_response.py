# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["UpdateProfileResponse"]


class UpdateProfileResponse(BaseModel):
    id: str

    email: str

    name: str

    profile_image_url: str

    role: str
