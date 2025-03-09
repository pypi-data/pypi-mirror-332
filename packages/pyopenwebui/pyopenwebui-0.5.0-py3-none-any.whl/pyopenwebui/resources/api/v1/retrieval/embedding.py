# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from .....types.api.v1.retrieval import embedding_update_config_params

__all__ = ["EmbeddingResource", "AsyncEmbeddingResource"]


class EmbeddingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbeddingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return EmbeddingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbeddingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return EmbeddingResourceWithStreamingResponse(self)

    def get_config(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Embedding Config"""
        return self._get(
            "/api/v1/retrieval/embedding",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update_config(
        self,
        *,
        embedding_engine: str,
        embedding_model: str,
        embedding_batch_size: Optional[int] | NotGiven = NOT_GIVEN,
        ollama_config: Optional[embedding_update_config_params.OllamaConfig] | NotGiven = NOT_GIVEN,
        openai_config: Optional[embedding_update_config_params.OpenAIConfig] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Embedding Config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/retrieval/embedding/update",
            body=maybe_transform(
                {
                    "embedding_engine": embedding_engine,
                    "embedding_model": embedding_model,
                    "embedding_batch_size": embedding_batch_size,
                    "ollama_config": ollama_config,
                    "openai_config": openai_config,
                },
                embedding_update_config_params.EmbeddingUpdateConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncEmbeddingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmbeddingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmbeddingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbeddingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncEmbeddingResourceWithStreamingResponse(self)

    async def get_config(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Embedding Config"""
        return await self._get(
            "/api/v1/retrieval/embedding",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update_config(
        self,
        *,
        embedding_engine: str,
        embedding_model: str,
        embedding_batch_size: Optional[int] | NotGiven = NOT_GIVEN,
        ollama_config: Optional[embedding_update_config_params.OllamaConfig] | NotGiven = NOT_GIVEN,
        openai_config: Optional[embedding_update_config_params.OpenAIConfig] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Embedding Config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/retrieval/embedding/update",
            body=await async_maybe_transform(
                {
                    "embedding_engine": embedding_engine,
                    "embedding_model": embedding_model,
                    "embedding_batch_size": embedding_batch_size,
                    "ollama_config": ollama_config,
                    "openai_config": openai_config,
                },
                embedding_update_config_params.EmbeddingUpdateConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class EmbeddingResourceWithRawResponse:
    def __init__(self, embedding: EmbeddingResource) -> None:
        self._embedding = embedding

        self.get_config = to_raw_response_wrapper(
            embedding.get_config,
        )
        self.update_config = to_raw_response_wrapper(
            embedding.update_config,
        )


class AsyncEmbeddingResourceWithRawResponse:
    def __init__(self, embedding: AsyncEmbeddingResource) -> None:
        self._embedding = embedding

        self.get_config = async_to_raw_response_wrapper(
            embedding.get_config,
        )
        self.update_config = async_to_raw_response_wrapper(
            embedding.update_config,
        )


class EmbeddingResourceWithStreamingResponse:
    def __init__(self, embedding: EmbeddingResource) -> None:
        self._embedding = embedding

        self.get_config = to_streamed_response_wrapper(
            embedding.get_config,
        )
        self.update_config = to_streamed_response_wrapper(
            embedding.update_config,
        )


class AsyncEmbeddingResourceWithStreamingResponse:
    def __init__(self, embedding: AsyncEmbeddingResource) -> None:
        self._embedding = embedding

        self.get_config = async_to_streamed_response_wrapper(
            embedding.get_config,
        )
        self.update_config = async_to_streamed_response_wrapper(
            embedding.update_config,
        )
