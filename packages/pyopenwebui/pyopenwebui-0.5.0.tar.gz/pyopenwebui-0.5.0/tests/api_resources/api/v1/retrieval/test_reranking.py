# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReranking:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_config(self, client: Pyopenwebui) -> None:
        reranking = client.api.v1.retrieval.reranking.get_config()
        assert_matches_type(object, reranking, path=["response"])

    @parametrize
    def test_raw_response_get_config(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.reranking.with_raw_response.get_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reranking = response.parse()
        assert_matches_type(object, reranking, path=["response"])

    @parametrize
    def test_streaming_response_get_config(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.reranking.with_streaming_response.get_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reranking = response.parse()
            assert_matches_type(object, reranking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_config(self, client: Pyopenwebui) -> None:
        reranking = client.api.v1.retrieval.reranking.update_config(
            reranking_model="reranking_model",
        )
        assert_matches_type(object, reranking, path=["response"])

    @parametrize
    def test_raw_response_update_config(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.reranking.with_raw_response.update_config(
            reranking_model="reranking_model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reranking = response.parse()
        assert_matches_type(object, reranking, path=["response"])

    @parametrize
    def test_streaming_response_update_config(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.reranking.with_streaming_response.update_config(
            reranking_model="reranking_model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reranking = response.parse()
            assert_matches_type(object, reranking, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReranking:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_config(self, async_client: AsyncPyopenwebui) -> None:
        reranking = await async_client.api.v1.retrieval.reranking.get_config()
        assert_matches_type(object, reranking, path=["response"])

    @parametrize
    async def test_raw_response_get_config(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.reranking.with_raw_response.get_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reranking = await response.parse()
        assert_matches_type(object, reranking, path=["response"])

    @parametrize
    async def test_streaming_response_get_config(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.reranking.with_streaming_response.get_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reranking = await response.parse()
            assert_matches_type(object, reranking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_config(self, async_client: AsyncPyopenwebui) -> None:
        reranking = await async_client.api.v1.retrieval.reranking.update_config(
            reranking_model="reranking_model",
        )
        assert_matches_type(object, reranking, path=["response"])

    @parametrize
    async def test_raw_response_update_config(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.reranking.with_raw_response.update_config(
            reranking_model="reranking_model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reranking = await response.parse()
        assert_matches_type(object, reranking, path=["response"])

    @parametrize
    async def test_streaming_response_update_config(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.reranking.with_streaming_response.update_config(
            reranking_model="reranking_model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reranking = await response.parse()
            assert_matches_type(object, reranking, path=["response"])

        assert cast(Any, response.is_closed) is True
