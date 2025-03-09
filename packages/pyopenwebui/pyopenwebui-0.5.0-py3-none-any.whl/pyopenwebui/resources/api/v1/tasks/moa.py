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
from .....types.api.v1.tasks import moa_generate_params

__all__ = ["MoaResource", "AsyncMoaResource"]


class MoaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MoaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return MoaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MoaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return MoaResourceWithStreamingResponse(self)

    def generate(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Generate Moa Response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/tasks/moa/completions",
            body=maybe_transform(body, moa_generate_params.MoaGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncMoaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMoaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMoaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMoaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncMoaResourceWithStreamingResponse(self)

    async def generate(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Generate Moa Response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/tasks/moa/completions",
            body=await async_maybe_transform(body, moa_generate_params.MoaGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class MoaResourceWithRawResponse:
    def __init__(self, moa: MoaResource) -> None:
        self._moa = moa

        self.generate = to_raw_response_wrapper(
            moa.generate,
        )


class AsyncMoaResourceWithRawResponse:
    def __init__(self, moa: AsyncMoaResource) -> None:
        self._moa = moa

        self.generate = async_to_raw_response_wrapper(
            moa.generate,
        )


class MoaResourceWithStreamingResponse:
    def __init__(self, moa: MoaResource) -> None:
        self._moa = moa

        self.generate = to_streamed_response_wrapper(
            moa.generate,
        )


class AsyncMoaResourceWithStreamingResponse:
    def __init__(self, moa: AsyncMoaResource) -> None:
        self._moa = moa

        self.generate = async_to_streamed_response_wrapper(
            moa.generate,
        )
