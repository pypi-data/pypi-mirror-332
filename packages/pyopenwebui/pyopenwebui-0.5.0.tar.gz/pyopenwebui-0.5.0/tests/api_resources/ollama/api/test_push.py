# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPush:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_push(self, client: Pyopenwebui) -> None:
        push = client.ollama.api.push.push(
            name="name",
        )
        assert_matches_type(object, push, path=["response"])

    @parametrize
    def test_method_push_with_all_params(self, client: Pyopenwebui) -> None:
        push = client.ollama.api.push.push(
            name="name",
            url_idx=0,
            insecure=True,
            stream=True,
        )
        assert_matches_type(object, push, path=["response"])

    @parametrize
    def test_raw_response_push(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.push.with_raw_response.push(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        push = response.parse()
        assert_matches_type(object, push, path=["response"])

    @parametrize
    def test_streaming_response_push(self, client: Pyopenwebui) -> None:
        with client.ollama.api.push.with_streaming_response.push(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            push = response.parse()
            assert_matches_type(object, push, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_push_by_index(self, client: Pyopenwebui) -> None:
        push = client.ollama.api.push.push_by_index(
            url_idx=0,
            name="name",
        )
        assert_matches_type(object, push, path=["response"])

    @parametrize
    def test_method_push_by_index_with_all_params(self, client: Pyopenwebui) -> None:
        push = client.ollama.api.push.push_by_index(
            url_idx=0,
            name="name",
            insecure=True,
            stream=True,
        )
        assert_matches_type(object, push, path=["response"])

    @parametrize
    def test_raw_response_push_by_index(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.push.with_raw_response.push_by_index(
            url_idx=0,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        push = response.parse()
        assert_matches_type(object, push, path=["response"])

    @parametrize
    def test_streaming_response_push_by_index(self, client: Pyopenwebui) -> None:
        with client.ollama.api.push.with_streaming_response.push_by_index(
            url_idx=0,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            push = response.parse()
            assert_matches_type(object, push, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPush:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_push(self, async_client: AsyncPyopenwebui) -> None:
        push = await async_client.ollama.api.push.push(
            name="name",
        )
        assert_matches_type(object, push, path=["response"])

    @parametrize
    async def test_method_push_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        push = await async_client.ollama.api.push.push(
            name="name",
            url_idx=0,
            insecure=True,
            stream=True,
        )
        assert_matches_type(object, push, path=["response"])

    @parametrize
    async def test_raw_response_push(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.push.with_raw_response.push(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        push = await response.parse()
        assert_matches_type(object, push, path=["response"])

    @parametrize
    async def test_streaming_response_push(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.push.with_streaming_response.push(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            push = await response.parse()
            assert_matches_type(object, push, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_push_by_index(self, async_client: AsyncPyopenwebui) -> None:
        push = await async_client.ollama.api.push.push_by_index(
            url_idx=0,
            name="name",
        )
        assert_matches_type(object, push, path=["response"])

    @parametrize
    async def test_method_push_by_index_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        push = await async_client.ollama.api.push.push_by_index(
            url_idx=0,
            name="name",
            insecure=True,
            stream=True,
        )
        assert_matches_type(object, push, path=["response"])

    @parametrize
    async def test_raw_response_push_by_index(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.push.with_raw_response.push_by_index(
            url_idx=0,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        push = await response.parse()
        assert_matches_type(object, push, path=["response"])

    @parametrize
    async def test_streaming_response_push_by_index(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.push.with_streaming_response.push_by_index(
            url_idx=0,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            push = await response.parse()
            assert_matches_type(object, push, path=["response"])

        assert cast(Any, response.is_closed) is True
