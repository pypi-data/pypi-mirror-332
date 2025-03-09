# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types import FunctionModel

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToggle:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_global(self, client: Pyopenwebui) -> None:
        toggle = client.api.v1.functions.id.toggle.global_(
            "id",
        )
        assert_matches_type(Optional[FunctionModel], toggle, path=["response"])

    @parametrize
    def test_raw_response_global(self, client: Pyopenwebui) -> None:
        response = client.api.v1.functions.id.toggle.with_raw_response.global_(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toggle = response.parse()
        assert_matches_type(Optional[FunctionModel], toggle, path=["response"])

    @parametrize
    def test_streaming_response_global(self, client: Pyopenwebui) -> None:
        with client.api.v1.functions.id.toggle.with_streaming_response.global_(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toggle = response.parse()
            assert_matches_type(Optional[FunctionModel], toggle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_global(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.functions.id.toggle.with_raw_response.global_(
                "",
            )


class TestAsyncToggle:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_global(self, async_client: AsyncPyopenwebui) -> None:
        toggle = await async_client.api.v1.functions.id.toggle.global_(
            "id",
        )
        assert_matches_type(Optional[FunctionModel], toggle, path=["response"])

    @parametrize
    async def test_raw_response_global(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.functions.id.toggle.with_raw_response.global_(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toggle = await response.parse()
        assert_matches_type(Optional[FunctionModel], toggle, path=["response"])

    @parametrize
    async def test_streaming_response_global(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.functions.id.toggle.with_streaming_response.global_(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toggle = await response.parse()
            assert_matches_type(Optional[FunctionModel], toggle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_global(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.functions.id.toggle.with_raw_response.global_(
                "",
            )
