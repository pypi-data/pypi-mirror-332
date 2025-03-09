# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ollama.api import copy_copy_params, copy_copy_by_index_params

__all__ = ["CopyResource", "AsyncCopyResource"]


class CopyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CopyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return CopyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CopyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return CopyResourceWithStreamingResponse(self)

    def copy(
        self,
        *,
        destination: str,
        source: str,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Copy Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ollama/api/copy",
            body=maybe_transform(
                {
                    "destination": destination,
                    "source": source,
                },
                copy_copy_params.CopyCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url_idx": url_idx}, copy_copy_params.CopyCopyParams),
            ),
            cast_to=object,
        )

    def copy_by_index(
        self,
        url_idx: int,
        *,
        destination: str,
        source: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Copy Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/ollama/api/copy/{url_idx}",
            body=maybe_transform(
                {
                    "destination": destination,
                    "source": source,
                },
                copy_copy_by_index_params.CopyCopyByIndexParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncCopyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCopyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCopyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCopyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncCopyResourceWithStreamingResponse(self)

    async def copy(
        self,
        *,
        destination: str,
        source: str,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Copy Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ollama/api/copy",
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "source": source,
                },
                copy_copy_params.CopyCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url_idx": url_idx}, copy_copy_params.CopyCopyParams),
            ),
            cast_to=object,
        )

    async def copy_by_index(
        self,
        url_idx: int,
        *,
        destination: str,
        source: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Copy Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/ollama/api/copy/{url_idx}",
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "source": source,
                },
                copy_copy_by_index_params.CopyCopyByIndexParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class CopyResourceWithRawResponse:
    def __init__(self, copy: CopyResource) -> None:
        self._copy = copy

        self.copy = to_raw_response_wrapper(
            copy.copy,
        )
        self.copy_by_index = to_raw_response_wrapper(
            copy.copy_by_index,
        )


class AsyncCopyResourceWithRawResponse:
    def __init__(self, copy: AsyncCopyResource) -> None:
        self._copy = copy

        self.copy = async_to_raw_response_wrapper(
            copy.copy,
        )
        self.copy_by_index = async_to_raw_response_wrapper(
            copy.copy_by_index,
        )


class CopyResourceWithStreamingResponse:
    def __init__(self, copy: CopyResource) -> None:
        self._copy = copy

        self.copy = to_streamed_response_wrapper(
            copy.copy,
        )
        self.copy_by_index = to_streamed_response_wrapper(
            copy.copy_by_index,
        )


class AsyncCopyResourceWithStreamingResponse:
    def __init__(self, copy: AsyncCopyResource) -> None:
        self._copy = copy

        self.copy = async_to_streamed_response_wrapper(
            copy.copy,
        )
        self.copy_by_index = async_to_streamed_response_wrapper(
            copy.copy_by_index,
        )
