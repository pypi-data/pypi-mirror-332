# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["OpensearchXmlResource", "AsyncOpensearchXmlResource"]


class OpensearchXmlResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OpensearchXmlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return OpensearchXmlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpensearchXmlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return OpensearchXmlResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Opensearch Xml"""
        return self._get(
            "/opensearch.xml",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncOpensearchXmlResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOpensearchXmlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOpensearchXmlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpensearchXmlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncOpensearchXmlResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Opensearch Xml"""
        return await self._get(
            "/opensearch.xml",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class OpensearchXmlResourceWithRawResponse:
    def __init__(self, opensearch_xml: OpensearchXmlResource) -> None:
        self._opensearch_xml = opensearch_xml

        self.retrieve = to_raw_response_wrapper(
            opensearch_xml.retrieve,
        )


class AsyncOpensearchXmlResourceWithRawResponse:
    def __init__(self, opensearch_xml: AsyncOpensearchXmlResource) -> None:
        self._opensearch_xml = opensearch_xml

        self.retrieve = async_to_raw_response_wrapper(
            opensearch_xml.retrieve,
        )


class OpensearchXmlResourceWithStreamingResponse:
    def __init__(self, opensearch_xml: OpensearchXmlResource) -> None:
        self._opensearch_xml = opensearch_xml

        self.retrieve = to_streamed_response_wrapper(
            opensearch_xml.retrieve,
        )


class AsyncOpensearchXmlResourceWithStreamingResponse:
    def __init__(self, opensearch_xml: AsyncOpensearchXmlResource) -> None:
        self._opensearch_xml = opensearch_xml

        self.retrieve = async_to_streamed_response_wrapper(
            opensearch_xml.retrieve,
        )
