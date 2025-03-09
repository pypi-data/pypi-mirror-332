# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.evaluations.feedbacks import AllGetResponse, AllExportResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAll:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Pyopenwebui) -> None:
        all = client.api.v1.evaluations.feedbacks.all.delete()
        assert_matches_type(object, all, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Pyopenwebui) -> None:
        response = client.api.v1.evaluations.feedbacks.all.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        all = response.parse()
        assert_matches_type(object, all, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Pyopenwebui) -> None:
        with client.api.v1.evaluations.feedbacks.all.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            all = response.parse()
            assert_matches_type(object, all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_export(self, client: Pyopenwebui) -> None:
        all = client.api.v1.evaluations.feedbacks.all.export()
        assert_matches_type(AllExportResponse, all, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Pyopenwebui) -> None:
        response = client.api.v1.evaluations.feedbacks.all.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        all = response.parse()
        assert_matches_type(AllExportResponse, all, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Pyopenwebui) -> None:
        with client.api.v1.evaluations.feedbacks.all.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            all = response.parse()
            assert_matches_type(AllExportResponse, all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        all = client.api.v1.evaluations.feedbacks.all.get()
        assert_matches_type(AllGetResponse, all, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.evaluations.feedbacks.all.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        all = response.parse()
        assert_matches_type(AllGetResponse, all, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.evaluations.feedbacks.all.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            all = response.parse()
            assert_matches_type(AllGetResponse, all, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAll:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncPyopenwebui) -> None:
        all = await async_client.api.v1.evaluations.feedbacks.all.delete()
        assert_matches_type(object, all, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.evaluations.feedbacks.all.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        all = await response.parse()
        assert_matches_type(object, all, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.evaluations.feedbacks.all.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            all = await response.parse()
            assert_matches_type(object, all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_export(self, async_client: AsyncPyopenwebui) -> None:
        all = await async_client.api.v1.evaluations.feedbacks.all.export()
        assert_matches_type(AllExportResponse, all, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.evaluations.feedbacks.all.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        all = await response.parse()
        assert_matches_type(AllExportResponse, all, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.evaluations.feedbacks.all.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            all = await response.parse()
            assert_matches_type(AllExportResponse, all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        all = await async_client.api.v1.evaluations.feedbacks.all.get()
        assert_matches_type(AllGetResponse, all, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.evaluations.feedbacks.all.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        all = await response.parse()
        assert_matches_type(AllGetResponse, all, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.evaluations.feedbacks.all.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            all = await response.parse()
            assert_matches_type(AllGetResponse, all, path=["response"])

        assert cast(Any, response.is_closed) is True
