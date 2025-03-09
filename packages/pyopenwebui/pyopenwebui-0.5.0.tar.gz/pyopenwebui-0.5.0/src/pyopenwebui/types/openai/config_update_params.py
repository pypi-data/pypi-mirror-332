# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConfigUpdateParams"]


class ConfigUpdateParams(TypedDict, total=False):
    openai_api_base_urls: Required[Annotated[List[str], PropertyInfo(alias="OPENAI_API_BASE_URLS")]]

    openai_api_configs: Required[Annotated[object, PropertyInfo(alias="OPENAI_API_CONFIGS")]]

    openai_api_keys: Required[Annotated[List[str], PropertyInfo(alias="OPENAI_API_KEYS")]]

    enable_openai_api: Annotated[Optional[bool], PropertyInfo(alias="ENABLE_OPENAI_API")]
