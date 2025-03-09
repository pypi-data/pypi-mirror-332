# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.configs import ModelGetResponse, ModelSetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        model = client.api.v1.configs.models.get()
        assert_matches_type(ModelGetResponse, model, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.configs.models.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelGetResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.configs.models.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelGetResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set(self, client: Pyopenwebui) -> None:
        model = client.api.v1.configs.models.set(
            default_models="DEFAULT_MODELS",
            model_order_list=["string"],
        )
        assert_matches_type(ModelSetResponse, model, path=["response"])

    @parametrize
    def test_raw_response_set(self, client: Pyopenwebui) -> None:
        response = client.api.v1.configs.models.with_raw_response.set(
            default_models="DEFAULT_MODELS",
            model_order_list=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelSetResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_set(self, client: Pyopenwebui) -> None:
        with client.api.v1.configs.models.with_streaming_response.set(
            default_models="DEFAULT_MODELS",
            model_order_list=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelSetResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        model = await async_client.api.v1.configs.models.get()
        assert_matches_type(ModelGetResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.configs.models.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelGetResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.configs.models.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelGetResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set(self, async_client: AsyncPyopenwebui) -> None:
        model = await async_client.api.v1.configs.models.set(
            default_models="DEFAULT_MODELS",
            model_order_list=["string"],
        )
        assert_matches_type(ModelSetResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_set(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.configs.models.with_raw_response.set(
            default_models="DEFAULT_MODELS",
            model_order_list=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelSetResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.configs.models.with_streaming_response.set(
            default_models="DEFAULT_MODELS",
            model_order_list=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelSetResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True
