# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .model import (
    ModelResource,
    AsyncModelResource,
    ModelResourceWithRawResponse,
    AsyncModelResourceWithRawResponse,
    ModelResourceWithStreamingResponse,
    AsyncModelResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1 import model_get_params, model_create_params
from .....types.model_model import ModelModel
from .....types.api.v1.model_get_response import ModelGetResponse
from .....types.api.v1.model_delete_response import ModelDeleteResponse
from .....types.api.v1.model_get_base_response import ModelGetBaseResponse

__all__ = ["ModelsResource", "AsyncModelsResource"]


class ModelsResource(SyncAPIResource):
    @cached_property
    def model(self) -> ModelResource:
        return ModelResource(self._client)

    @cached_property
    def with_raw_response(self) -> ModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ModelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        meta: model_create_params.Meta,
        name: str,
        params: Dict[str, object],
        access_control: Optional[object] | NotGiven = NOT_GIVEN,
        base_model_id: Optional[str] | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ModelModel]:
        """
        Create New Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/models/create",
            body=maybe_transform(
                {
                    "id": id,
                    "meta": meta,
                    "name": name,
                    "params": params,
                    "access_control": access_control,
                    "base_model_id": base_model_id,
                    "is_active": is_active,
                },
                model_create_params.ModelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelModel,
        )

    def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelDeleteResponse:
        """Delete All Models"""
        return self._delete(
            "/api/v1/models/delete/all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelDeleteResponse,
        )

    def get(
        self,
        *,
        id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelGetResponse:
        """
        Get Models

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/models/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, model_get_params.ModelGetParams),
            ),
            cast_to=ModelGetResponse,
        )

    def get_base(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelGetBaseResponse:
        """Get Base Models"""
        return self._get(
            "/api/v1/models/base",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelGetBaseResponse,
        )


class AsyncModelsResource(AsyncAPIResource):
    @cached_property
    def model(self) -> AsyncModelResource:
        return AsyncModelResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncModelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        meta: model_create_params.Meta,
        name: str,
        params: Dict[str, object],
        access_control: Optional[object] | NotGiven = NOT_GIVEN,
        base_model_id: Optional[str] | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ModelModel]:
        """
        Create New Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/models/create",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "meta": meta,
                    "name": name,
                    "params": params,
                    "access_control": access_control,
                    "base_model_id": base_model_id,
                    "is_active": is_active,
                },
                model_create_params.ModelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelModel,
        )

    async def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelDeleteResponse:
        """Delete All Models"""
        return await self._delete(
            "/api/v1/models/delete/all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelDeleteResponse,
        )

    async def get(
        self,
        *,
        id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelGetResponse:
        """
        Get Models

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/models/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, model_get_params.ModelGetParams),
            ),
            cast_to=ModelGetResponse,
        )

    async def get_base(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelGetBaseResponse:
        """Get Base Models"""
        return await self._get(
            "/api/v1/models/base",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelGetBaseResponse,
        )


class ModelsResourceWithRawResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.create = to_raw_response_wrapper(
            models.create,
        )
        self.delete = to_raw_response_wrapper(
            models.delete,
        )
        self.get = to_raw_response_wrapper(
            models.get,
        )
        self.get_base = to_raw_response_wrapper(
            models.get_base,
        )

    @cached_property
    def model(self) -> ModelResourceWithRawResponse:
        return ModelResourceWithRawResponse(self._models.model)


class AsyncModelsResourceWithRawResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.create = async_to_raw_response_wrapper(
            models.create,
        )
        self.delete = async_to_raw_response_wrapper(
            models.delete,
        )
        self.get = async_to_raw_response_wrapper(
            models.get,
        )
        self.get_base = async_to_raw_response_wrapper(
            models.get_base,
        )

    @cached_property
    def model(self) -> AsyncModelResourceWithRawResponse:
        return AsyncModelResourceWithRawResponse(self._models.model)


class ModelsResourceWithStreamingResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.create = to_streamed_response_wrapper(
            models.create,
        )
        self.delete = to_streamed_response_wrapper(
            models.delete,
        )
        self.get = to_streamed_response_wrapper(
            models.get,
        )
        self.get_base = to_streamed_response_wrapper(
            models.get_base,
        )

    @cached_property
    def model(self) -> ModelResourceWithStreamingResponse:
        return ModelResourceWithStreamingResponse(self._models.model)


class AsyncModelsResourceWithStreamingResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.create = async_to_streamed_response_wrapper(
            models.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            models.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            models.get,
        )
        self.get_base = async_to_streamed_response_wrapper(
            models.get_base,
        )

    @cached_property
    def model(self) -> AsyncModelResourceWithStreamingResponse:
        return AsyncModelResourceWithStreamingResponse(self._models.model)
