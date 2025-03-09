# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types import FunctionResponse
from pyopenwebui.types.api.v1 import FunctionGetResponse, FunctionGetExportResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Pyopenwebui) -> None:
        function = client.api.v1.functions.create(
            id="id",
            content="content",
            meta={},
            name="name",
        )
        assert_matches_type(Optional[FunctionResponse], function, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Pyopenwebui) -> None:
        function = client.api.v1.functions.create(
            id="id",
            content="content",
            meta={
                "description": "description",
                "manifest": {},
            },
            name="name",
        )
        assert_matches_type(Optional[FunctionResponse], function, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Pyopenwebui) -> None:
        response = client.api.v1.functions.with_raw_response.create(
            id="id",
            content="content",
            meta={},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(Optional[FunctionResponse], function, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Pyopenwebui) -> None:
        with client.api.v1.functions.with_streaming_response.create(
            id="id",
            content="content",
            meta={},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(Optional[FunctionResponse], function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        function = client.api.v1.functions.get()
        assert_matches_type(FunctionGetResponse, function, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.functions.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionGetResponse, function, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.functions.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionGetResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_export(self, client: Pyopenwebui) -> None:
        function = client.api.v1.functions.get_export()
        assert_matches_type(FunctionGetExportResponse, function, path=["response"])

    @parametrize
    def test_raw_response_get_export(self, client: Pyopenwebui) -> None:
        response = client.api.v1.functions.with_raw_response.get_export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionGetExportResponse, function, path=["response"])

    @parametrize
    def test_streaming_response_get_export(self, client: Pyopenwebui) -> None:
        with client.api.v1.functions.with_streaming_response.get_export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionGetExportResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFunctions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPyopenwebui) -> None:
        function = await async_client.api.v1.functions.create(
            id="id",
            content="content",
            meta={},
            name="name",
        )
        assert_matches_type(Optional[FunctionResponse], function, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        function = await async_client.api.v1.functions.create(
            id="id",
            content="content",
            meta={
                "description": "description",
                "manifest": {},
            },
            name="name",
        )
        assert_matches_type(Optional[FunctionResponse], function, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.functions.with_raw_response.create(
            id="id",
            content="content",
            meta={},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(Optional[FunctionResponse], function, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.functions.with_streaming_response.create(
            id="id",
            content="content",
            meta={},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(Optional[FunctionResponse], function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        function = await async_client.api.v1.functions.get()
        assert_matches_type(FunctionGetResponse, function, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.functions.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionGetResponse, function, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.functions.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionGetResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_export(self, async_client: AsyncPyopenwebui) -> None:
        function = await async_client.api.v1.functions.get_export()
        assert_matches_type(FunctionGetExportResponse, function, path=["response"])

    @parametrize
    async def test_raw_response_get_export(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.functions.with_raw_response.get_export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionGetExportResponse, function, path=["response"])

    @parametrize
    async def test_streaming_response_get_export(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.functions.with_streaming_response.get_export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionGetExportResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True
