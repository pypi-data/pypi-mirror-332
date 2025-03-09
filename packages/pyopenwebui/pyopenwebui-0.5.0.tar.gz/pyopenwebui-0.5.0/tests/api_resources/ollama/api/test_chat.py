# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_chat(self, client: Pyopenwebui) -> None:
        chat = client.ollama.api.chat.chat(
            body={},
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_method_chat_with_all_params(self, client: Pyopenwebui) -> None:
        chat = client.ollama.api.chat.chat(
            body={},
            bypass_filter=True,
            url_idx=0,
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_raw_response_chat(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.chat.with_raw_response.chat(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_streaming_response_chat(self, client: Pyopenwebui) -> None:
        with client.ollama.api.chat.with_streaming_response.chat(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_chat_by_index(self, client: Pyopenwebui) -> None:
        chat = client.ollama.api.chat.chat_by_index(
            url_idx=0,
            body={},
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_method_chat_by_index_with_all_params(self, client: Pyopenwebui) -> None:
        chat = client.ollama.api.chat.chat_by_index(
            url_idx=0,
            body={},
            bypass_filter=True,
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_raw_response_chat_by_index(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.chat.with_raw_response.chat_by_index(
            url_idx=0,
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_streaming_response_chat_by_index(self, client: Pyopenwebui) -> None:
        with client.ollama.api.chat.with_streaming_response.chat_by_index(
            url_idx=0,
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_chat(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.ollama.api.chat.chat(
            body={},
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_method_chat_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.ollama.api.chat.chat(
            body={},
            bypass_filter=True,
            url_idx=0,
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_raw_response_chat(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.chat.with_raw_response.chat(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_streaming_response_chat(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.chat.with_streaming_response.chat(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_chat_by_index(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.ollama.api.chat.chat_by_index(
            url_idx=0,
            body={},
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_method_chat_by_index_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.ollama.api.chat.chat_by_index(
            url_idx=0,
            body={},
            bypass_filter=True,
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_raw_response_chat_by_index(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.chat.with_raw_response.chat_by_index(
            url_idx=0,
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_streaming_response_chat_by_index(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.chat.with_streaming_response.chat_by_index(
            url_idx=0,
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
