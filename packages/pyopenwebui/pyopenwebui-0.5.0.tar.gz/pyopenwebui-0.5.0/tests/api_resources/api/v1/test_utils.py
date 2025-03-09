# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUtils:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_download_chat_as_pdf(self, client: Pyopenwebui) -> None:
        util = client.api.v1.utils.download_chat_as_pdf(
            messages=[{}],
            title="title",
        )
        assert_matches_type(object, util, path=["response"])

    @parametrize
    def test_raw_response_download_chat_as_pdf(self, client: Pyopenwebui) -> None:
        response = client.api.v1.utils.with_raw_response.download_chat_as_pdf(
            messages=[{}],
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        util = response.parse()
        assert_matches_type(object, util, path=["response"])

    @parametrize
    def test_streaming_response_download_chat_as_pdf(self, client: Pyopenwebui) -> None:
        with client.api.v1.utils.with_streaming_response.download_chat_as_pdf(
            messages=[{}],
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            util = response.parse()
            assert_matches_type(object, util, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_gravatar(self, client: Pyopenwebui) -> None:
        util = client.api.v1.utils.get_gravatar(
            email="email",
        )
        assert_matches_type(object, util, path=["response"])

    @parametrize
    def test_raw_response_get_gravatar(self, client: Pyopenwebui) -> None:
        response = client.api.v1.utils.with_raw_response.get_gravatar(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        util = response.parse()
        assert_matches_type(object, util, path=["response"])

    @parametrize
    def test_streaming_response_get_gravatar(self, client: Pyopenwebui) -> None:
        with client.api.v1.utils.with_streaming_response.get_gravatar(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            util = response.parse()
            assert_matches_type(object, util, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_markdown(self, client: Pyopenwebui) -> None:
        util = client.api.v1.utils.markdown(
            md="md",
        )
        assert_matches_type(object, util, path=["response"])

    @parametrize
    def test_raw_response_markdown(self, client: Pyopenwebui) -> None:
        response = client.api.v1.utils.with_raw_response.markdown(
            md="md",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        util = response.parse()
        assert_matches_type(object, util, path=["response"])

    @parametrize
    def test_streaming_response_markdown(self, client: Pyopenwebui) -> None:
        with client.api.v1.utils.with_streaming_response.markdown(
            md="md",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            util = response.parse()
            assert_matches_type(object, util, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUtils:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_download_chat_as_pdf(self, async_client: AsyncPyopenwebui) -> None:
        util = await async_client.api.v1.utils.download_chat_as_pdf(
            messages=[{}],
            title="title",
        )
        assert_matches_type(object, util, path=["response"])

    @parametrize
    async def test_raw_response_download_chat_as_pdf(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.utils.with_raw_response.download_chat_as_pdf(
            messages=[{}],
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        util = await response.parse()
        assert_matches_type(object, util, path=["response"])

    @parametrize
    async def test_streaming_response_download_chat_as_pdf(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.utils.with_streaming_response.download_chat_as_pdf(
            messages=[{}],
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            util = await response.parse()
            assert_matches_type(object, util, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_gravatar(self, async_client: AsyncPyopenwebui) -> None:
        util = await async_client.api.v1.utils.get_gravatar(
            email="email",
        )
        assert_matches_type(object, util, path=["response"])

    @parametrize
    async def test_raw_response_get_gravatar(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.utils.with_raw_response.get_gravatar(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        util = await response.parse()
        assert_matches_type(object, util, path=["response"])

    @parametrize
    async def test_streaming_response_get_gravatar(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.utils.with_streaming_response.get_gravatar(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            util = await response.parse()
            assert_matches_type(object, util, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_markdown(self, async_client: AsyncPyopenwebui) -> None:
        util = await async_client.api.v1.utils.markdown(
            md="md",
        )
        assert_matches_type(object, util, path=["response"])

    @parametrize
    async def test_raw_response_markdown(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.utils.with_raw_response.markdown(
            md="md",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        util = await response.parse()
        assert_matches_type(object, util, path=["response"])

    @parametrize
    async def test_streaming_response_markdown(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.utils.with_streaming_response.markdown(
            md="md",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            util = await response.parse()
            assert_matches_type(object, util, path=["response"])

        assert cast(Any, response.is_closed) is True
