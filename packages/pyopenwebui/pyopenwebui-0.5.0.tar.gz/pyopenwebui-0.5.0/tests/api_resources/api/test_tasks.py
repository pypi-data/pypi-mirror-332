# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Pyopenwebui) -> None:
        task = client.api.tasks.list()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Pyopenwebui) -> None:
        response = client.api.tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Pyopenwebui) -> None:
        with client.api.tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(object, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stop(self, client: Pyopenwebui) -> None:
        task = client.api.tasks.stop(
            "task_id",
        )
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_raw_response_stop(self, client: Pyopenwebui) -> None:
        response = client.api.tasks.with_raw_response.stop(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_streaming_response_stop(self, client: Pyopenwebui) -> None:
        with client.api.tasks.with_streaming_response.stop(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(object, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stop(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.api.tasks.with_raw_response.stop(
                "",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncPyopenwebui) -> None:
        task = await async_client.api.tasks.list()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(object, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stop(self, async_client: AsyncPyopenwebui) -> None:
        task = await async_client.api.tasks.stop(
            "task_id",
        )
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.tasks.with_raw_response.stop(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.tasks.with_streaming_response.stop(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(object, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stop(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.api.tasks.with_raw_response.stop(
                "",
            )
