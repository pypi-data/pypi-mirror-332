# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.channels import (
    MessageGetResponse,
    MessagePostResponse,
    MessageGetByIDResponse,
    MessageGetThreadResponse,
    MessageDeleteByIDResponse,
    MessageUpdateByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete_by_id(self, client: Pyopenwebui) -> None:
        message = client.api.v1.channels.messages.delete_by_id(
            message_id="message_id",
            id="id",
        )
        assert_matches_type(MessageDeleteByIDResponse, message, path=["response"])

    @parametrize
    def test_raw_response_delete_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.channels.messages.with_raw_response.delete_by_id(
            message_id="message_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageDeleteByIDResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_delete_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.channels.messages.with_streaming_response.delete_by_id(
            message_id="message_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageDeleteByIDResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.channels.messages.with_raw_response.delete_by_id(
                message_id="message_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.api.v1.channels.messages.with_raw_response.delete_by_id(
                message_id="",
                id="id",
            )

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        message = client.api.v1.channels.messages.get(
            id="id",
        )
        assert_matches_type(MessageGetResponse, message, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Pyopenwebui) -> None:
        message = client.api.v1.channels.messages.get(
            id="id",
            limit=0,
            skip=0,
        )
        assert_matches_type(MessageGetResponse, message, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.channels.messages.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageGetResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.channels.messages.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageGetResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.channels.messages.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_get_by_id(self, client: Pyopenwebui) -> None:
        message = client.api.v1.channels.messages.get_by_id(
            message_id="message_id",
            id="id",
        )
        assert_matches_type(Optional[MessageGetByIDResponse], message, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.channels.messages.with_raw_response.get_by_id(
            message_id="message_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Optional[MessageGetByIDResponse], message, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.channels.messages.with_streaming_response.get_by_id(
            message_id="message_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Optional[MessageGetByIDResponse], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.channels.messages.with_raw_response.get_by_id(
                message_id="message_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.api.v1.channels.messages.with_raw_response.get_by_id(
                message_id="",
                id="id",
            )

    @parametrize
    def test_method_get_thread(self, client: Pyopenwebui) -> None:
        message = client.api.v1.channels.messages.get_thread(
            message_id="message_id",
            id="id",
        )
        assert_matches_type(MessageGetThreadResponse, message, path=["response"])

    @parametrize
    def test_method_get_thread_with_all_params(self, client: Pyopenwebui) -> None:
        message = client.api.v1.channels.messages.get_thread(
            message_id="message_id",
            id="id",
            limit=0,
            skip=0,
        )
        assert_matches_type(MessageGetThreadResponse, message, path=["response"])

    @parametrize
    def test_raw_response_get_thread(self, client: Pyopenwebui) -> None:
        response = client.api.v1.channels.messages.with_raw_response.get_thread(
            message_id="message_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageGetThreadResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_get_thread(self, client: Pyopenwebui) -> None:
        with client.api.v1.channels.messages.with_streaming_response.get_thread(
            message_id="message_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageGetThreadResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_thread(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.channels.messages.with_raw_response.get_thread(
                message_id="message_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.api.v1.channels.messages.with_raw_response.get_thread(
                message_id="",
                id="id",
            )

    @parametrize
    def test_method_post(self, client: Pyopenwebui) -> None:
        message = client.api.v1.channels.messages.post(
            id="id",
            content="content",
        )
        assert_matches_type(Optional[MessagePostResponse], message, path=["response"])

    @parametrize
    def test_method_post_with_all_params(self, client: Pyopenwebui) -> None:
        message = client.api.v1.channels.messages.post(
            id="id",
            content="content",
            data={},
            meta={},
            parent_id="parent_id",
        )
        assert_matches_type(Optional[MessagePostResponse], message, path=["response"])

    @parametrize
    def test_raw_response_post(self, client: Pyopenwebui) -> None:
        response = client.api.v1.channels.messages.with_raw_response.post(
            id="id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Optional[MessagePostResponse], message, path=["response"])

    @parametrize
    def test_streaming_response_post(self, client: Pyopenwebui) -> None:
        with client.api.v1.channels.messages.with_streaming_response.post(
            id="id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Optional[MessagePostResponse], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_post(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.channels.messages.with_raw_response.post(
                id="",
                content="content",
            )

    @parametrize
    def test_method_update_by_id(self, client: Pyopenwebui) -> None:
        message = client.api.v1.channels.messages.update_by_id(
            message_id="message_id",
            id="id",
            content="content",
        )
        assert_matches_type(Optional[MessageUpdateByIDResponse], message, path=["response"])

    @parametrize
    def test_method_update_by_id_with_all_params(self, client: Pyopenwebui) -> None:
        message = client.api.v1.channels.messages.update_by_id(
            message_id="message_id",
            id="id",
            content="content",
            data={},
            meta={},
            parent_id="parent_id",
        )
        assert_matches_type(Optional[MessageUpdateByIDResponse], message, path=["response"])

    @parametrize
    def test_raw_response_update_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.channels.messages.with_raw_response.update_by_id(
            message_id="message_id",
            id="id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Optional[MessageUpdateByIDResponse], message, path=["response"])

    @parametrize
    def test_streaming_response_update_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.channels.messages.with_streaming_response.update_by_id(
            message_id="message_id",
            id="id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Optional[MessageUpdateByIDResponse], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.channels.messages.with_raw_response.update_by_id(
                message_id="message_id",
                id="",
                content="content",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.api.v1.channels.messages.with_raw_response.update_by_id(
                message_id="",
                id="id",
                content="content",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        message = await async_client.api.v1.channels.messages.delete_by_id(
            message_id="message_id",
            id="id",
        )
        assert_matches_type(MessageDeleteByIDResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.channels.messages.with_raw_response.delete_by_id(
            message_id="message_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageDeleteByIDResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.channels.messages.with_streaming_response.delete_by_id(
            message_id="message_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageDeleteByIDResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.channels.messages.with_raw_response.delete_by_id(
                message_id="message_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.api.v1.channels.messages.with_raw_response.delete_by_id(
                message_id="",
                id="id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        message = await async_client.api.v1.channels.messages.get(
            id="id",
        )
        assert_matches_type(MessageGetResponse, message, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        message = await async_client.api.v1.channels.messages.get(
            id="id",
            limit=0,
            skip=0,
        )
        assert_matches_type(MessageGetResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.channels.messages.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageGetResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.channels.messages.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageGetResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.channels.messages.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        message = await async_client.api.v1.channels.messages.get_by_id(
            message_id="message_id",
            id="id",
        )
        assert_matches_type(Optional[MessageGetByIDResponse], message, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.channels.messages.with_raw_response.get_by_id(
            message_id="message_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Optional[MessageGetByIDResponse], message, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.channels.messages.with_streaming_response.get_by_id(
            message_id="message_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Optional[MessageGetByIDResponse], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.channels.messages.with_raw_response.get_by_id(
                message_id="message_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.api.v1.channels.messages.with_raw_response.get_by_id(
                message_id="",
                id="id",
            )

    @parametrize
    async def test_method_get_thread(self, async_client: AsyncPyopenwebui) -> None:
        message = await async_client.api.v1.channels.messages.get_thread(
            message_id="message_id",
            id="id",
        )
        assert_matches_type(MessageGetThreadResponse, message, path=["response"])

    @parametrize
    async def test_method_get_thread_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        message = await async_client.api.v1.channels.messages.get_thread(
            message_id="message_id",
            id="id",
            limit=0,
            skip=0,
        )
        assert_matches_type(MessageGetThreadResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_get_thread(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.channels.messages.with_raw_response.get_thread(
            message_id="message_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageGetThreadResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_get_thread(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.channels.messages.with_streaming_response.get_thread(
            message_id="message_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageGetThreadResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_thread(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.channels.messages.with_raw_response.get_thread(
                message_id="message_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.api.v1.channels.messages.with_raw_response.get_thread(
                message_id="",
                id="id",
            )

    @parametrize
    async def test_method_post(self, async_client: AsyncPyopenwebui) -> None:
        message = await async_client.api.v1.channels.messages.post(
            id="id",
            content="content",
        )
        assert_matches_type(Optional[MessagePostResponse], message, path=["response"])

    @parametrize
    async def test_method_post_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        message = await async_client.api.v1.channels.messages.post(
            id="id",
            content="content",
            data={},
            meta={},
            parent_id="parent_id",
        )
        assert_matches_type(Optional[MessagePostResponse], message, path=["response"])

    @parametrize
    async def test_raw_response_post(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.channels.messages.with_raw_response.post(
            id="id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Optional[MessagePostResponse], message, path=["response"])

    @parametrize
    async def test_streaming_response_post(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.channels.messages.with_streaming_response.post(
            id="id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Optional[MessagePostResponse], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_post(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.channels.messages.with_raw_response.post(
                id="",
                content="content",
            )

    @parametrize
    async def test_method_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        message = await async_client.api.v1.channels.messages.update_by_id(
            message_id="message_id",
            id="id",
            content="content",
        )
        assert_matches_type(Optional[MessageUpdateByIDResponse], message, path=["response"])

    @parametrize
    async def test_method_update_by_id_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        message = await async_client.api.v1.channels.messages.update_by_id(
            message_id="message_id",
            id="id",
            content="content",
            data={},
            meta={},
            parent_id="parent_id",
        )
        assert_matches_type(Optional[MessageUpdateByIDResponse], message, path=["response"])

    @parametrize
    async def test_raw_response_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.channels.messages.with_raw_response.update_by_id(
            message_id="message_id",
            id="id",
            content="content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Optional[MessageUpdateByIDResponse], message, path=["response"])

    @parametrize
    async def test_streaming_response_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.channels.messages.with_streaming_response.update_by_id(
            message_id="message_id",
            id="id",
            content="content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Optional[MessageUpdateByIDResponse], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.channels.messages.with_raw_response.update_by_id(
                message_id="message_id",
                id="",
                content="content",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.api.v1.channels.messages.with_raw_response.update_by_id(
                message_id="",
                id="id",
                content="content",
            )
