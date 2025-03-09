# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmbedding:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_config(self, client: Pyopenwebui) -> None:
        embedding = client.api.v1.retrieval.embedding.get_config()
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    def test_raw_response_get_config(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.embedding.with_raw_response.get_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    def test_streaming_response_get_config(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.embedding.with_streaming_response.get_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(object, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_config(self, client: Pyopenwebui) -> None:
        embedding = client.api.v1.retrieval.embedding.update_config(
            embedding_engine="embedding_engine",
            embedding_model="embedding_model",
        )
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    def test_method_update_config_with_all_params(self, client: Pyopenwebui) -> None:
        embedding = client.api.v1.retrieval.embedding.update_config(
            embedding_engine="embedding_engine",
            embedding_model="embedding_model",
            embedding_batch_size=0,
            ollama_config={
                "key": "key",
                "url": "url",
            },
            openai_config={
                "key": "key",
                "url": "url",
            },
        )
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    def test_raw_response_update_config(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.embedding.with_raw_response.update_config(
            embedding_engine="embedding_engine",
            embedding_model="embedding_model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    def test_streaming_response_update_config(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.embedding.with_streaming_response.update_config(
            embedding_engine="embedding_engine",
            embedding_model="embedding_model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(object, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmbedding:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_config(self, async_client: AsyncPyopenwebui) -> None:
        embedding = await async_client.api.v1.retrieval.embedding.get_config()
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    async def test_raw_response_get_config(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.embedding.with_raw_response.get_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    async def test_streaming_response_get_config(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.embedding.with_streaming_response.get_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(object, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_config(self, async_client: AsyncPyopenwebui) -> None:
        embedding = await async_client.api.v1.retrieval.embedding.update_config(
            embedding_engine="embedding_engine",
            embedding_model="embedding_model",
        )
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    async def test_method_update_config_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        embedding = await async_client.api.v1.retrieval.embedding.update_config(
            embedding_engine="embedding_engine",
            embedding_model="embedding_model",
            embedding_batch_size=0,
            ollama_config={
                "key": "key",
                "url": "url",
            },
            openai_config={
                "key": "key",
                "url": "url",
            },
        )
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    async def test_raw_response_update_config(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.embedding.with_raw_response.update_config(
            embedding_engine="embedding_engine",
            embedding_model="embedding_model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(object, embedding, path=["response"])

    @parametrize
    async def test_streaming_response_update_config(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.embedding.with_streaming_response.update_config(
            embedding_engine="embedding_engine",
            embedding_model="embedding_model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(object, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True
