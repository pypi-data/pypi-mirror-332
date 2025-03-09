# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["CodeExecutionGetResponse"]


class CodeExecutionGetResponse(BaseModel):
    code_execution_engine: str = FieldInfo(alias="CODE_EXECUTION_ENGINE")

    code_execution_jupyter_auth: Optional[str] = FieldInfo(alias="CODE_EXECUTION_JUPYTER_AUTH", default=None)

    code_execution_jupyter_auth_password: Optional[str] = FieldInfo(
        alias="CODE_EXECUTION_JUPYTER_AUTH_PASSWORD", default=None
    )

    code_execution_jupyter_auth_token: Optional[str] = FieldInfo(
        alias="CODE_EXECUTION_JUPYTER_AUTH_TOKEN", default=None
    )

    code_execution_jupyter_timeout: Optional[int] = FieldInfo(alias="CODE_EXECUTION_JUPYTER_TIMEOUT", default=None)

    code_execution_jupyter_url: Optional[str] = FieldInfo(alias="CODE_EXECUTION_JUPYTER_URL", default=None)

    code_interpreter_engine: str = FieldInfo(alias="CODE_INTERPRETER_ENGINE")

    code_interpreter_jupyter_auth: Optional[str] = FieldInfo(alias="CODE_INTERPRETER_JUPYTER_AUTH", default=None)

    code_interpreter_jupyter_auth_password: Optional[str] = FieldInfo(
        alias="CODE_INTERPRETER_JUPYTER_AUTH_PASSWORD", default=None
    )

    code_interpreter_jupyter_auth_token: Optional[str] = FieldInfo(
        alias="CODE_INTERPRETER_JUPYTER_AUTH_TOKEN", default=None
    )

    code_interpreter_jupyter_timeout: Optional[int] = FieldInfo(alias="CODE_INTERPRETER_JUPYTER_TIMEOUT", default=None)

    code_interpreter_jupyter_url: Optional[str] = FieldInfo(alias="CODE_INTERPRETER_JUPYTER_URL", default=None)

    code_interpreter_prompt_template: Optional[str] = FieldInfo(alias="CODE_INTERPRETER_PROMPT_TEMPLATE", default=None)

    enable_code_execution: bool = FieldInfo(alias="ENABLE_CODE_EXECUTION")

    enable_code_interpreter: bool = FieldInfo(alias="ENABLE_CODE_INTERPRETER")
