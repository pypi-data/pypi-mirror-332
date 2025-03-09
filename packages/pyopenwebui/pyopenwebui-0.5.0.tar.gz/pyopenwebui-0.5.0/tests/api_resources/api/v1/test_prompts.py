# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1 import PromptGetResponse, PromptGetListResponse
from pyopenwebui.types.shared import PromptModel

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Pyopenwebui) -> None:
        prompt = client.api.v1.prompts.create(
            command="command",
            content="content",
            title="title",
        )
        assert_matches_type(Optional[PromptModel], prompt, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Pyopenwebui) -> None:
        prompt = client.api.v1.prompts.create(
            command="command",
            content="content",
            title="title",
            access_control={},
        )
        assert_matches_type(Optional[PromptModel], prompt, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Pyopenwebui) -> None:
        response = client.api.v1.prompts.with_raw_response.create(
            command="command",
            content="content",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Optional[PromptModel], prompt, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Pyopenwebui) -> None:
        with client.api.v1.prompts.with_streaming_response.create(
            command="command",
            content="content",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Optional[PromptModel], prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        prompt = client.api.v1.prompts.get()
        assert_matches_type(PromptGetResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.prompts.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptGetResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.prompts.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptGetResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_list(self, client: Pyopenwebui) -> None:
        prompt = client.api.v1.prompts.get_list()
        assert_matches_type(PromptGetListResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_get_list(self, client: Pyopenwebui) -> None:
        response = client.api.v1.prompts.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptGetListResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_get_list(self, client: Pyopenwebui) -> None:
        with client.api.v1.prompts.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptGetListResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrompts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPyopenwebui) -> None:
        prompt = await async_client.api.v1.prompts.create(
            command="command",
            content="content",
            title="title",
        )
        assert_matches_type(Optional[PromptModel], prompt, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        prompt = await async_client.api.v1.prompts.create(
            command="command",
            content="content",
            title="title",
            access_control={},
        )
        assert_matches_type(Optional[PromptModel], prompt, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.prompts.with_raw_response.create(
            command="command",
            content="content",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Optional[PromptModel], prompt, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.prompts.with_streaming_response.create(
            command="command",
            content="content",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Optional[PromptModel], prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        prompt = await async_client.api.v1.prompts.get()
        assert_matches_type(PromptGetResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.prompts.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptGetResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.prompts.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptGetResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_list(self, async_client: AsyncPyopenwebui) -> None:
        prompt = await async_client.api.v1.prompts.get_list()
        assert_matches_type(PromptGetListResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_get_list(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.prompts.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptGetListResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_get_list(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.prompts.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptGetListResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True
