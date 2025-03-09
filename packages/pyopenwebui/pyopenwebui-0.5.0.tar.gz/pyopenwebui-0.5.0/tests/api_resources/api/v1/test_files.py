# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1 import FileListResponse, FileUploadResponse
from pyopenwebui.types.shared import FileModel

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Pyopenwebui) -> None:
        file = client.api.v1.files.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Pyopenwebui) -> None:
        response = client.api.v1.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Pyopenwebui) -> None:
        with client.api.v1.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_all(self, client: Pyopenwebui) -> None:
        file = client.api.v1.files.delete_all()
        assert_matches_type(object, file, path=["response"])

    @parametrize
    def test_raw_response_delete_all(self, client: Pyopenwebui) -> None:
        response = client.api.v1.files.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(object, file, path=["response"])

    @parametrize
    def test_streaming_response_delete_all(self, client: Pyopenwebui) -> None:
        with client.api.v1.files.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_by_id(self, client: Pyopenwebui) -> None:
        file = client.api.v1.files.delete_by_id(
            "id",
        )
        assert_matches_type(object, file, path=["response"])

    @parametrize
    def test_raw_response_delete_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.files.with_raw_response.delete_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(object, file, path=["response"])

    @parametrize
    def test_streaming_response_delete_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.files.with_streaming_response.delete_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.files.with_raw_response.delete_by_id(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Pyopenwebui) -> None:
        file = client.api.v1.files.get_by_id(
            "id",
        )
        assert_matches_type(Optional[FileModel], file, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.files.with_raw_response.get_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(Optional[FileModel], file, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.files.with_streaming_response.get_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(Optional[FileModel], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.files.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_upload(self, client: Pyopenwebui) -> None:
        file = client.api.v1.files.upload(
            file=b"raw file contents",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: Pyopenwebui) -> None:
        file = client.api.v1.files.upload(
            file=b"raw file contents",
            file_metadata={},
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Pyopenwebui) -> None:
        response = client.api.v1.files.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Pyopenwebui) -> None:
        with client.api.v1.files.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncPyopenwebui) -> None:
        file = await async_client.api.v1.files.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_all(self, async_client: AsyncPyopenwebui) -> None:
        file = await async_client.api.v1.files.delete_all()
        assert_matches_type(object, file, path=["response"])

    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.files.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(object, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.files.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        file = await async_client.api.v1.files.delete_by_id(
            "id",
        )
        assert_matches_type(object, file, path=["response"])

    @parametrize
    async def test_raw_response_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.files.with_raw_response.delete_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(object, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.files.with_streaming_response.delete_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.files.with_raw_response.delete_by_id(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        file = await async_client.api.v1.files.get_by_id(
            "id",
        )
        assert_matches_type(Optional[FileModel], file, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.files.with_raw_response.get_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(Optional[FileModel], file, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.files.with_streaming_response.get_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(Optional[FileModel], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.files.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_upload(self, async_client: AsyncPyopenwebui) -> None:
        file = await async_client.api.v1.files.upload(
            file=b"raw file contents",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        file = await async_client.api.v1.files.upload(
            file=b"raw file contents",
            file_metadata={},
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.files.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.files.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
