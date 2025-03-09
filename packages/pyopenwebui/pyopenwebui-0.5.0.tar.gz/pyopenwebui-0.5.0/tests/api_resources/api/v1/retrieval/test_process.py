# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProcess:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_file(self, client: Pyopenwebui) -> None:
        process = client.api.v1.retrieval.process.file(
            file_id="file_id",
        )
        assert_matches_type(object, process, path=["response"])

    @parametrize
    def test_method_file_with_all_params(self, client: Pyopenwebui) -> None:
        process = client.api.v1.retrieval.process.file(
            file_id="file_id",
            collection_name="collection_name",
            content="content",
        )
        assert_matches_type(object, process, path=["response"])

    @parametrize
    def test_raw_response_file(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.process.with_raw_response.file(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = response.parse()
        assert_matches_type(object, process, path=["response"])

    @parametrize
    def test_streaming_response_file(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.process.with_streaming_response.file(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = response.parse()
            assert_matches_type(object, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_text(self, client: Pyopenwebui) -> None:
        process = client.api.v1.retrieval.process.text(
            content="content",
            name="name",
        )
        assert_matches_type(object, process, path=["response"])

    @parametrize
    def test_method_text_with_all_params(self, client: Pyopenwebui) -> None:
        process = client.api.v1.retrieval.process.text(
            content="content",
            name="name",
            collection_name="collection_name",
        )
        assert_matches_type(object, process, path=["response"])

    @parametrize
    def test_raw_response_text(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.process.with_raw_response.text(
            content="content",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = response.parse()
        assert_matches_type(object, process, path=["response"])

    @parametrize
    def test_streaming_response_text(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.process.with_streaming_response.text(
            content="content",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = response.parse()
            assert_matches_type(object, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_youtube(self, client: Pyopenwebui) -> None:
        process = client.api.v1.retrieval.process.youtube(
            url="url",
        )
        assert_matches_type(object, process, path=["response"])

    @parametrize
    def test_method_youtube_with_all_params(self, client: Pyopenwebui) -> None:
        process = client.api.v1.retrieval.process.youtube(
            url="url",
            collection_name="collection_name",
        )
        assert_matches_type(object, process, path=["response"])

    @parametrize
    def test_raw_response_youtube(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.process.with_raw_response.youtube(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = response.parse()
        assert_matches_type(object, process, path=["response"])

    @parametrize
    def test_streaming_response_youtube(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.process.with_streaming_response.youtube(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = response.parse()
            assert_matches_type(object, process, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProcess:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_file(self, async_client: AsyncPyopenwebui) -> None:
        process = await async_client.api.v1.retrieval.process.file(
            file_id="file_id",
        )
        assert_matches_type(object, process, path=["response"])

    @parametrize
    async def test_method_file_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        process = await async_client.api.v1.retrieval.process.file(
            file_id="file_id",
            collection_name="collection_name",
            content="content",
        )
        assert_matches_type(object, process, path=["response"])

    @parametrize
    async def test_raw_response_file(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.process.with_raw_response.file(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = await response.parse()
        assert_matches_type(object, process, path=["response"])

    @parametrize
    async def test_streaming_response_file(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.process.with_streaming_response.file(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = await response.parse()
            assert_matches_type(object, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_text(self, async_client: AsyncPyopenwebui) -> None:
        process = await async_client.api.v1.retrieval.process.text(
            content="content",
            name="name",
        )
        assert_matches_type(object, process, path=["response"])

    @parametrize
    async def test_method_text_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        process = await async_client.api.v1.retrieval.process.text(
            content="content",
            name="name",
            collection_name="collection_name",
        )
        assert_matches_type(object, process, path=["response"])

    @parametrize
    async def test_raw_response_text(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.process.with_raw_response.text(
            content="content",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = await response.parse()
        assert_matches_type(object, process, path=["response"])

    @parametrize
    async def test_streaming_response_text(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.process.with_streaming_response.text(
            content="content",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = await response.parse()
            assert_matches_type(object, process, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_youtube(self, async_client: AsyncPyopenwebui) -> None:
        process = await async_client.api.v1.retrieval.process.youtube(
            url="url",
        )
        assert_matches_type(object, process, path=["response"])

    @parametrize
    async def test_method_youtube_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        process = await async_client.api.v1.retrieval.process.youtube(
            url="url",
            collection_name="collection_name",
        )
        assert_matches_type(object, process, path=["response"])

    @parametrize
    async def test_raw_response_youtube(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.process.with_raw_response.youtube(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        process = await response.parse()
        assert_matches_type(object, process, path=["response"])

    @parametrize
    async def test_streaming_response_youtube(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.process.with_streaming_response.youtube(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            process = await response.parse()
            assert_matches_type(object, process, path=["response"])

        assert cast(Any, response.is_closed) is True
