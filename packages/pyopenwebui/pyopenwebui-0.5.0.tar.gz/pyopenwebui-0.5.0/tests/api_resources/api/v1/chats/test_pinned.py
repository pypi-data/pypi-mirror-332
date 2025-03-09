# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.chats import PinnedGetResponse, PinnedGetByIDResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPinned:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        pinned = client.api.v1.chats.pinned.get()
        assert_matches_type(PinnedGetResponse, pinned, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.pinned.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pinned = response.parse()
        assert_matches_type(PinnedGetResponse, pinned, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.pinned.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pinned = response.parse()
            assert_matches_type(PinnedGetResponse, pinned, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_id(self, client: Pyopenwebui) -> None:
        pinned = client.api.v1.chats.pinned.get_by_id(
            "id",
        )
        assert_matches_type(Optional[PinnedGetByIDResponse], pinned, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.pinned.with_raw_response.get_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pinned = response.parse()
        assert_matches_type(Optional[PinnedGetByIDResponse], pinned, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.pinned.with_streaming_response.get_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pinned = response.parse()
            assert_matches_type(Optional[PinnedGetByIDResponse], pinned, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.chats.pinned.with_raw_response.get_by_id(
                "",
            )


class TestAsyncPinned:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        pinned = await async_client.api.v1.chats.pinned.get()
        assert_matches_type(PinnedGetResponse, pinned, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.pinned.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pinned = await response.parse()
        assert_matches_type(PinnedGetResponse, pinned, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.pinned.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pinned = await response.parse()
            assert_matches_type(PinnedGetResponse, pinned, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        pinned = await async_client.api.v1.chats.pinned.get_by_id(
            "id",
        )
        assert_matches_type(Optional[PinnedGetByIDResponse], pinned, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.pinned.with_raw_response.get_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pinned = await response.parse()
        assert_matches_type(Optional[PinnedGetByIDResponse], pinned, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.pinned.with_streaming_response.get_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pinned = await response.parse()
            assert_matches_type(Optional[PinnedGetByIDResponse], pinned, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.chats.pinned.with_raw_response.get_by_id(
                "",
            )
