# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCopy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_copy(self, client: Pyopenwebui) -> None:
        copy = client.ollama.api.copy.copy(
            destination="destination",
            source="source",
        )
        assert_matches_type(object, copy, path=["response"])

    @parametrize
    def test_method_copy_with_all_params(self, client: Pyopenwebui) -> None:
        copy = client.ollama.api.copy.copy(
            destination="destination",
            source="source",
            url_idx=0,
        )
        assert_matches_type(object, copy, path=["response"])

    @parametrize
    def test_raw_response_copy(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.copy.with_raw_response.copy(
            destination="destination",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        copy = response.parse()
        assert_matches_type(object, copy, path=["response"])

    @parametrize
    def test_streaming_response_copy(self, client: Pyopenwebui) -> None:
        with client.ollama.api.copy.with_streaming_response.copy(
            destination="destination",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            copy = response.parse()
            assert_matches_type(object, copy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_copy_by_index(self, client: Pyopenwebui) -> None:
        copy = client.ollama.api.copy.copy_by_index(
            url_idx=0,
            destination="destination",
            source="source",
        )
        assert_matches_type(object, copy, path=["response"])

    @parametrize
    def test_raw_response_copy_by_index(self, client: Pyopenwebui) -> None:
        response = client.ollama.api.copy.with_raw_response.copy_by_index(
            url_idx=0,
            destination="destination",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        copy = response.parse()
        assert_matches_type(object, copy, path=["response"])

    @parametrize
    def test_streaming_response_copy_by_index(self, client: Pyopenwebui) -> None:
        with client.ollama.api.copy.with_streaming_response.copy_by_index(
            url_idx=0,
            destination="destination",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            copy = response.parse()
            assert_matches_type(object, copy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCopy:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_copy(self, async_client: AsyncPyopenwebui) -> None:
        copy = await async_client.ollama.api.copy.copy(
            destination="destination",
            source="source",
        )
        assert_matches_type(object, copy, path=["response"])

    @parametrize
    async def test_method_copy_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        copy = await async_client.ollama.api.copy.copy(
            destination="destination",
            source="source",
            url_idx=0,
        )
        assert_matches_type(object, copy, path=["response"])

    @parametrize
    async def test_raw_response_copy(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.copy.with_raw_response.copy(
            destination="destination",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        copy = await response.parse()
        assert_matches_type(object, copy, path=["response"])

    @parametrize
    async def test_streaming_response_copy(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.copy.with_streaming_response.copy(
            destination="destination",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            copy = await response.parse()
            assert_matches_type(object, copy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_copy_by_index(self, async_client: AsyncPyopenwebui) -> None:
        copy = await async_client.ollama.api.copy.copy_by_index(
            url_idx=0,
            destination="destination",
            source="source",
        )
        assert_matches_type(object, copy, path=["response"])

    @parametrize
    async def test_raw_response_copy_by_index(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.api.copy.with_raw_response.copy_by_index(
            url_idx=0,
            destination="destination",
            source="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        copy = await response.parse()
        assert_matches_type(object, copy, path=["response"])

    @parametrize
    async def test_streaming_response_copy_by_index(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.api.copy.with_streaming_response.copy_by_index(
            url_idx=0,
            destination="destination",
            source="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            copy = await response.parse()
            assert_matches_type(object, copy, path=["response"])

        assert cast(Any, response.is_closed) is True
