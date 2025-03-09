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
from ....types.ollama.api import delete_delete_params, delete_delete_by_index_params

__all__ = ["DeleteResource", "AsyncDeleteResource"]


class DeleteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeleteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return DeleteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeleteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return DeleteResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        name: str,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/ollama/api/delete",
            body=maybe_transform({"name": name}, delete_delete_params.DeleteDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url_idx": url_idx}, delete_delete_params.DeleteDeleteParams),
            ),
            cast_to=object,
        )

    def delete_by_index(
        self,
        url_idx: int,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/ollama/api/delete/{url_idx}",
            body=maybe_transform({"name": name}, delete_delete_by_index_params.DeleteDeleteByIndexParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncDeleteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeleteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeleteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeleteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncDeleteResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        name: str,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/ollama/api/delete",
            body=await async_maybe_transform({"name": name}, delete_delete_params.DeleteDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url_idx": url_idx}, delete_delete_params.DeleteDeleteParams),
            ),
            cast_to=object,
        )

    async def delete_by_index(
        self,
        url_idx: int,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/ollama/api/delete/{url_idx}",
            body=await async_maybe_transform({"name": name}, delete_delete_by_index_params.DeleteDeleteByIndexParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DeleteResourceWithRawResponse:
    def __init__(self, delete: DeleteResource) -> None:
        self._delete = delete

        self.delete = to_raw_response_wrapper(
            delete.delete,
        )
        self.delete_by_index = to_raw_response_wrapper(
            delete.delete_by_index,
        )


class AsyncDeleteResourceWithRawResponse:
    def __init__(self, delete: AsyncDeleteResource) -> None:
        self._delete = delete

        self.delete = async_to_raw_response_wrapper(
            delete.delete,
        )
        self.delete_by_index = async_to_raw_response_wrapper(
            delete.delete_by_index,
        )


class DeleteResourceWithStreamingResponse:
    def __init__(self, delete: DeleteResource) -> None:
        self._delete = delete

        self.delete = to_streamed_response_wrapper(
            delete.delete,
        )
        self.delete_by_index = to_streamed_response_wrapper(
            delete.delete_by_index,
        )


class AsyncDeleteResourceWithStreamingResponse:
    def __init__(self, delete: AsyncDeleteResource) -> None:
        self._delete = delete

        self.delete = async_to_streamed_response_wrapper(
            delete.delete,
        )
        self.delete_by_index = async_to_streamed_response_wrapper(
            delete.delete_by_index,
        )
