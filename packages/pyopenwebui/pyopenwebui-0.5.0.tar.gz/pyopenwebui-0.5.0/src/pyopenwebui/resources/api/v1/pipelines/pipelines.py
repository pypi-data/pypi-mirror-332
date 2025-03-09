# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast

import httpx

from .valves import (
    ValvesResource,
    AsyncValvesResource,
    ValvesResourceWithRawResponse,
    AsyncValvesResourceWithRawResponse,
    ValvesResourceWithStreamingResponse,
    AsyncValvesResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ....._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
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
from .....types.api.v1 import pipeline_add_params, pipeline_get_params, pipeline_delete_params, pipeline_upload_params

__all__ = ["PipelinesResource", "AsyncPipelinesResource"]


class PipelinesResource(SyncAPIResource):
    @cached_property
    def valves(self) -> ValvesResource:
        return ValvesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PipelinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return PipelinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PipelinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return PipelinesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Pipelines List"""
        return self._get(
            "/api/v1/pipelines/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def delete(
        self,
        *,
        id: str,
        url_idx: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Pipeline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/api/v1/pipelines/delete",
            body=maybe_transform(
                {
                    "id": id,
                    "url_idx": url_idx,
                },
                pipeline_delete_params.PipelineDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def add(
        self,
        *,
        url: str,
        url_idx: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Add Pipeline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/pipelines/add",
            body=maybe_transform(
                {
                    "url": url,
                    "url_idx": url_idx,
                },
                pipeline_add_params.PipelineAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get(
        self,
        *,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Pipelines

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/pipelines/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url_idx": url_idx}, pipeline_get_params.PipelineGetParams),
            ),
            cast_to=object,
        )

    def upload(
        self,
        *,
        file: FileTypes,
        url_idx: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Upload Pipeline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "url_idx": url_idx,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/pipelines/upload",
            body=maybe_transform(body, pipeline_upload_params.PipelineUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncPipelinesResource(AsyncAPIResource):
    @cached_property
    def valves(self) -> AsyncValvesResource:
        return AsyncValvesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPipelinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPipelinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPipelinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncPipelinesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Pipelines List"""
        return await self._get(
            "/api/v1/pipelines/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def delete(
        self,
        *,
        id: str,
        url_idx: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Pipeline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/api/v1/pipelines/delete",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "url_idx": url_idx,
                },
                pipeline_delete_params.PipelineDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def add(
        self,
        *,
        url: str,
        url_idx: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Add Pipeline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/pipelines/add",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "url_idx": url_idx,
                },
                pipeline_add_params.PipelineAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get(
        self,
        *,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Pipelines

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/pipelines/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url_idx": url_idx}, pipeline_get_params.PipelineGetParams),
            ),
            cast_to=object,
        )

    async def upload(
        self,
        *,
        file: FileTypes,
        url_idx: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Upload Pipeline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "url_idx": url_idx,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/pipelines/upload",
            body=await async_maybe_transform(body, pipeline_upload_params.PipelineUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class PipelinesResourceWithRawResponse:
    def __init__(self, pipelines: PipelinesResource) -> None:
        self._pipelines = pipelines

        self.list = to_raw_response_wrapper(
            pipelines.list,
        )
        self.delete = to_raw_response_wrapper(
            pipelines.delete,
        )
        self.add = to_raw_response_wrapper(
            pipelines.add,
        )
        self.get = to_raw_response_wrapper(
            pipelines.get,
        )
        self.upload = to_raw_response_wrapper(
            pipelines.upload,
        )

    @cached_property
    def valves(self) -> ValvesResourceWithRawResponse:
        return ValvesResourceWithRawResponse(self._pipelines.valves)


class AsyncPipelinesResourceWithRawResponse:
    def __init__(self, pipelines: AsyncPipelinesResource) -> None:
        self._pipelines = pipelines

        self.list = async_to_raw_response_wrapper(
            pipelines.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pipelines.delete,
        )
        self.add = async_to_raw_response_wrapper(
            pipelines.add,
        )
        self.get = async_to_raw_response_wrapper(
            pipelines.get,
        )
        self.upload = async_to_raw_response_wrapper(
            pipelines.upload,
        )

    @cached_property
    def valves(self) -> AsyncValvesResourceWithRawResponse:
        return AsyncValvesResourceWithRawResponse(self._pipelines.valves)


class PipelinesResourceWithStreamingResponse:
    def __init__(self, pipelines: PipelinesResource) -> None:
        self._pipelines = pipelines

        self.list = to_streamed_response_wrapper(
            pipelines.list,
        )
        self.delete = to_streamed_response_wrapper(
            pipelines.delete,
        )
        self.add = to_streamed_response_wrapper(
            pipelines.add,
        )
        self.get = to_streamed_response_wrapper(
            pipelines.get,
        )
        self.upload = to_streamed_response_wrapper(
            pipelines.upload,
        )

    @cached_property
    def valves(self) -> ValvesResourceWithStreamingResponse:
        return ValvesResourceWithStreamingResponse(self._pipelines.valves)


class AsyncPipelinesResourceWithStreamingResponse:
    def __init__(self, pipelines: AsyncPipelinesResource) -> None:
        self._pipelines = pipelines

        self.list = async_to_streamed_response_wrapper(
            pipelines.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pipelines.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            pipelines.add,
        )
        self.get = async_to_streamed_response_wrapper(
            pipelines.get,
        )
        self.upload = async_to_streamed_response_wrapper(
            pipelines.upload,
        )

    @cached_property
    def valves(self) -> AsyncValvesResourceWithStreamingResponse:
        return AsyncValvesResourceWithStreamingResponse(self._pipelines.valves)
