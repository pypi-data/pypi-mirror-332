# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValves:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Pyopenwebui) -> None:
        valve = client.api.v1.tools.id.valves.update(
            id="id",
            body={},
        )
        assert_matches_type(object, valve, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Pyopenwebui) -> None:
        response = client.api.v1.tools.id.valves.with_raw_response.update(
            id="id",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        valve = response.parse()
        assert_matches_type(object, valve, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Pyopenwebui) -> None:
        with client.api.v1.tools.id.valves.with_streaming_response.update(
            id="id",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            valve = response.parse()
            assert_matches_type(object, valve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.tools.id.valves.with_raw_response.update(
                id="",
                body={},
            )

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        valve = client.api.v1.tools.id.valves.get(
            "id",
        )
        assert_matches_type(object, valve, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.tools.id.valves.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        valve = response.parse()
        assert_matches_type(object, valve, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.tools.id.valves.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            valve = response.parse()
            assert_matches_type(object, valve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.tools.id.valves.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_get_spec(self, client: Pyopenwebui) -> None:
        valve = client.api.v1.tools.id.valves.get_spec(
            "id",
        )
        assert_matches_type(object, valve, path=["response"])

    @parametrize
    def test_raw_response_get_spec(self, client: Pyopenwebui) -> None:
        response = client.api.v1.tools.id.valves.with_raw_response.get_spec(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        valve = response.parse()
        assert_matches_type(object, valve, path=["response"])

    @parametrize
    def test_streaming_response_get_spec(self, client: Pyopenwebui) -> None:
        with client.api.v1.tools.id.valves.with_streaming_response.get_spec(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            valve = response.parse()
            assert_matches_type(object, valve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_spec(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.tools.id.valves.with_raw_response.get_spec(
                "",
            )


class TestAsyncValves:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncPyopenwebui) -> None:
        valve = await async_client.api.v1.tools.id.valves.update(
            id="id",
            body={},
        )
        assert_matches_type(object, valve, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.tools.id.valves.with_raw_response.update(
            id="id",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        valve = await response.parse()
        assert_matches_type(object, valve, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.tools.id.valves.with_streaming_response.update(
            id="id",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            valve = await response.parse()
            assert_matches_type(object, valve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.tools.id.valves.with_raw_response.update(
                id="",
                body={},
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        valve = await async_client.api.v1.tools.id.valves.get(
            "id",
        )
        assert_matches_type(object, valve, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.tools.id.valves.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        valve = await response.parse()
        assert_matches_type(object, valve, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.tools.id.valves.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            valve = await response.parse()
            assert_matches_type(object, valve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.tools.id.valves.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_get_spec(self, async_client: AsyncPyopenwebui) -> None:
        valve = await async_client.api.v1.tools.id.valves.get_spec(
            "id",
        )
        assert_matches_type(object, valve, path=["response"])

    @parametrize
    async def test_raw_response_get_spec(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.tools.id.valves.with_raw_response.get_spec(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        valve = await response.parse()
        assert_matches_type(object, valve, path=["response"])

    @parametrize
    async def test_streaming_response_get_spec(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.tools.id.valves.with_streaming_response.get_spec(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            valve = await response.parse()
            assert_matches_type(object, valve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_spec(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.tools.id.valves.with_raw_response.get_spec(
                "",
            )
