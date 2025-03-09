# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types import ChatResponse
from pyopenwebui.types.api.v1.chats import ShareDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShare:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Pyopenwebui) -> None:
        share = client.api.v1.chats.share.delete(
            "id",
        )
        assert_matches_type(Optional[ShareDeleteResponse], share, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.share.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = response.parse()
        assert_matches_type(Optional[ShareDeleteResponse], share, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.share.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = response.parse()
            assert_matches_type(Optional[ShareDeleteResponse], share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.chats.share.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        share = client.api.v1.chats.share.get(
            "share_id",
        )
        assert_matches_type(Optional[ChatResponse], share, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.share.with_raw_response.get(
            "share_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = response.parse()
        assert_matches_type(Optional[ChatResponse], share, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.share.with_streaming_response.get(
            "share_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = response.parse()
            assert_matches_type(Optional[ChatResponse], share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            client.api.v1.chats.share.with_raw_response.get(
                "",
            )


class TestAsyncShare:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncPyopenwebui) -> None:
        share = await async_client.api.v1.chats.share.delete(
            "id",
        )
        assert_matches_type(Optional[ShareDeleteResponse], share, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.share.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = await response.parse()
        assert_matches_type(Optional[ShareDeleteResponse], share, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.share.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = await response.parse()
            assert_matches_type(Optional[ShareDeleteResponse], share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.chats.share.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        share = await async_client.api.v1.chats.share.get(
            "share_id",
        )
        assert_matches_type(Optional[ChatResponse], share, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.share.with_raw_response.get(
            "share_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = await response.parse()
        assert_matches_type(Optional[ChatResponse], share, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.share.with_streaming_response.get(
            "share_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = await response.parse()
            assert_matches_type(Optional[ChatResponse], share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            await async_client.api.v1.chats.share.with_raw_response.get(
                "",
            )
