# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmbed:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_embed(self, client: Pyopenwebui) -> None:
        embed = client.ollama.api.embed.embed(
            input=["string"],
            model="model",
        )
        assert_matches_type(object, embed, path=["response"])

    @parametrize
    def test_method_embed_with_all_params(self, client: Pyopenwebui) -> None:
        embed = client.ollama.api.embed.embed(
            input=["string"],
            model="model",
            url_idx=0,
            keep_alive=0,
            options={},
            truncate=True,
        )
        assert_matches_type(object, embed, path=["response"])

    @parametrize
    def test_raw_response_embed(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.embed.with_raw_response.embed(
            input=["string"],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embed = response.parse()
        assert_matches_type(object, embed, path=["response"])

    @parametrize
    def test_streaming_response_embed(self, client: Pyopenwebui) -> None:
        with client.ollama.api.embed.with_streaming_response.embed(
            input=["string"],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embed = response.parse()
            assert_matches_type(object, embed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_embed_by_index(self, client: Pyopenwebui) -> None:
        embed = client.ollama.api.embed.embed_by_index(
            url_idx=0,
            input=["string"],
            model="model",
        )
        assert_matches_type(object, embed, path=["response"])

    @parametrize
    def test_method_embed_by_index_with_all_params(self, client: Pyopenwebui) -> None:
        embed = client.ollama.api.embed.embed_by_index(
            url_idx=0,
            input=["string"],
            model="model",
            keep_alive=0,
            options={},
            truncate=True,
        )
        assert_matches_type(object, embed, path=["response"])

    @parametrize
    def test_raw_response_embed_by_index(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.embed.with_raw_response.embed_by_index(
            url_idx=0,
            input=["string"],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embed = response.parse()
        assert_matches_type(object, embed, path=["response"])

    @parametrize
    def test_streaming_response_embed_by_index(self, client: Pyopenwebui) -> None:
        with client.ollama.api.embed.with_streaming_response.embed_by_index(
            url_idx=0,
            input=["string"],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embed = response.parse()
            assert_matches_type(object, embed, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmbed:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_embed(self, async_client: AsyncPyopenwebui) -> None:
        embed = await async_client.ollama.api.embed.embed(
            input=["string"],
            model="model",
        )
        assert_matches_type(object, embed, path=["response"])

    @parametrize
    async def test_method_embed_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        embed = await async_client.ollama.api.embed.embed(
            input=["string"],
            model="model",
            url_idx=0,
            keep_alive=0,
            options={},
            truncate=True,
        )
        assert_matches_type(object, embed, path=["response"])

    @parametrize
    async def test_raw_response_embed(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.embed.with_raw_response.embed(
            input=["string"],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embed = await response.parse()
        assert_matches_type(object, embed, path=["response"])

    @parametrize
    async def test_streaming_response_embed(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.embed.with_streaming_response.embed(
            input=["string"],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embed = await response.parse()
            assert_matches_type(object, embed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_embed_by_index(self, async_client: AsyncPyopenwebui) -> None:
        embed = await async_client.ollama.api.embed.embed_by_index(
            url_idx=0,
            input=["string"],
            model="model",
        )
        assert_matches_type(object, embed, path=["response"])

    @parametrize
    async def test_method_embed_by_index_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        embed = await async_client.ollama.api.embed.embed_by_index(
            url_idx=0,
            input=["string"],
            model="model",
            keep_alive=0,
            options={},
            truncate=True,
        )
        assert_matches_type(object, embed, path=["response"])

    @parametrize
    async def test_raw_response_embed_by_index(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.embed.with_raw_response.embed_by_index(
            url_idx=0,
            input=["string"],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embed = await response.parse()
        assert_matches_type(object, embed, path=["response"])

    @parametrize
    async def test_streaming_response_embed_by_index(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.embed.with_streaming_response.embed_by_index(
            url_idx=0,
            input=["string"],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embed = await response.parse()
            assert_matches_type(object, embed, path=["response"])

        assert cast(Any, response.is_closed) is True
