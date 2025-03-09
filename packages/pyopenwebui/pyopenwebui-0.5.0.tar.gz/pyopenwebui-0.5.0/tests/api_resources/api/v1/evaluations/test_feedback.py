# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1.evaluations import (
    FeedbackCreateResponse,
    FeedbackGetByIDResponse,
    FeedbackUpdateByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Pyopenwebui) -> None:
        feedback = client.api.v1.evaluations.feedback.create(
            type="type",
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Pyopenwebui) -> None:
        feedback = client.api.v1.evaluations.feedback.create(
            type="type",
            data={
                "comment": "comment",
                "model_id": "model_id",
                "rating": 0,
                "reason": "reason",
                "sibling_model_ids": ["string"],
            },
            meta={},
            snapshot={"chat": {}},
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Pyopenwebui) -> None:
        response = client.api.v1.evaluations.feedback.with_raw_response.create(
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Pyopenwebui) -> None:
        with client.api.v1.evaluations.feedback.with_streaming_response.create(
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_by_id(self, client: Pyopenwebui) -> None:
        feedback = client.api.v1.evaluations.feedback.delete_by_id(
            "id",
        )
        assert_matches_type(object, feedback, path=["response"])

    @parametrize
    def test_raw_response_delete_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.evaluations.feedback.with_raw_response.delete_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(object, feedback, path=["response"])

    @parametrize
    def test_streaming_response_delete_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.evaluations.feedback.with_streaming_response.delete_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(object, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.evaluations.feedback.with_raw_response.delete_by_id(
                "",
            )

    @parametrize
    def test_method_get_by_id(self, client: Pyopenwebui) -> None:
        feedback = client.api.v1.evaluations.feedback.get_by_id(
            "id",
        )
        assert_matches_type(FeedbackGetByIDResponse, feedback, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.evaluations.feedback.with_raw_response.get_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackGetByIDResponse, feedback, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.evaluations.feedback.with_streaming_response.get_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackGetByIDResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.evaluations.feedback.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_update_by_id(self, client: Pyopenwebui) -> None:
        feedback = client.api.v1.evaluations.feedback.update_by_id(
            id="id",
            type="type",
        )
        assert_matches_type(FeedbackUpdateByIDResponse, feedback, path=["response"])

    @parametrize
    def test_method_update_by_id_with_all_params(self, client: Pyopenwebui) -> None:
        feedback = client.api.v1.evaluations.feedback.update_by_id(
            id="id",
            type="type",
            data={
                "comment": "comment",
                "model_id": "model_id",
                "rating": 0,
                "reason": "reason",
                "sibling_model_ids": ["string"],
            },
            meta={},
            snapshot={"chat": {}},
        )
        assert_matches_type(FeedbackUpdateByIDResponse, feedback, path=["response"])

    @parametrize
    def test_raw_response_update_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.evaluations.feedback.with_raw_response.update_by_id(
            id="id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackUpdateByIDResponse, feedback, path=["response"])

    @parametrize
    def test_streaming_response_update_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.evaluations.feedback.with_streaming_response.update_by_id(
            id="id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackUpdateByIDResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.evaluations.feedback.with_raw_response.update_by_id(
                id="",
                type="type",
            )


class TestAsyncFeedback:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPyopenwebui) -> None:
        feedback = await async_client.api.v1.evaluations.feedback.create(
            type="type",
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        feedback = await async_client.api.v1.evaluations.feedback.create(
            type="type",
            data={
                "comment": "comment",
                "model_id": "model_id",
                "rating": 0,
                "reason": "reason",
                "sibling_model_ids": ["string"],
            },
            meta={},
            snapshot={"chat": {}},
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.evaluations.feedback.with_raw_response.create(
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.evaluations.feedback.with_streaming_response.create(
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        feedback = await async_client.api.v1.evaluations.feedback.delete_by_id(
            "id",
        )
        assert_matches_type(object, feedback, path=["response"])

    @parametrize
    async def test_raw_response_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.evaluations.feedback.with_raw_response.delete_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(object, feedback, path=["response"])

    @parametrize
    async def test_streaming_response_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.evaluations.feedback.with_streaming_response.delete_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(object, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.evaluations.feedback.with_raw_response.delete_by_id(
                "",
            )

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        feedback = await async_client.api.v1.evaluations.feedback.get_by_id(
            "id",
        )
        assert_matches_type(FeedbackGetByIDResponse, feedback, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.evaluations.feedback.with_raw_response.get_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackGetByIDResponse, feedback, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.evaluations.feedback.with_streaming_response.get_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackGetByIDResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.evaluations.feedback.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        feedback = await async_client.api.v1.evaluations.feedback.update_by_id(
            id="id",
            type="type",
        )
        assert_matches_type(FeedbackUpdateByIDResponse, feedback, path=["response"])

    @parametrize
    async def test_method_update_by_id_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        feedback = await async_client.api.v1.evaluations.feedback.update_by_id(
            id="id",
            type="type",
            data={
                "comment": "comment",
                "model_id": "model_id",
                "rating": 0,
                "reason": "reason",
                "sibling_model_ids": ["string"],
            },
            meta={},
            snapshot={"chat": {}},
        )
        assert_matches_type(FeedbackUpdateByIDResponse, feedback, path=["response"])

    @parametrize
    async def test_raw_response_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.evaluations.feedback.with_raw_response.update_by_id(
            id="id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackUpdateByIDResponse, feedback, path=["response"])

    @parametrize
    async def test_streaming_response_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.evaluations.feedback.with_streaming_response.update_by_id(
            id="id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackUpdateByIDResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.evaluations.feedback.with_raw_response.update_by_id(
                id="",
                type="type",
            )
