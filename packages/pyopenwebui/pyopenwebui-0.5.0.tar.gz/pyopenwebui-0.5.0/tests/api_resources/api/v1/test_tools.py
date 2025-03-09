# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types import ToolResponse
from pyopenwebui.types.api.v1 import ToolGetResponse, ToolExportResponse, ToolGetListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Pyopenwebui) -> None:
        tool = client.api.v1.tools.create(
            id="id",
            content="content",
            meta={},
            name="name",
        )
        assert_matches_type(Optional[ToolResponse], tool, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Pyopenwebui) -> None:
        tool = client.api.v1.tools.create(
            id="id",
            content="content",
            meta={
                "description": "description",
                "manifest": {},
            },
            name="name",
            access_control={},
        )
        assert_matches_type(Optional[ToolResponse], tool, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Pyopenwebui) -> None:
        response = client.api.v1.tools.with_raw_response.create(
            id="id",
            content="content",
            meta={},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Optional[ToolResponse], tool, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Pyopenwebui) -> None:
        with client.api.v1.tools.with_streaming_response.create(
            id="id",
            content="content",
            meta={},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Optional[ToolResponse], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_export(self, client: Pyopenwebui) -> None:
        tool = client.api.v1.tools.export()
        assert_matches_type(ToolExportResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Pyopenwebui) -> None:
        response = client.api.v1.tools.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolExportResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Pyopenwebui) -> None:
        with client.api.v1.tools.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolExportResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        tool = client.api.v1.tools.get()
        assert_matches_type(ToolGetResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.tools.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolGetResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.tools.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolGetResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_list(self, client: Pyopenwebui) -> None:
        tool = client.api.v1.tools.get_list()
        assert_matches_type(ToolGetListResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_get_list(self, client: Pyopenwebui) -> None:
        response = client.api.v1.tools.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolGetListResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_get_list(self, client: Pyopenwebui) -> None:
        with client.api.v1.tools.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolGetListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPyopenwebui) -> None:
        tool = await async_client.api.v1.tools.create(
            id="id",
            content="content",
            meta={},
            name="name",
        )
        assert_matches_type(Optional[ToolResponse], tool, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        tool = await async_client.api.v1.tools.create(
            id="id",
            content="content",
            meta={
                "description": "description",
                "manifest": {},
            },
            name="name",
            access_control={},
        )
        assert_matches_type(Optional[ToolResponse], tool, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.tools.with_raw_response.create(
            id="id",
            content="content",
            meta={},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Optional[ToolResponse], tool, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.tools.with_streaming_response.create(
            id="id",
            content="content",
            meta={},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Optional[ToolResponse], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_export(self, async_client: AsyncPyopenwebui) -> None:
        tool = await async_client.api.v1.tools.export()
        assert_matches_type(ToolExportResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.tools.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolExportResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.tools.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolExportResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        tool = await async_client.api.v1.tools.get()
        assert_matches_type(ToolGetResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.tools.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolGetResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.tools.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolGetResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_list(self, async_client: AsyncPyopenwebui) -> None:
        tool = await async_client.api.v1.tools.get_list()
        assert_matches_type(ToolGetListResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_get_list(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.tools.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolGetListResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_get_list(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.tools.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolGetListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True
