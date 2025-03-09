# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .models import (
    ModelsResource,
    AsyncModelsResource,
    ModelsResourceWithRawResponse,
    AsyncModelsResourceWithRawResponse,
    ModelsResourceWithStreamingResponse,
    AsyncModelsResourceWithStreamingResponse,
)
from .banners import (
    BannersResource,
    AsyncBannersResource,
    BannersResourceWithRawResponse,
    AsyncBannersResourceWithRawResponse,
    BannersResourceWithStreamingResponse,
    AsyncBannersResourceWithStreamingResponse,
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
from .code_execution import (
    CodeExecutionResource,
    AsyncCodeExecutionResource,
    CodeExecutionResourceWithRawResponse,
    AsyncCodeExecutionResourceWithRawResponse,
    CodeExecutionResourceWithStreamingResponse,
    AsyncCodeExecutionResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .....types.api.v1 import config_import_params, config_set_suggestions_params
from .direct_connections import (
    DirectConnectionsResource,
    AsyncDirectConnectionsResource,
    DirectConnectionsResourceWithRawResponse,
    AsyncDirectConnectionsResourceWithRawResponse,
    DirectConnectionsResourceWithStreamingResponse,
    AsyncDirectConnectionsResourceWithStreamingResponse,
)
from .....types.api.v1.config_set_suggestions_response import ConfigSetSuggestionsResponse
from .....types.configs.default.prompt_suggestion_param import PromptSuggestionParam

__all__ = ["ConfigsResource", "AsyncConfigsResource"]


class ConfigsResource(SyncAPIResource):
    @cached_property
    def direct_connections(self) -> DirectConnectionsResource:
        return DirectConnectionsResource(self._client)

    @cached_property
    def code_execution(self) -> CodeExecutionResource:
        return CodeExecutionResource(self._client)

    @cached_property
    def models(self) -> ModelsResource:
        return ModelsResource(self._client)

    @cached_property
    def banners(self) -> BannersResource:
        return BannersResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ConfigsResourceWithStreamingResponse(self)

    def export(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Export Config"""
        return self._get(
            "/api/v1/configs/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def import_(
        self,
        *,
        config: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Import Config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/configs/import",
            body=maybe_transform({"config": config}, config_import_params.ConfigImportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def set_suggestions(
        self,
        *,
        suggestions: Iterable[PromptSuggestionParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigSetSuggestionsResponse:
        """
        Set Default Suggestions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/configs/suggestions",
            body=maybe_transform(
                {"suggestions": suggestions}, config_set_suggestions_params.ConfigSetSuggestionsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigSetSuggestionsResponse,
        )


class AsyncConfigsResource(AsyncAPIResource):
    @cached_property
    def direct_connections(self) -> AsyncDirectConnectionsResource:
        return AsyncDirectConnectionsResource(self._client)

    @cached_property
    def code_execution(self) -> AsyncCodeExecutionResource:
        return AsyncCodeExecutionResource(self._client)

    @cached_property
    def models(self) -> AsyncModelsResource:
        return AsyncModelsResource(self._client)

    @cached_property
    def banners(self) -> AsyncBannersResource:
        return AsyncBannersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncConfigsResourceWithStreamingResponse(self)

    async def export(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Export Config"""
        return await self._get(
            "/api/v1/configs/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def import_(
        self,
        *,
        config: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Import Config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/configs/import",
            body=await async_maybe_transform({"config": config}, config_import_params.ConfigImportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def set_suggestions(
        self,
        *,
        suggestions: Iterable[PromptSuggestionParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigSetSuggestionsResponse:
        """
        Set Default Suggestions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/configs/suggestions",
            body=await async_maybe_transform(
                {"suggestions": suggestions}, config_set_suggestions_params.ConfigSetSuggestionsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigSetSuggestionsResponse,
        )


class ConfigsResourceWithRawResponse:
    def __init__(self, configs: ConfigsResource) -> None:
        self._configs = configs

        self.export = to_raw_response_wrapper(
            configs.export,
        )
        self.import_ = to_raw_response_wrapper(
            configs.import_,
        )
        self.set_suggestions = to_raw_response_wrapper(
            configs.set_suggestions,
        )

    @cached_property
    def direct_connections(self) -> DirectConnectionsResourceWithRawResponse:
        return DirectConnectionsResourceWithRawResponse(self._configs.direct_connections)

    @cached_property
    def code_execution(self) -> CodeExecutionResourceWithRawResponse:
        return CodeExecutionResourceWithRawResponse(self._configs.code_execution)

    @cached_property
    def models(self) -> ModelsResourceWithRawResponse:
        return ModelsResourceWithRawResponse(self._configs.models)

    @cached_property
    def banners(self) -> BannersResourceWithRawResponse:
        return BannersResourceWithRawResponse(self._configs.banners)


class AsyncConfigsResourceWithRawResponse:
    def __init__(self, configs: AsyncConfigsResource) -> None:
        self._configs = configs

        self.export = async_to_raw_response_wrapper(
            configs.export,
        )
        self.import_ = async_to_raw_response_wrapper(
            configs.import_,
        )
        self.set_suggestions = async_to_raw_response_wrapper(
            configs.set_suggestions,
        )

    @cached_property
    def direct_connections(self) -> AsyncDirectConnectionsResourceWithRawResponse:
        return AsyncDirectConnectionsResourceWithRawResponse(self._configs.direct_connections)

    @cached_property
    def code_execution(self) -> AsyncCodeExecutionResourceWithRawResponse:
        return AsyncCodeExecutionResourceWithRawResponse(self._configs.code_execution)

    @cached_property
    def models(self) -> AsyncModelsResourceWithRawResponse:
        return AsyncModelsResourceWithRawResponse(self._configs.models)

    @cached_property
    def banners(self) -> AsyncBannersResourceWithRawResponse:
        return AsyncBannersResourceWithRawResponse(self._configs.banners)


class ConfigsResourceWithStreamingResponse:
    def __init__(self, configs: ConfigsResource) -> None:
        self._configs = configs

        self.export = to_streamed_response_wrapper(
            configs.export,
        )
        self.import_ = to_streamed_response_wrapper(
            configs.import_,
        )
        self.set_suggestions = to_streamed_response_wrapper(
            configs.set_suggestions,
        )

    @cached_property
    def direct_connections(self) -> DirectConnectionsResourceWithStreamingResponse:
        return DirectConnectionsResourceWithStreamingResponse(self._configs.direct_connections)

    @cached_property
    def code_execution(self) -> CodeExecutionResourceWithStreamingResponse:
        return CodeExecutionResourceWithStreamingResponse(self._configs.code_execution)

    @cached_property
    def models(self) -> ModelsResourceWithStreamingResponse:
        return ModelsResourceWithStreamingResponse(self._configs.models)

    @cached_property
    def banners(self) -> BannersResourceWithStreamingResponse:
        return BannersResourceWithStreamingResponse(self._configs.banners)


class AsyncConfigsResourceWithStreamingResponse:
    def __init__(self, configs: AsyncConfigsResource) -> None:
        self._configs = configs

        self.export = async_to_streamed_response_wrapper(
            configs.export,
        )
        self.import_ = async_to_streamed_response_wrapper(
            configs.import_,
        )
        self.set_suggestions = async_to_streamed_response_wrapper(
            configs.set_suggestions,
        )

    @cached_property
    def direct_connections(self) -> AsyncDirectConnectionsResourceWithStreamingResponse:
        return AsyncDirectConnectionsResourceWithStreamingResponse(self._configs.direct_connections)

    @cached_property
    def code_execution(self) -> AsyncCodeExecutionResourceWithStreamingResponse:
        return AsyncCodeExecutionResourceWithStreamingResponse(self._configs.code_execution)

    @cached_property
    def models(self) -> AsyncModelsResourceWithStreamingResponse:
        return AsyncModelsResourceWithStreamingResponse(self._configs.models)

    @cached_property
    def banners(self) -> AsyncBannersResourceWithStreamingResponse:
        return AsyncBannersResourceWithStreamingResponse(self._configs.banners)
