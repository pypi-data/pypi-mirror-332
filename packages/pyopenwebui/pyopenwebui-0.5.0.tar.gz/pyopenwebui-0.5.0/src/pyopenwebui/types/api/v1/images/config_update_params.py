# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ConfigUpdateParams", "Automatic1111", "Comfyui", "Gemini", "OpenAI"]


class ConfigUpdateParams(TypedDict, total=False):
    automatic1111: Required[Automatic1111]

    comfyui: Required[Comfyui]

    enabled: Required[bool]

    engine: Required[str]

    gemini: Required[Gemini]

    openai: Required[OpenAI]

    prompt_generation: Required[bool]


class Automatic1111(TypedDict, total=False):
    automatic1111_api_auth: Required[Annotated[str, PropertyInfo(alias="AUTOMATIC1111_API_AUTH")]]

    automatic1111_base_url: Required[Annotated[str, PropertyInfo(alias="AUTOMATIC1111_BASE_URL")]]

    automatic1111_cfg_scale: Required[Annotated[Union[str, float, None], PropertyInfo(alias="AUTOMATIC1111_CFG_SCALE")]]

    automatic1111_sampler: Required[Annotated[Optional[str], PropertyInfo(alias="AUTOMATIC1111_SAMPLER")]]

    automatic1111_scheduler: Required[Annotated[Optional[str], PropertyInfo(alias="AUTOMATIC1111_SCHEDULER")]]


class Comfyui(TypedDict, total=False):
    comfyui_api_key: Required[Annotated[str, PropertyInfo(alias="COMFYUI_API_KEY")]]

    comfyui_base_url: Required[Annotated[str, PropertyInfo(alias="COMFYUI_BASE_URL")]]

    comfyui_workflow: Required[Annotated[str, PropertyInfo(alias="COMFYUI_WORKFLOW")]]

    comfyui_workflow_nodes: Required[Annotated[Iterable[object], PropertyInfo(alias="COMFYUI_WORKFLOW_NODES")]]


class Gemini(TypedDict, total=False):
    gemini_api_base_url: Required[Annotated[str, PropertyInfo(alias="GEMINI_API_BASE_URL")]]

    gemini_api_key: Required[Annotated[str, PropertyInfo(alias="GEMINI_API_KEY")]]


class OpenAI(TypedDict, total=False):
    openai_api_base_url: Required[Annotated[str, PropertyInfo(alias="OPENAI_API_BASE_URL")]]

    openai_api_key: Required[Annotated[str, PropertyInfo(alias="OPENAI_API_KEY")]]
