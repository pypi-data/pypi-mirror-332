# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetrieval:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete_entries(self, client: Pyopenwebui) -> None:
        retrieval = client.api.v1.retrieval.delete_entries(
            collection_name="collection_name",
            file_id="file_id",
        )
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    def test_raw_response_delete_entries(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.with_raw_response.delete_entries(
            collection_name="collection_name",
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    def test_streaming_response_delete_entries(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.with_streaming_response.delete_entries(
            collection_name="collection_name",
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(object, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_embeddings(self, client: Pyopenwebui) -> None:
        retrieval = client.api.v1.retrieval.get_embeddings(
            "text",
        )
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    def test_raw_response_get_embeddings(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.with_raw_response.get_embeddings(
            "text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    def test_streaming_response_get_embeddings(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.with_streaming_response.get_embeddings(
            "text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(object, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_embeddings(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `text` but received ''"):
            client.api.v1.retrieval.with_raw_response.get_embeddings(
                "",
            )

    @parametrize
    def test_method_get_status(self, client: Pyopenwebui) -> None:
        retrieval = client.api.v1.retrieval.get_status()
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    def test_raw_response_get_status(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    def test_streaming_response_get_status(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(object, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_template(self, client: Pyopenwebui) -> None:
        retrieval = client.api.v1.retrieval.get_template()
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    def test_raw_response_get_template(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.with_raw_response.get_template()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    def test_streaming_response_get_template(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.with_streaming_response.get_template() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(object, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRetrieval:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete_entries(self, async_client: AsyncPyopenwebui) -> None:
        retrieval = await async_client.api.v1.retrieval.delete_entries(
            collection_name="collection_name",
            file_id="file_id",
        )
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    async def test_raw_response_delete_entries(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.with_raw_response.delete_entries(
            collection_name="collection_name",
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    async def test_streaming_response_delete_entries(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.with_streaming_response.delete_entries(
            collection_name="collection_name",
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(object, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_embeddings(self, async_client: AsyncPyopenwebui) -> None:
        retrieval = await async_client.api.v1.retrieval.get_embeddings(
            "text",
        )
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    async def test_raw_response_get_embeddings(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.with_raw_response.get_embeddings(
            "text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    async def test_streaming_response_get_embeddings(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.with_streaming_response.get_embeddings(
            "text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(object, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_embeddings(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `text` but received ''"):
            await async_client.api.v1.retrieval.with_raw_response.get_embeddings(
                "",
            )

    @parametrize
    async def test_method_get_status(self, async_client: AsyncPyopenwebui) -> None:
        retrieval = await async_client.api.v1.retrieval.get_status()
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(object, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_template(self, async_client: AsyncPyopenwebui) -> None:
        retrieval = await async_client.api.v1.retrieval.get_template()
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    async def test_raw_response_get_template(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.with_raw_response.get_template()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(object, retrieval, path=["response"])

    @parametrize
    async def test_streaming_response_get_template(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.with_streaming_response.get_template() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(object, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True
