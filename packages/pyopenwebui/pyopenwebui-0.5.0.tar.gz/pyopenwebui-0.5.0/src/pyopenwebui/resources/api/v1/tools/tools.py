# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .id.id import (
    IDResource,
    AsyncIDResource,
    IDResourceWithRawResponse,
    AsyncIDResourceWithRawResponse,
    IDResourceWithStreamingResponse,
    AsyncIDResourceWithStreamingResponse,
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
from .....types.api.v1 import tool_create_params
from .....types.tool_response import ToolResponse
from .....types.api.v1.tool_get_response import ToolGetResponse
from .....types.api.v1.tool_export_response import ToolExportResponse
from .....types.api.v1.tool_get_list_response import ToolGetListResponse

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def id(self) -> IDResource:
        return IDResource(self._client)

    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        content: str,
        meta: tool_create_params.Meta,
        name: str,
        access_control: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ToolResponse]:
        """
        Create New Tools

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/tools/create",
            body=maybe_transform(
                {
                    "id": id,
                    "content": content,
                    "meta": meta,
                    "name": name,
                    "access_control": access_control,
                },
                tool_create_params.ToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolResponse,
        )

    def export(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolExportResponse:
        """Export Tools"""
        return self._get(
            "/api/v1/tools/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolExportResponse,
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
    ) -> ToolGetResponse:
        """Get Tools"""
        return self._get(
            "/api/v1/tools/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolGetResponse,
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
    ) -> ToolGetListResponse:
        """Get Tool List"""
        return self._get(
            "/api/v1/tools/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolGetListResponse,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def id(self) -> AsyncIDResource:
        return AsyncIDResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        content: str,
        meta: tool_create_params.Meta,
        name: str,
        access_control: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ToolResponse]:
        """
        Create New Tools

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/tools/create",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "content": content,
                    "meta": meta,
                    "name": name,
                    "access_control": access_control,
                },
                tool_create_params.ToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolResponse,
        )

    async def export(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolExportResponse:
        """Export Tools"""
        return await self._get(
            "/api/v1/tools/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolExportResponse,
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
    ) -> ToolGetResponse:
        """Get Tools"""
        return await self._get(
            "/api/v1/tools/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolGetResponse,
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
    ) -> ToolGetListResponse:
        """Get Tool List"""
        return await self._get(
            "/api/v1/tools/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolGetListResponse,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.create = to_raw_response_wrapper(
            tools.create,
        )
        self.export = to_raw_response_wrapper(
            tools.export,
        )
        self.get = to_raw_response_wrapper(
            tools.get,
        )
        self.get_list = to_raw_response_wrapper(
            tools.get_list,
        )

    @cached_property
    def id(self) -> IDResourceWithRawResponse:
        return IDResourceWithRawResponse(self._tools.id)


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.create = async_to_raw_response_wrapper(
            tools.create,
        )
        self.export = async_to_raw_response_wrapper(
            tools.export,
        )
        self.get = async_to_raw_response_wrapper(
            tools.get,
        )
        self.get_list = async_to_raw_response_wrapper(
            tools.get_list,
        )

    @cached_property
    def id(self) -> AsyncIDResourceWithRawResponse:
        return AsyncIDResourceWithRawResponse(self._tools.id)


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.create = to_streamed_response_wrapper(
            tools.create,
        )
        self.export = to_streamed_response_wrapper(
            tools.export,
        )
        self.get = to_streamed_response_wrapper(
            tools.get,
        )
        self.get_list = to_streamed_response_wrapper(
            tools.get_list,
        )

    @cached_property
    def id(self) -> IDResourceWithStreamingResponse:
        return IDResourceWithStreamingResponse(self._tools.id)


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.create = async_to_streamed_response_wrapper(
            tools.create,
        )
        self.export = async_to_streamed_response_wrapper(
            tools.export,
        )
        self.get = async_to_streamed_response_wrapper(
            tools.get,
        )
        self.get_list = async_to_streamed_response_wrapper(
            tools.get_list,
        )

    @cached_property
    def id(self) -> AsyncIDResourceWithStreamingResponse:
        return AsyncIDResourceWithStreamingResponse(self._tools.id)
