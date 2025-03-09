# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.knowledge import (
    FileAddResponse,
    FileRemoveResponse,
    FileUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Pyopenwebui) -> None:
        file = client.api.v1.knowledge.file.update(
            id="id",
            file_id="file_id",
        )
        assert_matches_type(Optional[FileUpdateResponse], file, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Pyopenwebui) -> None:
        response = client.api.v1.knowledge.file.with_raw_response.update(
            id="id",
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(Optional[FileUpdateResponse], file, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Pyopenwebui) -> None:
        with client.api.v1.knowledge.file.with_streaming_response.update(
            id="id",
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(Optional[FileUpdateResponse], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.knowledge.file.with_raw_response.update(
                id="",
                file_id="file_id",
            )

    @parametrize
    def test_method_add(self, client: Pyopenwebui) -> None:
        file = client.api.v1.knowledge.file.add(
            id="id",
            file_id="file_id",
        )
        assert_matches_type(Optional[FileAddResponse], file, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Pyopenwebui) -> None:
        response = client.api.v1.knowledge.file.with_raw_response.add(
            id="id",
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(Optional[FileAddResponse], file, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Pyopenwebui) -> None:
        with client.api.v1.knowledge.file.with_streaming_response.add(
            id="id",
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(Optional[FileAddResponse], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.knowledge.file.with_raw_response.add(
                id="",
                file_id="file_id",
            )

    @parametrize
    def test_method_remove(self, client: Pyopenwebui) -> None:
        file = client.api.v1.knowledge.file.remove(
            id="id",
            file_id="file_id",
        )
        assert_matches_type(Optional[FileRemoveResponse], file, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Pyopenwebui) -> None:
        response = client.api.v1.knowledge.file.with_raw_response.remove(
            id="id",
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(Optional[FileRemoveResponse], file, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Pyopenwebui) -> None:
        with client.api.v1.knowledge.file.with_streaming_response.remove(
            id="id",
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(Optional[FileRemoveResponse], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.knowledge.file.with_raw_response.remove(
                id="",
                file_id="file_id",
            )


class TestAsyncFile:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncPyopenwebui) -> None:
        file = await async_client.api.v1.knowledge.file.update(
            id="id",
            file_id="file_id",
        )
        assert_matches_type(Optional[FileUpdateResponse], file, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.knowledge.file.with_raw_response.update(
            id="id",
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(Optional[FileUpdateResponse], file, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.knowledge.file.with_streaming_response.update(
            id="id",
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(Optional[FileUpdateResponse], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.knowledge.file.with_raw_response.update(
                id="",
                file_id="file_id",
            )

    @parametrize
    async def test_method_add(self, async_client: AsyncPyopenwebui) -> None:
        file = await async_client.api.v1.knowledge.file.add(
            id="id",
            file_id="file_id",
        )
        assert_matches_type(Optional[FileAddResponse], file, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.knowledge.file.with_raw_response.add(
            id="id",
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(Optional[FileAddResponse], file, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.knowledge.file.with_streaming_response.add(
            id="id",
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(Optional[FileAddResponse], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.knowledge.file.with_raw_response.add(
                id="",
                file_id="file_id",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncPyopenwebui) -> None:
        file = await async_client.api.v1.knowledge.file.remove(
            id="id",
            file_id="file_id",
        )
        assert_matches_type(Optional[FileRemoveResponse], file, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.knowledge.file.with_raw_response.remove(
            id="id",
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(Optional[FileRemoveResponse], file, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.knowledge.file.with_streaming_response.remove(
            id="id",
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(Optional[FileRemoveResponse], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.knowledge.file.with_raw_response.remove(
                id="",
                file_id="file_id",
            )
