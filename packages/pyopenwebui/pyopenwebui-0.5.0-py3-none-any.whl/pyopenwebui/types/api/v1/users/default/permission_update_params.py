# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PermissionUpdateParams", "Chat", "Features", "Workspace"]


class PermissionUpdateParams(TypedDict, total=False):
    chat: Required[Chat]

    features: Required[Features]

    workspace: Required[Workspace]


class Chat(TypedDict, total=False):
    controls: bool

    delete: bool

    edit: bool

    file_upload: bool

    temporary: bool


class Features(TypedDict, total=False):
    code_interpreter: bool

    image_generation: bool

    web_search: bool


class Workspace(TypedDict, total=False):
    knowledge: bool

    models: bool

    prompts: bool

    tools: bool
