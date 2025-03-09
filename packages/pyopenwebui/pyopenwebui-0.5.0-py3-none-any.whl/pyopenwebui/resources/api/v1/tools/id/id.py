# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from .valves.valves import (
    ValvesResource,
    AsyncValvesResource,
    ValvesResourceWithRawResponse,
    AsyncValvesResourceWithRawResponse,
    ValvesResourceWithStreamingResponse,
    AsyncValvesResourceWithStreamingResponse,
)
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.tool_model import ToolModel
from ......types.api.v1.tools import id_update_params
from ......types.api.v1.tools.id_delete_response import IDDeleteResponse

__all__ = ["IDResource", "AsyncIDResource"]


class IDResource(SyncAPIResource):
    @cached_property
    def valves(self) -> ValvesResource:
        return ValvesResource(self._client)

    @cached_property
    def with_raw_response(self) -> IDResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return IDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IDResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return IDResourceWithStreamingResponse(self)

    def update(
        self,
        id_1: str,
        *,
        id_2: str,
        content: str,
        meta: id_update_params.Meta,
        name: str,
        access_control: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ToolModel]:
        """
        Update Tools By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_1:
            raise ValueError(f"Expected a non-empty value for `id_1` but received {id_1!r}")
        return self._post(
            f"/api/v1/tools/id/{id_1}/update",
            body=maybe_transform(
                {
                    "id_2": id_2,
                    "content": content,
                    "meta": meta,
                    "name": name,
                    "access_control": access_control,
                },
                id_update_params.IDUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolModel,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IDDeleteResponse:
        """
        Delete Tools By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v1/tools/id/{id}/delete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IDDeleteResponse,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ToolModel]:
        """
        Get Tools By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/tools/id/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolModel,
        )


class AsyncIDResource(AsyncAPIResource):
    @cached_property
    def valves(self) -> AsyncValvesResource:
        return AsyncValvesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIDResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIDResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncIDResourceWithStreamingResponse(self)

    async def update(
        self,
        id_1: str,
        *,
        id_2: str,
        content: str,
        meta: id_update_params.Meta,
        name: str,
        access_control: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ToolModel]:
        """
        Update Tools By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_1:
            raise ValueError(f"Expected a non-empty value for `id_1` but received {id_1!r}")
        return await self._post(
            f"/api/v1/tools/id/{id_1}/update",
            body=await async_maybe_transform(
                {
                    "id_2": id_2,
                    "content": content,
                    "meta": meta,
                    "name": name,
                    "access_control": access_control,
                },
                id_update_params.IDUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolModel,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IDDeleteResponse:
        """
        Delete Tools By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v1/tools/id/{id}/delete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IDDeleteResponse,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ToolModel]:
        """
        Get Tools By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/tools/id/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolModel,
        )


class IDResourceWithRawResponse:
    def __init__(self, id: IDResource) -> None:
        self._id = id

        self.update = to_raw_response_wrapper(
            id.update,
        )
        self.delete = to_raw_response_wrapper(
            id.delete,
        )
        self.get = to_raw_response_wrapper(
            id.get,
        )

    @cached_property
    def valves(self) -> ValvesResourceWithRawResponse:
        return ValvesResourceWithRawResponse(self._id.valves)


class AsyncIDResourceWithRawResponse:
    def __init__(self, id: AsyncIDResource) -> None:
        self._id = id

        self.update = async_to_raw_response_wrapper(
            id.update,
        )
        self.delete = async_to_raw_response_wrapper(
            id.delete,
        )
        self.get = async_to_raw_response_wrapper(
            id.get,
        )

    @cached_property
    def valves(self) -> AsyncValvesResourceWithRawResponse:
        return AsyncValvesResourceWithRawResponse(self._id.valves)


class IDResourceWithStreamingResponse:
    def __init__(self, id: IDResource) -> None:
        self._id = id

        self.update = to_streamed_response_wrapper(
            id.update,
        )
        self.delete = to_streamed_response_wrapper(
            id.delete,
        )
        self.get = to_streamed_response_wrapper(
            id.get,
        )

    @cached_property
    def valves(self) -> ValvesResourceWithStreamingResponse:
        return ValvesResourceWithStreamingResponse(self._id.valves)


class AsyncIDResourceWithStreamingResponse:
    def __init__(self, id: AsyncIDResource) -> None:
        self._id = id

        self.update = async_to_streamed_response_wrapper(
            id.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            id.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            id.get,
        )

    @cached_property
    def valves(self) -> AsyncValvesResourceWithStreamingResponse:
        return AsyncValvesResourceWithStreamingResponse(self._id.valves)
