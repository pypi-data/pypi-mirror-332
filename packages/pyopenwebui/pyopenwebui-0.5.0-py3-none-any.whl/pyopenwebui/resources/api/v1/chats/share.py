# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from .....types.chat_response import ChatResponse
from .....types.api.v1.chats.share_delete_response import ShareDeleteResponse

__all__ = ["ShareResource", "AsyncShareResource"]


class ShareResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShareResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ShareResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShareResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ShareResourceWithStreamingResponse(self)

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ShareDeleteResponse]:
        """
        Delete Shared Chat By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v1/chats/{id}/share",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShareDeleteResponse,
        )

    def get(
        self,
        share_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Get Shared Chat By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return self._get(
            f"/api/v1/chats/share/{share_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )


class AsyncShareResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShareResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncShareResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShareResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncShareResourceWithStreamingResponse(self)

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ShareDeleteResponse]:
        """
        Delete Shared Chat By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v1/chats/{id}/share",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShareDeleteResponse,
        )

    async def get(
        self,
        share_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Get Shared Chat By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return await self._get(
            f"/api/v1/chats/share/{share_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )


class ShareResourceWithRawResponse:
    def __init__(self, share: ShareResource) -> None:
        self._share = share

        self.delete = to_raw_response_wrapper(
            share.delete,
        )
        self.get = to_raw_response_wrapper(
            share.get,
        )


class AsyncShareResourceWithRawResponse:
    def __init__(self, share: AsyncShareResource) -> None:
        self._share = share

        self.delete = async_to_raw_response_wrapper(
            share.delete,
        )
        self.get = async_to_raw_response_wrapper(
            share.get,
        )


class ShareResourceWithStreamingResponse:
    def __init__(self, share: ShareResource) -> None:
        self._share = share

        self.delete = to_streamed_response_wrapper(
            share.delete,
        )
        self.get = to_streamed_response_wrapper(
            share.get,
        )


class AsyncShareResourceWithStreamingResponse:
    def __init__(self, share: AsyncShareResource) -> None:
        self._share = share

        self.delete = async_to_streamed_response_wrapper(
            share.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            share.get,
        )
