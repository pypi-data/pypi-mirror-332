# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .v1.v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from .config import (
    ConfigResource,
    AsyncConfigResource,
    ConfigResourceWithRawResponse,
    AsyncConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
    AsyncConfigResourceWithStreamingResponse,
)
from ...types import ollama_verify_connection_params
from .api.api import (
    APIResource,
    AsyncAPIResource,
    APIResourceWithRawResponse,
    AsyncAPIResourceWithRawResponse,
    APIResourceWithStreamingResponse,
    AsyncAPIResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .models.models import (
    ModelsResource,
    AsyncModelsResource,
    ModelsResourceWithRawResponse,
    AsyncModelsResourceWithRawResponse,
    ModelsResourceWithStreamingResponse,
    AsyncModelsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options

__all__ = ["OllamaResource", "AsyncOllamaResource"]


class OllamaResource(SyncAPIResource):
    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def api(self) -> APIResource:
        return APIResource(self._client)

    @cached_property
    def v1(self) -> V1Resource:
        return V1Resource(self._client)

    @cached_property
    def models(self) -> ModelsResource:
        return ModelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OllamaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return OllamaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OllamaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return OllamaResourceWithStreamingResponse(self)

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
            "/ollama/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def verify_connection(
        self,
        *,
        url: str,
        key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Verify Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ollama/verify",
            body=maybe_transform(
                {
                    "url": url,
                    "key": key,
                },
                ollama_verify_connection_params.OllamaVerifyConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncOllamaResource(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def api(self) -> AsyncAPIResource:
        return AsyncAPIResource(self._client)

    @cached_property
    def v1(self) -> AsyncV1Resource:
        return AsyncV1Resource(self._client)

    @cached_property
    def models(self) -> AsyncModelsResource:
        return AsyncModelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOllamaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOllamaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOllamaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncOllamaResourceWithStreamingResponse(self)

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
            "/ollama/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def verify_connection(
        self,
        *,
        url: str,
        key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Verify Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ollama/verify",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "key": key,
                },
                ollama_verify_connection_params.OllamaVerifyConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class OllamaResourceWithRawResponse:
    def __init__(self, ollama: OllamaResource) -> None:
        self._ollama = ollama

        self.get_status = to_raw_response_wrapper(
            ollama.get_status,
        )
        self.verify_connection = to_raw_response_wrapper(
            ollama.verify_connection,
        )

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._ollama.config)

    @cached_property
    def api(self) -> APIResourceWithRawResponse:
        return APIResourceWithRawResponse(self._ollama.api)

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        return V1ResourceWithRawResponse(self._ollama.v1)

    @cached_property
    def models(self) -> ModelsResourceWithRawResponse:
        return ModelsResourceWithRawResponse(self._ollama.models)


class AsyncOllamaResourceWithRawResponse:
    def __init__(self, ollama: AsyncOllamaResource) -> None:
        self._ollama = ollama

        self.get_status = async_to_raw_response_wrapper(
            ollama.get_status,
        )
        self.verify_connection = async_to_raw_response_wrapper(
            ollama.verify_connection,
        )

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._ollama.config)

    @cached_property
    def api(self) -> AsyncAPIResourceWithRawResponse:
        return AsyncAPIResourceWithRawResponse(self._ollama.api)

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        return AsyncV1ResourceWithRawResponse(self._ollama.v1)

    @cached_property
    def models(self) -> AsyncModelsResourceWithRawResponse:
        return AsyncModelsResourceWithRawResponse(self._ollama.models)


class OllamaResourceWithStreamingResponse:
    def __init__(self, ollama: OllamaResource) -> None:
        self._ollama = ollama

        self.get_status = to_streamed_response_wrapper(
            ollama.get_status,
        )
        self.verify_connection = to_streamed_response_wrapper(
            ollama.verify_connection,
        )

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._ollama.config)

    @cached_property
    def api(self) -> APIResourceWithStreamingResponse:
        return APIResourceWithStreamingResponse(self._ollama.api)

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        return V1ResourceWithStreamingResponse(self._ollama.v1)

    @cached_property
    def models(self) -> ModelsResourceWithStreamingResponse:
        return ModelsResourceWithStreamingResponse(self._ollama.models)


class AsyncOllamaResourceWithStreamingResponse:
    def __init__(self, ollama: AsyncOllamaResource) -> None:
        self._ollama = ollama

        self.get_status = async_to_streamed_response_wrapper(
            ollama.get_status,
        )
        self.verify_connection = async_to_streamed_response_wrapper(
            ollama.verify_connection,
        )

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._ollama.config)

    @cached_property
    def api(self) -> AsyncAPIResourceWithStreamingResponse:
        return AsyncAPIResourceWithStreamingResponse(self._ollama.api)

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        return AsyncV1ResourceWithStreamingResponse(self._ollama.v1)

    @cached_property
    def models(self) -> AsyncModelsResourceWithStreamingResponse:
        return AsyncModelsResourceWithStreamingResponse(self._ollama.models)
