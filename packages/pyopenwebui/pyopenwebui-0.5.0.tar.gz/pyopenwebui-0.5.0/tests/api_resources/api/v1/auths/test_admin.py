# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdmin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_details(self, client: Pyopenwebui) -> None:
        admin = client.api.v1.auths.admin.get_details()
        assert_matches_type(object, admin, path=["response"])

    @parametrize
    def test_raw_response_get_details(self, client: Pyopenwebui) -> None:
        response = client.api.v1.auths.admin.with_raw_response.get_details()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(object, admin, path=["response"])

    @parametrize
    def test_streaming_response_get_details(self, client: Pyopenwebui) -> None:
        with client.api.v1.auths.admin.with_streaming_response.get_details() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(object, admin, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdmin:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_details(self, async_client: AsyncPyopenwebui) -> None:
        admin = await async_client.api.v1.auths.admin.get_details()
        assert_matches_type(object, admin, path=["response"])

    @parametrize
    async def test_raw_response_get_details(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.auths.admin.with_raw_response.get_details()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(object, admin, path=["response"])

    @parametrize
    async def test_streaming_response_get_details(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.auths.admin.with_streaming_response.get_details() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(object, admin, path=["response"])

        assert cast(Any, response.is_closed) is True
