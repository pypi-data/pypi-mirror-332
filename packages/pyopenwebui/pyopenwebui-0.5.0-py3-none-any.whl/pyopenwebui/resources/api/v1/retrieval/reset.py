# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1.retrieval.reset_uploads_response import ResetUploadsResponse

__all__ = ["ResetResource", "AsyncResetResource"]


class ResetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ResetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ResetResourceWithStreamingResponse(self)

    def db(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Reset Vector Db"""
        return self._post(
            "/api/v1/retrieval/reset/db",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def uploads(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResetUploadsResponse:
        """Reset Upload Dir"""
        return self._post(
            "/api/v1/retrieval/reset/uploads",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResetUploadsResponse,
        )


class AsyncResetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncResetResourceWithStreamingResponse(self)

    async def db(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Reset Vector Db"""
        return await self._post(
            "/api/v1/retrieval/reset/db",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def uploads(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResetUploadsResponse:
        """Reset Upload Dir"""
        return await self._post(
            "/api/v1/retrieval/reset/uploads",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResetUploadsResponse,
        )


class ResetResourceWithRawResponse:
    def __init__(self, reset: ResetResource) -> None:
        self._reset = reset

        self.db = to_raw_response_wrapper(
            reset.db,
        )
        self.uploads = to_raw_response_wrapper(
            reset.uploads,
        )


class AsyncResetResourceWithRawResponse:
    def __init__(self, reset: AsyncResetResource) -> None:
        self._reset = reset

        self.db = async_to_raw_response_wrapper(
            reset.db,
        )
        self.uploads = async_to_raw_response_wrapper(
            reset.uploads,
        )


class ResetResourceWithStreamingResponse:
    def __init__(self, reset: ResetResource) -> None:
        self._reset = reset

        self.db = to_streamed_response_wrapper(
            reset.db,
        )
        self.uploads = to_streamed_response_wrapper(
            reset.uploads,
        )


class AsyncResetResourceWithStreamingResponse:
    def __init__(self, reset: AsyncResetResource) -> None:
        self._reset = reset

        self.db = async_to_streamed_response_wrapper(
            reset.db,
        )
        self.uploads = async_to_streamed_response_wrapper(
            reset.uploads,
        )
