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
from ....types.ollama.models import download_download_params, download_download_by_index_params

__all__ = ["DownloadResource", "AsyncDownloadResource"]


class DownloadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DownloadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return DownloadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DownloadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return DownloadResourceWithStreamingResponse(self)

    def download(
        self,
        *,
        url: str,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Download Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ollama/models/download",
            body=maybe_transform({"url": url}, download_download_params.DownloadDownloadParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url_idx": url_idx}, download_download_params.DownloadDownloadParams),
            ),
            cast_to=object,
        )

    def download_by_index(
        self,
        url_idx: int,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Download Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/ollama/models/download/{url_idx}",
            body=maybe_transform({"url": url}, download_download_by_index_params.DownloadDownloadByIndexParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncDownloadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDownloadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDownloadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDownloadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncDownloadResourceWithStreamingResponse(self)

    async def download(
        self,
        *,
        url: str,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Download Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ollama/models/download",
            body=await async_maybe_transform({"url": url}, download_download_params.DownloadDownloadParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"url_idx": url_idx}, download_download_params.DownloadDownloadParams
                ),
            ),
            cast_to=object,
        )

    async def download_by_index(
        self,
        url_idx: int,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Download Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/ollama/models/download/{url_idx}",
            body=await async_maybe_transform(
                {"url": url}, download_download_by_index_params.DownloadDownloadByIndexParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DownloadResourceWithRawResponse:
    def __init__(self, download: DownloadResource) -> None:
        self._download = download

        self.download = to_raw_response_wrapper(
            download.download,
        )
        self.download_by_index = to_raw_response_wrapper(
            download.download_by_index,
        )


class AsyncDownloadResourceWithRawResponse:
    def __init__(self, download: AsyncDownloadResource) -> None:
        self._download = download

        self.download = async_to_raw_response_wrapper(
            download.download,
        )
        self.download_by_index = async_to_raw_response_wrapper(
            download.download_by_index,
        )


class DownloadResourceWithStreamingResponse:
    def __init__(self, download: DownloadResource) -> None:
        self._download = download

        self.download = to_streamed_response_wrapper(
            download.download,
        )
        self.download_by_index = to_streamed_response_wrapper(
            download.download_by_index,
        )


class AsyncDownloadResourceWithStreamingResponse:
    def __init__(self, download: AsyncDownloadResource) -> None:
        self._download = download

        self.download = async_to_streamed_response_wrapper(
            download.download,
        )
        self.download_by_index = async_to_streamed_response_wrapper(
            download.download_by_index,
        )
