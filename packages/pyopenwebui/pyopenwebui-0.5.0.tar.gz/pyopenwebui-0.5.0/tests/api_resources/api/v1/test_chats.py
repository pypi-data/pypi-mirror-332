# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types import ChatResponse
from pyopenwebui.types.api.v1 import (
    ChatGetResponse,
    ChatListResponse,
    ChatSearchResponse,
    ChatDeleteAllResponse,
    ChatDeleteByIDResponse,
    ChatGetArchivedListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.create(
            chat={},
        )
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.with_raw_response.create(
            chat={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.with_streaming_response.create(
            chat={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Optional[ChatResponse], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.list(
            user_id="user_id",
        )
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.list(
            user_id="user_id",
            limit=0,
            skip=0,
        )
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.with_raw_response.list(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.with_streaming_response.list(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatListResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.api.v1.chats.with_raw_response.list(
                user_id="",
            )

    @parametrize
    def test_method_archive(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.archive(
            "id",
        )
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.with_raw_response.archive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.with_streaming_response.archive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Optional[ChatResponse], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.chats.with_raw_response.archive(
                "",
            )

    @parametrize
    def test_method_delete_all(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.delete_all()
        assert_matches_type(ChatDeleteAllResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_delete_all(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatDeleteAllResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_delete_all(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatDeleteAllResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_by_id(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.delete_by_id(
            "id",
        )
        assert_matches_type(ChatDeleteByIDResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_delete_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.with_raw_response.delete_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatDeleteByIDResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_delete_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.with_streaming_response.delete_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatDeleteByIDResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.chats.with_raw_response.delete_by_id(
                "",
            )

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.get()
        assert_matches_type(ChatGetResponse, chat, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.get(
            page=0,
        )
        assert_matches_type(ChatGetResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatGetResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatGetResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_archived_list(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.get_archived_list()
        assert_matches_type(ChatGetArchivedListResponse, chat, path=["response"])

    @parametrize
    def test_method_get_archived_list_with_all_params(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.get_archived_list(
            limit=0,
            skip=0,
        )
        assert_matches_type(ChatGetArchivedListResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_get_archived_list(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.with_raw_response.get_archived_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatGetArchivedListResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_get_archived_list(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.with_streaming_response.get_archived_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatGetArchivedListResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_id(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.get_by_id(
            "id",
        )
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.with_raw_response.get_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.with_streaming_response.get_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Optional[ChatResponse], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.chats.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_import(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.import_(
            chat={},
        )
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    def test_method_import_with_all_params(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.import_(
            chat={},
            folder_id="folder_id",
            meta={},
            pinned=True,
        )
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    def test_raw_response_import(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.with_raw_response.import_(
            chat={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    def test_streaming_response_import(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.with_streaming_response.import_(
            chat={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Optional[ChatResponse], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_pin_by_id(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.pin_by_id(
            "id",
        )
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    def test_raw_response_pin_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.with_raw_response.pin_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    def test_streaming_response_pin_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.with_streaming_response.pin_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Optional[ChatResponse], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_pin_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.chats.with_raw_response.pin_by_id(
                "",
            )

    @parametrize
    def test_method_search(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.search(
            text="text",
        )
        assert_matches_type(ChatSearchResponse, chat, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.search(
            text="text",
            page=0,
        )
        assert_matches_type(ChatSearchResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.with_raw_response.search(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatSearchResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.with_streaming_response.search(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatSearchResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_by_id(self, client: Pyopenwebui) -> None:
        chat = client.api.v1.chats.update_by_id(
            id="id",
            chat={},
        )
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    def test_raw_response_update_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.chats.with_raw_response.update_by_id(
            id="id",
            chat={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    def test_streaming_response_update_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.chats.with_streaming_response.update_by_id(
            id="id",
            chat={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Optional[ChatResponse], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.chats.with_raw_response.update_by_id(
                id="",
                chat={},
            )


class TestAsyncChats:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.create(
            chat={},
        )
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.with_raw_response.create(
            chat={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.with_streaming_response.create(
            chat={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Optional[ChatResponse], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.list(
            user_id="user_id",
        )
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.list(
            user_id="user_id",
            limit=0,
            skip=0,
        )
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.with_raw_response.list(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.with_streaming_response.list(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatListResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.api.v1.chats.with_raw_response.list(
                user_id="",
            )

    @parametrize
    async def test_method_archive(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.archive(
            "id",
        )
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.with_raw_response.archive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.with_streaming_response.archive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Optional[ChatResponse], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.chats.with_raw_response.archive(
                "",
            )

    @parametrize
    async def test_method_delete_all(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.delete_all()
        assert_matches_type(ChatDeleteAllResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatDeleteAllResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatDeleteAllResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.delete_by_id(
            "id",
        )
        assert_matches_type(ChatDeleteByIDResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.with_raw_response.delete_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatDeleteByIDResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.with_streaming_response.delete_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatDeleteByIDResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.chats.with_raw_response.delete_by_id(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.get()
        assert_matches_type(ChatGetResponse, chat, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.get(
            page=0,
        )
        assert_matches_type(ChatGetResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatGetResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatGetResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_archived_list(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.get_archived_list()
        assert_matches_type(ChatGetArchivedListResponse, chat, path=["response"])

    @parametrize
    async def test_method_get_archived_list_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.get_archived_list(
            limit=0,
            skip=0,
        )
        assert_matches_type(ChatGetArchivedListResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_get_archived_list(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.with_raw_response.get_archived_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatGetArchivedListResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_get_archived_list(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.with_streaming_response.get_archived_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatGetArchivedListResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.get_by_id(
            "id",
        )
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.with_raw_response.get_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.with_streaming_response.get_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Optional[ChatResponse], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.chats.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_import(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.import_(
            chat={},
        )
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    async def test_method_import_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.import_(
            chat={},
            folder_id="folder_id",
            meta={},
            pinned=True,
        )
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    async def test_raw_response_import(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.with_raw_response.import_(
            chat={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.with_streaming_response.import_(
            chat={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Optional[ChatResponse], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_pin_by_id(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.pin_by_id(
            "id",
        )
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    async def test_raw_response_pin_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.with_raw_response.pin_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    async def test_streaming_response_pin_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.with_streaming_response.pin_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Optional[ChatResponse], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_pin_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.chats.with_raw_response.pin_by_id(
                "",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.search(
            text="text",
        )
        assert_matches_type(ChatSearchResponse, chat, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.search(
            text="text",
            page=0,
        )
        assert_matches_type(ChatSearchResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.with_raw_response.search(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatSearchResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.with_streaming_response.search(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatSearchResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.v1.chats.update_by_id(
            id="id",
            chat={},
        )
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    async def test_raw_response_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.chats.with_raw_response.update_by_id(
            id="id",
            chat={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Optional[ChatResponse], chat, path=["response"])

    @parametrize
    async def test_streaming_response_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.chats.with_streaming_response.update_by_id(
            id="id",
            chat={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Optional[ChatResponse], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.chats.with_raw_response.update_by_id(
                id="",
                chat={},
            )
