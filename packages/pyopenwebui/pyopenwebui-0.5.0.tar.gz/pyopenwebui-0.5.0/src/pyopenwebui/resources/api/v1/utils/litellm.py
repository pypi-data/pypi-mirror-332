# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options

__all__ = ["LitellmResource", "AsyncLitellmResource"]


class LitellmResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LitellmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return LitellmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LitellmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return LitellmResourceWithStreamingResponse(self)

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
        """Download Litellm Config Yaml"""
        return self._get(
            "/api/v1/utils/litellm/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncLitellmResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLitellmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLitellmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLitellmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncLitellmResourceWithStreamingResponse(self)

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
        """Download Litellm Config Yaml"""
        return await self._get(
            "/api/v1/utils/litellm/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class LitellmResourceWithRawResponse:
    def __init__(self, litellm: LitellmResource) -> None:
        self._litellm = litellm

        self.get_config = to_raw_response_wrapper(
            litellm.get_config,
        )


class AsyncLitellmResourceWithRawResponse:
    def __init__(self, litellm: AsyncLitellmResource) -> None:
        self._litellm = litellm

        self.get_config = async_to_raw_response_wrapper(
            litellm.get_config,
        )


class LitellmResourceWithStreamingResponse:
    def __init__(self, litellm: LitellmResource) -> None:
        self._litellm = litellm

        self.get_config = to_streamed_response_wrapper(
            litellm.get_config,
        )


class AsyncLitellmResourceWithStreamingResponse:
    def __init__(self, litellm: AsyncLitellmResource) -> None:
        self._litellm = litellm

        self.get_config = async_to_streamed_response_wrapper(
            litellm.get_config,
        )
