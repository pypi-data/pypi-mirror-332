# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ......_models import BaseModel

__all__ = ["PermissionGetResponse", "Chat", "Features", "Workspace"]


class Chat(BaseModel):
    controls: Optional[bool] = None

    delete: Optional[bool] = None

    edit: Optional[bool] = None

    file_upload: Optional[bool] = None

    temporary: Optional[bool] = None


class Features(BaseModel):
    code_interpreter: Optional[bool] = None

    image_generation: Optional[bool] = None

    web_search: Optional[bool] = None


class Workspace(BaseModel):
    knowledge: Optional[bool] = None

    models: Optional[bool] = None

    prompts: Optional[bool] = None

    tools: Optional[bool] = None


class PermissionGetResponse(BaseModel):
    chat: Chat

    features: Features

    workspace: Workspace
