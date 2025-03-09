# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_loaded_models(self, client: Pyopenwebui) -> None:
        api = client.ollama.api.get_loaded_models()
        assert_matches_type(object, api, path=["response"])

    @parametrize
    def test_raw_response_get_loaded_models(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.with_raw_response.get_loaded_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(object, api, path=["response"])

    @parametrize
    def test_streaming_response_get_loaded_models(self, client: Pyopenwebui) -> None:
        with client.ollama.api.with_streaming_response.get_loaded_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(object, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_show_info(self, client: Pyopenwebui) -> None:
        api = client.ollama.api.show_info(
            name="name",
        )
        assert_matches_type(object, api, path=["response"])

    @parametrize
    def test_raw_response_show_info(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.with_raw_response.show_info(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(object, api, path=["response"])

    @parametrize
    def test_streaming_response_show_info(self, client: Pyopenwebui) -> None:
        with client.ollama.api.with_streaming_response.show_info(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(object, api, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPI:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_loaded_models(self, async_client: AsyncPyopenwebui) -> None:
        api = await async_client.ollama.api.get_loaded_models()
        assert_matches_type(object, api, path=["response"])

    @parametrize
    async def test_raw_response_get_loaded_models(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.with_raw_response.get_loaded_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(object, api, path=["response"])

    @parametrize
    async def test_streaming_response_get_loaded_models(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.with_streaming_response.get_loaded_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(object, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_show_info(self, async_client: AsyncPyopenwebui) -> None:
        api = await async_client.ollama.api.show_info(
            name="name",
        )
        assert_matches_type(object, api, path=["response"])

    @parametrize
    async def test_raw_response_show_info(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.with_raw_response.show_info(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(object, api, path=["response"])

    @parametrize
    async def test_streaming_response_show_info(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.with_streaming_response.show_info(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(object, api, path=["response"])

        assert cast(Any, response.is_closed) is True
