# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from pyopenwebui import Pyopenwebui, AsyncPyopenwebui
from tests.utils import assert_matches_type
from pyopenwebui.types.api.v1 import (
    KnowledgeGetResponse,
    KnowledgeCreateResponse,
    KnowledgeGetByIDResponse,
    KnowledgeGetListResponse,
    KnowledgeResetByIDResponse,
    KnowledgeDeleteByIDResponse,
    KnowledgeUpdateByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledge:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Pyopenwebui) -> None:
        knowledge = client.api.v1.knowledge.create(
            description="description",
            name="name",
        )
        assert_matches_type(Optional[KnowledgeCreateResponse], knowledge, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Pyopenwebui) -> None:
        knowledge = client.api.v1.knowledge.create(
            description="description",
            name="name",
            access_control={},
            data={},
        )
        assert_matches_type(Optional[KnowledgeCreateResponse], knowledge, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Pyopenwebui) -> None:
        response = client.api.v1.knowledge.with_raw_response.create(
            description="description",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(Optional[KnowledgeCreateResponse], knowledge, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Pyopenwebui) -> None:
        with client.api.v1.knowledge.with_streaming_response.create(
            description="description",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(Optional[KnowledgeCreateResponse], knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_by_id(self, client: Pyopenwebui) -> None:
        knowledge = client.api.v1.knowledge.delete_by_id(
            "id",
        )
        assert_matches_type(KnowledgeDeleteByIDResponse, knowledge, path=["response"])

    @parametrize
    def test_raw_response_delete_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.knowledge.with_raw_response.delete_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(KnowledgeDeleteByIDResponse, knowledge, path=["response"])

    @parametrize
    def test_streaming_response_delete_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.knowledge.with_streaming_response.delete_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(KnowledgeDeleteByIDResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.knowledge.with_raw_response.delete_by_id(
                "",
            )

    @parametrize
    def test_method_get(self, client: Pyopenwebui) -> None:
        knowledge = client.api.v1.knowledge.get()
        assert_matches_type(KnowledgeGetResponse, knowledge, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Pyopenwebui) -> None:
        response = client.api.v1.knowledge.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(KnowledgeGetResponse, knowledge, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Pyopenwebui) -> None:
        with client.api.v1.knowledge.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(KnowledgeGetResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_id(self, client: Pyopenwebui) -> None:
        knowledge = client.api.v1.knowledge.get_by_id(
            "id",
        )
        assert_matches_type(Optional[KnowledgeGetByIDResponse], knowledge, path=["response"])

    @parametrize
    def test_raw_response_get_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.knowledge.with_raw_response.get_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(Optional[KnowledgeGetByIDResponse], knowledge, path=["response"])

    @parametrize
    def test_streaming_response_get_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.knowledge.with_streaming_response.get_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(Optional[KnowledgeGetByIDResponse], knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.knowledge.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    def test_method_get_list(self, client: Pyopenwebui) -> None:
        knowledge = client.api.v1.knowledge.get_list()
        assert_matches_type(KnowledgeGetListResponse, knowledge, path=["response"])

    @parametrize
    def test_raw_response_get_list(self, client: Pyopenwebui) -> None:
        response = client.api.v1.knowledge.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(KnowledgeGetListResponse, knowledge, path=["response"])

    @parametrize
    def test_streaming_response_get_list(self, client: Pyopenwebui) -> None:
        with client.api.v1.knowledge.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(KnowledgeGetListResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_reset_by_id(self, client: Pyopenwebui) -> None:
        knowledge = client.api.v1.knowledge.reset_by_id(
            "id",
        )
        assert_matches_type(Optional[KnowledgeResetByIDResponse], knowledge, path=["response"])

    @parametrize
    def test_raw_response_reset_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.knowledge.with_raw_response.reset_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(Optional[KnowledgeResetByIDResponse], knowledge, path=["response"])

    @parametrize
    def test_streaming_response_reset_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.knowledge.with_streaming_response.reset_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(Optional[KnowledgeResetByIDResponse], knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reset_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.knowledge.with_raw_response.reset_by_id(
                "",
            )

    @parametrize
    def test_method_update_by_id(self, client: Pyopenwebui) -> None:
        knowledge = client.api.v1.knowledge.update_by_id(
            id="id",
            description="description",
            name="name",
        )
        assert_matches_type(Optional[KnowledgeUpdateByIDResponse], knowledge, path=["response"])

    @parametrize
    def test_method_update_by_id_with_all_params(self, client: Pyopenwebui) -> None:
        knowledge = client.api.v1.knowledge.update_by_id(
            id="id",
            description="description",
            name="name",
            access_control={},
            data={},
        )
        assert_matches_type(Optional[KnowledgeUpdateByIDResponse], knowledge, path=["response"])

    @parametrize
    def test_raw_response_update_by_id(self, client: Pyopenwebui) -> None:
        response = client.api.v1.knowledge.with_raw_response.update_by_id(
            id="id",
            description="description",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = response.parse()
        assert_matches_type(Optional[KnowledgeUpdateByIDResponse], knowledge, path=["response"])

    @parametrize
    def test_streaming_response_update_by_id(self, client: Pyopenwebui) -> None:
        with client.api.v1.knowledge.with_streaming_response.update_by_id(
            id="id",
            description="description",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = response.parse()
            assert_matches_type(Optional[KnowledgeUpdateByIDResponse], knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_by_id(self, client: Pyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.knowledge.with_raw_response.update_by_id(
                id="",
                description="description",
                name="name",
            )


class TestAsyncKnowledge:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPyopenwebui) -> None:
        knowledge = await async_client.api.v1.knowledge.create(
            description="description",
            name="name",
        )
        assert_matches_type(Optional[KnowledgeCreateResponse], knowledge, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        knowledge = await async_client.api.v1.knowledge.create(
            description="description",
            name="name",
            access_control={},
            data={},
        )
        assert_matches_type(Optional[KnowledgeCreateResponse], knowledge, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.knowledge.with_raw_response.create(
            description="description",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(Optional[KnowledgeCreateResponse], knowledge, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.knowledge.with_streaming_response.create(
            description="description",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(Optional[KnowledgeCreateResponse], knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        knowledge = await async_client.api.v1.knowledge.delete_by_id(
            "id",
        )
        assert_matches_type(KnowledgeDeleteByIDResponse, knowledge, path=["response"])

    @parametrize
    async def test_raw_response_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.knowledge.with_raw_response.delete_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(KnowledgeDeleteByIDResponse, knowledge, path=["response"])

    @parametrize
    async def test_streaming_response_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.knowledge.with_streaming_response.delete_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(KnowledgeDeleteByIDResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.knowledge.with_raw_response.delete_by_id(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncPyopenwebui) -> None:
        knowledge = await async_client.api.v1.knowledge.get()
        assert_matches_type(KnowledgeGetResponse, knowledge, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.knowledge.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(KnowledgeGetResponse, knowledge, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.knowledge.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(KnowledgeGetResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        knowledge = await async_client.api.v1.knowledge.get_by_id(
            "id",
        )
        assert_matches_type(Optional[KnowledgeGetByIDResponse], knowledge, path=["response"])

    @parametrize
    async def test_raw_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.knowledge.with_raw_response.get_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(Optional[KnowledgeGetByIDResponse], knowledge, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.knowledge.with_streaming_response.get_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(Optional[KnowledgeGetByIDResponse], knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.knowledge.with_raw_response.get_by_id(
                "",
            )

    @parametrize
    async def test_method_get_list(self, async_client: AsyncPyopenwebui) -> None:
        knowledge = await async_client.api.v1.knowledge.get_list()
        assert_matches_type(KnowledgeGetListResponse, knowledge, path=["response"])

    @parametrize
    async def test_raw_response_get_list(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.knowledge.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(KnowledgeGetListResponse, knowledge, path=["response"])

    @parametrize
    async def test_streaming_response_get_list(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.knowledge.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(KnowledgeGetListResponse, knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reset_by_id(self, async_client: AsyncPyopenwebui) -> None:
        knowledge = await async_client.api.v1.knowledge.reset_by_id(
            "id",
        )
        assert_matches_type(Optional[KnowledgeResetByIDResponse], knowledge, path=["response"])

    @parametrize
    async def test_raw_response_reset_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.knowledge.with_raw_response.reset_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(Optional[KnowledgeResetByIDResponse], knowledge, path=["response"])

    @parametrize
    async def test_streaming_response_reset_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.knowledge.with_streaming_response.reset_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(Optional[KnowledgeResetByIDResponse], knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reset_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.knowledge.with_raw_response.reset_by_id(
                "",
            )

    @parametrize
    async def test_method_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        knowledge = await async_client.api.v1.knowledge.update_by_id(
            id="id",
            description="description",
            name="name",
        )
        assert_matches_type(Optional[KnowledgeUpdateByIDResponse], knowledge, path=["response"])

    @parametrize
    async def test_method_update_by_id_with_all_params(self, async_client: AsyncPyopenwebui) -> None:
        knowledge = await async_client.api.v1.knowledge.update_by_id(
            id="id",
            description="description",
            name="name",
            access_control={},
            data={},
        )
        assert_matches_type(Optional[KnowledgeUpdateByIDResponse], knowledge, path=["response"])

    @parametrize
    async def test_raw_response_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        response = await async_client.api.v1.knowledge.with_raw_response.update_by_id(
            id="id",
            description="description",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge = await response.parse()
        assert_matches_type(Optional[KnowledgeUpdateByIDResponse], knowledge, path=["response"])

    @parametrize
    async def test_streaming_response_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        async with async_client.api.v1.knowledge.with_streaming_response.update_by_id(
            id="id",
            description="description",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge = await response.parse()
            assert_matches_type(Optional[KnowledgeUpdateByIDResponse], knowledge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_by_id(self, async_client: AsyncPyopenwebui) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.knowledge.with_raw_response.update_by_id(
                id="",
                description="description",
                name="name",
            )
