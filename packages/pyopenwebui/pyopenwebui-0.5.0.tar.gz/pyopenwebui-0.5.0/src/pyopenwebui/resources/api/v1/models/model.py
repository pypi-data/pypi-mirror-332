# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

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
from .....types.model_model import ModelModel
from .....types.api.v1.models import model_get_params, model_delete_params, model_toggle_params, model_update_params
from .....types.api.v1.models.model_get_response import ModelGetResponse
from .....types.api.v1.models.model_delete_response import ModelDeleteResponse
from .....types.api.v1.models.model_toggle_response import ModelToggleResponse

__all__ = ["ModelResource", "AsyncModelResource"]


class ModelResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ModelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ModelResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        id_1: str,
        id_2: str,
        meta: model_update_params.Meta,
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
        Update Model By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/models/model/update",
            body=maybe_transform(
                {
                    "id_2": id_2,
                    "meta": meta,
                    "name": name,
                    "params": params,
                    "access_control": access_control,
                    "base_model_id": base_model_id,
                    "is_active": is_active,
                },
                model_update_params.ModelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id_1": id_1}, model_update_params.ModelUpdateParams),
            ),
            cast_to=ModelModel,
        )

    def delete(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelDeleteResponse:
        """
        Delete Model By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/api/v1/models/model/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, model_delete_params.ModelDeleteParams),
            ),
            cast_to=ModelDeleteResponse,
        )

    def get(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ModelGetResponse]:
        """
        Get Model By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/models/model",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, model_get_params.ModelGetParams),
            ),
            cast_to=ModelGetResponse,
        )

    def toggle(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ModelToggleResponse]:
        """
        Toggle Model By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/models/model/toggle",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, model_toggle_params.ModelToggleParams),
            ),
            cast_to=ModelToggleResponse,
        )


class AsyncModelResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncModelResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        id_1: str,
        id_2: str,
        meta: model_update_params.Meta,
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
        Update Model By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/models/model/update",
            body=await async_maybe_transform(
                {
                    "id_2": id_2,
                    "meta": meta,
                    "name": name,
                    "params": params,
                    "access_control": access_control,
                    "base_model_id": base_model_id,
                    "is_active": is_active,
                },
                model_update_params.ModelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id_1": id_1}, model_update_params.ModelUpdateParams),
            ),
            cast_to=ModelModel,
        )

    async def delete(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelDeleteResponse:
        """
        Delete Model By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/api/v1/models/model/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, model_delete_params.ModelDeleteParams),
            ),
            cast_to=ModelDeleteResponse,
        )

    async def get(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ModelGetResponse]:
        """
        Get Model By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/models/model",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, model_get_params.ModelGetParams),
            ),
            cast_to=ModelGetResponse,
        )

    async def toggle(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ModelToggleResponse]:
        """
        Toggle Model By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/models/model/toggle",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, model_toggle_params.ModelToggleParams),
            ),
            cast_to=ModelToggleResponse,
        )


class ModelResourceWithRawResponse:
    def __init__(self, model: ModelResource) -> None:
        self._model = model

        self.update = to_raw_response_wrapper(
            model.update,
        )
        self.delete = to_raw_response_wrapper(
            model.delete,
        )
        self.get = to_raw_response_wrapper(
            model.get,
        )
        self.toggle = to_raw_response_wrapper(
            model.toggle,
        )


class AsyncModelResourceWithRawResponse:
    def __init__(self, model: AsyncModelResource) -> None:
        self._model = model

        self.update = async_to_raw_response_wrapper(
            model.update,
        )
        self.delete = async_to_raw_response_wrapper(
            model.delete,
        )
        self.get = async_to_raw_response_wrapper(
            model.get,
        )
        self.toggle = async_to_raw_response_wrapper(
            model.toggle,
        )


class ModelResourceWithStreamingResponse:
    def __init__(self, model: ModelResource) -> None:
        self._model = model

        self.update = to_streamed_response_wrapper(
            model.update,
        )
        self.delete = to_streamed_response_wrapper(
            model.delete,
        )
        self.get = to_streamed_response_wrapper(
            model.get,
        )
        self.toggle = to_streamed_response_wrapper(
            model.toggle,
        )


class AsyncModelResourceWithStreamingResponse:
    def __init__(self, model: AsyncModelResource) -> None:
        self._model = model

        self.update = async_to_streamed_response_wrapper(
            model.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            model.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            model.get,
        )
        self.toggle = async_to_streamed_response_wrapper(
            model.toggle,
        )
