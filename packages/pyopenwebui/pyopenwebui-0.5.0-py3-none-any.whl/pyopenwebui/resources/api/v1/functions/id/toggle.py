# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.function_model import FunctionModel

__all__ = ["ToggleResource", "AsyncToggleResource"]


class ToggleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToggleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ToggleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToggleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ToggleResourceWithStreamingResponse(self)

    def global_(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FunctionModel]:
        """
        Toggle Global By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/functions/id/{id}/toggle/global",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionModel,
        )


class AsyncToggleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToggleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToggleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToggleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncToggleResourceWithStreamingResponse(self)

    async def global_(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FunctionModel]:
        """
        Toggle Global By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/functions/id/{id}/toggle/global",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionModel,
        )


class ToggleResourceWithRawResponse:
    def __init__(self, toggle: ToggleResource) -> None:
        self._toggle = toggle

        self.global_ = to_raw_response_wrapper(
            toggle.global_,
        )


class AsyncToggleResourceWithRawResponse:
    def __init__(self, toggle: AsyncToggleResource) -> None:
        self._toggle = toggle

        self.global_ = async_to_raw_response_wrapper(
            toggle.global_,
        )


class ToggleResourceWithStreamingResponse:
    def __init__(self, toggle: ToggleResource) -> None:
        self._toggle = toggle

        self.global_ = to_streamed_response_wrapper(
            toggle.global_,
        )


class AsyncToggleResourceWithStreamingResponse:
    def __init__(self, toggle: AsyncToggleResource) -> None:
        self._toggle = toggle

        self.global_ = async_to_streamed_response_wrapper(
            toggle.global_,
        )
