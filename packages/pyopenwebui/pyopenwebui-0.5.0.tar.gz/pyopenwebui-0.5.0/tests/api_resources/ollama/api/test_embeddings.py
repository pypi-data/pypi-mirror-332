# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmbeddings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_embeddings(self, client: Pyopenwebui) -> None:
        embedding = client.ollama.api.embeddings.embeddings(
            model="model",
            prompt="prompt",
        )
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    def test_method_embeddings_with_all_params(self, client: Pyopenwebui) -> None:
        embedding = client.ollama.api.embeddings.embeddings(
            model="model",
            prompt="prompt",
            url_idx=0,
            keep_alive=0,
            options={},
        )
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    def test_raw_response_embeddings(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.embeddings.with_raw_response.embeddings(
            model="model",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    def test_streaming_response_embeddings(self, client: Pyopenwebui) -> None:
        with client.ollama.api.embeddings.with_streaming_response.embeddings(
            model="model",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(object, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_embeddings_by_index(self, client: Pyopenwebui) -> None:
        embedding = client.ollama.api.embeddings.embeddings_by_index(
            url_idx=0,
            model="model",
            prompt="prompt",
        )
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    def test_method_embeddings_by_index_with_all_params(self, client: Pyopenwebui) -> None:
        embedding = client.ollama.api.embeddings.embeddings_by_index(
            url_idx=0,
            model="model",
            prompt="prompt",
            keep_alive=0,
            options={},
        )
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    def test_raw_response_embeddings_by_index(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.embeddings.with_raw_response.embeddings_by_index(
            url_idx=0,
            model="model",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    def test_streaming_response_embeddings_by_index(self, client: Pyopenwebui) -> None:
        with client.ollama.api.embeddings.with_streaming_response.embeddings_by_index(
            url_idx=0,
            model="model",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(object, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmbeddings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_embeddings(self, async_client: AsyncPyopenwebui) -> None:
        embedding = await async_client.ollama.api.embeddings.embeddings(
            model="model",
            prompt="prompt",
        )
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    async def test_method_embeddings_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        embedding = await async_client.ollama.api.embeddings.embeddings(
            model="model",
            prompt="prompt",
            url_idx=0,
            keep_alive=0,
            options={},
        )
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    async def test_raw_response_embeddings(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.embeddings.with_raw_response.embeddings(
            model="model",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    async def test_streaming_response_embeddings(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.embeddings.with_streaming_response.embeddings(
            model="model",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(object, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_embeddings_by_index(self, async_client: AsyncPyopenwebui) -> None:
        embedding = await async_client.ollama.api.embeddings.embeddings_by_index(
            url_idx=0,
            model="model",
            prompt="prompt",
        )
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    async def test_method_embeddings_by_index_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        embedding = await async_client.ollama.api.embeddings.embeddings_by_index(
            url_idx=0,
            model="model",
            prompt="prompt",
            keep_alive=0,
            options={},
        )
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    async def test_raw_response_embeddings_by_index(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.embeddings.with_raw_response.embeddings_by_index(
            url_idx=0,
            model="model",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    async def test_streaming_response_embeddings_by_index(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.embeddings.with_streaming_response.embeddings_by_index(
            url_idx=0,
            model="model",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(object, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True
