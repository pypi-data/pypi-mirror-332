# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .update import (
    UpdateResource,
    AsyncUpdateResource,
    UpdateResourceWithRawResponse,
    AsyncUpdateResourceWithRawResponse,
    UpdateResourceWithStreamingResponse,
    AsyncUpdateResourceWithStreamingResponse,
)
from .api_key import (
    APIKeyResource,
    AsyncAPIKeyResource,
    APIKeyResourceWithRawResponse,
    AsyncAPIKeyResourceWithRawResponse,
    APIKeyResourceWithStreamingResponse,
    AsyncAPIKeyResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from .admin.admin import (
    AdminResource,
    AsyncAdminResource,
    AdminResourceWithRawResponse,
    AsyncAdminResourceWithRawResponse,
    AdminResourceWithStreamingResponse,
    AsyncAdminResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1 import auth_signin_params, auth_signup_params, auth_add_user_params, auth_ldap_auth_params
from .....types.signin_response import SigninResponse
from .....types.api.v1.auth_signin_response import AuthSigninResponse
from .....types.api.v1.auth_signup_response import AuthSignupResponse
from .....types.api.v1.auth_ldap_auth_response import AuthLdapAuthResponse
from .....types.api.v1.auth_get_session_user_response import AuthGetSessionUserResponse

__all__ = ["AuthsResource", "AsyncAuthsResource"]


class AuthsResource(SyncAPIResource):
    @cached_property
    def update(self) -> UpdateResource:
        return UpdateResource(self._client)

    @cached_property
    def admin(self) -> AdminResource:
        return AdminResource(self._client)

    @cached_property
    def api_key(self) -> APIKeyResource:
        return APIKeyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AuthsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AuthsResourceWithStreamingResponse(self)

    def add_user(
        self,
        *,
        email: str,
        name: str,
        password: str,
        profile_image_url: Optional[str] | NotGiven = NOT_GIVEN,
        role: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SigninResponse:
        """
        Add User

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auths/add",
            body=maybe_transform(
                {
                    "email": email,
                    "name": name,
                    "password": password,
                    "profile_image_url": profile_image_url,
                    "role": role,
                },
                auth_add_user_params.AuthAddUserParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SigninResponse,
        )

    def get_session_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthGetSessionUserResponse:
        """Get Session User"""
        return self._get(
            "/api/v1/auths/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthGetSessionUserResponse,
        )

    def ldap_auth(
        self,
        *,
        password: str,
        user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthLdapAuthResponse:
        """
        Ldap Auth

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auths/ldap",
            body=maybe_transform(
                {
                    "password": password,
                    "user": user,
                },
                auth_ldap_auth_params.AuthLdapAuthParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthLdapAuthResponse,
        )

    def signin(
        self,
        *,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthSigninResponse:
        """
        Signin

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auths/signin",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                },
                auth_signin_params.AuthSigninParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthSigninResponse,
        )

    def signout(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Signout"""
        return self._get(
            "/api/v1/auths/signout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def signup(
        self,
        *,
        email: str,
        name: str,
        password: str,
        profile_image_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthSignupResponse:
        """
        Signup

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auths/signup",
            body=maybe_transform(
                {
                    "email": email,
                    "name": name,
                    "password": password,
                    "profile_image_url": profile_image_url,
                },
                auth_signup_params.AuthSignupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthSignupResponse,
        )


class AsyncAuthsResource(AsyncAPIResource):
    @cached_property
    def update(self) -> AsyncUpdateResource:
        return AsyncUpdateResource(self._client)

    @cached_property
    def admin(self) -> AsyncAdminResource:
        return AsyncAdminResource(self._client)

    @cached_property
    def api_key(self) -> AsyncAPIKeyResource:
        return AsyncAPIKeyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncAuthsResourceWithStreamingResponse(self)

    async def add_user(
        self,
        *,
        email: str,
        name: str,
        password: str,
        profile_image_url: Optional[str] | NotGiven = NOT_GIVEN,
        role: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SigninResponse:
        """
        Add User

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auths/add",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "name": name,
                    "password": password,
                    "profile_image_url": profile_image_url,
                    "role": role,
                },
                auth_add_user_params.AuthAddUserParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SigninResponse,
        )

    async def get_session_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthGetSessionUserResponse:
        """Get Session User"""
        return await self._get(
            "/api/v1/auths/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthGetSessionUserResponse,
        )

    async def ldap_auth(
        self,
        *,
        password: str,
        user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthLdapAuthResponse:
        """
        Ldap Auth

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auths/ldap",
            body=await async_maybe_transform(
                {
                    "password": password,
                    "user": user,
                },
                auth_ldap_auth_params.AuthLdapAuthParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthLdapAuthResponse,
        )

    async def signin(
        self,
        *,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthSigninResponse:
        """
        Signin

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auths/signin",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                },
                auth_signin_params.AuthSigninParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthSigninResponse,
        )

    async def signout(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Signout"""
        return await self._get(
            "/api/v1/auths/signout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def signup(
        self,
        *,
        email: str,
        name: str,
        password: str,
        profile_image_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthSignupResponse:
        """
        Signup

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auths/signup",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "name": name,
                    "password": password,
                    "profile_image_url": profile_image_url,
                },
                auth_signup_params.AuthSignupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthSignupResponse,
        )


class AuthsResourceWithRawResponse:
    def __init__(self, auths: AuthsResource) -> None:
        self._auths = auths

        self.add_user = to_raw_response_wrapper(
            auths.add_user,
        )
        self.get_session_user = to_raw_response_wrapper(
            auths.get_session_user,
        )
        self.ldap_auth = to_raw_response_wrapper(
            auths.ldap_auth,
        )
        self.signin = to_raw_response_wrapper(
            auths.signin,
        )
        self.signout = to_raw_response_wrapper(
            auths.signout,
        )
        self.signup = to_raw_response_wrapper(
            auths.signup,
        )

    @cached_property
    def update(self) -> UpdateResourceWithRawResponse:
        return UpdateResourceWithRawResponse(self._auths.update)

    @cached_property
    def admin(self) -> AdminResourceWithRawResponse:
        return AdminResourceWithRawResponse(self._auths.admin)

    @cached_property
    def api_key(self) -> APIKeyResourceWithRawResponse:
        return APIKeyResourceWithRawResponse(self._auths.api_key)


class AsyncAuthsResourceWithRawResponse:
    def __init__(self, auths: AsyncAuthsResource) -> None:
        self._auths = auths

        self.add_user = async_to_raw_response_wrapper(
            auths.add_user,
        )
        self.get_session_user = async_to_raw_response_wrapper(
            auths.get_session_user,
        )
        self.ldap_auth = async_to_raw_response_wrapper(
            auths.ldap_auth,
        )
        self.signin = async_to_raw_response_wrapper(
            auths.signin,
        )
        self.signout = async_to_raw_response_wrapper(
            auths.signout,
        )
        self.signup = async_to_raw_response_wrapper(
            auths.signup,
        )

    @cached_property
    def update(self) -> AsyncUpdateResourceWithRawResponse:
        return AsyncUpdateResourceWithRawResponse(self._auths.update)

    @cached_property
    def admin(self) -> AsyncAdminResourceWithRawResponse:
        return AsyncAdminResourceWithRawResponse(self._auths.admin)

    @cached_property
    def api_key(self) -> AsyncAPIKeyResourceWithRawResponse:
        return AsyncAPIKeyResourceWithRawResponse(self._auths.api_key)


class AuthsResourceWithStreamingResponse:
    def __init__(self, auths: AuthsResource) -> None:
        self._auths = auths

        self.add_user = to_streamed_response_wrapper(
            auths.add_user,
        )
        self.get_session_user = to_streamed_response_wrapper(
            auths.get_session_user,
        )
        self.ldap_auth = to_streamed_response_wrapper(
            auths.ldap_auth,
        )
        self.signin = to_streamed_response_wrapper(
            auths.signin,
        )
        self.signout = to_streamed_response_wrapper(
            auths.signout,
        )
        self.signup = to_streamed_response_wrapper(
            auths.signup,
        )

    @cached_property
    def update(self) -> UpdateResourceWithStreamingResponse:
        return UpdateResourceWithStreamingResponse(self._auths.update)

    @cached_property
    def admin(self) -> AdminResourceWithStreamingResponse:
        return AdminResourceWithStreamingResponse(self._auths.admin)

    @cached_property
    def api_key(self) -> APIKeyResourceWithStreamingResponse:
        return APIKeyResourceWithStreamingResponse(self._auths.api_key)


class AsyncAuthsResourceWithStreamingResponse:
    def __init__(self, auths: AsyncAuthsResource) -> None:
        self._auths = auths

        self.add_user = async_to_streamed_response_wrapper(
            auths.add_user,
        )
        self.get_session_user = async_to_streamed_response_wrapper(
            auths.get_session_user,
        )
        self.ldap_auth = async_to_streamed_response_wrapper(
            auths.ldap_auth,
        )
        self.signin = async_to_streamed_response_wrapper(
            auths.signin,
        )
        self.signout = async_to_streamed_response_wrapper(
            auths.signout,
        )
        self.signup = async_to_streamed_response_wrapper(
            auths.signup,
        )

    @cached_property
    def update(self) -> AsyncUpdateResourceWithStreamingResponse:
        return AsyncUpdateResourceWithStreamingResponse(self._auths.update)

    @cached_property
    def admin(self) -> AsyncAdminResourceWithStreamingResponse:
        return AsyncAdminResourceWithStreamingResponse(self._auths.admin)

    @cached_property
    def api_key(self) -> AsyncAPIKeyResourceWithStreamingResponse:
        return AsyncAPIKeyResourceWithStreamingResponse(self._auths.api_key)
