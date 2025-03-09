# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

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
from .....types.api.v1.groups import id_update_params
from .....types.api.v1.groups.id_get_response import IDGetResponse
from .....types.api.v1.groups.id_delete_response import IDDeleteResponse
from .....types.api.v1.groups.id_update_response import IDUpdateResponse

__all__ = ["IDResource", "AsyncIDResource"]


class IDResource(SyncAPIResource):
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
        id: str,
        *,
        description: str,
        name: str,
        permissions: Optional[object] | NotGiven = NOT_GIVEN,
        user_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IDUpdateResponse]:
        """
        Update Group By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/groups/id/{id}/update",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "permissions": permissions,
                    "user_ids": user_ids,
                },
                id_update_params.IDUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IDUpdateResponse,
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
        Delete Group By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v1/groups/id/{id}/delete",
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
    ) -> Optional[IDGetResponse]:
        """
        Get Group By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/groups/id/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IDGetResponse,
        )


class AsyncIDResource(AsyncAPIResource):
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
        id: str,
        *,
        description: str,
        name: str,
        permissions: Optional[object] | NotGiven = NOT_GIVEN,
        user_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IDUpdateResponse]:
        """
        Update Group By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/groups/id/{id}/update",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "permissions": permissions,
                    "user_ids": user_ids,
                },
                id_update_params.IDUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IDUpdateResponse,
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
        Delete Group By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v1/groups/id/{id}/delete",
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
    ) -> Optional[IDGetResponse]:
        """
        Get Group By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/groups/id/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IDGetResponse,
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
