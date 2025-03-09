# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .server import (
    ServerResource,
    AsyncServerResource,
    ServerResourceWithRawResponse,
    AsyncServerResourceWithRawResponse,
    ServerResourceWithStreamingResponse,
    AsyncServerResourceWithStreamingResponse,
)
from ........_types import (
    NOT_GIVEN,
    Body,
    Query,
    Headers,
    NotGiven,
)
from ........_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ........_compat import cached_property
from ........_resource import SyncAPIResource, AsyncAPIResource
from ........_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ........_base_client import make_request_options
from ........types.api.v1.auths.admin.config import ldap_update_params

__all__ = ["LdapResource", "AsyncLdapResource"]


class LdapResource(SyncAPIResource):
    @cached_property
    def server(self) -> ServerResource:
        return ServerResource(self._client)

    @cached_property
    def with_raw_response(self) -> LdapResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return LdapResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LdapResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return LdapResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        enable_ldap: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Ldap Config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auths/admin/config/ldap",
            body=maybe_transform({"enable_ldap": enable_ldap}, ldap_update_params.LdapUpdateParams),
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
        """Get Ldap Config"""
        return self._get(
            "/api/v1/auths/admin/config/ldap",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncLdapResource(AsyncAPIResource):
    @cached_property
    def server(self) -> AsyncServerResource:
        return AsyncServerResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLdapResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLdapResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLdapResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncLdapResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        enable_ldap: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Ldap Config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auths/admin/config/ldap",
            body=await async_maybe_transform({"enable_ldap": enable_ldap}, ldap_update_params.LdapUpdateParams),
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
        """Get Ldap Config"""
        return await self._get(
            "/api/v1/auths/admin/config/ldap",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class LdapResourceWithRawResponse:
    def __init__(self, ldap: LdapResource) -> None:
        self._ldap = ldap

        self.update = to_raw_response_wrapper(
            ldap.update,
        )
        self.get = to_raw_response_wrapper(
            ldap.get,
        )

    @cached_property
    def server(self) -> ServerResourceWithRawResponse:
        return ServerResourceWithRawResponse(self._ldap.server)


class AsyncLdapResourceWithRawResponse:
    def __init__(self, ldap: AsyncLdapResource) -> None:
        self._ldap = ldap

        self.update = async_to_raw_response_wrapper(
            ldap.update,
        )
        self.get = async_to_raw_response_wrapper(
            ldap.get,
        )

    @cached_property
    def server(self) -> AsyncServerResourceWithRawResponse:
        return AsyncServerResourceWithRawResponse(self._ldap.server)


class LdapResourceWithStreamingResponse:
    def __init__(self, ldap: LdapResource) -> None:
        self._ldap = ldap

        self.update = to_streamed_response_wrapper(
            ldap.update,
        )
        self.get = to_streamed_response_wrapper(
            ldap.get,
        )

    @cached_property
    def server(self) -> ServerResourceWithStreamingResponse:
        return ServerResourceWithStreamingResponse(self._ldap.server)


class AsyncLdapResourceWithStreamingResponse:
    def __init__(self, ldap: AsyncLdapResource) -> None:
        self._ldap = ldap

        self.update = async_to_streamed_response_wrapper(
            ldap.update,
        )
        self.get = async_to_streamed_response_wrapper(
            ldap.get,
        )

    @cached_property
    def server(self) -> AsyncServerResourceWithStreamingResponse:
        return AsyncServerResourceWithStreamingResponse(self._ldap.server)
