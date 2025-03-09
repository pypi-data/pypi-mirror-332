# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        content = client.api.v1.files.content.get(
            "id",
        )
        assert_matches_type(object, content, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.files.content.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = response.parse()
        assert_matches_type(object, content, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.files.content.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = response.parse()
            assert_matches_type(object, content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.files.content.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_get_by_name(self, client: Pyopenwebui) -> None:
        content = client.api.v1.files.content.get_by_name(
            file_name="file_name",
            id="id",
        )
        assert_matches_type(object, content, path=["response"])

    @parametrize
    def test_raw_response_get_by_name(self, client: Pyopenwebui) -> None:
        response = client.api.v1.files.content.with_raw_response.get_by_name(
            file_name="file_name",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = response.parse()
        assert_matches_type(object, content, path=["response"])

    @parametrize
    def test_streaming_response_get_by_name(self, client: Pyopenwebui) -> None:
        with client.api.v1.files.content.with_streaming_response.get_by_name(
            file_name="file_name",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = response.parse()
            assert_matches_type(object, content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_name(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.files.content.with_raw_response.get_by_name(
                file_name="file_name",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_name` but received ''"):
            client.api.v1.files.content.with_raw_response.get_by_name(
                file_name="",
                id="id",
            )

    @parametrize
    def test_method_get_html(self, client: Pyopenwebui) -> None:
        content = client.api.v1.files.content.get_html(
            "id",
        )
        assert_matches_type(object, content, path=["response"])

    @parametrize
    def test_raw_response_get_html(self, client: Pyopenwebui) -> None:
        response = client.api.v1.files.content.with_raw_response.get_html(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = response.parse()
        assert_matches_type(object, content, path=["response"])

    @parametrize
    def test_streaming_response_get_html(self, client: Pyopenwebui) -> None:
        with client.api.v1.files.content.with_streaming_response.get_html(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = response.parse()
            assert_matches_type(object, content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_html(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.files.content.with_raw_response.get_html(
                "",
            )


class TestAsyncContent:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        content = await async_client.api.v1.files.content.get(
            "id",
        )
        assert_matches_type(object, content, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.files.content.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = await response.parse()
        assert_matches_type(object, content, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.files.content.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = await response.parse()
            assert_matches_type(object, content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.files.content.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_get_by_name(self, async_client: AsyncPyopenwebui) -> None:
        content = await async_client.api.v1.files.content.get_by_name(
            file_name="file_name",
            id="id",
        )
        assert_matches_type(object, content, path=["response"])

    @parametrize
    async def test_raw_response_get_by_name(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.files.content.with_raw_response.get_by_name(
            file_name="file_name",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = await response.parse()
        assert_matches_type(object, content, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_name(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.files.content.with_streaming_response.get_by_name(
            file_name="file_name",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = await response.parse()
            assert_matches_type(object, content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_name(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.files.content.with_raw_response.get_by_name(
                file_name="file_name",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_name` but received ''"):
            await async_client.api.v1.files.content.with_raw_response.get_by_name(
                file_name="",
                id="id",
            )

    @parametrize
    async def test_method_get_html(self, async_client: AsyncPyopenwebui) -> None:
        content = await async_client.api.v1.files.content.get_html(
            "id",
        )
        assert_matches_type(object, content, path=["response"])

    @parametrize
    async def test_raw_response_get_html(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.files.content.with_raw_response.get_html(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = await response.parse()
        assert_matches_type(object, content, path=["response"])

    @parametrize
    async def test_streaming_response_get_html(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.files.content.with_streaming_response.get_html(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = await response.parse()
            assert_matches_type(object, content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_html(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.files.content.with_raw_response.get_html(
                "",
            )
