# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CodeExecutionSetParams"]


class CodeExecutionSetParams(TypedDict, total=False):
    code_execution_engine: Required[Annotated[str, PropertyInfo(alias="CODE_EXECUTION_ENGINE")]]

    code_execution_jupyter_auth: Required[Annotated[Optional[str], PropertyInfo(alias="CODE_EXECUTION_JUPYTER_AUTH")]]

    code_execution_jupyter_auth_password: Required[
        Annotated[Optional[str], PropertyInfo(alias="CODE_EXECUTION_JUPYTER_AUTH_PASSWORD")]
    ]

    code_execution_jupyter_auth_token: Required[
        Annotated[Optional[str], PropertyInfo(alias="CODE_EXECUTION_JUPYTER_AUTH_TOKEN")]
    ]

    code_execution_jupyter_timeout: Required[
        Annotated[Optional[int], PropertyInfo(alias="CODE_EXECUTION_JUPYTER_TIMEOUT")]
    ]

    code_execution_jupyter_url: Required[Annotated[Optional[str], PropertyInfo(alias="CODE_EXECUTION_JUPYTER_URL")]]

    code_interpreter_engine: Required[Annotated[str, PropertyInfo(alias="CODE_INTERPRETER_ENGINE")]]

    code_interpreter_jupyter_auth: Required[
        Annotated[Optional[str], PropertyInfo(alias="CODE_INTERPRETER_JUPYTER_AUTH")]
    ]

    code_interpreter_jupyter_auth_password: Required[
        Annotated[Optional[str], PropertyInfo(alias="CODE_INTERPRETER_JUPYTER_AUTH_PASSWORD")]
    ]

    code_interpreter_jupyter_auth_token: Required[
        Annotated[Optional[str], PropertyInfo(alias="CODE_INTERPRETER_JUPYTER_AUTH_TOKEN")]
    ]

    code_interpreter_jupyter_timeout: Required[
        Annotated[Optional[int], PropertyInfo(alias="CODE_INTERPRETER_JUPYTER_TIMEOUT")]
    ]

    code_interpreter_jupyter_url: Required[Annotated[Optional[str], PropertyInfo(alias="CODE_INTERPRETER_JUPYTER_URL")]]

    code_interpreter_prompt_template: Required[
        Annotated[Optional[str], PropertyInfo(alias="CODE_INTERPRETER_PROMPT_TEMPLATE")]
    ]

    enable_code_execution: Required[Annotated[bool, PropertyInfo(alias="ENABLE_CODE_EXECUTION")]]

    enable_code_interpreter: Required[Annotated[bool, PropertyInfo(alias="ENABLE_CODE_INTERPRETER")]]
