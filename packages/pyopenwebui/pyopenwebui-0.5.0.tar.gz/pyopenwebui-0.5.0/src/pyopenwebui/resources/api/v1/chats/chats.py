# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .all import (
    AllResource,
    AsyncAllResource,
    AllResourceWithRawResponse,
    AsyncAllResourceWithRawResponse,
    AllResourceWithStreamingResponse,
    AsyncAllResourceWithStreamingResponse,
)
from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from .clone import (
    CloneResource,
    AsyncCloneResource,
    CloneResourceWithRawResponse,
    AsyncCloneResourceWithRawResponse,
    CloneResourceWithStreamingResponse,
    AsyncCloneResourceWithStreamingResponse,
)
from .share import (
    ShareResource,
    AsyncShareResource,
    ShareResourceWithRawResponse,
    AsyncShareResourceWithRawResponse,
    ShareResourceWithStreamingResponse,
    AsyncShareResourceWithStreamingResponse,
)
from .folder import (
    FolderResource,
    AsyncFolderResource,
    FolderResourceWithRawResponse,
    AsyncFolderResourceWithRawResponse,
    FolderResourceWithStreamingResponse,
    AsyncFolderResourceWithStreamingResponse,
)
from .pinned import (
    PinnedResource,
    AsyncPinnedResource,
    PinnedResourceWithRawResponse,
    AsyncPinnedResourceWithRawResponse,
    PinnedResourceWithStreamingResponse,
    AsyncPinnedResourceWithStreamingResponse,
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
from .....types.api.v1 import (
    chat_get_params,
    chat_list_params,
    chat_create_params,
    chat_import_params,
    chat_search_params,
    chat_update_by_id_params,
    chat_get_archived_list_params,
)
from .....types.chat_response import ChatResponse
from .....types.api.v1.chat_get_response import ChatGetResponse
from .....types.api.v1.chat_list_response import ChatListResponse
from .....types.api.v1.chat_search_response import ChatSearchResponse
from .....types.api.v1.chat_delete_all_response import ChatDeleteAllResponse
from .....types.api.v1.chat_delete_by_id_response import ChatDeleteByIDResponse
from .....types.api.v1.chat_get_archived_list_response import ChatGetArchivedListResponse

__all__ = ["ChatsResource", "AsyncChatsResource"]


class ChatsResource(SyncAPIResource):
    @cached_property
    def folder(self) -> FolderResource:
        return FolderResource(self._client)

    @cached_property
    def pinned(self) -> PinnedResource:
        return PinnedResource(self._client)

    @cached_property
    def all(self) -> AllResource:
        return AllResource(self._client)

    @cached_property
    def share(self) -> ShareResource:
        return ShareResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def clone(self) -> CloneResource:
        return CloneResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ChatsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        chat: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Create New Chat

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/chats/new",
            body=maybe_transform({"chat": chat}, chat_create_params.ChatCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )

    def list(
        self,
        user_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        skip: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatListResponse:
        """
        Get User Chat List By User Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/api/v1/chats/list/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    chat_list_params.ChatListParams,
                ),
            ),
            cast_to=ChatListResponse,
        )

    def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Archive Chat By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/chats/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )

    def delete_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatDeleteAllResponse:
        """Delete All User Chats"""
        return self._delete(
            "/api/v1/chats/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatDeleteAllResponse,
        )

    def delete_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatDeleteByIDResponse:
        """
        Delete Chat By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v1/chats/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatDeleteByIDResponse,
        )

    def get(
        self,
        *,
        page: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatGetResponse:
        """
        Get Session User Chat List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/chats/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, chat_get_params.ChatGetParams),
            ),
            cast_to=ChatGetResponse,
        )

    def get_archived_list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        skip: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatGetArchivedListResponse:
        """
        Get Archived Session User Chat List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/chats/archived",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    chat_get_archived_list_params.ChatGetArchivedListParams,
                ),
            ),
            cast_to=ChatGetArchivedListResponse,
        )

    def get_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Get Chat By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/chats/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )

    def import_(
        self,
        *,
        chat: object,
        folder_id: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        pinned: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Import Chat

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/chats/import",
            body=maybe_transform(
                {
                    "chat": chat,
                    "folder_id": folder_id,
                    "meta": meta,
                    "pinned": pinned,
                },
                chat_import_params.ChatImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )

    def pin_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Pin Chat By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/chats/{id}/pin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )

    def search(
        self,
        *,
        text: str,
        page: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatSearchResponse:
        """
        Search User Chats

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/chats/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "text": text,
                        "page": page,
                    },
                    chat_search_params.ChatSearchParams,
                ),
            ),
            cast_to=ChatSearchResponse,
        )

    def update_by_id(
        self,
        id: str,
        *,
        chat: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Update Chat By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/chats/{id}",
            body=maybe_transform({"chat": chat}, chat_update_by_id_params.ChatUpdateByIDParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )


class AsyncChatsResource(AsyncAPIResource):
    @cached_property
    def folder(self) -> AsyncFolderResource:
        return AsyncFolderResource(self._client)

    @cached_property
    def pinned(self) -> AsyncPinnedResource:
        return AsyncPinnedResource(self._client)

    @cached_property
    def all(self) -> AsyncAllResource:
        return AsyncAllResource(self._client)

    @cached_property
    def share(self) -> AsyncShareResource:
        return AsyncShareResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def clone(self) -> AsyncCloneResource:
        return AsyncCloneResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncChatsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        chat: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Create New Chat

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/chats/new",
            body=await async_maybe_transform({"chat": chat}, chat_create_params.ChatCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )

    async def list(
        self,
        user_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        skip: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatListResponse:
        """
        Get User Chat List By User Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/api/v1/chats/list/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    chat_list_params.ChatListParams,
                ),
            ),
            cast_to=ChatListResponse,
        )

    async def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Archive Chat By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/chats/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )

    async def delete_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatDeleteAllResponse:
        """Delete All User Chats"""
        return await self._delete(
            "/api/v1/chats/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatDeleteAllResponse,
        )

    async def delete_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatDeleteByIDResponse:
        """
        Delete Chat By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v1/chats/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatDeleteByIDResponse,
        )

    async def get(
        self,
        *,
        page: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatGetResponse:
        """
        Get Session User Chat List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/chats/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, chat_get_params.ChatGetParams),
            ),
            cast_to=ChatGetResponse,
        )

    async def get_archived_list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        skip: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatGetArchivedListResponse:
        """
        Get Archived Session User Chat List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/chats/archived",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    chat_get_archived_list_params.ChatGetArchivedListParams,
                ),
            ),
            cast_to=ChatGetArchivedListResponse,
        )

    async def get_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Get Chat By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/chats/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )

    async def import_(
        self,
        *,
        chat: object,
        folder_id: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        pinned: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Import Chat

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/chats/import",
            body=await async_maybe_transform(
                {
                    "chat": chat,
                    "folder_id": folder_id,
                    "meta": meta,
                    "pinned": pinned,
                },
                chat_import_params.ChatImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )

    async def pin_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Pin Chat By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/chats/{id}/pin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )

    async def search(
        self,
        *,
        text: str,
        page: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatSearchResponse:
        """
        Search User Chats

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/chats/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "text": text,
                        "page": page,
                    },
                    chat_search_params.ChatSearchParams,
                ),
            ),
            cast_to=ChatSearchResponse,
        )

    async def update_by_id(
        self,
        id: str,
        *,
        chat: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChatResponse]:
        """
        Update Chat By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/chats/{id}",
            body=await async_maybe_transform({"chat": chat}, chat_update_by_id_params.ChatUpdateByIDParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )


class ChatsResourceWithRawResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.create = to_raw_response_wrapper(
            chats.create,
        )
        self.list = to_raw_response_wrapper(
            chats.list,
        )
        self.archive = to_raw_response_wrapper(
            chats.archive,
        )
        self.delete_all = to_raw_response_wrapper(
            chats.delete_all,
        )
        self.delete_by_id = to_raw_response_wrapper(
            chats.delete_by_id,
        )
        self.get = to_raw_response_wrapper(
            chats.get,
        )
        self.get_archived_list = to_raw_response_wrapper(
            chats.get_archived_list,
        )
        self.get_by_id = to_raw_response_wrapper(
            chats.get_by_id,
        )
        self.import_ = to_raw_response_wrapper(
            chats.import_,
        )
        self.pin_by_id = to_raw_response_wrapper(
            chats.pin_by_id,
        )
        self.search = to_raw_response_wrapper(
            chats.search,
        )
        self.update_by_id = to_raw_response_wrapper(
            chats.update_by_id,
        )

    @cached_property
    def folder(self) -> FolderResourceWithRawResponse:
        return FolderResourceWithRawResponse(self._chats.folder)

    @cached_property
    def pinned(self) -> PinnedResourceWithRawResponse:
        return PinnedResourceWithRawResponse(self._chats.pinned)

    @cached_property
    def all(self) -> AllResourceWithRawResponse:
        return AllResourceWithRawResponse(self._chats.all)

    @cached_property
    def share(self) -> ShareResourceWithRawResponse:
        return ShareResourceWithRawResponse(self._chats.share)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._chats.tags)

    @cached_property
    def clone(self) -> CloneResourceWithRawResponse:
        return CloneResourceWithRawResponse(self._chats.clone)


class AsyncChatsResourceWithRawResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.create = async_to_raw_response_wrapper(
            chats.create,
        )
        self.list = async_to_raw_response_wrapper(
            chats.list,
        )
        self.archive = async_to_raw_response_wrapper(
            chats.archive,
        )
        self.delete_all = async_to_raw_response_wrapper(
            chats.delete_all,
        )
        self.delete_by_id = async_to_raw_response_wrapper(
            chats.delete_by_id,
        )
        self.get = async_to_raw_response_wrapper(
            chats.get,
        )
        self.get_archived_list = async_to_raw_response_wrapper(
            chats.get_archived_list,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            chats.get_by_id,
        )
        self.import_ = async_to_raw_response_wrapper(
            chats.import_,
        )
        self.pin_by_id = async_to_raw_response_wrapper(
            chats.pin_by_id,
        )
        self.search = async_to_raw_response_wrapper(
            chats.search,
        )
        self.update_by_id = async_to_raw_response_wrapper(
            chats.update_by_id,
        )

    @cached_property
    def folder(self) -> AsyncFolderResourceWithRawResponse:
        return AsyncFolderResourceWithRawResponse(self._chats.folder)

    @cached_property
    def pinned(self) -> AsyncPinnedResourceWithRawResponse:
        return AsyncPinnedResourceWithRawResponse(self._chats.pinned)

    @cached_property
    def all(self) -> AsyncAllResourceWithRawResponse:
        return AsyncAllResourceWithRawResponse(self._chats.all)

    @cached_property
    def share(self) -> AsyncShareResourceWithRawResponse:
        return AsyncShareResourceWithRawResponse(self._chats.share)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._chats.tags)

    @cached_property
    def clone(self) -> AsyncCloneResourceWithRawResponse:
        return AsyncCloneResourceWithRawResponse(self._chats.clone)


class ChatsResourceWithStreamingResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.create = to_streamed_response_wrapper(
            chats.create,
        )
        self.list = to_streamed_response_wrapper(
            chats.list,
        )
        self.archive = to_streamed_response_wrapper(
            chats.archive,
        )
        self.delete_all = to_streamed_response_wrapper(
            chats.delete_all,
        )
        self.delete_by_id = to_streamed_response_wrapper(
            chats.delete_by_id,
        )
        self.get = to_streamed_response_wrapper(
            chats.get,
        )
        self.get_archived_list = to_streamed_response_wrapper(
            chats.get_archived_list,
        )
        self.get_by_id = to_streamed_response_wrapper(
            chats.get_by_id,
        )
        self.import_ = to_streamed_response_wrapper(
            chats.import_,
        )
        self.pin_by_id = to_streamed_response_wrapper(
            chats.pin_by_id,
        )
        self.search = to_streamed_response_wrapper(
            chats.search,
        )
        self.update_by_id = to_streamed_response_wrapper(
            chats.update_by_id,
        )

    @cached_property
    def folder(self) -> FolderResourceWithStreamingResponse:
        return FolderResourceWithStreamingResponse(self._chats.folder)

    @cached_property
    def pinned(self) -> PinnedResourceWithStreamingResponse:
        return PinnedResourceWithStreamingResponse(self._chats.pinned)

    @cached_property
    def all(self) -> AllResourceWithStreamingResponse:
        return AllResourceWithStreamingResponse(self._chats.all)

    @cached_property
    def share(self) -> ShareResourceWithStreamingResponse:
        return ShareResourceWithStreamingResponse(self._chats.share)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._chats.tags)

    @cached_property
    def clone(self) -> CloneResourceWithStreamingResponse:
        return CloneResourceWithStreamingResponse(self._chats.clone)


class AsyncChatsResourceWithStreamingResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.create = async_to_streamed_response_wrapper(
            chats.create,
        )
        self.list = async_to_streamed_response_wrapper(
            chats.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            chats.archive,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            chats.delete_all,
        )
        self.delete_by_id = async_to_streamed_response_wrapper(
            chats.delete_by_id,
        )
        self.get = async_to_streamed_response_wrapper(
            chats.get,
        )
        self.get_archived_list = async_to_streamed_response_wrapper(
            chats.get_archived_list,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            chats.get_by_id,
        )
        self.import_ = async_to_streamed_response_wrapper(
            chats.import_,
        )
        self.pin_by_id = async_to_streamed_response_wrapper(
            chats.pin_by_id,
        )
        self.search = async_to_streamed_response_wrapper(
            chats.search,
        )
        self.update_by_id = async_to_streamed_response_wrapper(
            chats.update_by_id,
        )

    @cached_property
    def folder(self) -> AsyncFolderResourceWithStreamingResponse:
        return AsyncFolderResourceWithStreamingResponse(self._chats.folder)

    @cached_property
    def pinned(self) -> AsyncPinnedResourceWithStreamingResponse:
        return AsyncPinnedResourceWithStreamingResponse(self._chats.pinned)

    @cached_property
    def all(self) -> AsyncAllResourceWithStreamingResponse:
        return AsyncAllResourceWithStreamingResponse(self._chats.all)

    @cached_property
    def share(self) -> AsyncShareResourceWithStreamingResponse:
        return AsyncShareResourceWithStreamingResponse(self._chats.share)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._chats.tags)

    @cached_property
    def clone(self) -> AsyncCloneResourceWithStreamingResponse:
        return AsyncCloneResourceWithStreamingResponse(self._chats.clone)
