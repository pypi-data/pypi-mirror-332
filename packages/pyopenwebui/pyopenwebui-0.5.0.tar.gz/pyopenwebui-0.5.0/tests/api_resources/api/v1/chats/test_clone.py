# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types import ChatResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClone:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_shared(self, client: Pyopenwebui) -> None:
        clone = client.api.v1.chats.clone.shared(
            "id",
        )
        assert_matches_type(Optional[ChatResponse], clone, path=["response"])

    @parametrize
    def test_raw_response_shared(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.clone.with_raw_response.shared(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clone = response.parse()
        assert_matches_type(Optional[ChatResponse], clone, path=["response"])

    @parametrize
    def test_streaming_response_shared(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.clone.with_streaming_response.shared(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clone = response.parse()
            assert_matches_type(Optional[ChatResponse], clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_shared(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.chats.clone.with_raw_response.shared(
                "",
            )


class TestAsyncClone:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_shared(self, async_client: AsyncPyopenwebui) -> None:
        clone = await async_client.api.v1.chats.clone.shared(
            "id",
        )
        assert_matches_type(Optional[ChatResponse], clone, path=["response"])

    @parametrize
    async def test_raw_response_shared(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.clone.with_raw_response.shared(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clone = await response.parse()
        assert_matches_type(Optional[ChatResponse], clone, path=["response"])

    @parametrize
    async def test_streaming_response_shared(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.clone.with_streaming_response.shared(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clone = await response.parse()
            assert_matches_type(Optional[ChatResponse], clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_shared(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.chats.clone.with_raw_response.shared(
                "",
            )
