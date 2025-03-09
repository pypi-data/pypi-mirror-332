# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1 import UserGetResponse, UserGetByIDResponse, UserDeleteByIDResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete_by_id(self, client: Pyopenwebui) -> None:
        user = client.api.v1.users.delete_by_id(
            "user_id",
        )
        assert_matches_type(UserDeleteByIDResponse, user, path=["response"])

    @parametrize
    def test_raw_response_delete_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.users.with_raw_response.delete_by_id(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserDeleteByIDResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_delete_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.users.with_streaming_response.delete_by_id(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserDeleteByIDResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.api.v1.users.with_raw_response.delete_by_id(
                "",
            )

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        user = client.api.v1.users.get()
        assert_matches_type(UserGetResponse, user, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Pyopenwebui) -> None:
        user = client.api.v1.users.get(
            limit=0,
            skip=0,
        )
        assert_matches_type(UserGetResponse, user, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.users.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserGetResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.users.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserGetResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_id(self, client: Pyopenwebui) -> None:
        user = client.api.v1.users.get_by_id(
            "user_id",
        )
        assert_matches_type(UserGetByIDResponse, user, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.users.with_raw_response.get_by_id(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserGetByIDResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.users.with_streaming_response.get_by_id(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserGetByIDResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.api.v1.users.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_get_groups(self, client: Pyopenwebui) -> None:
        user = client.api.v1.users.get_groups()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_raw_response_get_groups(self, client: Pyopenwebui) -> None:
        response = client.api.v1.users.with_raw_response.get_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_streaming_response_get_groups(self, client: Pyopenwebui) -> None:
        with client.api.v1.users.with_streaming_response.get_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_permissions(self, client: Pyopenwebui) -> None:
        user = client.api.v1.users.get_permissions()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_raw_response_get_permissions(self, client: Pyopenwebui) -> None:
        response = client.api.v1.users.with_raw_response.get_permissions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_streaming_response_get_permissions(self, client: Pyopenwebui) -> None:
        with client.api.v1.users.with_streaming_response.get_permissions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        user = await async_client.api.v1.users.delete_by_id(
            "user_id",
        )
        assert_matches_type(UserDeleteByIDResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.users.with_raw_response.delete_by_id(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserDeleteByIDResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.users.with_streaming_response.delete_by_id(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserDeleteByIDResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.api.v1.users.with_raw_response.delete_by_id(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        user = await async_client.api.v1.users.get()
        assert_matches_type(UserGetResponse, user, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        user = await async_client.api.v1.users.get(
            limit=0,
            skip=0,
        )
        assert_matches_type(UserGetResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.users.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserGetResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.users.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserGetResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        user = await async_client.api.v1.users.get_by_id(
            "user_id",
        )
        assert_matches_type(UserGetByIDResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.users.with_raw_response.get_by_id(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserGetByIDResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.users.with_streaming_response.get_by_id(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserGetByIDResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.api.v1.users.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_get_groups(self, async_client: AsyncPyopenwebui) -> None:
        user = await async_client.api.v1.users.get_groups()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_raw_response_get_groups(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.users.with_raw_response.get_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_streaming_response_get_groups(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.users.with_streaming_response.get_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_permissions(self, async_client: AsyncPyopenwebui) -> None:
        user = await async_client.api.v1.users.get_permissions()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_raw_response_get_permissions(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.users.with_raw_response.get_permissions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_streaming_response_get_permissions(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.users.with_streaming_response.get_permissions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True
