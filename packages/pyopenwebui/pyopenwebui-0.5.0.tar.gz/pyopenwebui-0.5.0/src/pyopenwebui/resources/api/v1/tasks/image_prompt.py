# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from .....types.api.v1.tasks import image_prompt_generate_params

__all__ = ["ImagePromptResource", "AsyncImagePromptResource"]


class ImagePromptResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImagePromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ImagePromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagePromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ImagePromptResourceWithStreamingResponse(self)

    def generate(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Generate Image Prompt

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/tasks/image_prompt/completions",
            body=maybe_transform(body, image_prompt_generate_params.ImagePromptGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncImagePromptResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImagePromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImagePromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImagePromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncImagePromptResourceWithStreamingResponse(self)

    async def generate(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Generate Image Prompt

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/tasks/image_prompt/completions",
            body=await async_maybe_transform(body, image_prompt_generate_params.ImagePromptGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ImagePromptResourceWithRawResponse:
    def __init__(self, image_prompt: ImagePromptResource) -> None:
        self._image_prompt = image_prompt

        self.generate = to_raw_response_wrapper(
            image_prompt.generate,
        )


class AsyncImagePromptResourceWithRawResponse:
    def __init__(self, image_prompt: AsyncImagePromptResource) -> None:
        self._image_prompt = image_prompt

        self.generate = async_to_raw_response_wrapper(
            image_prompt.generate,
        )


class ImagePromptResourceWithStreamingResponse:
    def __init__(self, image_prompt: ImagePromptResource) -> None:
        self._image_prompt = image_prompt

        self.generate = to_streamed_response_wrapper(
            image_prompt.generate,
        )


class AsyncImagePromptResourceWithStreamingResponse:
    def __init__(self, image_prompt: AsyncImagePromptResource) -> None:
        self._image_prompt = image_prompt

        self.generate = async_to_streamed_response_wrapper(
            image_prompt.generate,
        )
