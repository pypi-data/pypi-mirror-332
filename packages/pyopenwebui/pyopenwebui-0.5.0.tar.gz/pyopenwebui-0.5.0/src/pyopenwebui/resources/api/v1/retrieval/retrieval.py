# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .reset import (
    ResetResource,
    AsyncResetResource,
    ResetResourceWithRawResponse,
    AsyncResetResourceWithRawResponse,
    ResetResourceWithStreamingResponse,
    AsyncResetResourceWithStreamingResponse,
)
from .config import (
    ConfigResource,
    AsyncConfigResource,
    ConfigResourceWithRawResponse,
    AsyncConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
    AsyncConfigResourceWithStreamingResponse,
)
from .embedding import (
    EmbeddingResource,
    AsyncEmbeddingResource,
    EmbeddingResourceWithRawResponse,
    AsyncEmbeddingResourceWithRawResponse,
    EmbeddingResourceWithStreamingResponse,
    AsyncEmbeddingResourceWithStreamingResponse,
)
from .reranking import (
    RerankingResource,
    AsyncRerankingResource,
    RerankingResourceWithRawResponse,
    AsyncRerankingResourceWithRawResponse,
    RerankingResourceWithStreamingResponse,
    AsyncRerankingResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from .query.query import (
    QueryResource,
    AsyncQueryResource,
    QueryResourceWithRawResponse,
    AsyncQueryResourceWithRawResponse,
    QueryResourceWithStreamingResponse,
    AsyncQueryResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .process.process import (
    ProcessResource,
    AsyncProcessResource,
    ProcessResourceWithRawResponse,
    AsyncProcessResourceWithRawResponse,
    ProcessResourceWithStreamingResponse,
    AsyncProcessResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .....types.api.v1 import retrieval_delete_entries_params

__all__ = ["RetrievalResource", "AsyncRetrievalResource"]


class RetrievalResource(SyncAPIResource):
    @cached_property
    def embedding(self) -> EmbeddingResource:
        return EmbeddingResource(self._client)

    @cached_property
    def reranking(self) -> RerankingResource:
        return RerankingResource(self._client)

    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def query(self) -> QueryResource:
        return QueryResource(self._client)

    @cached_property
    def process(self) -> ProcessResource:
        return ProcessResource(self._client)

    @cached_property
    def reset(self) -> ResetResource:
        return ResetResource(self._client)

    @cached_property
    def with_raw_response(self) -> RetrievalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return RetrievalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetrievalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return RetrievalResourceWithStreamingResponse(self)

    def delete_entries(
        self,
        *,
        collection_name: str,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Entries From Collection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/retrieval/delete",
            body=maybe_transform(
                {
                    "collection_name": collection_name,
                    "file_id": file_id,
                },
                retrieval_delete_entries_params.RetrievalDeleteEntriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_embeddings(
        self,
        text: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Embeddings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not text:
            raise ValueError(f"Expected a non-empty value for `text` but received {text!r}")
        return self._get(
            f"/api/v1/retrieval/ef/{text}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Status"""
        return self._get(
            "/api/v1/retrieval/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_template(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Rag Template"""
        return self._get(
            "/api/v1/retrieval/template",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncRetrievalResource(AsyncAPIResource):
    @cached_property
    def embedding(self) -> AsyncEmbeddingResource:
        return AsyncEmbeddingResource(self._client)

    @cached_property
    def reranking(self) -> AsyncRerankingResource:
        return AsyncRerankingResource(self._client)

    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def query(self) -> AsyncQueryResource:
        return AsyncQueryResource(self._client)

    @cached_property
    def process(self) -> AsyncProcessResource:
        return AsyncProcessResource(self._client)

    @cached_property
    def reset(self) -> AsyncResetResource:
        return AsyncResetResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRetrievalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRetrievalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetrievalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncRetrievalResourceWithStreamingResponse(self)

    async def delete_entries(
        self,
        *,
        collection_name: str,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Entries From Collection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/retrieval/delete",
            body=await async_maybe_transform(
                {
                    "collection_name": collection_name,
                    "file_id": file_id,
                },
                retrieval_delete_entries_params.RetrievalDeleteEntriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_embeddings(
        self,
        text: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Embeddings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not text:
            raise ValueError(f"Expected a non-empty value for `text` but received {text!r}")
        return await self._get(
            f"/api/v1/retrieval/ef/{text}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Status"""
        return await self._get(
            "/api/v1/retrieval/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_template(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Rag Template"""
        return await self._get(
            "/api/v1/retrieval/template",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class RetrievalResourceWithRawResponse:
    def __init__(self, retrieval: RetrievalResource) -> None:
        self._retrieval = retrieval

        self.delete_entries = to_raw_response_wrapper(
            retrieval.delete_entries,
        )
        self.get_embeddings = to_raw_response_wrapper(
            retrieval.get_embeddings,
        )
        self.get_status = to_raw_response_wrapper(
            retrieval.get_status,
        )
        self.get_template = to_raw_response_wrapper(
            retrieval.get_template,
        )

    @cached_property
    def embedding(self) -> EmbeddingResourceWithRawResponse:
        return EmbeddingResourceWithRawResponse(self._retrieval.embedding)

    @cached_property
    def reranking(self) -> RerankingResourceWithRawResponse:
        return RerankingResourceWithRawResponse(self._retrieval.reranking)

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._retrieval.config)

    @cached_property
    def query(self) -> QueryResourceWithRawResponse:
        return QueryResourceWithRawResponse(self._retrieval.query)

    @cached_property
    def process(self) -> ProcessResourceWithRawResponse:
        return ProcessResourceWithRawResponse(self._retrieval.process)

    @cached_property
    def reset(self) -> ResetResourceWithRawResponse:
        return ResetResourceWithRawResponse(self._retrieval.reset)


class AsyncRetrievalResourceWithRawResponse:
    def __init__(self, retrieval: AsyncRetrievalResource) -> None:
        self._retrieval = retrieval

        self.delete_entries = async_to_raw_response_wrapper(
            retrieval.delete_entries,
        )
        self.get_embeddings = async_to_raw_response_wrapper(
            retrieval.get_embeddings,
        )
        self.get_status = async_to_raw_response_wrapper(
            retrieval.get_status,
        )
        self.get_template = async_to_raw_response_wrapper(
            retrieval.get_template,
        )

    @cached_property
    def embedding(self) -> AsyncEmbeddingResourceWithRawResponse:
        return AsyncEmbeddingResourceWithRawResponse(self._retrieval.embedding)

    @cached_property
    def reranking(self) -> AsyncRerankingResourceWithRawResponse:
        return AsyncRerankingResourceWithRawResponse(self._retrieval.reranking)

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._retrieval.config)

    @cached_property
    def query(self) -> AsyncQueryResourceWithRawResponse:
        return AsyncQueryResourceWithRawResponse(self._retrieval.query)

    @cached_property
    def process(self) -> AsyncProcessResourceWithRawResponse:
        return AsyncProcessResourceWithRawResponse(self._retrieval.process)

    @cached_property
    def reset(self) -> AsyncResetResourceWithRawResponse:
        return AsyncResetResourceWithRawResponse(self._retrieval.reset)


class RetrievalResourceWithStreamingResponse:
    def __init__(self, retrieval: RetrievalResource) -> None:
        self._retrieval = retrieval

        self.delete_entries = to_streamed_response_wrapper(
            retrieval.delete_entries,
        )
        self.get_embeddings = to_streamed_response_wrapper(
            retrieval.get_embeddings,
        )
        self.get_status = to_streamed_response_wrapper(
            retrieval.get_status,
        )
        self.get_template = to_streamed_response_wrapper(
            retrieval.get_template,
        )

    @cached_property
    def embedding(self) -> EmbeddingResourceWithStreamingResponse:
        return EmbeddingResourceWithStreamingResponse(self._retrieval.embedding)

    @cached_property
    def reranking(self) -> RerankingResourceWithStreamingResponse:
        return RerankingResourceWithStreamingResponse(self._retrieval.reranking)

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._retrieval.config)

    @cached_property
    def query(self) -> QueryResourceWithStreamingResponse:
        return QueryResourceWithStreamingResponse(self._retrieval.query)

    @cached_property
    def process(self) -> ProcessResourceWithStreamingResponse:
        return ProcessResourceWithStreamingResponse(self._retrieval.process)

    @cached_property
    def reset(self) -> ResetResourceWithStreamingResponse:
        return ResetResourceWithStreamingResponse(self._retrieval.reset)


class AsyncRetrievalResourceWithStreamingResponse:
    def __init__(self, retrieval: AsyncRetrievalResource) -> None:
        self._retrieval = retrieval

        self.delete_entries = async_to_streamed_response_wrapper(
            retrieval.delete_entries,
        )
        self.get_embeddings = async_to_streamed_response_wrapper(
            retrieval.get_embeddings,
        )
        self.get_status = async_to_streamed_response_wrapper(
            retrieval.get_status,
        )
        self.get_template = async_to_streamed_response_wrapper(
            retrieval.get_template,
        )

    @cached_property
    def embedding(self) -> AsyncEmbeddingResourceWithStreamingResponse:
        return AsyncEmbeddingResourceWithStreamingResponse(self._retrieval.embedding)

    @cached_property
    def reranking(self) -> AsyncRerankingResourceWithStreamingResponse:
        return AsyncRerankingResourceWithStreamingResponse(self._retrieval.reranking)

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._retrieval.config)

    @cached_property
    def query(self) -> AsyncQueryResourceWithStreamingResponse:
        return AsyncQueryResourceWithStreamingResponse(self._retrieval.query)

    @cached_property
    def process(self) -> AsyncProcessResourceWithStreamingResponse:
        return AsyncProcessResourceWithStreamingResponse(self._retrieval.process)

    @cached_property
    def reset(self) -> AsyncResetResourceWithStreamingResponse:
        return AsyncResetResourceWithStreamingResponse(self._retrieval.reset)
