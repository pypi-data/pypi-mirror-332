# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.retrieval.process import FileBatchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_batch(self, client: Pyopenwebui) -> None:
        file = client.api.v1.retrieval.process.files.batch(
            collection_name="collection_name",
            files=[
                {
                    "id": "id",
                    "created_at": 0,
                    "filename": "filename",
                    "updated_at": 0,
                    "user_id": "user_id",
                }
            ],
        )
        assert_matches_type(FileBatchResponse, file, path=["response"])

    @parametrize
    def test_raw_response_batch(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.process.files.with_raw_response.batch(
            collection_name="collection_name",
            files=[
                {
                    "id": "id",
                    "created_at": 0,
                    "filename": "filename",
                    "updated_at": 0,
                    "user_id": "user_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileBatchResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_batch(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.process.files.with_streaming_response.batch(
            collection_name="collection_name",
            files=[
                {
                    "id": "id",
                    "created_at": 0,
                    "filename": "filename",
                    "updated_at": 0,
                    "user_id": "user_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileBatchResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_batch(self, async_client: AsyncPyopenwebui) -> None:
        file = await async_client.api.v1.retrieval.process.files.batch(
            collection_name="collection_name",
            files=[
                {
                    "id": "id",
                    "created_at": 0,
                    "filename": "filename",
                    "updated_at": 0,
                    "user_id": "user_id",
                }
            ],
        )
        assert_matches_type(FileBatchResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.process.files.with_raw_response.batch(
            collection_name="collection_name",
            files=[
                {
                    "id": "id",
                    "created_at": 0,
                    "filename": "filename",
                    "updated_at": 0,
                    "user_id": "user_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileBatchResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.process.files.with_streaming_response.batch(
            collection_name="collection_name",
            files=[
                {
                    "id": "id",
                    "created_at": 0,
                    "filename": "filename",
                    "updated_at": 0,
                    "user_id": "user_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileBatchResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
