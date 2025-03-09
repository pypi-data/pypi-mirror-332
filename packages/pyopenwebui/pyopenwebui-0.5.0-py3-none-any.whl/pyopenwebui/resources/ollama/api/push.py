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
from ....types.ollama.api import push_push_params, push_push_by_index_params

__all__ = ["PushResource", "AsyncPushResource"]


class PushResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PushResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return PushResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PushResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return PushResourceWithStreamingResponse(self)

    def push(
        self,
        *,
        name: str,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        insecure: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Push Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/ollama/api/push",
            body=maybe_transform(
                {
                    "name": name,
                    "insecure": insecure,
                    "stream": stream,
                },
                push_push_params.PushPushParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url_idx": url_idx}, push_push_params.PushPushParams),
            ),
            cast_to=object,
        )

    def push_by_index(
        self,
        url_idx: int,
        *,
        name: str,
        insecure: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Push Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/ollama/api/push/{url_idx}",
            body=maybe_transform(
                {
                    "name": name,
                    "insecure": insecure,
                    "stream": stream,
                },
                push_push_by_index_params.PushPushByIndexParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncPushResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPushResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPushResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPushResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncPushResourceWithStreamingResponse(self)

    async def push(
        self,
        *,
        name: str,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        insecure: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Push Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/ollama/api/push",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "insecure": insecure,
                    "stream": stream,
                },
                push_push_params.PushPushParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url_idx": url_idx}, push_push_params.PushPushParams),
            ),
            cast_to=object,
        )

    async def push_by_index(
        self,
        url_idx: int,
        *,
        name: str,
        insecure: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Push Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/ollama/api/push/{url_idx}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "insecure": insecure,
                    "stream": stream,
                },
                push_push_by_index_params.PushPushByIndexParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class PushResourceWithRawResponse:
    def __init__(self, push: PushResource) -> None:
        self._push = push

        self.push = to_raw_response_wrapper(
            push.push,
        )
        self.push_by_index = to_raw_response_wrapper(
            push.push_by_index,
        )


class AsyncPushResourceWithRawResponse:
    def __init__(self, push: AsyncPushResource) -> None:
        self._push = push

        self.push = async_to_raw_response_wrapper(
            push.push,
        )
        self.push_by_index = async_to_raw_response_wrapper(
            push.push_by_index,
        )


class PushResourceWithStreamingResponse:
    def __init__(self, push: PushResource) -> None:
        self._push = push

        self.push = to_streamed_response_wrapper(
            push.push,
        )
        self.push_by_index = to_streamed_response_wrapper(
            push.push_by_index,
        )


class AsyncPushResourceWithStreamingResponse:
    def __init__(self, push: AsyncPushResource) -> None:
        self._push = push

        self.push = async_to_streamed_response_wrapper(
            push.push,
        )
        self.push_by_index = async_to_streamed_response_wrapper(
            push.push_by_index,
        )
