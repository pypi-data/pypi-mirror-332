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
        config = client.api.v1.images.config.update(
            automatic1111={
                "automatic1111_api_auth": "AUTOMATIC1111_API_AUTH",
                "automatic1111_base_url": "AUTOMATIC1111_BASE_URL",
                "automatic1111_cfg_scale": "string",
                "automatic1111_sampler": "AUTOMATIC1111_SAMPLER",
                "automatic1111_scheduler": "AUTOMATIC1111_SCHEDULER",
            },
            comfyui={
                "comfyui_api_key": "COMFYUI_API_KEY",
                "comfyui_base_url": "COMFYUI_BASE_URL",
                "comfyui_workflow": "COMFYUI_WORKFLOW",
                "comfyui_workflow_nodes": [{}],
            },
            enabled=True,
            engine="engine",
            gemini={
                "gemini_api_base_url": "GEMINI_API_BASE_URL",
                "gemini_api_key": "GEMINI_API_KEY",
            },
            openai={
                "openai_api_base_url": "OPENAI_API_BASE_URL",
                "openai_api_key": "OPENAI_API_KEY",
            },
            prompt_generation=True,
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Pyopenwebui) -> None:
        response = client.api.v1.images.config.with_raw_response.update(
            automatic1111={
                "automatic1111_api_auth": "AUTOMATIC1111_API_AUTH",
                "automatic1111_base_url": "AUTOMATIC1111_BASE_URL",
                "automatic1111_cfg_scale": "string",
                "automatic1111_sampler": "AUTOMATIC1111_SAMPLER",
                "automatic1111_scheduler": "AUTOMATIC1111_SCHEDULER",
            },
            comfyui={
                "comfyui_api_key": "COMFYUI_API_KEY",
                "comfyui_base_url": "COMFYUI_BASE_URL",
                "comfyui_workflow": "COMFYUI_WORKFLOW",
                "comfyui_workflow_nodes": [{}],
            },
            enabled=True,
            engine="engine",
            gemini={
                "gemini_api_base_url": "GEMINI_API_BASE_URL",
                "gemini_api_key": "GEMINI_API_KEY",
            },
            openai={
                "openai_api_base_url": "OPENAI_API_BASE_URL",
                "openai_api_key": "OPENAI_API_KEY",
            },
            prompt_generation=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Pyopenwebui) -> None:
        with client.api.v1.images.config.with_streaming_response.update(
            automatic1111={
                "automatic1111_api_auth": "AUTOMATIC1111_API_AUTH",
                "automatic1111_base_url": "AUTOMATIC1111_BASE_URL",
                "automatic1111_cfg_scale": "string",
                "automatic1111_sampler": "AUTOMATIC1111_SAMPLER",
                "automatic1111_scheduler": "AUTOMATIC1111_SCHEDULER",
            },
            comfyui={
                "comfyui_api_key": "COMFYUI_API_KEY",
                "comfyui_base_url": "COMFYUI_BASE_URL",
                "comfyui_workflow": "COMFYUI_WORKFLOW",
                "comfyui_workflow_nodes": [{}],
            },
            enabled=True,
            engine="engine",
            gemini={
                "gemini_api_base_url": "GEMINI_API_BASE_URL",
                "gemini_api_key": "GEMINI_API_KEY",
            },
            openai={
                "openai_api_base_url": "OPENAI_API_BASE_URL",
                "openai_api_key": "OPENAI_API_KEY",
            },
            prompt_generation=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        config = client.api.v1.images.config.get()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.images.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.images.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.api.v1.images.config.update(
            automatic1111={
                "automatic1111_api_auth": "AUTOMATIC1111_API_AUTH",
                "automatic1111_base_url": "AUTOMATIC1111_BASE_URL",
                "automatic1111_cfg_scale": "string",
                "automatic1111_sampler": "AUTOMATIC1111_SAMPLER",
                "automatic1111_scheduler": "AUTOMATIC1111_SCHEDULER",
            },
            comfyui={
                "comfyui_api_key": "COMFYUI_API_KEY",
                "comfyui_base_url": "COMFYUI_BASE_URL",
                "comfyui_workflow": "COMFYUI_WORKFLOW",
                "comfyui_workflow_nodes": [{}],
            },
            enabled=True,
            engine="engine",
            gemini={
                "gemini_api_base_url": "GEMINI_API_BASE_URL",
                "gemini_api_key": "GEMINI_API_KEY",
            },
            openai={
                "openai_api_base_url": "OPENAI_API_BASE_URL",
                "openai_api_key": "OPENAI_API_KEY",
            },
            prompt_generation=True,
        )
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.images.config.with_raw_response.update(
            automatic1111={
                "automatic1111_api_auth": "AUTOMATIC1111_API_AUTH",
                "automatic1111_base_url": "AUTOMATIC1111_BASE_URL",
                "automatic1111_cfg_scale": "string",
                "automatic1111_sampler": "AUTOMATIC1111_SAMPLER",
                "automatic1111_scheduler": "AUTOMATIC1111_SCHEDULER",
            },
            comfyui={
                "comfyui_api_key": "COMFYUI_API_KEY",
                "comfyui_base_url": "COMFYUI_BASE_URL",
                "comfyui_workflow": "COMFYUI_WORKFLOW",
                "comfyui_workflow_nodes": [{}],
            },
            enabled=True,
            engine="engine",
            gemini={
                "gemini_api_base_url": "GEMINI_API_BASE_URL",
                "gemini_api_key": "GEMINI_API_KEY",
            },
            openai={
                "openai_api_base_url": "OPENAI_API_BASE_URL",
                "openai_api_key": "OPENAI_API_KEY",
            },
            prompt_generation=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.images.config.with_streaming_response.update(
            automatic1111={
                "automatic1111_api_auth": "AUTOMATIC1111_API_AUTH",
                "automatic1111_base_url": "AUTOMATIC1111_BASE_URL",
                "automatic1111_cfg_scale": "string",
                "automatic1111_sampler": "AUTOMATIC1111_SAMPLER",
                "automatic1111_scheduler": "AUTOMATIC1111_SCHEDULER",
            },
            comfyui={
                "comfyui_api_key": "COMFYUI_API_KEY",
                "comfyui_base_url": "COMFYUI_BASE_URL",
                "comfyui_workflow": "COMFYUI_WORKFLOW",
                "comfyui_workflow_nodes": [{}],
            },
            enabled=True,
            engine="engine",
            gemini={
                "gemini_api_base_url": "GEMINI_API_BASE_URL",
                "gemini_api_key": "GEMINI_API_KEY",
            },
            openai={
                "openai_api_base_url": "OPENAI_API_BASE_URL",
                "openai_api_key": "OPENAI_API_KEY",
            },
            prompt_generation=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        config = await async_client.api.v1.images.config.get()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.images.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.images.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True
