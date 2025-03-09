# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generate(self, client: Pyopenwebui) -> None:
        completion = client.ollama.v1.completions.generate(
            body={},
        )
        assert_matches_type(object, completion, path=["response"])

    @parametrize
    def test_method_generate_with_all_params(self, client: Pyopenwebui) -> None:
        completion = client.ollama.v1.completions.generate(
            body={},
            url_idx=0,
        )
        assert_matches_type(object, completion, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Pyopenwebui) -> None:
        response = client.ollama.v1.completions.with_raw_response.generate(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(object, completion, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Pyopenwebui) -> None:
        with client.ollama.v1.completions.with_streaming_response.generate(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(object, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generate_by_index(self, client: Pyopenwebui) -> None:
        completion = client.ollama.v1.completions.generate_by_index(
            url_idx=0,
            body={},
        )
        assert_matches_type(object, completion, path=["response"])

    @parametrize
    def test_raw_response_generate_by_index(self, client: Pyopenwebui) -> None:
        response = client.ollama.v1.completions.with_raw_response.generate_by_index(
            url_idx=0,
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(object, completion, path=["response"])

    @parametrize
    def test_streaming_response_generate_by_index(self, client: Pyopenwebui) -> None:
        with client.ollama.v1.completions.with_streaming_response.generate_by_index(
            url_idx=0,
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(object, completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_generate(self, async_client: AsyncPyopenwebui) -> None:
        completion = await async_client.ollama.v1.completions.generate(
            body={},
        )
        assert_matches_type(object, completion, path=["response"])

    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        completion = await async_client.ollama.v1.completions.generate(
            body={},
            url_idx=0,
        )
        assert_matches_type(object, completion, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.v1.completions.with_raw_response.generate(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(object, completion, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.v1.completions.with_streaming_response.generate(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(object, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generate_by_index(self, async_client: AsyncPyopenwebui) -> None:
        completion = await async_client.ollama.v1.completions.generate_by_index(
            url_idx=0,
            body={},
        )
        assert_matches_type(object, completion, path=["response"])

    @parametrize
    async def test_raw_response_generate_by_index(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.v1.completions.with_raw_response.generate_by_index(
            url_idx=0,
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(object, completion, path=["response"])

    @parametrize
    async def test_streaming_response_generate_by_index(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.v1.completions.with_streaming_response.generate_by_index(
            url_idx=0,
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(object, completion, path=["response"])

        assert cast(Any, response.is_closed) is True
