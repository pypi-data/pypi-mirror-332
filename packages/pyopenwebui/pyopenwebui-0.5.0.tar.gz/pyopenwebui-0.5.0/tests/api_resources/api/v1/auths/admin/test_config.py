# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Pyopenwebui) -> None:
        config = client.api.v1.auths.admin.config.update(
            api_key_allowed_endpoints="API_KEY_ALLOWED_ENDPOINTS",
            default_user_role="DEFAULT_USER_ROLE",
            enable_api_key=True,
            enable_api_key_endpoint_restrictions=True,
            enable_channels=True,
            enable_community_sharing=True,
            enable_message_rating=True,
            enable_signup=True,
            jwt_expires_in="JWT_EXPIRES_IN",
            show_admin_details=True,
            webui_url="WEBUI_URL",
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Pyopenwebui) -> None:
        response = client.api.v1.auths.admin.config.with_raw_response.update(
            api_key_allowed_endpoints="API_KEY_ALLOWED_ENDPOINTS",
            default_user_role="DEFAULT_USER_ROLE",
            enable_api_key=True,
            enable_api_key_endpoint_restrictions=True,
            enable_channels=True,
            enable_community_sharing=True,
            enable_message_rating=True,
            enable_signup=True,
            jwt_expires_in="JWT_EXPIRES_IN",
            show_admin_details=True,
            webui_url="WEBUI_URL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Pyopenwebui) -> None:
        with client.api.v1.auths.admin.config.with_streaming_response.update(
            api_key_allowed_endpoints="API_KEY_ALLOWED_ENDPOINTS",
            default_user_role="DEFAULT_USER_ROLE",
            enable_api_key=True,
            enable_api_key_endpoint_restrictions=True,
            enable_channels=True,
            enable_community_sharing=True,
            enable_message_rating=True,
            enable_signup=True,
            jwt_expires_in="JWT_EXPIRES_IN",
            show_admin_details=True,
            webui_url="WEBUI_URL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        config = client.api.v1.auths.admin.config.get()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.auths.admin.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.auths.admin.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.api.v1.auths.admin.config.update(
            api_key_allowed_endpoints="API_KEY_ALLOWED_ENDPOINTS",
            default_user_role="DEFAULT_USER_ROLE",
            enable_api_key=True,
            enable_api_key_endpoint_restrictions=True,
            enable_channels=True,
            enable_community_sharing=True,
            enable_message_rating=True,
            enable_signup=True,
            jwt_expires_in="JWT_EXPIRES_IN",
            show_admin_details=True,
            webui_url="WEBUI_URL",
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.auths.admin.config.with_raw_response.update(
            api_key_allowed_endpoints="API_KEY_ALLOWED_ENDPOINTS",
            default_user_role="DEFAULT_USER_ROLE",
            enable_api_key=True,
            enable_api_key_endpoint_restrictions=True,
            enable_channels=True,
            enable_community_sharing=True,
            enable_message_rating=True,
            enable_signup=True,
            jwt_expires_in="JWT_EXPIRES_IN",
            show_admin_details=True,
            webui_url="WEBUI_URL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.auths.admin.config.with_streaming_response.update(
            api_key_allowed_endpoints="API_KEY_ALLOWED_ENDPOINTS",
            default_user_role="DEFAULT_USER_ROLE",
            enable_api_key=True,
            enable_api_key_endpoint_restrictions=True,
            enable_channels=True,
            enable_community_sharing=True,
            enable_message_rating=True,
            enable_signup=True,
            jwt_expires_in="JWT_EXPIRES_IN",
            show_admin_details=True,
            webui_url="WEBUI_URL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.api.v1.auths.admin.config.get()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.auths.admin.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.auths.admin.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True
