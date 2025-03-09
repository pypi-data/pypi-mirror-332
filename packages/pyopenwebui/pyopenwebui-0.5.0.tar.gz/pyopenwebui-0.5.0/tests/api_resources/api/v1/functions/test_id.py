# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types import FunctionModel
from pyopenwebui.types.api.v1.functions import IDDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestID:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Pyopenwebui) -> None:
        id = client.api.v1.functions.id.update(
            id_1="id",
            id_2="id",
            content="content",
            meta={},
            name="name",
        )
        assert_matches_type(Optional[FunctionModel], id, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Pyopenwebui) -> None:
        id = client.api.v1.functions.id.update(
            id_1="id",
            id_2="id",
            content="content",
            meta={
                "description": "description",
                "manifest": {},
            },
            name="name",
        )
        assert_matches_type(Optional[FunctionModel], id, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Pyopenwebui) -> None:
        response = client.api.v1.functions.id.with_raw_response.update(
            id_1="id",
            id_2="id",
            content="content",
            meta={},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        id = response.parse()
        assert_matches_type(Optional[FunctionModel], id, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Pyopenwebui) -> None:
        with client.api.v1.functions.id.with_streaming_response.update(
            id_1="id",
            id_2="id",
            content="content",
            meta={},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            id = response.parse()
            assert_matches_type(Optional[FunctionModel], id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            client.api.v1.functions.id.with_raw_response.update(
                id_1="",
                id_2="",
                content="content",
                meta={},
                name="name",
            )

    @parametrize
    def test_method_delete(self, client: Pyopenwebui) -> None:
        id = client.api.v1.functions.id.delete(
            "id",
        )
        assert_matches_type(IDDeleteResponse, id, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Pyopenwebui) -> None:
        response = client.api.v1.functions.id.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        id = response.parse()
        assert_matches_type(IDDeleteResponse, id, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Pyopenwebui) -> None:
        with client.api.v1.functions.id.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            id = response.parse()
            assert_matches_type(IDDeleteResponse, id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.functions.id.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        id = client.api.v1.functions.id.get(
            "id",
        )
        assert_matches_type(Optional[FunctionModel], id, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.functions.id.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        id = response.parse()
        assert_matches_type(Optional[FunctionModel], id, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.functions.id.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            id = response.parse()
            assert_matches_type(Optional[FunctionModel], id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.functions.id.with_raw_response.get(
                "",
            )


class TestAsyncID:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncPyopenwebui) -> None:
        id = await async_client.api.v1.functions.id.update(
            id_1="id",
            id_2="id",
            content="content",
            meta={},
            name="name",
        )
        assert_matches_type(Optional[FunctionModel], id, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        id = await async_client.api.v1.functions.id.update(
            id_1="id",
            id_2="id",
            content="content",
            meta={
                "description": "description",
                "manifest": {},
            },
            name="name",
        )
        assert_matches_type(Optional[FunctionModel], id, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.functions.id.with_raw_response.update(
            id_1="id",
            id_2="id",
            content="content",
            meta={},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        id = await response.parse()
        assert_matches_type(Optional[FunctionModel], id, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.functions.id.with_streaming_response.update(
            id_1="id",
            id_2="id",
            content="content",
            meta={},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            id = await response.parse()
            assert_matches_type(Optional[FunctionModel], id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_1` but received ''"):
            await async_client.api.v1.functions.id.with_raw_response.update(
                id_1="",
                id_2="",
                content="content",
                meta={},
                name="name",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncPyopenwebui) -> None:
        id = await async_client.api.v1.functions.id.delete(
            "id",
        )
        assert_matches_type(IDDeleteResponse, id, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.functions.id.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        id = await response.parse()
        assert_matches_type(IDDeleteResponse, id, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.functions.id.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            id = await response.parse()
            assert_matches_type(IDDeleteResponse, id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.functions.id.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        id = await async_client.api.v1.functions.id.get(
            "id",
        )
        assert_matches_type(Optional[FunctionModel], id, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.functions.id.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        id = await response.parse()
        assert_matches_type(Optional[FunctionModel], id, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.functions.id.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            id = await response.parse()
            assert_matches_type(Optional[FunctionModel], id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.functions.id.with_raw_response.get(
                "",
            )
