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
from .....types.api.v1.tasks import emoji_generate_params

__all__ = ["EmojiResource", "AsyncEmojiResource"]


class EmojiResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmojiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return EmojiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmojiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return EmojiResourceWithStreamingResponse(self)

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
        Generate Emoji

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/tasks/emoji/completions",
            body=maybe_transform(body, emoji_generate_params.EmojiGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncEmojiResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmojiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmojiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmojiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncEmojiResourceWithStreamingResponse(self)

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
        Generate Emoji

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/tasks/emoji/completions",
            body=await async_maybe_transform(body, emoji_generate_params.EmojiGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class EmojiResourceWithRawResponse:
    def __init__(self, emoji: EmojiResource) -> None:
        self._emoji = emoji

        self.generate = to_raw_response_wrapper(
            emoji.generate,
        )


class AsyncEmojiResourceWithRawResponse:
    def __init__(self, emoji: AsyncEmojiResource) -> None:
        self._emoji = emoji

        self.generate = async_to_raw_response_wrapper(
            emoji.generate,
        )


class EmojiResourceWithStreamingResponse:
    def __init__(self, emoji: EmojiResource) -> None:
        self._emoji = emoji

        self.generate = to_streamed_response_wrapper(
            emoji.generate,
        )


class AsyncEmojiResourceWithStreamingResponse:
    def __init__(self, emoji: AsyncEmojiResource) -> None:
        self._emoji = emoji

        self.generate = async_to_streamed_response_wrapper(
            emoji.generate,
        )
