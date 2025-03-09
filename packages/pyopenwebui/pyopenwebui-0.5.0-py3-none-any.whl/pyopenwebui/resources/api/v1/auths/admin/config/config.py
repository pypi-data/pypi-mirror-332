# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .ldap.ldap import (
    LdapResource,
    AsyncLdapResource,
    LdapResourceWithRawResponse,
    AsyncLdapResourceWithRawResponse,
    LdapResourceWithStreamingResponse,
    AsyncLdapResourceWithStreamingResponse,
)
from ......._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......._compat import cached_property
from ......._resource import SyncAPIResource, AsyncAPIResource
from ......._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......._base_client import make_request_options
from .......types.api.v1.auths.admin import config_update_params

__all__ = ["ConfigResource", "AsyncConfigResource"]


class ConfigResource(SyncAPIResource):
    @cached_property
    def ldap(self) -> LdapResource:
        return LdapResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ConfigResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        api_key_allowed_endpoints: str,
        default_user_role: str,
        enable_api_key: bool,
        enable_api_key_endpoint_restrictions: bool,
        enable_channels: bool,
        enable_community_sharing: bool,
        enable_message_rating: bool,
        enable_signup: bool,
        jwt_expires_in: str,
        show_admin_details: bool,
        webui_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Admin Config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auths/admin/config",
            body=maybe_transform(
                {
                    "api_key_allowed_endpoints": api_key_allowed_endpoints,
                    "default_user_role": default_user_role,
                    "enable_api_key": enable_api_key,
                    "enable_api_key_endpoint_restrictions": enable_api_key_endpoint_restrictions,
                    "enable_channels": enable_channels,
                    "enable_community_sharing": enable_community_sharing,
                    "enable_message_rating": enable_message_rating,
                    "enable_signup": enable_signup,
                    "jwt_expires_in": jwt_expires_in,
                    "show_admin_details": show_admin_details,
                    "webui_url": webui_url,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Admin Config"""
        return self._get(
            "/api/v1/auths/admin/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncConfigResource(AsyncAPIResource):
    @cached_property
    def ldap(self) -> AsyncLdapResource:
        return AsyncLdapResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncConfigResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        api_key_allowed_endpoints: str,
        default_user_role: str,
        enable_api_key: bool,
        enable_api_key_endpoint_restrictions: bool,
        enable_channels: bool,
        enable_community_sharing: bool,
        enable_message_rating: bool,
        enable_signup: bool,
        jwt_expires_in: str,
        show_admin_details: bool,
        webui_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Admin Config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auths/admin/config",
            body=await async_maybe_transform(
                {
                    "api_key_allowed_endpoints": api_key_allowed_endpoints,
                    "default_user_role": default_user_role,
                    "enable_api_key": enable_api_key,
                    "enable_api_key_endpoint_restrictions": enable_api_key_endpoint_restrictions,
                    "enable_channels": enable_channels,
                    "enable_community_sharing": enable_community_sharing,
                    "enable_message_rating": enable_message_rating,
                    "enable_signup": enable_signup,
                    "jwt_expires_in": jwt_expires_in,
                    "show_admin_details": show_admin_details,
                    "webui_url": webui_url,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Admin Config"""
        return await self._get(
            "/api/v1/auths/admin/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ConfigResourceWithRawResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.update = to_raw_response_wrapper(
            config.update,
        )
        self.get = to_raw_response_wrapper(
            config.get,
        )

    @cached_property
    def ldap(self) -> LdapResourceWithRawResponse:
        return LdapResourceWithRawResponse(self._config.ldap)


class AsyncConfigResourceWithRawResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.update = async_to_raw_response_wrapper(
            config.update,
        )
        self.get = async_to_raw_response_wrapper(
            config.get,
        )

    @cached_property
    def ldap(self) -> AsyncLdapResourceWithRawResponse:
        return AsyncLdapResourceWithRawResponse(self._config.ldap)


class ConfigResourceWithStreamingResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.update = to_streamed_response_wrapper(
            config.update,
        )
        self.get = to_streamed_response_wrapper(
            config.get,
        )

    @cached_property
    def ldap(self) -> LdapResourceWithStreamingResponse:
        return LdapResourceWithStreamingResponse(self._config.ldap)


class AsyncConfigResourceWithStreamingResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.update = async_to_streamed_response_wrapper(
            config.update,
        )
        self.get = async_to_streamed_response_wrapper(
            config.get,
        )

    @cached_property
    def ldap(self) -> AsyncLdapResourceWithStreamingResponse:
        return AsyncLdapResourceWithStreamingResponse(self._config.ldap)
