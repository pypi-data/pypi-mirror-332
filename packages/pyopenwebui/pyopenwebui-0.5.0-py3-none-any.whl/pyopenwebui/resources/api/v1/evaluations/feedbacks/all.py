# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.api.v1.evaluations.feedbacks.all_get_response import AllGetResponse
from ......types.api.v1.evaluations.feedbacks.all_export_response import AllExportResponse

__all__ = ["AllResource", "AsyncAllResource"]


class AllResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AllResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AllResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AllResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AllResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete All Feedbacks"""
        return self._delete(
            "/api/v1/evaluations/feedbacks/all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
    ) -> AllExportResponse:
        """Get All Feedbacks"""
        return self._get(
            "/api/v1/evaluations/feedbacks/all/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllExportResponse,
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
    ) -> AllGetResponse:
        """Get All Feedbacks"""
        return self._get(
            "/api/v1/evaluations/feedbacks/all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllGetResponse,
        )


class AsyncAllResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAllResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAllResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAllResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncAllResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete All Feedbacks"""
        return await self._delete(
            "/api/v1/evaluations/feedbacks/all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
    ) -> AllExportResponse:
        """Get All Feedbacks"""
        return await self._get(
            "/api/v1/evaluations/feedbacks/all/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllExportResponse,
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
    ) -> AllGetResponse:
        """Get All Feedbacks"""
        return await self._get(
            "/api/v1/evaluations/feedbacks/all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllGetResponse,
        )


class AllResourceWithRawResponse:
    def __init__(self, all: AllResource) -> None:
        self._all = all

        self.delete = to_raw_response_wrapper(
            all.delete,
        )
        self.export = to_raw_response_wrapper(
            all.export,
        )
        self.get = to_raw_response_wrapper(
            all.get,
        )


class AsyncAllResourceWithRawResponse:
    def __init__(self, all: AsyncAllResource) -> None:
        self._all = all

        self.delete = async_to_raw_response_wrapper(
            all.delete,
        )
        self.export = async_to_raw_response_wrapper(
            all.export,
        )
        self.get = async_to_raw_response_wrapper(
            all.get,
        )


class AllResourceWithStreamingResponse:
    def __init__(self, all: AllResource) -> None:
        self._all = all

        self.delete = to_streamed_response_wrapper(
            all.delete,
        )
        self.export = to_streamed_response_wrapper(
            all.export,
        )
        self.get = to_streamed_response_wrapper(
            all.get,
        )


class AsyncAllResourceWithStreamingResponse:
    def __init__(self, all: AsyncAllResource) -> None:
        self._all = all

        self.delete = async_to_streamed_response_wrapper(
            all.delete,
        )
        self.export = async_to_streamed_response_wrapper(
            all.export,
        )
        self.get = async_to_streamed_response_wrapper(
            all.get,
        )
