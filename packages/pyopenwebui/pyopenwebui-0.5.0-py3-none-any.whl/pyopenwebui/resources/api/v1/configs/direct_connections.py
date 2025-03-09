# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from .....types.api.v1.configs import direct_connection_set_params
from .....types.api.v1.configs.direct_connection_get_response import DirectConnectionGetResponse
from .....types.api.v1.configs.direct_connection_set_response import DirectConnectionSetResponse

__all__ = ["DirectConnectionsResource", "AsyncDirectConnectionsResource"]


class DirectConnectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DirectConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return DirectConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirectConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return DirectConnectionsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DirectConnectionGetResponse:
        """Get Direct Connections Config"""
        return self._get(
            "/api/v1/configs/direct_connections",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectConnectionGetResponse,
        )

    def set(
        self,
        *,
        enable_direct_connections: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DirectConnectionSetResponse:
        """
        Set Direct Connections Config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/configs/direct_connections",
            body=maybe_transform(
                {"enable_direct_connections": enable_direct_connections},
                direct_connection_set_params.DirectConnectionSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectConnectionSetResponse,
        )


class AsyncDirectConnectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDirectConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDirectConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirectConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncDirectConnectionsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DirectConnectionGetResponse:
        """Get Direct Connections Config"""
        return await self._get(
            "/api/v1/configs/direct_connections",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectConnectionGetResponse,
        )

    async def set(
        self,
        *,
        enable_direct_connections: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DirectConnectionSetResponse:
        """
        Set Direct Connections Config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/configs/direct_connections",
            body=await async_maybe_transform(
                {"enable_direct_connections": enable_direct_connections},
                direct_connection_set_params.DirectConnectionSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectConnectionSetResponse,
        )


class DirectConnectionsResourceWithRawResponse:
    def __init__(self, direct_connections: DirectConnectionsResource) -> None:
        self._direct_connections = direct_connections

        self.get = to_raw_response_wrapper(
            direct_connections.get,
        )
        self.set = to_raw_response_wrapper(
            direct_connections.set,
        )


class AsyncDirectConnectionsResourceWithRawResponse:
    def __init__(self, direct_connections: AsyncDirectConnectionsResource) -> None:
        self._direct_connections = direct_connections

        self.get = async_to_raw_response_wrapper(
            direct_connections.get,
        )
        self.set = async_to_raw_response_wrapper(
            direct_connections.set,
        )


class DirectConnectionsResourceWithStreamingResponse:
    def __init__(self, direct_connections: DirectConnectionsResource) -> None:
        self._direct_connections = direct_connections

        self.get = to_streamed_response_wrapper(
            direct_connections.get,
        )
        self.set = to_streamed_response_wrapper(
            direct_connections.set,
        )


class AsyncDirectConnectionsResourceWithStreamingResponse:
    def __init__(self, direct_connections: AsyncDirectConnectionsResource) -> None:
        self._direct_connections = direct_connections

        self.get = async_to_streamed_response_wrapper(
            direct_connections.get,
        )
        self.set = async_to_streamed_response_wrapper(
            direct_connections.set,
        )
