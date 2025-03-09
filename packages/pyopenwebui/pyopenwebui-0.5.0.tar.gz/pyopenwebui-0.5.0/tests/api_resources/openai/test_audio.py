# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudio:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_speech(self, client: Pyopenwebui) -> None:
        audio = client.openai.audio.speech()
        assert_matches_type(object, audio, path=["response"])

    @parametrize
    def test_raw_response_speech(self, client: Pyopenwebui) -> None:
        response = client.openai.audio.with_raw_response.speech()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio = response.parse()
        assert_matches_type(object, audio, path=["response"])

    @parametrize
    def test_streaming_response_speech(self, client: Pyopenwebui) -> None:
        with client.openai.audio.with_streaming_response.speech() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio = response.parse()
            assert_matches_type(object, audio, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAudio:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_speech(self, async_client: AsyncPyopenwebui) -> None:
        audio = await async_client.openai.audio.speech()
        assert_matches_type(object, audio, path=["response"])

    @parametrize
    async def test_raw_response_speech(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.openai.audio.with_raw_response.speech()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio = await response.parse()
        assert_matches_type(object, audio, path=["response"])

    @parametrize
    async def test_streaming_response_speech(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.openai.audio.with_streaming_response.speech() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio = await response.parse()
            assert_matches_type(object, audio, path=["response"])

        assert cast(Any, response.is_closed) is True
