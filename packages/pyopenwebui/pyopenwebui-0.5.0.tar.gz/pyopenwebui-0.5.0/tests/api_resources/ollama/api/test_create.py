# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Pyopenwebui) -> None:
        create = client.ollama.api.create.create()
        assert_matches_type(object, create, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Pyopenwebui) -> None:
        create = client.ollama.api.create.create(
            url_idx=0,
            model="model",
            path="path",
            stream=True,
        )
        assert_matches_type(object, create, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.create.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        create = response.parse()
        assert_matches_type(object, create, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Pyopenwebui) -> None:
        with client.ollama.api.create.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            create = response.parse()
            assert_matches_type(object, create, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_by_index(self, client: Pyopenwebui) -> None:
        create = client.ollama.api.create.create_by_index(
            url_idx=0,
        )
        assert_matches_type(object, create, path=["response"])

    @parametrize
    def test_method_create_by_index_with_all_params(self, client: Pyopenwebui) -> None:
        create = client.ollama.api.create.create_by_index(
            url_idx=0,
            model="model",
            path="path",
            stream=True,
        )
        assert_matches_type(object, create, path=["response"])

    @parametrize
    def test_raw_response_create_by_index(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.create.with_raw_response.create_by_index(
            url_idx=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        create = response.parse()
        assert_matches_type(object, create, path=["response"])

    @parametrize
    def test_streaming_response_create_by_index(self, client: Pyopenwebui) -> None:
        with client.ollama.api.create.with_streaming_response.create_by_index(
            url_idx=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            create = response.parse()
            assert_matches_type(object, create, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCreate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPyopenwebui) -> None:
        create = await async_client.ollama.api.create.create()
        assert_matches_type(object, create, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        create = await async_client.ollama.api.create.create(
            url_idx=0,
            model="model",
            path="path",
            stream=True,
        )
        assert_matches_type(object, create, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.create.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        create = await response.parse()
        assert_matches_type(object, create, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.create.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            create = await response.parse()
            assert_matches_type(object, create, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_by_index(self, async_client: AsyncPyopenwebui) -> None:
        create = await async_client.ollama.api.create.create_by_index(
            url_idx=0,
        )
        assert_matches_type(object, create, path=["response"])

    @parametrize
    async def test_method_create_by_index_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        create = await async_client.ollama.api.create.create_by_index(
            url_idx=0,
            model="model",
            path="path",
            stream=True,
        )
        assert_matches_type(object, create, path=["response"])

    @parametrize
    async def test_raw_response_create_by_index(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.create.with_raw_response.create_by_index(
            url_idx=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        create = await response.parse()
        assert_matches_type(object, create, path=["response"])

    @parametrize
    async def test_streaming_response_create_by_index(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.create.with_streaming_response.create_by_index(
            url_idx=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            create = await response.parse()
            assert_matches_type(object, create, path=["response"])

        assert cast(Any, response.is_closed) is True
