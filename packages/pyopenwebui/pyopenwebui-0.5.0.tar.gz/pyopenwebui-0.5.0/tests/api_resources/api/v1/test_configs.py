# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1 import ConfigSetSuggestionsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_export(self, client: Pyopenwebui) -> None:
        config = client.api.v1.configs.export()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Pyopenwebui) -> None:
        response = client.api.v1.configs.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Pyopenwebui) -> None:
        with client.api.v1.configs.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_import(self, client: Pyopenwebui) -> None:
        config = client.api.v1.configs.import_(
            config={},
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_raw_response_import(self, client: Pyopenwebui) -> None:
        response = client.api.v1.configs.with_raw_response.import_(
            config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_streaming_response_import(self, client: Pyopenwebui) -> None:
        with client.api.v1.configs.with_streaming_response.import_(
            config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_suggestions(self, client: Pyopenwebui) -> None:
        config = client.api.v1.configs.set_suggestions(
            suggestions=[
                {
                    "content": "content",
                    "title": ["string"],
                }
            ],
        )
        assert_matches_type(ConfigSetSuggestionsResponse, config, path=["response"])

    @parametrize
    def test_raw_response_set_suggestions(self, client: Pyopenwebui) -> None:
        response = client.api.v1.configs.with_raw_response.set_suggestions(
            suggestions=[
                {
                    "content": "content",
                    "title": ["string"],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigSetSuggestionsResponse, config, path=["response"])

    @parametrize
    def test_streaming_response_set_suggestions(self, client: Pyopenwebui) -> None:
        with client.api.v1.configs.with_streaming_response.set_suggestions(
            suggestions=[
                {
                    "content": "content",
                    "title": ["string"],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigSetSuggestionsResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_export(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.api.v1.configs.export()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.configs.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.configs.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_import(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.api.v1.configs.import_(
            config={},
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_raw_response_import(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.configs.with_raw_response.import_(
            config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.configs.with_streaming_response.import_(
            config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_suggestions(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.api.v1.configs.set_suggestions(
            suggestions=[
                {
                    "content": "content",
                    "title": ["string"],
                }
            ],
        )
        assert_matches_type(ConfigSetSuggestionsResponse, config, path=["response"])

    @parametrize
    async def test_raw_response_set_suggestions(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.configs.with_raw_response.set_suggestions(
            suggestions=[
                {
                    "content": "content",
                    "title": ["string"],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigSetSuggestionsResponse, config, path=["response"])

    @parametrize
    async def test_streaming_response_set_suggestions(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.configs.with_streaming_response.set_suggestions(
            suggestions=[
                {
                    "content": "content",
                    "title": ["string"],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigSetSuggestionsResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True
