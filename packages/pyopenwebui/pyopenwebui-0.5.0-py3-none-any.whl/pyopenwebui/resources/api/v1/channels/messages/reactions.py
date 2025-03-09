# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.api.v1.channels.messages import reaction_add_params, reaction_remove_params
from ......types.api.v1.channels.messages.reaction_add_response import ReactionAddResponse
from ......types.api.v1.channels.messages.reaction_remove_response import ReactionRemoveResponse

__all__ = ["ReactionsResource", "AsyncReactionsResource"]


class ReactionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ReactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ReactionsResourceWithStreamingResponse(self)

    def add(
        self,
        message_id: str,
        *,
        id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReactionAddResponse:
        """
        Add Reaction To Message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            f"/api/v1/channels/{id}/messages/{message_id}/reactions/add",
            body=maybe_transform({"name": name}, reaction_add_params.ReactionAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReactionAddResponse,
        )

    def remove(
        self,
        message_id: str,
        *,
        id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReactionRemoveResponse:
        """
        Remove Reaction By Id And User Id And Name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            f"/api/v1/channels/{id}/messages/{message_id}/reactions/remove",
            body=maybe_transform({"name": name}, reaction_remove_params.ReactionRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReactionRemoveResponse,
        )


class AsyncReactionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncReactionsResourceWithStreamingResponse(self)

    async def add(
        self,
        message_id: str,
        *,
        id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReactionAddResponse:
        """
        Add Reaction To Message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            f"/api/v1/channels/{id}/messages/{message_id}/reactions/add",
            body=await async_maybe_transform({"name": name}, reaction_add_params.ReactionAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReactionAddResponse,
        )

    async def remove(
        self,
        message_id: str,
        *,
        id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReactionRemoveResponse:
        """
        Remove Reaction By Id And User Id And Name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            f"/api/v1/channels/{id}/messages/{message_id}/reactions/remove",
            body=await async_maybe_transform({"name": name}, reaction_remove_params.ReactionRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReactionRemoveResponse,
        )


class ReactionsResourceWithRawResponse:
    def __init__(self, reactions: ReactionsResource) -> None:
        self._reactions = reactions

        self.add = to_raw_response_wrapper(
            reactions.add,
        )
        self.remove = to_raw_response_wrapper(
            reactions.remove,
        )


class AsyncReactionsResourceWithRawResponse:
    def __init__(self, reactions: AsyncReactionsResource) -> None:
        self._reactions = reactions

        self.add = async_to_raw_response_wrapper(
            reactions.add,
        )
        self.remove = async_to_raw_response_wrapper(
            reactions.remove,
        )


class ReactionsResourceWithStreamingResponse:
    def __init__(self, reactions: ReactionsResource) -> None:
        self._reactions = reactions

        self.add = to_streamed_response_wrapper(
            reactions.add,
        )
        self.remove = to_streamed_response_wrapper(
            reactions.remove,
        )


class AsyncReactionsResourceWithStreamingResponse:
    def __init__(self, reactions: AsyncReactionsResource) -> None:
        self._reactions = reactions

        self.add = async_to_streamed_response_wrapper(
            reactions.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            reactions.remove,
        )
