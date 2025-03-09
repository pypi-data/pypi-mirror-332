# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types import ModelModel
from pyopenwebui.types.api.v1 import (
    ModelGetResponse,
    ModelDeleteResponse,
    ModelGetBaseResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Pyopenwebui) -> None:
        model = client.api.v1.models.create(
            id="id",
            meta={},
            name="name",
            params={"foo": "bar"},
        )
        assert_matches_type(Optional[ModelModel], model, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Pyopenwebui) -> None:
        model = client.api.v1.models.create(
            id="id",
            meta={
                "capabilities": {},
                "description": "description",
                "profile_image_url": "profile_image_url",
            },
            name="name",
            params={"foo": "bar"},
            access_control={},
            base_model_id="base_model_id",
            is_active=True,
        )
        assert_matches_type(Optional[ModelModel], model, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Pyopenwebui) -> None:
        response = client.api.v1.models.with_raw_response.create(
            id="id",
            meta={},
            name="name",
            params={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(Optional[ModelModel], model, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Pyopenwebui) -> None:
        with client.api.v1.models.with_streaming_response.create(
            id="id",
            meta={},
            name="name",
            params={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(Optional[ModelModel], model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Pyopenwebui) -> None:
        model = client.api.v1.models.delete()
        assert_matches_type(ModelDeleteResponse, model, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Pyopenwebui) -> None:
        response = client.api.v1.models.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelDeleteResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Pyopenwebui) -> None:
        with client.api.v1.models.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelDeleteResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        model = client.api.v1.models.get()
        assert_matches_type(ModelGetResponse, model, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Pyopenwebui) -> None:
        model = client.api.v1.models.get(
            id="id",
        )
        assert_matches_type(ModelGetResponse, model, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.models.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelGetResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.models.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelGetResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_base(self, client: Pyopenwebui) -> None:
        model = client.api.v1.models.get_base()
        assert_matches_type(ModelGetBaseResponse, model, path=["response"])

    @parametrize
    def test_raw_response_get_base(self, client: Pyopenwebui) -> None:
        response = client.api.v1.models.with_raw_response.get_base()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelGetBaseResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_get_base(self, client: Pyopenwebui) -> None:
        with client.api.v1.models.with_streaming_response.get_base() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelGetBaseResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPyopenwebui) -> None:
        model = await async_client.api.v1.models.create(
            id="id",
            meta={},
            name="name",
            params={"foo": "bar"},
        )
        assert_matches_type(Optional[ModelModel], model, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        model = await async_client.api.v1.models.create(
            id="id",
            meta={
                "capabilities": {},
                "description": "description",
                "profile_image_url": "profile_image_url",
            },
            name="name",
            params={"foo": "bar"},
            access_control={},
            base_model_id="base_model_id",
            is_active=True,
        )
        assert_matches_type(Optional[ModelModel], model, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.models.with_raw_response.create(
            id="id",
            meta={},
            name="name",
            params={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(Optional[ModelModel], model, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.models.with_streaming_response.create(
            id="id",
            meta={},
            name="name",
            params={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(Optional[ModelModel], model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPyopenwebui) -> None:
        model = await async_client.api.v1.models.delete()
        assert_matches_type(ModelDeleteResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.models.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelDeleteResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.models.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelDeleteResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        model = await async_client.api.v1.models.get()
        assert_matches_type(ModelGetResponse, model, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        model = await async_client.api.v1.models.get(
            id="id",
        )
        assert_matches_type(ModelGetResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.models.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelGetResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.models.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelGetResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_base(self, async_client: AsyncPyopenwebui) -> None:
        model = await async_client.api.v1.models.get_base()
        assert_matches_type(ModelGetBaseResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_get_base(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.models.with_raw_response.get_base()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelGetBaseResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_get_base(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.models.with_streaming_response.get_base() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelGetBaseResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True
