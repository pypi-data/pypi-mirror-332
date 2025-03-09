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
from .....types.api.v1.retrieval import reranking_update_config_params

__all__ = ["RerankingResource", "AsyncRerankingResource"]


class RerankingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RerankingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return RerankingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RerankingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return RerankingResourceWithStreamingResponse(self)

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
        """Get Reraanking Config"""
        return self._get(
            "/api/v1/retrieval/reranking",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update_config(
        self,
        *,
        reranking_model: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Reranking Config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/retrieval/reranking/update",
            body=maybe_transform(
                {"reranking_model": reranking_model}, reranking_update_config_params.RerankingUpdateConfigParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncRerankingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRerankingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRerankingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRerankingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncRerankingResourceWithStreamingResponse(self)

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
        """Get Reraanking Config"""
        return await self._get(
            "/api/v1/retrieval/reranking",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update_config(
        self,
        *,
        reranking_model: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Reranking Config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/retrieval/reranking/update",
            body=await async_maybe_transform(
                {"reranking_model": reranking_model}, reranking_update_config_params.RerankingUpdateConfigParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class RerankingResourceWithRawResponse:
    def __init__(self, reranking: RerankingResource) -> None:
        self._reranking = reranking

        self.get_config = to_raw_response_wrapper(
            reranking.get_config,
        )
        self.update_config = to_raw_response_wrapper(
            reranking.update_config,
        )


class AsyncRerankingResourceWithRawResponse:
    def __init__(self, reranking: AsyncRerankingResource) -> None:
        self._reranking = reranking

        self.get_config = async_to_raw_response_wrapper(
            reranking.get_config,
        )
        self.update_config = async_to_raw_response_wrapper(
            reranking.update_config,
        )


class RerankingResourceWithStreamingResponse:
    def __init__(self, reranking: RerankingResource) -> None:
        self._reranking = reranking

        self.get_config = to_streamed_response_wrapper(
            reranking.get_config,
        )
        self.update_config = to_streamed_response_wrapper(
            reranking.update_config,
        )


class AsyncRerankingResourceWithStreamingResponse:
    def __init__(self, reranking: AsyncRerankingResource) -> None:
        self._reranking = reranking

        self.get_config = async_to_streamed_response_wrapper(
            reranking.get_config,
        )
        self.update_config = async_to_streamed_response_wrapper(
            reranking.update_config,
        )
