# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDownload:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_download(self, client: Pyopenwebui) -> None:
        download = client.ollama.models.download.download(
            url="url",
        )
        assert_matches_type(object, download, path=["response"])

    @parametrize
    def test_method_download_with_all_params(self, client: Pyopenwebui) -> None:
        download = client.ollama.models.download.download(
            url="url",
            url_idx=0,
        )
        assert_matches_type(object, download, path=["response"])

    @parametrize
    def test_raw_response_download(self, client: Pyopenwebui) -> None:
        response = client.ollama.models.download.with_raw_response.download(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = response.parse()
        assert_matches_type(object, download, path=["response"])

    @parametrize
    def test_streaming_response_download(self, client: Pyopenwebui) -> None:
        with client.ollama.models.download.with_streaming_response.download(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = response.parse()
            assert_matches_type(object, download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_download_by_index(self, client: Pyopenwebui) -> None:
        download = client.ollama.models.download.download_by_index(
            url_idx=0,
            url="url",
        )
        assert_matches_type(object, download, path=["response"])

    @parametrize
    def test_raw_response_download_by_index(self, client: Pyopenwebui) -> None:
        response = client.ollama.models.download.with_raw_response.download_by_index(
            url_idx=0,
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = response.parse()
        assert_matches_type(object, download, path=["response"])

    @parametrize
    def test_streaming_response_download_by_index(self, client: Pyopenwebui) -> None:
        with client.ollama.models.download.with_streaming_response.download_by_index(
            url_idx=0,
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = response.parse()
            assert_matches_type(object, download, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDownload:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_download(self, async_client: AsyncPyopenwebui) -> None:
        download = await async_client.ollama.models.download.download(
            url="url",
        )
        assert_matches_type(object, download, path=["response"])

    @parametrize
    async def test_method_download_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        download = await async_client.ollama.models.download.download(
            url="url",
            url_idx=0,
        )
        assert_matches_type(object, download, path=["response"])

    @parametrize
    async def test_raw_response_download(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.models.download.with_raw_response.download(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = await response.parse()
        assert_matches_type(object, download, path=["response"])

    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.models.download.with_streaming_response.download(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = await response.parse()
            assert_matches_type(object, download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_download_by_index(self, async_client: AsyncPyopenwebui) -> None:
        download = await async_client.ollama.models.download.download_by_index(
            url_idx=0,
            url="url",
        )
        assert_matches_type(object, download, path=["response"])

    @parametrize
    async def test_raw_response_download_by_index(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.models.download.with_raw_response.download_by_index(
            url_idx=0,
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = await response.parse()
        assert_matches_type(object, download, path=["response"])

    @parametrize
    async def test_streaming_response_download_by_index(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.models.download.with_streaming_response.download_by_index(
            url_idx=0,
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = await response.parse()
            assert_matches_type(object, download, path=["response"])

        assert cast(Any, response.is_closed) is True
