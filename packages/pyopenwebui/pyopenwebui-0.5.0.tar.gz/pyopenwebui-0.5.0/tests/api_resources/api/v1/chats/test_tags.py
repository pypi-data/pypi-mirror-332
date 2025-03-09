# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.chats import (
    TagAddResponse,
    TagGetResponse,
    TagDeleteResponse,
    TagGetByIDResponse,
    TagDeleteAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Pyopenwebui) -> None:
        tag = client.api.v1.chats.tags.delete(
            id="id",
            name="name",
        )
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.tags.with_raw_response.delete(
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.tags.with_streaming_response.delete(
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagDeleteResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.chats.tags.with_raw_response.delete(
                id="",
                name="name",
            )

    @parametrize
    def test_method_add(self, client: Pyopenwebui) -> None:
        tag = client.api.v1.chats.tags.add(
            id="id",
            name="name",
        )
        assert_matches_type(TagAddResponse, tag, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.tags.with_raw_response.add(
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagAddResponse, tag, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.tags.with_streaming_response.add(
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagAddResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.chats.tags.with_raw_response.add(
                id="",
                name="name",
            )

    @parametrize
    def test_method_delete_all(self, client: Pyopenwebui) -> None:
        tag = client.api.v1.chats.tags.delete_all(
            "id",
        )
        assert_matches_type(Optional[TagDeleteAllResponse], tag, path=["response"])

    @parametrize
    def test_raw_response_delete_all(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.tags.with_raw_response.delete_all(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Optional[TagDeleteAllResponse], tag, path=["response"])

    @parametrize
    def test_streaming_response_delete_all(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.tags.with_streaming_response.delete_all(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Optional[TagDeleteAllResponse], tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_all(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.chats.tags.with_raw_response.delete_all(
                "",
            )

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        tag = client.api.v1.chats.tags.get(
            name="name",
        )
        assert_matches_type(TagGetResponse, tag, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Pyopenwebui) -> None:
        tag = client.api.v1.chats.tags.get(
            name="name",
            limit=0,
            skip=0,
        )
        assert_matches_type(TagGetResponse, tag, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.tags.with_raw_response.get(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagGetResponse, tag, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.tags.with_streaming_response.get(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagGetResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_id(self, client: Pyopenwebui) -> None:
        tag = client.api.v1.chats.tags.get_by_id(
            "id",
        )
        assert_matches_type(TagGetByIDResponse, tag, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.tags.with_raw_response.get_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagGetByIDResponse, tag, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.tags.with_streaming_response.get_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagGetByIDResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.chats.tags.with_raw_response.get_by_id(
                "",
            )


class TestAsyncTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncPyopenwebui) -> None:
        tag = await async_client.api.v1.chats.tags.delete(
            id="id",
            name="name",
        )
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.tags.with_raw_response.delete(
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagDeleteResponse, tag, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.tags.with_streaming_response.delete(
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagDeleteResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.chats.tags.with_raw_response.delete(
                id="",
                name="name",
            )

    @parametrize
    async def test_method_add(self, async_client: AsyncPyopenwebui) -> None:
        tag = await async_client.api.v1.chats.tags.add(
            id="id",
            name="name",
        )
        assert_matches_type(TagAddResponse, tag, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.tags.with_raw_response.add(
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagAddResponse, tag, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.tags.with_streaming_response.add(
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagAddResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.chats.tags.with_raw_response.add(
                id="",
                name="name",
            )

    @parametrize
    async def test_method_delete_all(self, async_client: AsyncPyopenwebui) -> None:
        tag = await async_client.api.v1.chats.tags.delete_all(
            "id",
        )
        assert_matches_type(Optional[TagDeleteAllResponse], tag, path=["response"])

    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.tags.with_raw_response.delete_all(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Optional[TagDeleteAllResponse], tag, path=["response"])

    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.tags.with_streaming_response.delete_all(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Optional[TagDeleteAllResponse], tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_all(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.chats.tags.with_raw_response.delete_all(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        tag = await async_client.api.v1.chats.tags.get(
            name="name",
        )
        assert_matches_type(TagGetResponse, tag, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        tag = await async_client.api.v1.chats.tags.get(
            name="name",
            limit=0,
            skip=0,
        )
        assert_matches_type(TagGetResponse, tag, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.tags.with_raw_response.get(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagGetResponse, tag, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.tags.with_streaming_response.get(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagGetResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        tag = await async_client.api.v1.chats.tags.get_by_id(
            "id",
        )
        assert_matches_type(TagGetByIDResponse, tag, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.tags.with_raw_response.get_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagGetByIDResponse, tag, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.tags.with_streaming_response.get_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagGetByIDResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.chats.tags.with_raw_response.get_by_id(
                "",
            )
