# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from .....types.api.v1.configs import banner_set_params
from .....types.configs.banner_model_param import BannerModelParam
from .....types.api.v1.configs.banner_get_response import BannerGetResponse
from .....types.api.v1.configs.banner_set_response import BannerSetResponse

__all__ = ["BannersResource", "AsyncBannersResource"]


class BannersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BannersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return BannersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BannersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return BannersResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BannerGetResponse:
        """Get Banners"""
        return self._get(
            "/api/v1/configs/banners",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BannerGetResponse,
        )

    def set(
        self,
        *,
        banners: Iterable[BannerModelParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BannerSetResponse:
        """
        Set Banners

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/configs/banners",
            body=maybe_transform({"banners": banners}, banner_set_params.BannerSetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BannerSetResponse,
        )


class AsyncBannersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBannersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBannersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBannersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncBannersResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BannerGetResponse:
        """Get Banners"""
        return await self._get(
            "/api/v1/configs/banners",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BannerGetResponse,
        )

    async def set(
        self,
        *,
        banners: Iterable[BannerModelParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BannerSetResponse:
        """
        Set Banners

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/configs/banners",
            body=await async_maybe_transform({"banners": banners}, banner_set_params.BannerSetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BannerSetResponse,
        )


class BannersResourceWithRawResponse:
    def __init__(self, banners: BannersResource) -> None:
        self._banners = banners

        self.get = to_raw_response_wrapper(
            banners.get,
        )
        self.set = to_raw_response_wrapper(
            banners.set,
        )


class AsyncBannersResourceWithRawResponse:
    def __init__(self, banners: AsyncBannersResource) -> None:
        self._banners = banners

        self.get = async_to_raw_response_wrapper(
            banners.get,
        )
        self.set = async_to_raw_response_wrapper(
            banners.set,
        )


class BannersResourceWithStreamingResponse:
    def __init__(self, banners: BannersResource) -> None:
        self._banners = banners

        self.get = to_streamed_response_wrapper(
            banners.get,
        )
        self.set = to_streamed_response_wrapper(
            banners.set,
        )


class AsyncBannersResourceWithStreamingResponse:
    def __init__(self, banners: AsyncBannersResource) -> None:
        self._banners = banners

        self.get = async_to_streamed_response_wrapper(
            banners.get,
        )
        self.set = async_to_streamed_response_wrapper(
            banners.set,
        )
