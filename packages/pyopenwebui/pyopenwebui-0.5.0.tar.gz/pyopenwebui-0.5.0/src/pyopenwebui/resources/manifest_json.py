# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["ManifestJsonResource", "AsyncManifestJsonResource"]


class ManifestJsonResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ManifestJsonResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ManifestJsonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManifestJsonResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ManifestJsonResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Manifest Json"""
        return self._get(
            "/manifest.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncManifestJsonResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncManifestJsonResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncManifestJsonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManifestJsonResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncManifestJsonResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Manifest Json"""
        return await self._get(
            "/manifest.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ManifestJsonResourceWithRawResponse:
    def __init__(self, manifest_json: ManifestJsonResource) -> None:
        self._manifest_json = manifest_json

        self.retrieve = to_raw_response_wrapper(
            manifest_json.retrieve,
        )


class AsyncManifestJsonResourceWithRawResponse:
    def __init__(self, manifest_json: AsyncManifestJsonResource) -> None:
        self._manifest_json = manifest_json

        self.retrieve = async_to_raw_response_wrapper(
            manifest_json.retrieve,
        )


class ManifestJsonResourceWithStreamingResponse:
    def __init__(self, manifest_json: ManifestJsonResource) -> None:
        self._manifest_json = manifest_json

        self.retrieve = to_streamed_response_wrapper(
            manifest_json.retrieve,
        )


class AsyncManifestJsonResourceWithStreamingResponse:
    def __init__(self, manifest_json: AsyncManifestJsonResource) -> None:
        self._manifest_json = manifest_json

        self.retrieve = async_to_streamed_response_wrapper(
            manifest_json.retrieve,
        )
