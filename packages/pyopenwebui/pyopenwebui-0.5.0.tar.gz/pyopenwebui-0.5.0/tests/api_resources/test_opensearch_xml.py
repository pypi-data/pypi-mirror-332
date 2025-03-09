# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOpensearchXml:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Pyopenwebui) -> None:
        opensearch_xml = client.opensearch_xml.retrieve()
        assert_matches_type(object, opensearch_xml, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Pyopenwebui) -> None:
        response = client.opensearch_xml.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opensearch_xml = response.parse()
        assert_matches_type(object, opensearch_xml, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Pyopenwebui) -> None:
        with client.opensearch_xml.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opensearch_xml = response.parse()
            assert_matches_type(object, opensearch_xml, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOpensearchXml:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPyopenwebui) -> None:
        opensearch_xml = await async_client.opensearch_xml.retrieve()
        assert_matches_type(object, opensearch_xml, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.opensearch_xml.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opensearch_xml = await response.parse()
        assert_matches_type(object, opensearch_xml, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.opensearch_xml.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opensearch_xml = await response.parse()
            assert_matches_type(object, opensearch_xml, path=["response"])

        assert cast(Any, response.is_closed) is True
