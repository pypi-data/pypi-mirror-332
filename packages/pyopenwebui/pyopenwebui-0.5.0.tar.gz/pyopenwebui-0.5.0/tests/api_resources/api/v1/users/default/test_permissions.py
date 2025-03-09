# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.users.default import PermissionGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPermissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Pyopenwebui) -> None:
        permission = client.api.v1.users.default.permissions.update(
            chat={},
            features={},
            workspace={},
        )
        assert_matches_type(object, permission, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Pyopenwebui) -> None:
        permission = client.api.v1.users.default.permissions.update(
            chat={
                "controls": True,
                "delete": True,
                "edit": True,
                "file_upload": True,
                "temporary": True,
            },
            features={
                "code_interpreter": True,
                "image_generation": True,
                "web_search": True,
            },
            workspace={
                "knowledge": True,
                "models": True,
                "prompts": True,
                "tools": True,
            },
        )
        assert_matches_type(object, permission, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Pyopenwebui) -> None:
        response = client.api.v1.users.default.permissions.with_raw_response.update(
            chat={},
            features={},
            workspace={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert_matches_type(object, permission, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Pyopenwebui) -> None:
        with client.api.v1.users.default.permissions.with_streaming_response.update(
            chat={},
            features={},
            workspace={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert_matches_type(object, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        permission = client.api.v1.users.default.permissions.get()
        assert_matches_type(PermissionGetResponse, permission, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.users.default.permissions.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert_matches_type(PermissionGetResponse, permission, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.users.default.permissions.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert_matches_type(PermissionGetResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPermissions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncPyopenwebui) -> None:
        permission = await async_client.api.v1.users.default.permissions.update(
            chat={},
            features={},
            workspace={},
        )
        assert_matches_type(object, permission, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        permission = await async_client.api.v1.users.default.permissions.update(
            chat={
                "controls": True,
                "delete": True,
                "edit": True,
                "file_upload": True,
                "temporary": True,
            },
            features={
                "code_interpreter": True,
                "image_generation": True,
                "web_search": True,
            },
            workspace={
                "knowledge": True,
                "models": True,
                "prompts": True,
                "tools": True,
            },
        )
        assert_matches_type(object, permission, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.users.default.permissions.with_raw_response.update(
            chat={},
            features={},
            workspace={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert_matches_type(object, permission, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.users.default.permissions.with_streaming_response.update(
            chat={},
            features={},
            workspace={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert_matches_type(object, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        permission = await async_client.api.v1.users.default.permissions.get()
        assert_matches_type(PermissionGetResponse, permission, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.users.default.permissions.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert_matches_type(PermissionGetResponse, permission, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.users.default.permissions.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert_matches_type(PermissionGetResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True
