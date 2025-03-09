# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional

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
from ....types.ollama.api import embed_embed_params, embed_embed_by_index_params

__all__ = ["EmbedResource", "AsyncEmbedResource"]


class EmbedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return EmbedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return EmbedResourceWithStreamingResponse(self)

    def embed(
        self,
        *,
        input: Union[List[str], str],
        model: str,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        keep_alive: Union[int, str, None] | NotGiven = NOT_GIVEN,
        options: Optional[object] | NotGiven = NOT_GIVEN,
        truncate: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ollama/api/embed",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "keep_alive": keep_alive,
                    "options": options,
                    "truncate": truncate,
                },
                embed_embed_params.EmbedEmbedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url_idx": url_idx}, embed_embed_params.EmbedEmbedParams),
            ),
            cast_to=object,
        )

    def embed_by_index(
        self,
        url_idx: int,
        *,
        input: Union[List[str], str],
        model: str,
        keep_alive: Union[int, str, None] | NotGiven = NOT_GIVEN,
        options: Optional[object] | NotGiven = NOT_GIVEN,
        truncate: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/ollama/api/embed/{url_idx}",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "keep_alive": keep_alive,
                    "options": options,
                    "truncate": truncate,
                },
                embed_embed_by_index_params.EmbedEmbedByIndexParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncEmbedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmbedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmbedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncEmbedResourceWithStreamingResponse(self)

    async def embed(
        self,
        *,
        input: Union[List[str], str],
        model: str,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        keep_alive: Union[int, str, None] | NotGiven = NOT_GIVEN,
        options: Optional[object] | NotGiven = NOT_GIVEN,
        truncate: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ollama/api/embed",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "keep_alive": keep_alive,
                    "options": options,
                    "truncate": truncate,
                },
                embed_embed_params.EmbedEmbedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url_idx": url_idx}, embed_embed_params.EmbedEmbedParams),
            ),
            cast_to=object,
        )

    async def embed_by_index(
        self,
        url_idx: int,
        *,
        input: Union[List[str], str],
        model: str,
        keep_alive: Union[int, str, None] | NotGiven = NOT_GIVEN,
        options: Optional[object] | NotGiven = NOT_GIVEN,
        truncate: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Embed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/ollama/api/embed/{url_idx}",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "keep_alive": keep_alive,
                    "options": options,
                    "truncate": truncate,
                },
                embed_embed_by_index_params.EmbedEmbedByIndexParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class EmbedResourceWithRawResponse:
    def __init__(self, embed: EmbedResource) -> None:
        self._embed = embed

        self.embed = to_raw_response_wrapper(
            embed.embed,
        )
        self.embed_by_index = to_raw_response_wrapper(
            embed.embed_by_index,
        )


class AsyncEmbedResourceWithRawResponse:
    def __init__(self, embed: AsyncEmbedResource) -> None:
        self._embed = embed

        self.embed = async_to_raw_response_wrapper(
            embed.embed,
        )
        self.embed_by_index = async_to_raw_response_wrapper(
            embed.embed_by_index,
        )


class EmbedResourceWithStreamingResponse:
    def __init__(self, embed: EmbedResource) -> None:
        self._embed = embed

        self.embed = to_streamed_response_wrapper(
            embed.embed,
        )
        self.embed_by_index = to_streamed_response_wrapper(
            embed.embed_by_index,
        )


class AsyncEmbedResourceWithStreamingResponse:
    def __init__(self, embed: AsyncEmbedResource) -> None:
        self._embed = embed

        self.embed = async_to_streamed_response_wrapper(
            embed.embed,
        )
        self.embed_by_index = async_to_streamed_response_wrapper(
            embed.embed_by_index,
        )
