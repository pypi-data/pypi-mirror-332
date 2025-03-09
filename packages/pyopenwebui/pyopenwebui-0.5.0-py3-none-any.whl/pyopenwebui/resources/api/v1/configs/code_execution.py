# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1.configs import code_execution_set_params
from .....types.api.v1.configs.code_execution_get_response import CodeExecutionGetResponse
from .....types.api.v1.configs.code_execution_set_response import CodeExecutionSetResponse

__all__ = ["CodeExecutionResource", "AsyncCodeExecutionResource"]


class CodeExecutionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CodeExecutionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return CodeExecutionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CodeExecutionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return CodeExecutionResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeExecutionGetResponse:
        """Get Code Execution Config"""
        return self._get(
            "/api/v1/configs/code_execution",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CodeExecutionGetResponse,
        )

    def set(
        self,
        *,
        code_execution_engine: str,
        code_execution_jupyter_auth: Optional[str],
        code_execution_jupyter_auth_password: Optional[str],
        code_execution_jupyter_auth_token: Optional[str],
        code_execution_jupyter_timeout: Optional[int],
        code_execution_jupyter_url: Optional[str],
        code_interpreter_engine: str,
        code_interpreter_jupyter_auth: Optional[str],
        code_interpreter_jupyter_auth_password: Optional[str],
        code_interpreter_jupyter_auth_token: Optional[str],
        code_interpreter_jupyter_timeout: Optional[int],
        code_interpreter_jupyter_url: Optional[str],
        code_interpreter_prompt_template: Optional[str],
        enable_code_execution: bool,
        enable_code_interpreter: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeExecutionSetResponse:
        """
        Set Code Execution Config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/configs/code_execution",
            body=maybe_transform(
                {
                    "code_execution_engine": code_execution_engine,
                    "code_execution_jupyter_auth": code_execution_jupyter_auth,
                    "code_execution_jupyter_auth_password": code_execution_jupyter_auth_password,
                    "code_execution_jupyter_auth_token": code_execution_jupyter_auth_token,
                    "code_execution_jupyter_timeout": code_execution_jupyter_timeout,
                    "code_execution_jupyter_url": code_execution_jupyter_url,
                    "code_interpreter_engine": code_interpreter_engine,
                    "code_interpreter_jupyter_auth": code_interpreter_jupyter_auth,
                    "code_interpreter_jupyter_auth_password": code_interpreter_jupyter_auth_password,
                    "code_interpreter_jupyter_auth_token": code_interpreter_jupyter_auth_token,
                    "code_interpreter_jupyter_timeout": code_interpreter_jupyter_timeout,
                    "code_interpreter_jupyter_url": code_interpreter_jupyter_url,
                    "code_interpreter_prompt_template": code_interpreter_prompt_template,
                    "enable_code_execution": enable_code_execution,
                    "enable_code_interpreter": enable_code_interpreter,
                },
                code_execution_set_params.CodeExecutionSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CodeExecutionSetResponse,
        )


class AsyncCodeExecutionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCodeExecutionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCodeExecutionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCodeExecutionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncCodeExecutionResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeExecutionGetResponse:
        """Get Code Execution Config"""
        return await self._get(
            "/api/v1/configs/code_execution",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CodeExecutionGetResponse,
        )

    async def set(
        self,
        *,
        code_execution_engine: str,
        code_execution_jupyter_auth: Optional[str],
        code_execution_jupyter_auth_password: Optional[str],
        code_execution_jupyter_auth_token: Optional[str],
        code_execution_jupyter_timeout: Optional[int],
        code_execution_jupyter_url: Optional[str],
        code_interpreter_engine: str,
        code_interpreter_jupyter_auth: Optional[str],
        code_interpreter_jupyter_auth_password: Optional[str],
        code_interpreter_jupyter_auth_token: Optional[str],
        code_interpreter_jupyter_timeout: Optional[int],
        code_interpreter_jupyter_url: Optional[str],
        code_interpreter_prompt_template: Optional[str],
        enable_code_execution: bool,
        enable_code_interpreter: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeExecutionSetResponse:
        """
        Set Code Execution Config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/configs/code_execution",
            body=await async_maybe_transform(
                {
                    "code_execution_engine": code_execution_engine,
                    "code_execution_jupyter_auth": code_execution_jupyter_auth,
                    "code_execution_jupyter_auth_password": code_execution_jupyter_auth_password,
                    "code_execution_jupyter_auth_token": code_execution_jupyter_auth_token,
                    "code_execution_jupyter_timeout": code_execution_jupyter_timeout,
                    "code_execution_jupyter_url": code_execution_jupyter_url,
                    "code_interpreter_engine": code_interpreter_engine,
                    "code_interpreter_jupyter_auth": code_interpreter_jupyter_auth,
                    "code_interpreter_jupyter_auth_password": code_interpreter_jupyter_auth_password,
                    "code_interpreter_jupyter_auth_token": code_interpreter_jupyter_auth_token,
                    "code_interpreter_jupyter_timeout": code_interpreter_jupyter_timeout,
                    "code_interpreter_jupyter_url": code_interpreter_jupyter_url,
                    "code_interpreter_prompt_template": code_interpreter_prompt_template,
                    "enable_code_execution": enable_code_execution,
                    "enable_code_interpreter": enable_code_interpreter,
                },
                code_execution_set_params.CodeExecutionSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CodeExecutionSetResponse,
        )


class CodeExecutionResourceWithRawResponse:
    def __init__(self, code_execution: CodeExecutionResource) -> None:
        self._code_execution = code_execution

        self.get = to_raw_response_wrapper(
            code_execution.get,
        )
        self.set = to_raw_response_wrapper(
            code_execution.set,
        )


class AsyncCodeExecutionResourceWithRawResponse:
    def __init__(self, code_execution: AsyncCodeExecutionResource) -> None:
        self._code_execution = code_execution

        self.get = async_to_raw_response_wrapper(
            code_execution.get,
        )
        self.set = async_to_raw_response_wrapper(
            code_execution.set,
        )


class CodeExecutionResourceWithStreamingResponse:
    def __init__(self, code_execution: CodeExecutionResource) -> None:
        self._code_execution = code_execution

        self.get = to_streamed_response_wrapper(
            code_execution.get,
        )
        self.set = to_streamed_response_wrapper(
            code_execution.set,
        )


class AsyncCodeExecutionResourceWithStreamingResponse:
    def __init__(self, code_execution: AsyncCodeExecutionResource) -> None:
        self._code_execution = code_execution

        self.get = async_to_streamed_response_wrapper(
            code_execution.get,
        )
        self.set = async_to_streamed_response_wrapper(
            code_execution.set,
        )
