# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ConfigUpdateParams"]


class ConfigUpdateParams(TypedDict, total=False):
    autocomplete_generation_input_max_length: Required[
        Annotated[int, PropertyInfo(alias="AUTOCOMPLETE_GENERATION_INPUT_MAX_LENGTH")]
    ]

    enable_autocomplete_generation: Required[Annotated[bool, PropertyInfo(alias="ENABLE_AUTOCOMPLETE_GENERATION")]]

    enable_retrieval_query_generation: Required[
        Annotated[bool, PropertyInfo(alias="ENABLE_RETRIEVAL_QUERY_GENERATION")]
    ]

    enable_search_query_generation: Required[Annotated[bool, PropertyInfo(alias="ENABLE_SEARCH_QUERY_GENERATION")]]

    enable_tags_generation: Required[Annotated[bool, PropertyInfo(alias="ENABLE_TAGS_GENERATION")]]

    enable_title_generation: Required[Annotated[bool, PropertyInfo(alias="ENABLE_TITLE_GENERATION")]]

    image_prompt_generation_prompt_template: Required[
        Annotated[str, PropertyInfo(alias="IMAGE_PROMPT_GENERATION_PROMPT_TEMPLATE")]
    ]

    query_generation_prompt_template: Required[Annotated[str, PropertyInfo(alias="QUERY_GENERATION_PROMPT_TEMPLATE")]]

    tags_generation_prompt_template: Required[Annotated[str, PropertyInfo(alias="TAGS_GENERATION_PROMPT_TEMPLATE")]]

    task_model: Required[Annotated[Optional[str], PropertyInfo(alias="TASK_MODEL")]]

    task_model_external: Required[Annotated[Optional[str], PropertyInfo(alias="TASK_MODEL_EXTERNAL")]]

    title_generation_prompt_template: Required[Annotated[str, PropertyInfo(alias="TITLE_GENERATION_PROMPT_TEMPLATE")]]

    tools_function_calling_prompt_template: Required[
        Annotated[str, PropertyInfo(alias="TOOLS_FUNCTION_CALLING_PROMPT_TEMPLATE")]
    ]
