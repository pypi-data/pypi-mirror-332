# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.retrieval import ResetUploadsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReset:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_db(self, client: Pyopenwebui) -> None:
        reset = client.api.v1.retrieval.reset.db()
        assert_matches_type(object, reset, path=["response"])

    @parametrize
    def test_raw_response_db(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.reset.with_raw_response.db()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reset = response.parse()
        assert_matches_type(object, reset, path=["response"])

    @parametrize
    def test_streaming_response_db(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.reset.with_streaming_response.db() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reset = response.parse()
            assert_matches_type(object, reset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_uploads(self, client: Pyopenwebui) -> None:
        reset = client.api.v1.retrieval.reset.uploads()
        assert_matches_type(ResetUploadsResponse, reset, path=["response"])

    @parametrize
    def test_raw_response_uploads(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.reset.with_raw_response.uploads()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reset = response.parse()
        assert_matches_type(ResetUploadsResponse, reset, path=["response"])

    @parametrize
    def test_streaming_response_uploads(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.reset.with_streaming_response.uploads() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reset = response.parse()
            assert_matches_type(ResetUploadsResponse, reset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReset:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_db(self, async_client: AsyncPyopenwebui) -> None:
        reset = await async_client.api.v1.retrieval.reset.db()
        assert_matches_type(object, reset, path=["response"])

    @parametrize
    async def test_raw_response_db(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.reset.with_raw_response.db()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reset = await response.parse()
        assert_matches_type(object, reset, path=["response"])

    @parametrize
    async def test_streaming_response_db(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.reset.with_streaming_response.db() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reset = await response.parse()
            assert_matches_type(object, reset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_uploads(self, async_client: AsyncPyopenwebui) -> None:
        reset = await async_client.api.v1.retrieval.reset.uploads()
        assert_matches_type(ResetUploadsResponse, reset, path=["response"])

    @parametrize
    async def test_raw_response_uploads(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.reset.with_raw_response.uploads()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reset = await response.parse()
        assert_matches_type(ResetUploadsResponse, reset, path=["response"])

    @parametrize
    async def test_streaming_response_uploads(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.reset.with_streaming_response.uploads() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reset = await response.parse()
            assert_matches_type(ResetUploadsResponse, reset, path=["response"])

        assert cast(Any, response.is_closed) is True
