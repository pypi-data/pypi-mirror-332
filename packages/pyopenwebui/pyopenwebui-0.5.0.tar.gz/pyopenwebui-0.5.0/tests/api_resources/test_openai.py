# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOpenAI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_proxy_delete(self, client: Pyopenwebui) -> None:
        openai = client.openai.proxy_delete(
            "path",
        )
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    def test_raw_response_proxy_delete(self, client: Pyopenwebui) -> None:
        response = client.openai.with_raw_response.proxy_delete(
            "path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = response.parse()
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    def test_streaming_response_proxy_delete(self, client: Pyopenwebui) -> None:
        with client.openai.with_streaming_response.proxy_delete(
            "path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = response.parse()
            assert_matches_type(object, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_proxy_delete(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.openai.with_raw_response.proxy_delete(
                "",
            )

    @parametrize
    def test_method_proxy_get(self, client: Pyopenwebui) -> None:
        openai = client.openai.proxy_get(
            "path",
        )
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    def test_raw_response_proxy_get(self, client: Pyopenwebui) -> None:
        response = client.openai.with_raw_response.proxy_get(
            "path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = response.parse()
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    def test_streaming_response_proxy_get(self, client: Pyopenwebui) -> None:
        with client.openai.with_streaming_response.proxy_get(
            "path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = response.parse()
            assert_matches_type(object, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_proxy_get(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.openai.with_raw_response.proxy_get(
                "",
            )

    @parametrize
    def test_method_proxy_post(self, client: Pyopenwebui) -> None:
        openai = client.openai.proxy_post(
            "path",
        )
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    def test_raw_response_proxy_post(self, client: Pyopenwebui) -> None:
        response = client.openai.with_raw_response.proxy_post(
            "path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = response.parse()
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    def test_streaming_response_proxy_post(self, client: Pyopenwebui) -> None:
        with client.openai.with_streaming_response.proxy_post(
            "path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = response.parse()
            assert_matches_type(object, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_proxy_post(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.openai.with_raw_response.proxy_post(
                "",
            )

    @parametrize
    def test_method_proxy_put(self, client: Pyopenwebui) -> None:
        openai = client.openai.proxy_put(
            "path",
        )
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    def test_raw_response_proxy_put(self, client: Pyopenwebui) -> None:
        response = client.openai.with_raw_response.proxy_put(
            "path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = response.parse()
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    def test_streaming_response_proxy_put(self, client: Pyopenwebui) -> None:
        with client.openai.with_streaming_response.proxy_put(
            "path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = response.parse()
            assert_matches_type(object, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_proxy_put(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.openai.with_raw_response.proxy_put(
                "",
            )

    @parametrize
    def test_method_verify_connection(self, client: Pyopenwebui) -> None:
        openai = client.openai.verify_connection(
            key="key",
            url="url",
        )
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    def test_raw_response_verify_connection(self, client: Pyopenwebui) -> None:
        response = client.openai.with_raw_response.verify_connection(
            key="key",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = response.parse()
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    def test_streaming_response_verify_connection(self, client: Pyopenwebui) -> None:
        with client.openai.with_streaming_response.verify_connection(
            key="key",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = response.parse()
            assert_matches_type(object, openai, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOpenAI:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_proxy_delete(self, async_client: AsyncPyopenwebui) -> None:
        openai = await async_client.openai.proxy_delete(
            "path",
        )
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    async def test_raw_response_proxy_delete(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.openai.with_raw_response.proxy_delete(
            "path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = await response.parse()
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    async def test_streaming_response_proxy_delete(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.openai.with_streaming_response.proxy_delete(
            "path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = await response.parse()
            assert_matches_type(object, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_proxy_delete(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.openai.with_raw_response.proxy_delete(
                "",
            )

    @parametrize
    async def test_method_proxy_get(self, async_client: AsyncPyopenwebui) -> None:
        openai = await async_client.openai.proxy_get(
            "path",
        )
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    async def test_raw_response_proxy_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.openai.with_raw_response.proxy_get(
            "path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = await response.parse()
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    async def test_streaming_response_proxy_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.openai.with_streaming_response.proxy_get(
            "path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = await response.parse()
            assert_matches_type(object, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_proxy_get(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.openai.with_raw_response.proxy_get(
                "",
            )

    @parametrize
    async def test_method_proxy_post(self, async_client: AsyncPyopenwebui) -> None:
        openai = await async_client.openai.proxy_post(
            "path",
        )
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    async def test_raw_response_proxy_post(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.openai.with_raw_response.proxy_post(
            "path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = await response.parse()
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    async def test_streaming_response_proxy_post(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.openai.with_streaming_response.proxy_post(
            "path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = await response.parse()
            assert_matches_type(object, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_proxy_post(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.openai.with_raw_response.proxy_post(
                "",
            )

    @parametrize
    async def test_method_proxy_put(self, async_client: AsyncPyopenwebui) -> None:
        openai = await async_client.openai.proxy_put(
            "path",
        )
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    async def test_raw_response_proxy_put(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.openai.with_raw_response.proxy_put(
            "path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = await response.parse()
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    async def test_streaming_response_proxy_put(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.openai.with_streaming_response.proxy_put(
            "path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = await response.parse()
            assert_matches_type(object, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_proxy_put(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.openai.with_raw_response.proxy_put(
                "",
            )

    @parametrize
    async def test_method_verify_connection(self, async_client: AsyncPyopenwebui) -> None:
        openai = await async_client.openai.verify_connection(
            key="key",
            url="url",
        )
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    async def test_raw_response_verify_connection(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.openai.with_raw_response.verify_connection(
            key="key",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = await response.parse()
        assert_matches_type(object, openai, path=["response"])

    @parametrize
    async def test_streaming_response_verify_connection(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.openai.with_streaming_response.verify_connection(
            key="key",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = await response.parse()
            assert_matches_type(object, openai, path=["response"])

        assert cast(Any, response.is_closed) is True
