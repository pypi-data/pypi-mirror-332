# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1.chats.all_get_response import AllGetResponse
from .....types.api.v1.chats.all_get_db_response import AllGetDBResponse
from .....types.api.v1.chats.all_get_tags_response import AllGetTagsResponse
from .....types.api.v1.chats.all_get_archived_response import AllGetArchivedResponse

__all__ = ["AllResource", "AsyncAllResource"]


class AllResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AllResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AllResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AllResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AllResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllGetResponse:
        """Get User Chats"""
        return self._get(
            "/api/v1/chats/all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllGetResponse,
        )

    def get_archived(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllGetArchivedResponse:
        """Get User Archived Chats"""
        return self._get(
            "/api/v1/chats/all/archived",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllGetArchivedResponse,
        )

    def get_db(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllGetDBResponse:
        """Get All User Chats In Db"""
        return self._get(
            "/api/v1/chats/all/db",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllGetDBResponse,
        )

    def get_tags(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllGetTagsResponse:
        """Get All User Tags"""
        return self._get(
            "/api/v1/chats/all/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllGetTagsResponse,
        )


class AsyncAllResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAllResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAllResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAllResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncAllResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllGetResponse:
        """Get User Chats"""
        return await self._get(
            "/api/v1/chats/all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllGetResponse,
        )

    async def get_archived(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllGetArchivedResponse:
        """Get User Archived Chats"""
        return await self._get(
            "/api/v1/chats/all/archived",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllGetArchivedResponse,
        )

    async def get_db(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllGetDBResponse:
        """Get All User Chats In Db"""
        return await self._get(
            "/api/v1/chats/all/db",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllGetDBResponse,
        )

    async def get_tags(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllGetTagsResponse:
        """Get All User Tags"""
        return await self._get(
            "/api/v1/chats/all/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllGetTagsResponse,
        )


class AllResourceWithRawResponse:
    def __init__(self, all: AllResource) -> None:
        self._all = all

        self.get = to_raw_response_wrapper(
            all.get,
        )
        self.get_archived = to_raw_response_wrapper(
            all.get_archived,
        )
        self.get_db = to_raw_response_wrapper(
            all.get_db,
        )
        self.get_tags = to_raw_response_wrapper(
            all.get_tags,
        )


class AsyncAllResourceWithRawResponse:
    def __init__(self, all: AsyncAllResource) -> None:
        self._all = all

        self.get = async_to_raw_response_wrapper(
            all.get,
        )
        self.get_archived = async_to_raw_response_wrapper(
            all.get_archived,
        )
        self.get_db = async_to_raw_response_wrapper(
            all.get_db,
        )
        self.get_tags = async_to_raw_response_wrapper(
            all.get_tags,
        )


class AllResourceWithStreamingResponse:
    def __init__(self, all: AllResource) -> None:
        self._all = all

        self.get = to_streamed_response_wrapper(
            all.get,
        )
        self.get_archived = to_streamed_response_wrapper(
            all.get_archived,
        )
        self.get_db = to_streamed_response_wrapper(
            all.get_db,
        )
        self.get_tags = to_streamed_response_wrapper(
            all.get_tags,
        )


class AsyncAllResourceWithStreamingResponse:
    def __init__(self, all: AsyncAllResource) -> None:
        self._all = all

        self.get = async_to_streamed_response_wrapper(
            all.get,
        )
        self.get_archived = async_to_streamed_response_wrapper(
            all.get_archived,
        )
        self.get_db = async_to_streamed_response_wrapper(
            all.get_db,
        )
        self.get_tags = async_to_streamed_response_wrapper(
            all.get_tags,
        )
