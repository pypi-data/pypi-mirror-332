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
        config = client.api.v1.tasks.config.update(
            autocomplete_generation_input_max_length=0,
            enable_autocomplete_generation=True,
            enable_retrieval_query_generation=True,
            enable_search_query_generation=True,
            enable_tags_generation=True,
            enable_title_generation=True,
            image_prompt_generation_prompt_template="IMAGE_PROMPT_GENERATION_PROMPT_TEMPLATE",
            query_generation_prompt_template="QUERY_GENERATION_PROMPT_TEMPLATE",
            tags_generation_prompt_template="TAGS_GENERATION_PROMPT_TEMPLATE",
            task_model="TASK_MODEL",
            task_model_external="TASK_MODEL_EXTERNAL",
            title_generation_prompt_template="TITLE_GENERATION_PROMPT_TEMPLATE",
            tools_function_calling_prompt_template="TOOLS_FUNCTION_CALLING_PROMPT_TEMPLATE",
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Pyopenwebui) -> None:
        response = client.api.v1.tasks.config.with_raw_response.update(
            autocomplete_generation_input_max_length=0,
            enable_autocomplete_generation=True,
            enable_retrieval_query_generation=True,
            enable_search_query_generation=True,
            enable_tags_generation=True,
            enable_title_generation=True,
            image_prompt_generation_prompt_template="IMAGE_PROMPT_GENERATION_PROMPT_TEMPLATE",
            query_generation_prompt_template="QUERY_GENERATION_PROMPT_TEMPLATE",
            tags_generation_prompt_template="TAGS_GENERATION_PROMPT_TEMPLATE",
            task_model="TASK_MODEL",
            task_model_external="TASK_MODEL_EXTERNAL",
            title_generation_prompt_template="TITLE_GENERATION_PROMPT_TEMPLATE",
            tools_function_calling_prompt_template="TOOLS_FUNCTION_CALLING_PROMPT_TEMPLATE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Pyopenwebui) -> None:
        with client.api.v1.tasks.config.with_streaming_response.update(
            autocomplete_generation_input_max_length=0,
            enable_autocomplete_generation=True,
            enable_retrieval_query_generation=True,
            enable_search_query_generation=True,
            enable_tags_generation=True,
            enable_title_generation=True,
            image_prompt_generation_prompt_template="IMAGE_PROMPT_GENERATION_PROMPT_TEMPLATE",
            query_generation_prompt_template="QUERY_GENERATION_PROMPT_TEMPLATE",
            tags_generation_prompt_template="TAGS_GENERATION_PROMPT_TEMPLATE",
            task_model="TASK_MODEL",
            task_model_external="TASK_MODEL_EXTERNAL",
            title_generation_prompt_template="TITLE_GENERATION_PROMPT_TEMPLATE",
            tools_function_calling_prompt_template="TOOLS_FUNCTION_CALLING_PROMPT_TEMPLATE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        config = client.api.v1.tasks.config.get()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.tasks.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.tasks.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.api.v1.tasks.config.update(
            autocomplete_generation_input_max_length=0,
            enable_autocomplete_generation=True,
            enable_retrieval_query_generation=True,
            enable_search_query_generation=True,
            enable_tags_generation=True,
            enable_title_generation=True,
            image_prompt_generation_prompt_template="IMAGE_PROMPT_GENERATION_PROMPT_TEMPLATE",
            query_generation_prompt_template="QUERY_GENERATION_PROMPT_TEMPLATE",
            tags_generation_prompt_template="TAGS_GENERATION_PROMPT_TEMPLATE",
            task_model="TASK_MODEL",
            task_model_external="TASK_MODEL_EXTERNAL",
            title_generation_prompt_template="TITLE_GENERATION_PROMPT_TEMPLATE",
            tools_function_calling_prompt_template="TOOLS_FUNCTION_CALLING_PROMPT_TEMPLATE",
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.tasks.config.with_raw_response.update(
            autocomplete_generation_input_max_length=0,
            enable_autocomplete_generation=True,
            enable_retrieval_query_generation=True,
            enable_search_query_generation=True,
            enable_tags_generation=True,
            enable_title_generation=True,
            image_prompt_generation_prompt_template="IMAGE_PROMPT_GENERATION_PROMPT_TEMPLATE",
            query_generation_prompt_template="QUERY_GENERATION_PROMPT_TEMPLATE",
            tags_generation_prompt_template="TAGS_GENERATION_PROMPT_TEMPLATE",
            task_model="TASK_MODEL",
            task_model_external="TASK_MODEL_EXTERNAL",
            title_generation_prompt_template="TITLE_GENERATION_PROMPT_TEMPLATE",
            tools_function_calling_prompt_template="TOOLS_FUNCTION_CALLING_PROMPT_TEMPLATE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.tasks.config.with_streaming_response.update(
            autocomplete_generation_input_max_length=0,
            enable_autocomplete_generation=True,
            enable_retrieval_query_generation=True,
            enable_search_query_generation=True,
            enable_tags_generation=True,
            enable_title_generation=True,
            image_prompt_generation_prompt_template="IMAGE_PROMPT_GENERATION_PROMPT_TEMPLATE",
            query_generation_prompt_template="QUERY_GENERATION_PROMPT_TEMPLATE",
            tags_generation_prompt_template="TAGS_GENERATION_PROMPT_TEMPLATE",
            task_model="TASK_MODEL",
            task_model_external="TASK_MODEL_EXTERNAL",
            title_generation_prompt_template="TITLE_GENERATION_PROMPT_TEMPLATE",
            tools_function_calling_prompt_template="TOOLS_FUNCTION_CALLING_PROMPT_TEMPLATE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.api.v1.tasks.config.get()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.tasks.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.tasks.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True
