# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .db import (
    DBResource,
    AsyncDBResource,
    DBResourceWithRawResponse,
    AsyncDBResourceWithRawResponse,
    DBResourceWithStreamingResponse,
    AsyncDBResourceWithStreamingResponse,
)
from .code import (
    CodeResource,
    AsyncCodeResource,
    CodeResourceWithRawResponse,
    AsyncCodeResourceWithRawResponse,
    CodeResourceWithStreamingResponse,
    AsyncCodeResourceWithStreamingResponse,
)
from .litellm import (
    LitellmResource,
    AsyncLitellmResource,
    LitellmResourceWithRawResponse,
    AsyncLitellmResourceWithRawResponse,
    LitellmResourceWithStreamingResponse,
    AsyncLitellmResourceWithStreamingResponse,
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
from .....types.api.v1 import util_markdown_params, util_get_gravatar_params, util_download_chat_as_pdf_params

__all__ = ["UtilsResource", "AsyncUtilsResource"]


class UtilsResource(SyncAPIResource):
    @cached_property
    def code(self) -> CodeResource:
        return CodeResource(self._client)

    @cached_property
    def db(self) -> DBResource:
        return DBResource(self._client)

    @cached_property
    def litellm(self) -> LitellmResource:
        return LitellmResource(self._client)

    @cached_property
    def with_raw_response(self) -> UtilsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return UtilsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UtilsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return UtilsResourceWithStreamingResponse(self)

    def download_chat_as_pdf(
        self,
        *,
        messages: Iterable[object],
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Download Chat As Pdf

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/utils/pdf",
            body=maybe_transform(
                {
                    "messages": messages,
                    "title": title,
                },
                util_download_chat_as_pdf_params.UtilDownloadChatAsPdfParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_gravatar(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Gravatar

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/utils/gravatar",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"email": email}, util_get_gravatar_params.UtilGetGravatarParams),
            ),
            cast_to=object,
        )

    def markdown(
        self,
        *,
        md: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Html From Markdown

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/utils/markdown",
            body=maybe_transform({"md": md}, util_markdown_params.UtilMarkdownParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncUtilsResource(AsyncAPIResource):
    @cached_property
    def code(self) -> AsyncCodeResource:
        return AsyncCodeResource(self._client)

    @cached_property
    def db(self) -> AsyncDBResource:
        return AsyncDBResource(self._client)

    @cached_property
    def litellm(self) -> AsyncLitellmResource:
        return AsyncLitellmResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUtilsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUtilsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUtilsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncUtilsResourceWithStreamingResponse(self)

    async def download_chat_as_pdf(
        self,
        *,
        messages: Iterable[object],
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Download Chat As Pdf

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/utils/pdf",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "title": title,
                },
                util_download_chat_as_pdf_params.UtilDownloadChatAsPdfParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_gravatar(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Gravatar

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/utils/gravatar",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"email": email}, util_get_gravatar_params.UtilGetGravatarParams),
            ),
            cast_to=object,
        )

    async def markdown(
        self,
        *,
        md: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Html From Markdown

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/utils/markdown",
            body=await async_maybe_transform({"md": md}, util_markdown_params.UtilMarkdownParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class UtilsResourceWithRawResponse:
    def __init__(self, utils: UtilsResource) -> None:
        self._utils = utils

        self.download_chat_as_pdf = to_raw_response_wrapper(
            utils.download_chat_as_pdf,
        )
        self.get_gravatar = to_raw_response_wrapper(
            utils.get_gravatar,
        )
        self.markdown = to_raw_response_wrapper(
            utils.markdown,
        )

    @cached_property
    def code(self) -> CodeResourceWithRawResponse:
        return CodeResourceWithRawResponse(self._utils.code)

    @cached_property
    def db(self) -> DBResourceWithRawResponse:
        return DBResourceWithRawResponse(self._utils.db)

    @cached_property
    def litellm(self) -> LitellmResourceWithRawResponse:
        return LitellmResourceWithRawResponse(self._utils.litellm)


class AsyncUtilsResourceWithRawResponse:
    def __init__(self, utils: AsyncUtilsResource) -> None:
        self._utils = utils

        self.download_chat_as_pdf = async_to_raw_response_wrapper(
            utils.download_chat_as_pdf,
        )
        self.get_gravatar = async_to_raw_response_wrapper(
            utils.get_gravatar,
        )
        self.markdown = async_to_raw_response_wrapper(
            utils.markdown,
        )

    @cached_property
    def code(self) -> AsyncCodeResourceWithRawResponse:
        return AsyncCodeResourceWithRawResponse(self._utils.code)

    @cached_property
    def db(self) -> AsyncDBResourceWithRawResponse:
        return AsyncDBResourceWithRawResponse(self._utils.db)

    @cached_property
    def litellm(self) -> AsyncLitellmResourceWithRawResponse:
        return AsyncLitellmResourceWithRawResponse(self._utils.litellm)


class UtilsResourceWithStreamingResponse:
    def __init__(self, utils: UtilsResource) -> None:
        self._utils = utils

        self.download_chat_as_pdf = to_streamed_response_wrapper(
            utils.download_chat_as_pdf,
        )
        self.get_gravatar = to_streamed_response_wrapper(
            utils.get_gravatar,
        )
        self.markdown = to_streamed_response_wrapper(
            utils.markdown,
        )

    @cached_property
    def code(self) -> CodeResourceWithStreamingResponse:
        return CodeResourceWithStreamingResponse(self._utils.code)

    @cached_property
    def db(self) -> DBResourceWithStreamingResponse:
        return DBResourceWithStreamingResponse(self._utils.db)

    @cached_property
    def litellm(self) -> LitellmResourceWithStreamingResponse:
        return LitellmResourceWithStreamingResponse(self._utils.litellm)


class AsyncUtilsResourceWithStreamingResponse:
    def __init__(self, utils: AsyncUtilsResource) -> None:
        self._utils = utils

        self.download_chat_as_pdf = async_to_streamed_response_wrapper(
            utils.download_chat_as_pdf,
        )
        self.get_gravatar = async_to_streamed_response_wrapper(
            utils.get_gravatar,
        )
        self.markdown = async_to_streamed_response_wrapper(
            utils.markdown,
        )

    @cached_property
    def code(self) -> AsyncCodeResourceWithStreamingResponse:
        return AsyncCodeResourceWithStreamingResponse(self._utils.code)

    @cached_property
    def db(self) -> AsyncDBResourceWithStreamingResponse:
        return AsyncDBResourceWithStreamingResponse(self._utils.db)

    @cached_property
    def litellm(self) -> AsyncLitellmResourceWithStreamingResponse:
        return AsyncLitellmResourceWithStreamingResponse(self._utils.litellm)
