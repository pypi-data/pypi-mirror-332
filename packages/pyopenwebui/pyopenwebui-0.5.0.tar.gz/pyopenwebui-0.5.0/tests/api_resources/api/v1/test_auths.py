# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types import SigninResponse
from pyopenwebui.types.api.v1 import (
    AuthSigninResponse,
    AuthSignupResponse,
    AuthLdapAuthResponse,
    AuthGetSessionUserResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuths:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add_user(self, client: Pyopenwebui) -> None:
        auth = client.api.v1.auths.add_user(
            email="email",
            name="name",
            password="password",
        )
        assert_matches_type(SigninResponse, auth, path=["response"])

    @parametrize
    def test_method_add_user_with_all_params(self, client: Pyopenwebui) -> None:
        auth = client.api.v1.auths.add_user(
            email="email",
            name="name",
            password="password",
            profile_image_url="profile_image_url",
            role="role",
        )
        assert_matches_type(SigninResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_add_user(self, client: Pyopenwebui) -> None:
        response = client.api.v1.auths.with_raw_response.add_user(
            email="email",
            name="name",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(SigninResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_add_user(self, client: Pyopenwebui) -> None:
        with client.api.v1.auths.with_streaming_response.add_user(
            email="email",
            name="name",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(SigninResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_session_user(self, client: Pyopenwebui) -> None:
        auth = client.api.v1.auths.get_session_user()
        assert_matches_type(AuthGetSessionUserResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_get_session_user(self, client: Pyopenwebui) -> None:
        response = client.api.v1.auths.with_raw_response.get_session_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthGetSessionUserResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_get_session_user(self, client: Pyopenwebui) -> None:
        with client.api.v1.auths.with_streaming_response.get_session_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthGetSessionUserResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ldap_auth(self, client: Pyopenwebui) -> None:
        auth = client.api.v1.auths.ldap_auth(
            password="password",
            user="user",
        )
        assert_matches_type(AuthLdapAuthResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_ldap_auth(self, client: Pyopenwebui) -> None:
        response = client.api.v1.auths.with_raw_response.ldap_auth(
            password="password",
            user="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthLdapAuthResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_ldap_auth(self, client: Pyopenwebui) -> None:
        with client.api.v1.auths.with_streaming_response.ldap_auth(
            password="password",
            user="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthLdapAuthResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_signin(self, client: Pyopenwebui) -> None:
        auth = client.api.v1.auths.signin(
            email="email",
            password="password",
        )
        assert_matches_type(AuthSigninResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_signin(self, client: Pyopenwebui) -> None:
        response = client.api.v1.auths.with_raw_response.signin(
            email="email",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthSigninResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_signin(self, client: Pyopenwebui) -> None:
        with client.api.v1.auths.with_streaming_response.signin(
            email="email",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthSigninResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_signout(self, client: Pyopenwebui) -> None:
        auth = client.api.v1.auths.signout()
        assert_matches_type(object, auth, path=["response"])

    @parametrize
    def test_raw_response_signout(self, client: Pyopenwebui) -> None:
        response = client.api.v1.auths.with_raw_response.signout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(object, auth, path=["response"])

    @parametrize
    def test_streaming_response_signout(self, client: Pyopenwebui) -> None:
        with client.api.v1.auths.with_streaming_response.signout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_signup(self, client: Pyopenwebui) -> None:
        auth = client.api.v1.auths.signup(
            email="email",
            name="name",
            password="password",
        )
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    def test_method_signup_with_all_params(self, client: Pyopenwebui) -> None:
        auth = client.api.v1.auths.signup(
            email="email",
            name="name",
            password="password",
            profile_image_url="profile_image_url",
        )
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_signup(self, client: Pyopenwebui) -> None:
        response = client.api.v1.auths.with_raw_response.signup(
            email="email",
            name="name",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_signup(self, client: Pyopenwebui) -> None:
        with client.api.v1.auths.with_streaming_response.signup(
            email="email",
            name="name",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthSignupResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuths:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_add_user(self, async_client: AsyncPyopenwebui) -> None:
        auth = await async_client.api.v1.auths.add_user(
            email="email",
            name="name",
            password="password",
        )
        assert_matches_type(SigninResponse, auth, path=["response"])

    @parametrize
    async def test_method_add_user_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        auth = await async_client.api.v1.auths.add_user(
            email="email",
            name="name",
            password="password",
            profile_image_url="profile_image_url",
            role="role",
        )
        assert_matches_type(SigninResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_add_user(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.auths.with_raw_response.add_user(
            email="email",
            name="name",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(SigninResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_add_user(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.auths.with_streaming_response.add_user(
            email="email",
            name="name",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(SigninResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_session_user(self, async_client: AsyncPyopenwebui) -> None:
        auth = await async_client.api.v1.auths.get_session_user()
        assert_matches_type(AuthGetSessionUserResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_get_session_user(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.auths.with_raw_response.get_session_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthGetSessionUserResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_get_session_user(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.auths.with_streaming_response.get_session_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthGetSessionUserResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ldap_auth(self, async_client: AsyncPyopenwebui) -> None:
        auth = await async_client.api.v1.auths.ldap_auth(
            password="password",
            user="user",
        )
        assert_matches_type(AuthLdapAuthResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_ldap_auth(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.auths.with_raw_response.ldap_auth(
            password="password",
            user="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthLdapAuthResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_ldap_auth(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.auths.with_streaming_response.ldap_auth(
            password="password",
            user="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthLdapAuthResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_signin(self, async_client: AsyncPyopenwebui) -> None:
        auth = await async_client.api.v1.auths.signin(
            email="email",
            password="password",
        )
        assert_matches_type(AuthSigninResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_signin(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.auths.with_raw_response.signin(
            email="email",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthSigninResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_signin(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.auths.with_streaming_response.signin(
            email="email",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthSigninResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_signout(self, async_client: AsyncPyopenwebui) -> None:
        auth = await async_client.api.v1.auths.signout()
        assert_matches_type(object, auth, path=["response"])

    @parametrize
    async def test_raw_response_signout(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.auths.with_raw_response.signout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(object, auth, path=["response"])

    @parametrize
    async def test_streaming_response_signout(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.auths.with_streaming_response.signout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_signup(self, async_client: AsyncPyopenwebui) -> None:
        auth = await async_client.api.v1.auths.signup(
            email="email",
            name="name",
            password="password",
        )
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    async def test_method_signup_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        auth = await async_client.api.v1.auths.signup(
            email="email",
            name="name",
            password="password",
            profile_image_url="profile_image_url",
        )
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_signup(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.auths.with_raw_response.signup(
            email="email",
            name="name",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_signup(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.auths.with_streaming_response.signup(
            email="email",
            name="name",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthSignupResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True
