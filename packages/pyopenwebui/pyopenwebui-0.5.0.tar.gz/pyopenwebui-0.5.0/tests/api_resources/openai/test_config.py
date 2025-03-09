# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Pyopenwebui) -> None:
        config = client.openai.config.retrieve()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Pyopenwebui) -> None:
        response = client.openai.config.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Pyopenwebui) -> None:
        with client.openai.config.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Pyopenwebui) -> None:
        config = client.openai.config.update(
            openai_api_base_urls=["string"],
            openai_api_configs={},
            openai_api_keys=["string"],
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Pyopenwebui) -> None:
        config = client.openai.config.update(
            openai_api_base_urls=["string"],
            openai_api_configs={},
            openai_api_keys=["string"],
            enable_openai_api=True,
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Pyopenwebui) -> None:
        response = client.openai.config.with_raw_response.update(
            openai_api_base_urls=["string"],
            openai_api_configs={},
            openai_api_keys=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Pyopenwebui) -> None:
        with client.openai.config.with_streaming_response.update(
            openai_api_base_urls=["string"],
            openai_api_configs={},
            openai_api_keys=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.openai.config.retrieve()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.openai.config.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.openai.config.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.openai.config.update(
            openai_api_base_urls=["string"],
            openai_api_configs={},
            openai_api_keys=["string"],
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.openai.config.update(
            openai_api_base_urls=["string"],
            openai_api_configs={},
            openai_api_keys=["string"],
            enable_openai_api=True,
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.openai.config.with_raw_response.update(
            openai_api_base_urls=["string"],
            openai_api_configs={},
            openai_api_keys=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.openai.config.with_streaming_response.update(
            openai_api_base_urls=["string"],
            openai_api_configs={},
            openai_api_keys=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True
