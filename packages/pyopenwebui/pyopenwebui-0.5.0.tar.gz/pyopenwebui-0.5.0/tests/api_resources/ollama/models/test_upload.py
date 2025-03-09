# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUpload:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_upload(self, client: Pyopenwebui) -> None:
        upload = client.ollama.models.upload.upload(
            file=b"raw file contents",
        )
        assert_matches_type(object, upload, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: Pyopenwebui) -> None:
        upload = client.ollama.models.upload.upload(
            file=b"raw file contents",
            url_idx=0,
        )
        assert_matches_type(object, upload, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Pyopenwebui) -> None:
        response = client.ollama.models.upload.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(object, upload, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Pyopenwebui) -> None:
        with client.ollama.models.upload.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(object, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_by_index(self, client: Pyopenwebui) -> None:
        upload = client.ollama.models.upload.upload_by_index(
            url_idx=0,
            file=b"raw file contents",
        )
        assert_matches_type(object, upload, path=["response"])

    @parametrize
    def test_raw_response_upload_by_index(self, client: Pyopenwebui) -> None:
        response = client.ollama.models.upload.with_raw_response.upload_by_index(
            url_idx=0,
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(object, upload, path=["response"])

    @parametrize
    def test_streaming_response_upload_by_index(self, client: Pyopenwebui) -> None:
        with client.ollama.models.upload.with_streaming_response.upload_by_index(
            url_idx=0,
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(object, upload, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUpload:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_upload(self, async_client: AsyncPyopenwebui) -> None:
        upload = await async_client.ollama.models.upload.upload(
            file=b"raw file contents",
        )
        assert_matches_type(object, upload, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        upload = await async_client.ollama.models.upload.upload(
            file=b"raw file contents",
            url_idx=0,
        )
        assert_matches_type(object, upload, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.models.upload.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(object, upload, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.models.upload.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(object, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_by_index(self, async_client: AsyncPyopenwebui) -> None:
        upload = await async_client.ollama.models.upload.upload_by_index(
            url_idx=0,
            file=b"raw file contents",
        )
        assert_matches_type(object, upload, path=["response"])

    @parametrize
    async def test_raw_response_upload_by_index(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.ollama.models.upload.with_raw_response.upload_by_index(
            url_idx=0,
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(object, upload, path=["response"])

    @parametrize
    async def test_streaming_response_upload_by_index(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.ollama.models.upload.with_streaming_response.upload_by_index(
            url_idx=0,
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(object, upload, path=["response"])

        assert cast(Any, response.is_closed) is True
