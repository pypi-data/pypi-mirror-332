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
    def test_method_get_changelog(self, client: Pyopenwebui) -> None:
        api = client.api.get_changelog()
        assert_matches_type(object, api, path=["response"])

    @parametrize
    def test_raw_response_get_changelog(self, client: Pyopenwebui) -> None:
        response = client.api.with_raw_response.get_changelog()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(object, api, path=["response"])

    @parametrize
    def test_streaming_response_get_changelog(self, client: Pyopenwebui) -> None:
        with client.api.with_streaming_response.get_changelog() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(object, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_config(self, client: Pyopenwebui) -> None:
        api = client.api.get_config()
        assert_matches_type(object, api, path=["response"])

    @parametrize
    def test_raw_response_get_config(self, client: Pyopenwebui) -> None:
        response = client.api.with_raw_response.get_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(object, api, path=["response"])

    @parametrize
    def test_streaming_response_get_config(self, client: Pyopenwebui) -> None:
        with client.api.with_streaming_response.get_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(object, api, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPI:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_changelog(self, async_client: AsyncPyopenwebui) -> None:
        api = await async_client.api.get_changelog()
        assert_matches_type(object, api, path=["response"])

    @parametrize
    async def test_raw_response_get_changelog(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.with_raw_response.get_changelog()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(object, api, path=["response"])

    @parametrize
    async def test_streaming_response_get_changelog(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.with_streaming_response.get_changelog() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(object, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_config(self, async_client: AsyncPyopenwebui) -> None:
        api = await async_client.api.get_config()
        assert_matches_type(object, api, path=["response"])

    @parametrize
    async def test_raw_response_get_config(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.with_raw_response.get_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(object, api, path=["response"])

    @parametrize
    async def test_streaming_response_get_config(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.with_streaming_response.get_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(object, api, path=["response"])

        assert cast(Any, response.is_closed) is True
