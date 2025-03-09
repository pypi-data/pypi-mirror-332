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
from .....types.api.v1 import channel_create_params, channel_update_by_id_params
from .messages.messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from .....types.api.v1.channel_get_response import ChannelGetResponse
from .....types.api.v1.channel_create_response import ChannelCreateResponse
from .....types.api.v1.channel_get_by_id_response import ChannelGetByIDResponse
from .....types.api.v1.channel_delete_by_id_response import ChannelDeleteByIDResponse
from .....types.api.v1.channel_update_by_id_response import ChannelUpdateByIDResponse

__all__ = ["ChannelsResource", "AsyncChannelsResource"]


class ChannelsResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ChannelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        access_control: Optional[object] | NotGiven = NOT_GIVEN,
        data: Optional[object] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChannelCreateResponse]:
        """
        Create New Channel

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/channels/create",
            body=maybe_transform(
                {
                    "name": name,
                    "access_control": access_control,
                    "data": data,
                    "description": description,
                    "meta": meta,
                },
                channel_create_params.ChannelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelCreateResponse,
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
    ) -> ChannelDeleteByIDResponse:
        """
        Delete Channel By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v1/channels/{id}/delete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelDeleteByIDResponse,
        )

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelGetResponse:
        """Get Channels"""
        return self._get(
            "/api/v1/channels/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelGetResponse,
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
    ) -> Optional[ChannelGetByIDResponse]:
        """
        Get Channel By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/channels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelGetByIDResponse,
        )

    def update_by_id(
        self,
        id: str,
        *,
        name: str,
        access_control: Optional[object] | NotGiven = NOT_GIVEN,
        data: Optional[object] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChannelUpdateByIDResponse]:
        """
        Update Channel By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/channels/{id}/update",
            body=maybe_transform(
                {
                    "name": name,
                    "access_control": access_control,
                    "data": data,
                    "description": description,
                    "meta": meta,
                },
                channel_update_by_id_params.ChannelUpdateByIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelUpdateByIDResponse,
        )


class AsyncChannelsResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncChannelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        access_control: Optional[object] | NotGiven = NOT_GIVEN,
        data: Optional[object] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChannelCreateResponse]:
        """
        Create New Channel

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/channels/create",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "access_control": access_control,
                    "data": data,
                    "description": description,
                    "meta": meta,
                },
                channel_create_params.ChannelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelCreateResponse,
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
    ) -> ChannelDeleteByIDResponse:
        """
        Delete Channel By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v1/channels/{id}/delete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelDeleteByIDResponse,
        )

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelGetResponse:
        """Get Channels"""
        return await self._get(
            "/api/v1/channels/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelGetResponse,
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
    ) -> Optional[ChannelGetByIDResponse]:
        """
        Get Channel By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/channels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelGetByIDResponse,
        )

    async def update_by_id(
        self,
        id: str,
        *,
        name: str,
        access_control: Optional[object] | NotGiven = NOT_GIVEN,
        data: Optional[object] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        meta: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ChannelUpdateByIDResponse]:
        """
        Update Channel By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/channels/{id}/update",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "access_control": access_control,
                    "data": data,
                    "description": description,
                    "meta": meta,
                },
                channel_update_by_id_params.ChannelUpdateByIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelUpdateByIDResponse,
        )


class ChannelsResourceWithRawResponse:
    def __init__(self, channels: ChannelsResource) -> None:
        self._channels = channels

        self.create = to_raw_response_wrapper(
            channels.create,
        )
        self.delete_by_id = to_raw_response_wrapper(
            channels.delete_by_id,
        )
        self.get = to_raw_response_wrapper(
            channels.get,
        )
        self.get_by_id = to_raw_response_wrapper(
            channels.get_by_id,
        )
        self.update_by_id = to_raw_response_wrapper(
            channels.update_by_id,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._channels.messages)


class AsyncChannelsResourceWithRawResponse:
    def __init__(self, channels: AsyncChannelsResource) -> None:
        self._channels = channels

        self.create = async_to_raw_response_wrapper(
            channels.create,
        )
        self.delete_by_id = async_to_raw_response_wrapper(
            channels.delete_by_id,
        )
        self.get = async_to_raw_response_wrapper(
            channels.get,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            channels.get_by_id,
        )
        self.update_by_id = async_to_raw_response_wrapper(
            channels.update_by_id,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._channels.messages)


class ChannelsResourceWithStreamingResponse:
    def __init__(self, channels: ChannelsResource) -> None:
        self._channels = channels

        self.create = to_streamed_response_wrapper(
            channels.create,
        )
        self.delete_by_id = to_streamed_response_wrapper(
            channels.delete_by_id,
        )
        self.get = to_streamed_response_wrapper(
            channels.get,
        )
        self.get_by_id = to_streamed_response_wrapper(
            channels.get_by_id,
        )
        self.update_by_id = to_streamed_response_wrapper(
            channels.update_by_id,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._channels.messages)


class AsyncChannelsResourceWithStreamingResponse:
    def __init__(self, channels: AsyncChannelsResource) -> None:
        self._channels = channels

        self.create = async_to_streamed_response_wrapper(
            channels.create,
        )
        self.delete_by_id = async_to_streamed_response_wrapper(
            channels.delete_by_id,
        )
        self.get = async_to_streamed_response_wrapper(
            channels.get,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            channels.get_by_id,
        )
        self.update_by_id = async_to_streamed_response_wrapper(
            channels.update_by_id,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._channels.messages)
