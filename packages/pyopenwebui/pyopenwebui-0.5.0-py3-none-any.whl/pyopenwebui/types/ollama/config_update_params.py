# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConfigUpdateParams"]


class ConfigUpdateParams(TypedDict, total=False):
    ollama_api_configs: Required[Annotated[object, PropertyInfo(alias="OLLAMA_API_CONFIGS")]]

    ollama_base_urls: Required[Annotated[List[str], PropertyInfo(alias="OLLAMA_BASE_URLS")]]

    enable_ollama_api: Annotated[Optional[bool], PropertyInfo(alias="ENABLE_OLLAMA_API")]
