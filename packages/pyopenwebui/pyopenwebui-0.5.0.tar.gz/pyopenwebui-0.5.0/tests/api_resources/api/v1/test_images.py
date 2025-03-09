# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generate(self, client: Pyopenwebui) -> None:
        image = client.api.v1.images.generate(
            prompt="prompt",
        )
        assert_matches_type(object, image, path=["response"])

    @parametrize
    def test_method_generate_with_all_params(self, client: Pyopenwebui) -> None:
        image = client.api.v1.images.generate(
            prompt="prompt",
            model="model",
            n=0,
            negative_prompt="negative_prompt",
            size="size",
        )
        assert_matches_type(object, image, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Pyopenwebui) -> None:
        response = client.api.v1.images.with_raw_response.generate(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(object, image, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Pyopenwebui) -> None:
        with client.api.v1.images.with_streaming_response.generate(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(object, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_models(self, client: Pyopenwebui) -> None:
        image = client.api.v1.images.get_models()
        assert_matches_type(object, image, path=["response"])

    @parametrize
    def test_raw_response_get_models(self, client: Pyopenwebui) -> None:
        response = client.api.v1.images.with_raw_response.get_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(object, image, path=["response"])

    @parametrize
    def test_streaming_response_get_models(self, client: Pyopenwebui) -> None:
        with client.api.v1.images.with_streaming_response.get_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(object, image, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_generate(self, async_client: AsyncPyopenwebui) -> None:
        image = await async_client.api.v1.images.generate(
            prompt="prompt",
        )
        assert_matches_type(object, image, path=["response"])

    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        image = await async_client.api.v1.images.generate(
            prompt="prompt",
            model="model",
            n=0,
            negative_prompt="negative_prompt",
            size="size",
        )
        assert_matches_type(object, image, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.images.with_raw_response.generate(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(object, image, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.images.with_streaming_response.generate(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(object, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_models(self, async_client: AsyncPyopenwebui) -> None:
        image = await async_client.api.v1.images.get_models()
        assert_matches_type(object, image, path=["response"])

    @parametrize
    async def test_raw_response_get_models(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.images.with_raw_response.get_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(object, image, path=["response"])

    @parametrize
    async def test_streaming_response_get_models(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.images.with_streaming_response.get_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(object, image, path=["response"])

        assert cast(Any, response.is_closed) is True
