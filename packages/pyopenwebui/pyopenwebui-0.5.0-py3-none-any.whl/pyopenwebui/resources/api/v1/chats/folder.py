# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from .....types.api.v1.chats import folder_update_params
from .....types.chat_response import ChatResponse
from .....types.api.v1.chats.folder_get_response import FolderGetResponse

__all__ = ["FolderResource", "AsyncFolderResource"]


class FolderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FolderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return FolderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FolderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return FolderResourceWithStreamingResponse(self)

    def update(
        self,
        id: str,
        *,
        folder_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Update Chat Folder Id By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/chats/{id}/folder",
            body=maybe_transform({"folder_id": folder_id}, folder_update_params.FolderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )

    def get(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FolderGetResponse:
        """
        Get Chats By Folder Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._get(
            f"/api/v1/chats/folder/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderGetResponse,
        )


class AsyncFolderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFolderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFolderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFolderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncFolderResourceWithStreamingResponse(self)

    async def update(
        self,
        id: str,
        *,
        folder_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Update Chat Folder Id By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/chats/{id}/folder",
            body=await async_maybe_transform({"folder_id": folder_id}, folder_update_params.FolderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )

    async def get(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FolderGetResponse:
        """
        Get Chats By Folder Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._get(
            f"/api/v1/chats/folder/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderGetResponse,
        )


class FolderResourceWithRawResponse:
    def __init__(self, folder: FolderResource) -> None:
        self._folder = folder

        self.update = to_raw_response_wrapper(
            folder.update,
        )
        self.get = to_raw_response_wrapper(
            folder.get,
        )


class AsyncFolderResourceWithRawResponse:
    def __init__(self, folder: AsyncFolderResource) -> None:
        self._folder = folder

        self.update = async_to_raw_response_wrapper(
            folder.update,
        )
        self.get = async_to_raw_response_wrapper(
            folder.get,
        )


class FolderResourceWithStreamingResponse:
    def __init__(self, folder: FolderResource) -> None:
        self._folder = folder

        self.update = to_streamed_response_wrapper(
            folder.update,
        )
        self.get = to_streamed_response_wrapper(
            folder.get,
        )


class AsyncFolderResourceWithStreamingResponse:
    def __init__(self, folder: AsyncFolderResource) -> None:
        self._folder = folder

        self.update = async_to_streamed_response_wrapper(
            folder.update,
        )
        self.get = async_to_streamed_response_wrapper(
            folder.get,
        )
