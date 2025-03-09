# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .all import (
    AllResource,
    AsyncAllResource,
    AllResourceWithRawResponse,
    AsyncAllResourceWithRawResponse,
    AllResourceWithStreamingResponse,
    AsyncAllResourceWithStreamingResponse,
)
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
from ......types.api.v1.evaluations.feedback_get_response import FeedbackGetResponse
from ......types.api.v1.evaluations.feedback_delete_response import FeedbackDeleteResponse

__all__ = ["FeedbacksResource", "AsyncFeedbacksResource"]


class FeedbacksResource(SyncAPIResource):
    @cached_property
    def all(self) -> AllResource:
        return AllResource(self._client)

    @cached_property
    def with_raw_response(self) -> FeedbacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return FeedbacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedbacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return FeedbacksResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackDeleteResponse:
        """Delete Feedbacks"""
        return self._delete(
            "/api/v1/evaluations/feedbacks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackDeleteResponse,
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
    ) -> FeedbackGetResponse:
        """Get Feedbacks"""
        return self._get(
            "/api/v1/evaluations/feedbacks/user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackGetResponse,
        )


class AsyncFeedbacksResource(AsyncAPIResource):
    @cached_property
    def all(self) -> AsyncAllResource:
        return AsyncAllResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFeedbacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeedbacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedbacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncFeedbacksResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackDeleteResponse:
        """Delete Feedbacks"""
        return await self._delete(
            "/api/v1/evaluations/feedbacks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackDeleteResponse,
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
    ) -> FeedbackGetResponse:
        """Get Feedbacks"""
        return await self._get(
            "/api/v1/evaluations/feedbacks/user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackGetResponse,
        )


class FeedbacksResourceWithRawResponse:
    def __init__(self, feedbacks: FeedbacksResource) -> None:
        self._feedbacks = feedbacks

        self.delete = to_raw_response_wrapper(
            feedbacks.delete,
        )
        self.get = to_raw_response_wrapper(
            feedbacks.get,
        )

    @cached_property
    def all(self) -> AllResourceWithRawResponse:
        return AllResourceWithRawResponse(self._feedbacks.all)


class AsyncFeedbacksResourceWithRawResponse:
    def __init__(self, feedbacks: AsyncFeedbacksResource) -> None:
        self._feedbacks = feedbacks

        self.delete = async_to_raw_response_wrapper(
            feedbacks.delete,
        )
        self.get = async_to_raw_response_wrapper(
            feedbacks.get,
        )

    @cached_property
    def all(self) -> AsyncAllResourceWithRawResponse:
        return AsyncAllResourceWithRawResponse(self._feedbacks.all)


class FeedbacksResourceWithStreamingResponse:
    def __init__(self, feedbacks: FeedbacksResource) -> None:
        self._feedbacks = feedbacks

        self.delete = to_streamed_response_wrapper(
            feedbacks.delete,
        )
        self.get = to_streamed_response_wrapper(
            feedbacks.get,
        )

    @cached_property
    def all(self) -> AllResourceWithStreamingResponse:
        return AllResourceWithStreamingResponse(self._feedbacks.all)


class AsyncFeedbacksResourceWithStreamingResponse:
    def __init__(self, feedbacks: AsyncFeedbacksResource) -> None:
        self._feedbacks = feedbacks

        self.delete = async_to_streamed_response_wrapper(
            feedbacks.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            feedbacks.get,
        )

    @cached_property
    def all(self) -> AsyncAllResourceWithStreamingResponse:
        return AsyncAllResourceWithStreamingResponse(self._feedbacks.all)
