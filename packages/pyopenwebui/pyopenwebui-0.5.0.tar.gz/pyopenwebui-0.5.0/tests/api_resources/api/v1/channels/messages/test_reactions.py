# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.channels.messages import (
    ReactionAddResponse,
    ReactionRemoveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add(self, client: Pyopenwebui) -> None:
        reaction = client.api.v1.channels.messages.reactions.add(
            message_id="message_id",
            id="id",
            name="name",
        )
        assert_matches_type(ReactionAddResponse, reaction, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Pyopenwebui) -> None:
        response = client.api.v1.channels.messages.reactions.with_raw_response.add(
            message_id="message_id",
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reaction = response.parse()
        assert_matches_type(ReactionAddResponse, reaction, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Pyopenwebui) -> None:
        with client.api.v1.channels.messages.reactions.with_streaming_response.add(
            message_id="message_id",
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reaction = response.parse()
            assert_matches_type(ReactionAddResponse, reaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.channels.messages.reactions.with_raw_response.add(
                message_id="message_id",
                id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.api.v1.channels.messages.reactions.with_raw_response.add(
                message_id="",
                id="id",
                name="name",
            )

    @parametrize
    def test_method_remove(self, client: Pyopenwebui) -> None:
        reaction = client.api.v1.channels.messages.reactions.remove(
            message_id="message_id",
            id="id",
            name="name",
        )
        assert_matches_type(ReactionRemoveResponse, reaction, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Pyopenwebui) -> None:
        response = client.api.v1.channels.messages.reactions.with_raw_response.remove(
            message_id="message_id",
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reaction = response.parse()
        assert_matches_type(ReactionRemoveResponse, reaction, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Pyopenwebui) -> None:
        with client.api.v1.channels.messages.reactions.with_streaming_response.remove(
            message_id="message_id",
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reaction = response.parse()
            assert_matches_type(ReactionRemoveResponse, reaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.channels.messages.reactions.with_raw_response.remove(
                message_id="message_id",
                id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.api.v1.channels.messages.reactions.with_raw_response.remove(
                message_id="",
                id="id",
                name="name",
            )


class TestAsyncReactions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_add(self, async_client: AsyncPyopenwebui) -> None:
        reaction = await async_client.api.v1.channels.messages.reactions.add(
            message_id="message_id",
            id="id",
            name="name",
        )
        assert_matches_type(ReactionAddResponse, reaction, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.channels.messages.reactions.with_raw_response.add(
            message_id="message_id",
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reaction = await response.parse()
        assert_matches_type(ReactionAddResponse, reaction, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.channels.messages.reactions.with_streaming_response.add(
            message_id="message_id",
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reaction = await response.parse()
            assert_matches_type(ReactionAddResponse, reaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.channels.messages.reactions.with_raw_response.add(
                message_id="message_id",
                id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.api.v1.channels.messages.reactions.with_raw_response.add(
                message_id="",
                id="id",
                name="name",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncPyopenwebui) -> None:
        reaction = await async_client.api.v1.channels.messages.reactions.remove(
            message_id="message_id",
            id="id",
            name="name",
        )
        assert_matches_type(ReactionRemoveResponse, reaction, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.channels.messages.reactions.with_raw_response.remove(
            message_id="message_id",
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reaction = await response.parse()
        assert_matches_type(ReactionRemoveResponse, reaction, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.channels.messages.reactions.with_streaming_response.remove(
            message_id="message_id",
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reaction = await response.parse()
            assert_matches_type(ReactionRemoveResponse, reaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.channels.messages.reactions.with_raw_response.remove(
                message_id="message_id",
                id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.api.v1.channels.messages.reactions.with_raw_response.remove(
                message_id="",
                id="id",
                name="name",
            )
