# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .web import (
    WebResource,
    AsyncWebResource,
    WebResourceWithRawResponse,
    AsyncWebResourceWithRawResponse,
    WebResourceWithStreamingResponse,
    AsyncWebResourceWithStreamingResponse,
)
from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.api.v1.retrieval import process_file_params, process_text_params, process_youtube_params

__all__ = ["ProcessResource", "AsyncProcessResource"]


class ProcessResource(SyncAPIResource):
    @cached_property
    def web(self) -> WebResource:
        return WebResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProcessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ProcessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProcessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ProcessResourceWithStreamingResponse(self)

    def file(
        self,
        *,
        file_id: str,
        collection_name: Optional[str] | NotGiven = NOT_GIVEN,
        content: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Process File

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/retrieval/process/file",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "collection_name": collection_name,
                    "content": content,
                },
                process_file_params.ProcessFileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def text(
        self,
        *,
        content: str,
        name: str,
        collection_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Process Text

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/retrieval/process/text",
            body=maybe_transform(
                {
                    "content": content,
                    "name": name,
                    "collection_name": collection_name,
                },
                process_text_params.ProcessTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def youtube(
        self,
        *,
        url: str,
        collection_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Process Youtube Video

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/retrieval/process/youtube",
            body=maybe_transform(
                {
                    "url": url,
                    "collection_name": collection_name,
                },
                process_youtube_params.ProcessYoutubeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncProcessResource(AsyncAPIResource):
    @cached_property
    def web(self) -> AsyncWebResource:
        return AsyncWebResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProcessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProcessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProcessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncProcessResourceWithStreamingResponse(self)

    async def file(
        self,
        *,
        file_id: str,
        collection_name: Optional[str] | NotGiven = NOT_GIVEN,
        content: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Process File

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/retrieval/process/file",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "collection_name": collection_name,
                    "content": content,
                },
                process_file_params.ProcessFileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def text(
        self,
        *,
        content: str,
        name: str,
        collection_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Process Text

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/retrieval/process/text",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "name": name,
                    "collection_name": collection_name,
                },
                process_text_params.ProcessTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def youtube(
        self,
        *,
        url: str,
        collection_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Process Youtube Video

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/retrieval/process/youtube",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "collection_name": collection_name,
                },
                process_youtube_params.ProcessYoutubeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ProcessResourceWithRawResponse:
    def __init__(self, process: ProcessResource) -> None:
        self._process = process

        self.file = to_raw_response_wrapper(
            process.file,
        )
        self.text = to_raw_response_wrapper(
            process.text,
        )
        self.youtube = to_raw_response_wrapper(
            process.youtube,
        )

    @cached_property
    def web(self) -> WebResourceWithRawResponse:
        return WebResourceWithRawResponse(self._process.web)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._process.files)


class AsyncProcessResourceWithRawResponse:
    def __init__(self, process: AsyncProcessResource) -> None:
        self._process = process

        self.file = async_to_raw_response_wrapper(
            process.file,
        )
        self.text = async_to_raw_response_wrapper(
            process.text,
        )
        self.youtube = async_to_raw_response_wrapper(
            process.youtube,
        )

    @cached_property
    def web(self) -> AsyncWebResourceWithRawResponse:
        return AsyncWebResourceWithRawResponse(self._process.web)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._process.files)


class ProcessResourceWithStreamingResponse:
    def __init__(self, process: ProcessResource) -> None:
        self._process = process

        self.file = to_streamed_response_wrapper(
            process.file,
        )
        self.text = to_streamed_response_wrapper(
            process.text,
        )
        self.youtube = to_streamed_response_wrapper(
            process.youtube,
        )

    @cached_property
    def web(self) -> WebResourceWithStreamingResponse:
        return WebResourceWithStreamingResponse(self._process.web)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._process.files)


class AsyncProcessResourceWithStreamingResponse:
    def __init__(self, process: AsyncProcessResource) -> None:
        self._process = process

        self.file = async_to_streamed_response_wrapper(
            process.file,
        )
        self.text = async_to_streamed_response_wrapper(
            process.text,
        )
        self.youtube = async_to_streamed_response_wrapper(
            process.youtube,
        )

    @cached_property
    def web(self) -> AsyncWebResourceWithStreamingResponse:
        return AsyncWebResourceWithStreamingResponse(self._process.web)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._process.files)
