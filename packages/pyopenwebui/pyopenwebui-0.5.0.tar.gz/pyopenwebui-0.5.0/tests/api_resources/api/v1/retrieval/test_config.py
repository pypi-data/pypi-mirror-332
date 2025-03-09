# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Pyopenwebui) -> None:
        config = client.api.v1.retrieval.config.update()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Pyopenwebui) -> None:
        config = client.api.v1.retrieval.config.update(
            bypass_embedding_and_retrieval=True,
            chunk={
                "chunk_overlap": 0,
                "chunk_size": 0,
                "text_splitter": "text_splitter",
            },
            content_extraction={
                "document_intelligence_config": {
                    "endpoint": "endpoint",
                    "key": "key",
                },
                "engine": "engine",
                "tika_server_url": "tika_server_url",
            },
            enable_google_drive_integration=True,
            enable_onedrive_integration=True,
            file={
                "max_count": 0,
                "max_size": 0,
            },
            pdf_extract_images=True,
            rag_full_context=True,
            web={
                "search": {
                    "enabled": True,
                    "bing_search_v7_endpoint": "bing_search_v7_endpoint",
                    "bing_search_v7_subscription_key": "bing_search_v7_subscription_key",
                    "bocha_search_api_key": "bocha_search_api_key",
                    "brave_search_api_key": "brave_search_api_key",
                    "concurrent_requests": 0,
                    "domain_filter_list": ["string"],
                    "engine": "engine",
                    "exa_api_key": "exa_api_key",
                    "google_pse_api_key": "google_pse_api_key",
                    "google_pse_engine_id": "google_pse_engine_id",
                    "jina_api_key": "jina_api_key",
                    "kagi_search_api_key": "kagi_search_api_key",
                    "mojeek_search_api_key": "mojeek_search_api_key",
                    "perplexity_api_key": "perplexity_api_key",
                    "result_count": 0,
                    "searchapi_api_key": "searchapi_api_key",
                    "searchapi_engine": "searchapi_engine",
                    "searxng_query_url": "searxng_query_url",
                    "serpapi_api_key": "serpapi_api_key",
                    "serpapi_engine": "serpapi_engine",
                    "serper_api_key": "serper_api_key",
                    "serply_api_key": "serply_api_key",
                    "serpstack_api_key": "serpstack_api_key",
                    "serpstack_https": True,
                    "tavily_api_key": "tavily_api_key",
                    "trust_env": True,
                },
                "bypass_web_search_embedding_and_retrieval": True,
                "enable_rag_web_loader_ssl_verification": True,
            },
            youtube={
                "language": ["string"],
                "proxy_url": "proxy_url",
                "translation": "translation",
            },
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.config.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.config.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        config = client.api.v1.retrieval.config.get()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.retrieval.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.retrieval.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.api.v1.retrieval.config.update()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.api.v1.retrieval.config.update(
            bypass_embedding_and_retrieval=True,
            chunk={
                "chunk_overlap": 0,
                "chunk_size": 0,
                "text_splitter": "text_splitter",
            },
            content_extraction={
                "document_intelligence_config": {
                    "endpoint": "endpoint",
                    "key": "key",
                },
                "engine": "engine",
                "tika_server_url": "tika_server_url",
            },
            enable_google_drive_integration=True,
            enable_onedrive_integration=True,
            file={
                "max_count": 0,
                "max_size": 0,
            },
            pdf_extract_images=True,
            rag_full_context=True,
            web={
                "search": {
                    "enabled": True,
                    "bing_search_v7_endpoint": "bing_search_v7_endpoint",
                    "bing_search_v7_subscription_key": "bing_search_v7_subscription_key",
                    "bocha_search_api_key": "bocha_search_api_key",
                    "brave_search_api_key": "brave_search_api_key",
                    "concurrent_requests": 0,
                    "domain_filter_list": ["string"],
                    "engine": "engine",
                    "exa_api_key": "exa_api_key",
                    "google_pse_api_key": "google_pse_api_key",
                    "google_pse_engine_id": "google_pse_engine_id",
                    "jina_api_key": "jina_api_key",
                    "kagi_search_api_key": "kagi_search_api_key",
                    "mojeek_search_api_key": "mojeek_search_api_key",
                    "perplexity_api_key": "perplexity_api_key",
                    "result_count": 0,
                    "searchapi_api_key": "searchapi_api_key",
                    "searchapi_engine": "searchapi_engine",
                    "searxng_query_url": "searxng_query_url",
                    "serpapi_api_key": "serpapi_api_key",
                    "serpapi_engine": "serpapi_engine",
                    "serper_api_key": "serper_api_key",
                    "serply_api_key": "serply_api_key",
                    "serpstack_api_key": "serpstack_api_key",
                    "serpstack_https": True,
                    "tavily_api_key": "tavily_api_key",
                    "trust_env": True,
                },
                "bypass_web_search_embedding_and_retrieval": True,
                "enable_rag_web_loader_ssl_verification": True,
            },
            youtube={
                "language": ["string"],
                "proxy_url": "proxy_url",
                "translation": "translation",
            },
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.config.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.config.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.api.v1.retrieval.config.get()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.retrieval.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.retrieval.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True
