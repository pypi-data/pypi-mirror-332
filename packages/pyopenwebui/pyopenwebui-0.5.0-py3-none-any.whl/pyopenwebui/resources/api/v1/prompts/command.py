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
from .....types.api.v1.prompts import command_update_by_command_params
from .....types.shared.prompt_model import PromptModel
from .....types.api.v1.prompts.command_delete_by_command_response import CommandDeleteByCommandResponse

__all__ = ["CommandResource", "AsyncCommandResource"]


class CommandResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return CommandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return CommandResourceWithStreamingResponse(self)

    def delete_by_command(
        self,
        command: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommandDeleteByCommandResponse:
        """
        Delete Prompt By Command

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not command:
            raise ValueError(f"Expected a non-empty value for `command` but received {command!r}")
        return self._delete(
            f"/api/v1/prompts/command/{command}/delete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommandDeleteByCommandResponse,
        )

    def get_by_command(
        self,
        command: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PromptModel]:
        """
        Get Prompt By Command

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not command:
            raise ValueError(f"Expected a non-empty value for `command` but received {command!r}")
        return self._get(
            f"/api/v1/prompts/command/{command}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptModel,
        )

    def update_by_command(
        self,
        command_1: str,
        *,
        command_2: str,
        content: str,
        title: str,
        access_control: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PromptModel]:
        """
        Update Prompt By Command

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not command_1:
            raise ValueError(f"Expected a non-empty value for `command_1` but received {command_1!r}")
        return self._post(
            f"/api/v1/prompts/command/{command_1}/update",
            body=maybe_transform(
                {
                    "command_2": command_2,
                    "content": content,
                    "title": title,
                    "access_control": access_control,
                },
                command_update_by_command_params.CommandUpdateByCommandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptModel,
        )


class AsyncCommandResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncCommandResourceWithStreamingResponse(self)

    async def delete_by_command(
        self,
        command: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommandDeleteByCommandResponse:
        """
        Delete Prompt By Command

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not command:
            raise ValueError(f"Expected a non-empty value for `command` but received {command!r}")
        return await self._delete(
            f"/api/v1/prompts/command/{command}/delete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommandDeleteByCommandResponse,
        )

    async def get_by_command(
        self,
        command: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PromptModel]:
        """
        Get Prompt By Command

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not command:
            raise ValueError(f"Expected a non-empty value for `command` but received {command!r}")
        return await self._get(
            f"/api/v1/prompts/command/{command}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptModel,
        )

    async def update_by_command(
        self,
        command_1: str,
        *,
        command_2: str,
        content: str,
        title: str,
        access_control: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PromptModel]:
        """
        Update Prompt By Command

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not command_1:
            raise ValueError(f"Expected a non-empty value for `command_1` but received {command_1!r}")
        return await self._post(
            f"/api/v1/prompts/command/{command_1}/update",
            body=await async_maybe_transform(
                {
                    "command_2": command_2,
                    "content": content,
                    "title": title,
                    "access_control": access_control,
                },
                command_update_by_command_params.CommandUpdateByCommandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptModel,
        )


class CommandResourceWithRawResponse:
    def __init__(self, command: CommandResource) -> None:
        self._command = command

        self.delete_by_command = to_raw_response_wrapper(
            command.delete_by_command,
        )
        self.get_by_command = to_raw_response_wrapper(
            command.get_by_command,
        )
        self.update_by_command = to_raw_response_wrapper(
            command.update_by_command,
        )


class AsyncCommandResourceWithRawResponse:
    def __init__(self, command: AsyncCommandResource) -> None:
        self._command = command

        self.delete_by_command = async_to_raw_response_wrapper(
            command.delete_by_command,
        )
        self.get_by_command = async_to_raw_response_wrapper(
            command.get_by_command,
        )
        self.update_by_command = async_to_raw_response_wrapper(
            command.update_by_command,
        )


class CommandResourceWithStreamingResponse:
    def __init__(self, command: CommandResource) -> None:
        self._command = command

        self.delete_by_command = to_streamed_response_wrapper(
            command.delete_by_command,
        )
        self.get_by_command = to_streamed_response_wrapper(
            command.get_by_command,
        )
        self.update_by_command = to_streamed_response_wrapper(
            command.update_by_command,
        )


class AsyncCommandResourceWithStreamingResponse:
    def __init__(self, command: AsyncCommandResource) -> None:
        self._command = command

        self.delete_by_command = async_to_streamed_response_wrapper(
            command.delete_by_command,
        )
        self.get_by_command = async_to_streamed_response_wrapper(
            command.get_by_command,
        )
        self.update_by_command = async_to_streamed_response_wrapper(
            command.update_by_command,
        )
