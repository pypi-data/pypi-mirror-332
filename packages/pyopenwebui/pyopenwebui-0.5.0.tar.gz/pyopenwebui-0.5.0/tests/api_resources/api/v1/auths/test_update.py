# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.auths import (
    UpdateProfileResponse,
    UpdatePasswordResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUpdate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_password(self, client: Pyopenwebui) -> None:
        update = client.api.v1.auths.update.password(
            new_password="new_password",
            password="password",
        )
        assert_matches_type(UpdatePasswordResponse, update, path=["response"])

    @parametrize
    def test_raw_response_password(self, client: Pyopenwebui) -> None:
        response = client.api.v1.auths.update.with_raw_response.password(
            new_password="new_password",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        update = response.parse()
        assert_matches_type(UpdatePasswordResponse, update, path=["response"])

    @parametrize
    def test_streaming_response_password(self, client: Pyopenwebui) -> None:
        with client.api.v1.auths.update.with_streaming_response.password(
            new_password="new_password",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            update = response.parse()
            assert_matches_type(UpdatePasswordResponse, update, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_profile(self, client: Pyopenwebui) -> None:
        update = client.api.v1.auths.update.profile(
            name="name",
            profile_image_url="profile_image_url",
        )
        assert_matches_type(UpdateProfileResponse, update, path=["response"])

    @parametrize
    def test_raw_response_profile(self, client: Pyopenwebui) -> None:
        response = client.api.v1.auths.update.with_raw_response.profile(
            name="name",
            profile_image_url="profile_image_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        update = response.parse()
        assert_matches_type(UpdateProfileResponse, update, path=["response"])

    @parametrize
    def test_streaming_response_profile(self, client: Pyopenwebui) -> None:
        with client.api.v1.auths.update.with_streaming_response.profile(
            name="name",
            profile_image_url="profile_image_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            update = response.parse()
            assert_matches_type(UpdateProfileResponse, update, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUpdate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_password(self, async_client: AsyncPyopenwebui) -> None:
        update = await async_client.api.v1.auths.update.password(
            new_password="new_password",
            password="password",
        )
        assert_matches_type(UpdatePasswordResponse, update, path=["response"])

    @parametrize
    async def test_raw_response_password(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.auths.update.with_raw_response.password(
            new_password="new_password",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        update = await response.parse()
        assert_matches_type(UpdatePasswordResponse, update, path=["response"])

    @parametrize
    async def test_streaming_response_password(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.auths.update.with_streaming_response.password(
            new_password="new_password",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            update = await response.parse()
            assert_matches_type(UpdatePasswordResponse, update, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_profile(self, async_client: AsyncPyopenwebui) -> None:
        update = await async_client.api.v1.auths.update.profile(
            name="name",
            profile_image_url="profile_image_url",
        )
        assert_matches_type(UpdateProfileResponse, update, path=["response"])

    @parametrize
    async def test_raw_response_profile(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.auths.update.with_raw_response.profile(
            name="name",
            profile_image_url="profile_image_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        update = await response.parse()
        assert_matches_type(UpdateProfileResponse, update, path=["response"])

    @parametrize
    async def test_streaming_response_profile(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.auths.update.with_streaming_response.profile(
            name="name",
            profile_image_url="profile_image_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            update = await response.parse()
            assert_matches_type(UpdateProfileResponse, update, path=["response"])

        assert cast(Any, response.is_closed) is True
