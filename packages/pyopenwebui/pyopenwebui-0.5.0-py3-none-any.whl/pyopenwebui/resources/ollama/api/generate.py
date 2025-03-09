# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ollama.api import generate_generate_params, generate_generate_by_index_params

__all__ = ["GenerateResource", "AsyncGenerateResource"]


class GenerateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return GenerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return GenerateResourceWithStreamingResponse(self)

    def generate(
        self,
        *,
        model: str,
        prompt: str,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        context: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        format: Optional[str] | NotGiven = NOT_GIVEN,
        images: Optional[List[str]] | NotGiven = NOT_GIVEN,
        keep_alive: Union[int, str, None] | NotGiven = NOT_GIVEN,
        options: Optional[object] | NotGiven = NOT_GIVEN,
        raw: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        suffix: Optional[str] | NotGiven = NOT_GIVEN,
        system: Optional[str] | NotGiven = NOT_GIVEN,
        template: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Generate Completion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ollama/api/generate",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "context": context,
                    "format": format,
                    "images": images,
                    "keep_alive": keep_alive,
                    "options": options,
                    "raw": raw,
                    "stream": stream,
                    "suffix": suffix,
                    "system": system,
                    "template": template,
                },
                generate_generate_params.GenerateGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url_idx": url_idx}, generate_generate_params.GenerateGenerateParams),
            ),
            cast_to=object,
        )

    def generate_by_index(
        self,
        url_idx: int,
        *,
        model: str,
        prompt: str,
        context: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        format: Optional[str] | NotGiven = NOT_GIVEN,
        images: Optional[List[str]] | NotGiven = NOT_GIVEN,
        keep_alive: Union[int, str, None] | NotGiven = NOT_GIVEN,
        options: Optional[object] | NotGiven = NOT_GIVEN,
        raw: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        suffix: Optional[str] | NotGiven = NOT_GIVEN,
        system: Optional[str] | NotGiven = NOT_GIVEN,
        template: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Generate Completion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/ollama/api/generate/{url_idx}",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "context": context,
                    "format": format,
                    "images": images,
                    "keep_alive": keep_alive,
                    "options": options,
                    "raw": raw,
                    "stream": stream,
                    "suffix": suffix,
                    "system": system,
                    "template": template,
                },
                generate_generate_by_index_params.GenerateGenerateByIndexParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncGenerateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncGenerateResourceWithStreamingResponse(self)

    async def generate(
        self,
        *,
        model: str,
        prompt: str,
        url_idx: Optional[int] | NotGiven = NOT_GIVEN,
        context: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        format: Optional[str] | NotGiven = NOT_GIVEN,
        images: Optional[List[str]] | NotGiven = NOT_GIVEN,
        keep_alive: Union[int, str, None] | NotGiven = NOT_GIVEN,
        options: Optional[object] | NotGiven = NOT_GIVEN,
        raw: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        suffix: Optional[str] | NotGiven = NOT_GIVEN,
        system: Optional[str] | NotGiven = NOT_GIVEN,
        template: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Generate Completion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ollama/api/generate",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "context": context,
                    "format": format,
                    "images": images,
                    "keep_alive": keep_alive,
                    "options": options,
                    "raw": raw,
                    "stream": stream,
                    "suffix": suffix,
                    "system": system,
                    "template": template,
                },
                generate_generate_params.GenerateGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"url_idx": url_idx}, generate_generate_params.GenerateGenerateParams
                ),
            ),
            cast_to=object,
        )

    async def generate_by_index(
        self,
        url_idx: int,
        *,
        model: str,
        prompt: str,
        context: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        format: Optional[str] | NotGiven = NOT_GIVEN,
        images: Optional[List[str]] | NotGiven = NOT_GIVEN,
        keep_alive: Union[int, str, None] | NotGiven = NOT_GIVEN,
        options: Optional[object] | NotGiven = NOT_GIVEN,
        raw: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        suffix: Optional[str] | NotGiven = NOT_GIVEN,
        system: Optional[str] | NotGiven = NOT_GIVEN,
        template: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Generate Completion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/ollama/api/generate/{url_idx}",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "context": context,
                    "format": format,
                    "images": images,
                    "keep_alive": keep_alive,
                    "options": options,
                    "raw": raw,
                    "stream": stream,
                    "suffix": suffix,
                    "system": system,
                    "template": template,
                },
                generate_generate_by_index_params.GenerateGenerateByIndexParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class GenerateResourceWithRawResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

        self.generate = to_raw_response_wrapper(
            generate.generate,
        )
        self.generate_by_index = to_raw_response_wrapper(
            generate.generate_by_index,
        )


class AsyncGenerateResourceWithRawResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

        self.generate = async_to_raw_response_wrapper(
            generate.generate,
        )
        self.generate_by_index = async_to_raw_response_wrapper(
            generate.generate_by_index,
        )


class GenerateResourceWithStreamingResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

        self.generate = to_streamed_response_wrapper(
            generate.generate,
        )
        self.generate_by_index = to_streamed_response_wrapper(
            generate.generate_by_index,
        )


class AsyncGenerateResourceWithStreamingResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

        self.generate = async_to_streamed_response_wrapper(
            generate.generate,
        )
        self.generate_by_index = async_to_streamed_response_wrapper(
            generate.generate_by_index,
        )
