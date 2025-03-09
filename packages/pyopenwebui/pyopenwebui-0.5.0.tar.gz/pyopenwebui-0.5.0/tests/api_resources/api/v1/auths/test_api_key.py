# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types import APIKey
from pyopenwebui.types.api.v1.auths import APIKeyDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKey:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Pyopenwebui) -> None:
        api_key = client.api.v1.auths.api_key.delete()
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Pyopenwebui) -> None:
        response = client.api.v1.auths.api_key.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Pyopenwebui) -> None:
        with client.api.v1.auths.api_key.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generate(self, client: Pyopenwebui) -> None:
        api_key = client.api.v1.auths.api_key.generate()
        assert_matches_type(APIKey, api_key, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Pyopenwebui) -> None:
        response = client.api.v1.auths.api_key.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Pyopenwebui) -> None:
        with client.api.v1.auths.api_key.with_streaming_response.generate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        api_key = client.api.v1.auths.api_key.get()
        assert_matches_type(APIKey, api_key, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.auths.api_key.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.auths.api_key.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIKey:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncPyopenwebui) -> None:
        api_key = await async_client.api.v1.auths.api_key.delete()
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.auths.api_key.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.auths.api_key.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyDeleteResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generate(self, async_client: AsyncPyopenwebui) -> None:
        api_key = await async_client.api.v1.auths.api_key.generate()
        assert_matches_type(APIKey, api_key, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.auths.api_key.with_raw_response.generate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.auths.api_key.with_streaming_response.generate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        api_key = await async_client.api.v1.auths.api_key.get()
        assert_matches_type(APIKey, api_key, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.auths.api_key.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.auths.api_key.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True
