# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

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
from ........types.api.v1.auths.admin.config.ldap import server_update_params
from ........types.api.v1.auths.admin.config.ldap.server_get_response import ServerGetResponse

__all__ = ["ServerResource", "AsyncServerResource"]


class ServerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ServerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ServerResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        app_dn: str,
        app_dn_password: str,
        host: str,
        label: str,
        search_base: str,
        attribute_for_mail: str | NotGiven = NOT_GIVEN,
        attribute_for_username: str | NotGiven = NOT_GIVEN,
        certificate_path: Optional[str] | NotGiven = NOT_GIVEN,
        ciphers: Optional[str] | NotGiven = NOT_GIVEN,
        port: Optional[int] | NotGiven = NOT_GIVEN,
        search_filters: str | NotGiven = NOT_GIVEN,
        use_tls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Ldap Server

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auths/admin/config/ldap/server",
            body=maybe_transform(
                {
                    "app_dn": app_dn,
                    "app_dn_password": app_dn_password,
                    "host": host,
                    "label": label,
                    "search_base": search_base,
                    "attribute_for_mail": attribute_for_mail,
                    "attribute_for_username": attribute_for_username,
                    "certificate_path": certificate_path,
                    "ciphers": ciphers,
                    "port": port,
                    "search_filters": search_filters,
                    "use_tls": use_tls,
                },
                server_update_params.ServerUpdateParams,
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
    ) -> ServerGetResponse:
        """Get Ldap Server"""
        return self._get(
            "/api/v1/auths/admin/config/ldap/server",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerGetResponse,
        )


class AsyncServerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncServerResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        app_dn: str,
        app_dn_password: str,
        host: str,
        label: str,
        search_base: str,
        attribute_for_mail: str | NotGiven = NOT_GIVEN,
        attribute_for_username: str | NotGiven = NOT_GIVEN,
        certificate_path: Optional[str] | NotGiven = NOT_GIVEN,
        ciphers: Optional[str] | NotGiven = NOT_GIVEN,
        port: Optional[int] | NotGiven = NOT_GIVEN,
        search_filters: str | NotGiven = NOT_GIVEN,
        use_tls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Ldap Server

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auths/admin/config/ldap/server",
            body=await async_maybe_transform(
                {
                    "app_dn": app_dn,
                    "app_dn_password": app_dn_password,
                    "host": host,
                    "label": label,
                    "search_base": search_base,
                    "attribute_for_mail": attribute_for_mail,
                    "attribute_for_username": attribute_for_username,
                    "certificate_path": certificate_path,
                    "ciphers": ciphers,
                    "port": port,
                    "search_filters": search_filters,
                    "use_tls": use_tls,
                },
                server_update_params.ServerUpdateParams,
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
    ) -> ServerGetResponse:
        """Get Ldap Server"""
        return await self._get(
            "/api/v1/auths/admin/config/ldap/server",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerGetResponse,
        )


class ServerResourceWithRawResponse:
    def __init__(self, server: ServerResource) -> None:
        self._server = server

        self.update = to_raw_response_wrapper(
            server.update,
        )
        self.get = to_raw_response_wrapper(
            server.get,
        )


class AsyncServerResourceWithRawResponse:
    def __init__(self, server: AsyncServerResource) -> None:
        self._server = server

        self.update = async_to_raw_response_wrapper(
            server.update,
        )
        self.get = async_to_raw_response_wrapper(
            server.get,
        )


class ServerResourceWithStreamingResponse:
    def __init__(self, server: ServerResource) -> None:
        self._server = server

        self.update = to_streamed_response_wrapper(
            server.update,
        )
        self.get = to_streamed_response_wrapper(
            server.get,
        )


class AsyncServerResourceWithStreamingResponse:
    def __init__(self, server: AsyncServerResource) -> None:
        self._server = server

        self.update = async_to_streamed_response_wrapper(
            server.update,
        )
        self.get = async_to_streamed_response_wrapper(
            server.get,
        )
