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
from .....types.api.v1.pipelines import valve_get_params, valve_update_params, valve_get_spec_params

__all__ = ["ValvesResource", "AsyncValvesResource"]


class ValvesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValvesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ValvesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValvesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ValvesResourceWithStreamingResponse(self)

    def update(
        self,
        pipeline_id: str,
        *,
        url_idx: Optional[int],
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Pipeline Valves

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._post(
            f"/api/v1/pipelines/{pipeline_id}/valves/update",
            body=maybe_transform(body, valve_update_params.ValveUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url_idx": url_idx}, valve_update_params.ValveUpdateParams),
            ),
            cast_to=object,
        )

    def get(
        self,
        pipeline_id: str,
        *,
        url_idx: Optional[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Pipeline Valves

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._get(
            f"/api/v1/pipelines/{pipeline_id}/valves",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url_idx": url_idx}, valve_get_params.ValveGetParams),
            ),
            cast_to=object,
        )

    def get_spec(
        self,
        pipeline_id: str,
        *,
        url_idx: Optional[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Pipeline Valves Spec

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._get(
            f"/api/v1/pipelines/{pipeline_id}/valves/spec",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url_idx": url_idx}, valve_get_spec_params.ValveGetSpecParams),
            ),
            cast_to=object,
        )


class AsyncValvesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValvesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncValvesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValvesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncValvesResourceWithStreamingResponse(self)

    async def update(
        self,
        pipeline_id: str,
        *,
        url_idx: Optional[int],
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update Pipeline Valves

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._post(
            f"/api/v1/pipelines/{pipeline_id}/valves/update",
            body=await async_maybe_transform(body, valve_update_params.ValveUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url_idx": url_idx}, valve_update_params.ValveUpdateParams),
            ),
            cast_to=object,
        )

    async def get(
        self,
        pipeline_id: str,
        *,
        url_idx: Optional[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Pipeline Valves

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._get(
            f"/api/v1/pipelines/{pipeline_id}/valves",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url_idx": url_idx}, valve_get_params.ValveGetParams),
            ),
            cast_to=object,
        )

    async def get_spec(
        self,
        pipeline_id: str,
        *,
        url_idx: Optional[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Pipeline Valves Spec

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._get(
            f"/api/v1/pipelines/{pipeline_id}/valves/spec",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url_idx": url_idx}, valve_get_spec_params.ValveGetSpecParams),
            ),
            cast_to=object,
        )


class ValvesResourceWithRawResponse:
    def __init__(self, valves: ValvesResource) -> None:
        self._valves = valves

        self.update = to_raw_response_wrapper(
            valves.update,
        )
        self.get = to_raw_response_wrapper(
            valves.get,
        )
        self.get_spec = to_raw_response_wrapper(
            valves.get_spec,
        )


class AsyncValvesResourceWithRawResponse:
    def __init__(self, valves: AsyncValvesResource) -> None:
        self._valves = valves

        self.update = async_to_raw_response_wrapper(
            valves.update,
        )
        self.get = async_to_raw_response_wrapper(
            valves.get,
        )
        self.get_spec = async_to_raw_response_wrapper(
            valves.get_spec,
        )


class ValvesResourceWithStreamingResponse:
    def __init__(self, valves: ValvesResource) -> None:
        self._valves = valves

        self.update = to_streamed_response_wrapper(
            valves.update,
        )
        self.get = to_streamed_response_wrapper(
            valves.get,
        )
        self.get_spec = to_streamed_response_wrapper(
            valves.get_spec,
        )


class AsyncValvesResourceWithStreamingResponse:
    def __init__(self, valves: AsyncValvesResource) -> None:
        self._valves = valves

        self.update = async_to_streamed_response_wrapper(
            valves.update,
        )
        self.get = async_to_streamed_response_wrapper(
            valves.get,
        )
        self.get_spec = async_to_streamed_response_wrapper(
            valves.get_spec,
        )
