# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.configs import (
    CodeExecutionGetResponse,
    CodeExecutionSetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCodeExecution:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        code_execution = client.api.v1.configs.code_execution.get()
        assert_matches_type(CodeExecutionGetResponse, code_execution, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.configs.code_execution.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        code_execution = response.parse()
        assert_matches_type(CodeExecutionGetResponse, code_execution, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.configs.code_execution.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            code_execution = response.parse()
            assert_matches_type(CodeExecutionGetResponse, code_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set(self, client: Pyopenwebui) -> None:
        code_execution = client.api.v1.configs.code_execution.set(
            code_execution_engine="CODE_EXECUTION_ENGINE",
            code_execution_jupyter_auth="CODE_EXECUTION_JUPYTER_AUTH",
            code_execution_jupyter_auth_password="CODE_EXECUTION_JUPYTER_AUTH_PASSWORD",
            code_execution_jupyter_auth_token="CODE_EXECUTION_JUPYTER_AUTH_TOKEN",
            code_execution_jupyter_timeout=0,
            code_execution_jupyter_url="CODE_EXECUTION_JUPYTER_URL",
            code_interpreter_engine="CODE_INTERPRETER_ENGINE",
            code_interpreter_jupyter_auth="CODE_INTERPRETER_JUPYTER_AUTH",
            code_interpreter_jupyter_auth_password="CODE_INTERPRETER_JUPYTER_AUTH_PASSWORD",
            code_interpreter_jupyter_auth_token="CODE_INTERPRETER_JUPYTER_AUTH_TOKEN",
            code_interpreter_jupyter_timeout=0,
            code_interpreter_jupyter_url="CODE_INTERPRETER_JUPYTER_URL",
            code_interpreter_prompt_template="CODE_INTERPRETER_PROMPT_TEMPLATE",
            enable_code_execution=True,
            enable_code_interpreter=True,
        )
        assert_matches_type(CodeExecutionSetResponse, code_execution, path=["response"])

    @parametrize
    def test_raw_response_set(self, client: Pyopenwebui) -> None:
        response = client.api.v1.configs.code_execution.with_raw_response.set(
            code_execution_engine="CODE_EXECUTION_ENGINE",
            code_execution_jupyter_auth="CODE_EXECUTION_JUPYTER_AUTH",
            code_execution_jupyter_auth_password="CODE_EXECUTION_JUPYTER_AUTH_PASSWORD",
            code_execution_jupyter_auth_token="CODE_EXECUTION_JUPYTER_AUTH_TOKEN",
            code_execution_jupyter_timeout=0,
            code_execution_jupyter_url="CODE_EXECUTION_JUPYTER_URL",
            code_interpreter_engine="CODE_INTERPRETER_ENGINE",
            code_interpreter_jupyter_auth="CODE_INTERPRETER_JUPYTER_AUTH",
            code_interpreter_jupyter_auth_password="CODE_INTERPRETER_JUPYTER_AUTH_PASSWORD",
            code_interpreter_jupyter_auth_token="CODE_INTERPRETER_JUPYTER_AUTH_TOKEN",
            code_interpreter_jupyter_timeout=0,
            code_interpreter_jupyter_url="CODE_INTERPRETER_JUPYTER_URL",
            code_interpreter_prompt_template="CODE_INTERPRETER_PROMPT_TEMPLATE",
            enable_code_execution=True,
            enable_code_interpreter=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        code_execution = response.parse()
        assert_matches_type(CodeExecutionSetResponse, code_execution, path=["response"])

    @parametrize
    def test_streaming_response_set(self, client: Pyopenwebui) -> None:
        with client.api.v1.configs.code_execution.with_streaming_response.set(
            code_execution_engine="CODE_EXECUTION_ENGINE",
            code_execution_jupyter_auth="CODE_EXECUTION_JUPYTER_AUTH",
            code_execution_jupyter_auth_password="CODE_EXECUTION_JUPYTER_AUTH_PASSWORD",
            code_execution_jupyter_auth_token="CODE_EXECUTION_JUPYTER_AUTH_TOKEN",
            code_execution_jupyter_timeout=0,
            code_execution_jupyter_url="CODE_EXECUTION_JUPYTER_URL",
            code_interpreter_engine="CODE_INTERPRETER_ENGINE",
            code_interpreter_jupyter_auth="CODE_INTERPRETER_JUPYTER_AUTH",
            code_interpreter_jupyter_auth_password="CODE_INTERPRETER_JUPYTER_AUTH_PASSWORD",
            code_interpreter_jupyter_auth_token="CODE_INTERPRETER_JUPYTER_AUTH_TOKEN",
            code_interpreter_jupyter_timeout=0,
            code_interpreter_jupyter_url="CODE_INTERPRETER_JUPYTER_URL",
            code_interpreter_prompt_template="CODE_INTERPRETER_PROMPT_TEMPLATE",
            enable_code_execution=True,
            enable_code_interpreter=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            code_execution = response.parse()
            assert_matches_type(CodeExecutionSetResponse, code_execution, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCodeExecution:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        code_execution = await async_client.api.v1.configs.code_execution.get()
        assert_matches_type(CodeExecutionGetResponse, code_execution, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.configs.code_execution.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        code_execution = await response.parse()
        assert_matches_type(CodeExecutionGetResponse, code_execution, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.configs.code_execution.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            code_execution = await response.parse()
            assert_matches_type(CodeExecutionGetResponse, code_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set(self, async_client: AsyncPyopenwebui) -> None:
        code_execution = await async_client.api.v1.configs.code_execution.set(
            code_execution_engine="CODE_EXECUTION_ENGINE",
            code_execution_jupyter_auth="CODE_EXECUTION_JUPYTER_AUTH",
            code_execution_jupyter_auth_password="CODE_EXECUTION_JUPYTER_AUTH_PASSWORD",
            code_execution_jupyter_auth_token="CODE_EXECUTION_JUPYTER_AUTH_TOKEN",
            code_execution_jupyter_timeout=0,
            code_execution_jupyter_url="CODE_EXECUTION_JUPYTER_URL",
            code_interpreter_engine="CODE_INTERPRETER_ENGINE",
            code_interpreter_jupyter_auth="CODE_INTERPRETER_JUPYTER_AUTH",
            code_interpreter_jupyter_auth_password="CODE_INTERPRETER_JUPYTER_AUTH_PASSWORD",
            code_interpreter_jupyter_auth_token="CODE_INTERPRETER_JUPYTER_AUTH_TOKEN",
            code_interpreter_jupyter_timeout=0,
            code_interpreter_jupyter_url="CODE_INTERPRETER_JUPYTER_URL",
            code_interpreter_prompt_template="CODE_INTERPRETER_PROMPT_TEMPLATE",
            enable_code_execution=True,
            enable_code_interpreter=True,
        )
        assert_matches_type(CodeExecutionSetResponse, code_execution, path=["response"])

    @parametrize
    async def test_raw_response_set(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.configs.code_execution.with_raw_response.set(
            code_execution_engine="CODE_EXECUTION_ENGINE",
            code_execution_jupyter_auth="CODE_EXECUTION_JUPYTER_AUTH",
            code_execution_jupyter_auth_password="CODE_EXECUTION_JUPYTER_AUTH_PASSWORD",
            code_execution_jupyter_auth_token="CODE_EXECUTION_JUPYTER_AUTH_TOKEN",
            code_execution_jupyter_timeout=0,
            code_execution_jupyter_url="CODE_EXECUTION_JUPYTER_URL",
            code_interpreter_engine="CODE_INTERPRETER_ENGINE",
            code_interpreter_jupyter_auth="CODE_INTERPRETER_JUPYTER_AUTH",
            code_interpreter_jupyter_auth_password="CODE_INTERPRETER_JUPYTER_AUTH_PASSWORD",
            code_interpreter_jupyter_auth_token="CODE_INTERPRETER_JUPYTER_AUTH_TOKEN",
            code_interpreter_jupyter_timeout=0,
            code_interpreter_jupyter_url="CODE_INTERPRETER_JUPYTER_URL",
            code_interpreter_prompt_template="CODE_INTERPRETER_PROMPT_TEMPLATE",
            enable_code_execution=True,
            enable_code_interpreter=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        code_execution = await response.parse()
        assert_matches_type(CodeExecutionSetResponse, code_execution, path=["response"])

    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.configs.code_execution.with_streaming_response.set(
            code_execution_engine="CODE_EXECUTION_ENGINE",
            code_execution_jupyter_auth="CODE_EXECUTION_JUPYTER_AUTH",
            code_execution_jupyter_auth_password="CODE_EXECUTION_JUPYTER_AUTH_PASSWORD",
            code_execution_jupyter_auth_token="CODE_EXECUTION_JUPYTER_AUTH_TOKEN",
            code_execution_jupyter_timeout=0,
            code_execution_jupyter_url="CODE_EXECUTION_JUPYTER_URL",
            code_interpreter_engine="CODE_INTERPRETER_ENGINE",
            code_interpreter_jupyter_auth="CODE_INTERPRETER_JUPYTER_AUTH",
            code_interpreter_jupyter_auth_password="CODE_INTERPRETER_JUPYTER_AUTH_PASSWORD",
            code_interpreter_jupyter_auth_token="CODE_INTERPRETER_JUPYTER_AUTH_TOKEN",
            code_interpreter_jupyter_timeout=0,
            code_interpreter_jupyter_url="CODE_INTERPRETER_JUPYTER_URL",
            code_interpreter_prompt_template="CODE_INTERPRETER_PROMPT_TEMPLATE",
            enable_code_execution=True,
            enable_code_interpreter=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            code_execution = await response.parse()
            assert_matches_type(CodeExecutionSetResponse, code_execution, path=["response"])

        assert cast(Any, response.is_closed) is True
