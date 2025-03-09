# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWeb:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_search(self, client: Pyopenwebui) -> None:
        web = client.api.v1.retrieval.process.web.search(
            query="query",
        )
        assert_matches_type(object, web, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Pyopenwebui) -> None:
        web = client.api.v1.retrieval.process.web.search(
            query="query",
            collection_name="collection_name",
        )
        assert_matches_type(object, web, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.process.web.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(object, web, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.process.web.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(object, web, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWeb:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_search(self, async_client: AsyncPyopenwebui) -> None:
        web = await async_client.api.v1.retrieval.process.web.search(
            query="query",
        )
        assert_matches_type(object, web, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        web = await async_client.api.v1.retrieval.process.web.search(
            query="query",
            collection_name="collection_name",
        )
        assert_matches_type(object, web, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.process.web.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(object, web, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.process.web.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(object, web, path=["response"])

        assert cast(Any, response.is_closed) is True
