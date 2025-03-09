# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_complete(self, client: Pyopenwebui) -> None:
        chat = client.api.chat.complete(
            body={},
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_raw_response_complete(self, client: Pyopenwebui) -> None:
        response = client.api.chat.with_raw_response.complete(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_streaming_response_complete(self, client: Pyopenwebui) -> None:
        with client.api.chat.with_streaming_response.complete(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_completion(self, client: Pyopenwebui) -> None:
        chat = client.api.chat.create_completion(
            body={},
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_raw_response_create_completion(self, client: Pyopenwebui) -> None:
        response = client.api.chat.with_raw_response.create_completion(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_streaming_response_create_completion(self, client: Pyopenwebui) -> None:
        with client.api.chat.with_streaming_response.create_completion(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_perform_action(self, client: Pyopenwebui) -> None:
        chat = client.api.chat.perform_action(
            action_id="action_id",
            body={},
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_raw_response_perform_action(self, client: Pyopenwebui) -> None:
        response = client.api.chat.with_raw_response.perform_action(
            action_id="action_id",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_streaming_response_perform_action(self, client: Pyopenwebui) -> None:
        with client.api.chat.with_streaming_response.perform_action(
            action_id="action_id",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_perform_action(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            client.api.chat.with_raw_response.perform_action(
                action_id="",
                body={},
            )


class TestAsyncChat:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_complete(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.chat.complete(
            body={},
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.chat.with_raw_response.complete(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.chat.with_streaming_response.complete(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_completion(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.chat.create_completion(
            body={},
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.chat.with_raw_response.create_completion(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.chat.with_streaming_response.create_completion(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_perform_action(self, async_client: AsyncPyopenwebui) -> None:
        chat = await async_client.api.chat.perform_action(
            action_id="action_id",
            body={},
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_raw_response_perform_action(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.chat.with_raw_response.perform_action(
            action_id="action_id",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_streaming_response_perform_action(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.chat.with_streaming_response.perform_action(
            action_id="action_id",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_perform_action(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            await async_client.api.chat.with_raw_response.perform_action(
                action_id="",
                body={},
            )
