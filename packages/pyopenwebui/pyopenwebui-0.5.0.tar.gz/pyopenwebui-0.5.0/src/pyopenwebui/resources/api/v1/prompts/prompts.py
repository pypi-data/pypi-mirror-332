# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .command import (
    CommandResource,
    AsyncCommandResource,
    CommandResourceWithRawResponse,
    AsyncCommandResourceWithRawResponse,
    CommandResourceWithStreamingResponse,
    AsyncCommandResourceWithStreamingResponse,
)
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
from .....types.api.v1 import prompt_create_params
from .....types.shared.prompt_model import PromptModel
from .....types.api.v1.prompt_get_response import PromptGetResponse
from .....types.api.v1.prompt_get_list_response import PromptGetListResponse

__all__ = ["PromptsResource", "AsyncPromptsResource"]


class PromptsResource(SyncAPIResource):
    @cached_property
    def command(self) -> CommandResource:
        return CommandResource(self._client)

    @cached_property
    def with_raw_response(self) -> PromptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return PromptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return PromptsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        command: str,
        content: str,
        title: str,
        access_control: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PromptModel]:
        """
        Create New Prompt

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/prompts/create",
            body=maybe_transform(
                {
                    "command": command,
                    "content": content,
                    "title": title,
                    "access_control": access_control,
                },
                prompt_create_params.PromptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptModel,
        )

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptGetResponse:
        """Get Prompts"""
        return self._get(
            "/api/v1/prompts/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptGetResponse,
        )

    def get_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptGetListResponse:
        """Get Prompt List"""
        return self._get(
            "/api/v1/prompts/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptGetListResponse,
        )


class AsyncPromptsResource(AsyncAPIResource):
    @cached_property
    def command(self) -> AsyncCommandResource:
        return AsyncCommandResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPromptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncPromptsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        command: str,
        content: str,
        title: str,
        access_control: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PromptModel]:
        """
        Create New Prompt

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/prompts/create",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "content": content,
                    "title": title,
                    "access_control": access_control,
                },
                prompt_create_params.PromptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptModel,
        )

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptGetResponse:
        """Get Prompts"""
        return await self._get(
            "/api/v1/prompts/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptGetResponse,
        )

    async def get_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptGetListResponse:
        """Get Prompt List"""
        return await self._get(
            "/api/v1/prompts/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptGetListResponse,
        )


class PromptsResourceWithRawResponse:
    def __init__(self, prompts: PromptsResource) -> None:
        self._prompts = prompts

        self.create = to_raw_response_wrapper(
            prompts.create,
        )
        self.get = to_raw_response_wrapper(
            prompts.get,
        )
        self.get_list = to_raw_response_wrapper(
            prompts.get_list,
        )

    @cached_property
    def command(self) -> CommandResourceWithRawResponse:
        return CommandResourceWithRawResponse(self._prompts.command)


class AsyncPromptsResourceWithRawResponse:
    def __init__(self, prompts: AsyncPromptsResource) -> None:
        self._prompts = prompts

        self.create = async_to_raw_response_wrapper(
            prompts.create,
        )
        self.get = async_to_raw_response_wrapper(
            prompts.get,
        )
        self.get_list = async_to_raw_response_wrapper(
            prompts.get_list,
        )

    @cached_property
    def command(self) -> AsyncCommandResourceWithRawResponse:
        return AsyncCommandResourceWithRawResponse(self._prompts.command)


class PromptsResourceWithStreamingResponse:
    def __init__(self, prompts: PromptsResource) -> None:
        self._prompts = prompts

        self.create = to_streamed_response_wrapper(
            prompts.create,
        )
        self.get = to_streamed_response_wrapper(
            prompts.get,
        )
        self.get_list = to_streamed_response_wrapper(
            prompts.get_list,
        )

    @cached_property
    def command(self) -> CommandResourceWithStreamingResponse:
        return CommandResourceWithStreamingResponse(self._prompts.command)


class AsyncPromptsResourceWithStreamingResponse:
    def __init__(self, prompts: AsyncPromptsResource) -> None:
        self._prompts = prompts

        self.create = async_to_streamed_response_wrapper(
            prompts.create,
        )
        self.get = async_to_streamed_response_wrapper(
            prompts.get,
        )
        self.get_list = async_to_streamed_response_wrapper(
            prompts.get_list,
        )

    @cached_property
    def command(self) -> AsyncCommandResourceWithStreamingResponse:
        return AsyncCommandResourceWithStreamingResponse(self._prompts.command)
