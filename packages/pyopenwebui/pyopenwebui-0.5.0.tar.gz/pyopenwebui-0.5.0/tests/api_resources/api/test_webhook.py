# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhook:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_url(self, client: Pyopenwebui) -> None:
        webhook = client.api.webhook.get_url()
        assert_matches_type(object, webhook, path=["response"])

    @parametrize
    def test_raw_response_get_url(self, client: Pyopenwebui) -> None:
        response = client.api.webhook.with_raw_response.get_url()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(object, webhook, path=["response"])

    @parametrize
    def test_streaming_response_get_url(self, client: Pyopenwebui) -> None:
        with client.api.webhook.with_streaming_response.get_url() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(object, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_url(self, client: Pyopenwebui) -> None:
        webhook = client.api.webhook.update_url(
            url="url",
        )
        assert_matches_type(object, webhook, path=["response"])

    @parametrize
    def test_raw_response_update_url(self, client: Pyopenwebui) -> None:
        response = client.api.webhook.with_raw_response.update_url(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(object, webhook, path=["response"])

    @parametrize
    def test_streaming_response_update_url(self, client: Pyopenwebui) -> None:
        with client.api.webhook.with_streaming_response.update_url(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(object, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhook:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_url(self, async_client: AsyncPyopenwebui) -> None:
        webhook = await async_client.api.webhook.get_url()
        assert_matches_type(object, webhook, path=["response"])

    @parametrize
    async def test_raw_response_get_url(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.webhook.with_raw_response.get_url()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(object, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_get_url(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.webhook.with_streaming_response.get_url() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(object, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_url(self, async_client: AsyncPyopenwebui) -> None:
        webhook = await async_client.api.webhook.update_url(
            url="url",
        )
        assert_matches_type(object, webhook, path=["response"])

    @parametrize
    async def test_raw_response_update_url(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.webhook.with_raw_response.update_url(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(object, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_update_url(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.webhook.with_streaming_response.update_url(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(object, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True
