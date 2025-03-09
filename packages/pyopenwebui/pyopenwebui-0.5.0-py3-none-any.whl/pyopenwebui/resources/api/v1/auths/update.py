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
from .....types.api.v1.auths import update_profile_params, update_password_params
from .....types.api.v1.auths.update_profile_response import UpdateProfileResponse
from .....types.api.v1.auths.update_password_response import UpdatePasswordResponse

__all__ = ["UpdateResource", "AsyncUpdateResource"]


class UpdateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UpdateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return UpdateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UpdateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return UpdateResourceWithStreamingResponse(self)

    def password(
        self,
        *,
        new_password: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpdatePasswordResponse:
        """
        Update Password

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auths/update/password",
            body=maybe_transform(
                {
                    "new_password": new_password,
                    "password": password,
                },
                update_password_params.UpdatePasswordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdatePasswordResponse,
        )

    def profile(
        self,
        *,
        name: str,
        profile_image_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpdateProfileResponse:
        """
        Update Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auths/update/profile",
            body=maybe_transform(
                {
                    "name": name,
                    "profile_image_url": profile_image_url,
                },
                update_profile_params.UpdateProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateProfileResponse,
        )


class AsyncUpdateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUpdateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUpdateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUpdateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncUpdateResourceWithStreamingResponse(self)

    async def password(
        self,
        *,
        new_password: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpdatePasswordResponse:
        """
        Update Password

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auths/update/password",
            body=await async_maybe_transform(
                {
                    "new_password": new_password,
                    "password": password,
                },
                update_password_params.UpdatePasswordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdatePasswordResponse,
        )

    async def profile(
        self,
        *,
        name: str,
        profile_image_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpdateProfileResponse:
        """
        Update Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auths/update/profile",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "profile_image_url": profile_image_url,
                },
                update_profile_params.UpdateProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateProfileResponse,
        )


class UpdateResourceWithRawResponse:
    def __init__(self, update: UpdateResource) -> None:
        self._update = update

        self.password = to_raw_response_wrapper(
            update.password,
        )
        self.profile = to_raw_response_wrapper(
            update.profile,
        )


class AsyncUpdateResourceWithRawResponse:
    def __init__(self, update: AsyncUpdateResource) -> None:
        self._update = update

        self.password = async_to_raw_response_wrapper(
            update.password,
        )
        self.profile = async_to_raw_response_wrapper(
            update.profile,
        )


class UpdateResourceWithStreamingResponse:
    def __init__(self, update: UpdateResource) -> None:
        self._update = update

        self.password = to_streamed_response_wrapper(
            update.password,
        )
        self.profile = to_streamed_response_wrapper(
            update.profile,
        )


class AsyncUpdateResourceWithStreamingResponse:
    def __init__(self, update: AsyncUpdateResource) -> None:
        self._update = update

        self.password = async_to_streamed_response_wrapper(
            update.password,
        )
        self.profile = async_to_streamed_response_wrapper(
            update.profile,
        )
