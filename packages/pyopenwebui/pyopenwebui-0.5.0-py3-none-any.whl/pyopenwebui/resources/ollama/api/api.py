# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .chat import (
    ChatResource,
    AsyncChatResource,
    ChatResourceWithRawResponse,
    AsyncChatResourceWithRawResponse,
    ChatResourceWithStreamingResponse,
    AsyncChatResourceWithStreamingResponse,
)
from .copy import (
    CopyResource,
    AsyncCopyResource,
    CopyResourceWithRawResponse,
    AsyncCopyResourceWithRawResponse,
    CopyResourceWithStreamingResponse,
    AsyncCopyResourceWithStreamingResponse,
)
from .pull import (
    PullResource,
    AsyncPullResource,
    PullResourceWithRawResponse,
    AsyncPullResourceWithRawResponse,
    PullResourceWithStreamingResponse,
    AsyncPullResourceWithStreamingResponse,
)
from .push import (
    PushResource,
    AsyncPushResource,
    PushResourceWithRawResponse,
    AsyncPushResourceWithRawResponse,
    PushResourceWithStreamingResponse,
    AsyncPushResourceWithStreamingResponse,
)
from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from .embed import (
    EmbedResource,
    AsyncEmbedResource,
    EmbedResourceWithRawResponse,
    AsyncEmbedResourceWithRawResponse,
    EmbedResourceWithStreamingResponse,
    AsyncEmbedResourceWithStreamingResponse,
)
from .create import (
    CreateResource,
    AsyncCreateResource,
    CreateResourceWithRawResponse,
    AsyncCreateResourceWithRawResponse,
    CreateResourceWithStreamingResponse,
    AsyncCreateResourceWithStreamingResponse,
)
from .delete import (
    DeleteResource,
    AsyncDeleteResource,
    DeleteResourceWithRawResponse,
    AsyncDeleteResourceWithRawResponse,
    DeleteResourceWithStreamingResponse,
    AsyncDeleteResourceWithStreamingResponse,
)
from .version import (
    VersionResource,
    AsyncVersionResource,
    VersionResourceWithRawResponse,
    AsyncVersionResourceWithRawResponse,
    VersionResourceWithStreamingResponse,
    AsyncVersionResourceWithStreamingResponse,
)
from .generate import (
    GenerateResource,
    AsyncGenerateResource,
    GenerateResourceWithRawResponse,
    AsyncGenerateResourceWithRawResponse,
    GenerateResourceWithStreamingResponse,
    AsyncGenerateResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .embeddings import (
    EmbeddingsResource,
    AsyncEmbeddingsResource,
    EmbeddingsResourceWithRawResponse,
    AsyncEmbeddingsResourceWithRawResponse,
    EmbeddingsResourceWithStreamingResponse,
    AsyncEmbeddingsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ollama import api_show_info_params

__all__ = ["APIResource", "AsyncAPIResource"]


class APIResource(SyncAPIResource):
    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def version(self) -> VersionResource:
        return VersionResource(self._client)

    @cached_property
    def pull(self) -> PullResource:
        return PullResource(self._client)

    @cached_property
    def push(self) -> PushResource:
        return PushResource(self._client)

    @cached_property
    def create(self) -> CreateResource:
        return CreateResource(self._client)

    @cached_property
    def copy(self) -> CopyResource:
        return CopyResource(self._client)

    @cached_property
    def delete(self) -> DeleteResource:
        return DeleteResource(self._client)

    @cached_property
    def embed(self) -> EmbedResource:
        return EmbedResource(self._client)

    @cached_property
    def embeddings(self) -> EmbeddingsResource:
        return EmbeddingsResource(self._client)

    @cached_property
    def generate(self) -> GenerateResource:
        return GenerateResource(self._client)

    @cached_property
    def chat(self) -> ChatResource:
        return ChatResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return APIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return APIResourceWithStreamingResponse(self)

    def get_loaded_models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        List models that are currently loaded into Ollama memory, and which node they
        are loaded on.
        """
        return self._get(
            "/ollama/api/ps",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def show_info(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Show Model Info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ollama/api/show",
            body=maybe_transform({"name": name}, api_show_info_params.APIShowInfoParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAPIResource(AsyncAPIResource):
    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def version(self) -> AsyncVersionResource:
        return AsyncVersionResource(self._client)

    @cached_property
    def pull(self) -> AsyncPullResource:
        return AsyncPullResource(self._client)

    @cached_property
    def push(self) -> AsyncPushResource:
        return AsyncPushResource(self._client)

    @cached_property
    def create(self) -> AsyncCreateResource:
        return AsyncCreateResource(self._client)

    @cached_property
    def copy(self) -> AsyncCopyResource:
        return AsyncCopyResource(self._client)

    @cached_property
    def delete(self) -> AsyncDeleteResource:
        return AsyncDeleteResource(self._client)

    @cached_property
    def embed(self) -> AsyncEmbedResource:
        return AsyncEmbedResource(self._client)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResource:
        return AsyncEmbeddingsResource(self._client)

    @cached_property
    def generate(self) -> AsyncGenerateResource:
        return AsyncGenerateResource(self._client)

    @cached_property
    def chat(self) -> AsyncChatResource:
        return AsyncChatResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncAPIResourceWithStreamingResponse(self)

    async def get_loaded_models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        List models that are currently loaded into Ollama memory, and which node they
        are loaded on.
        """
        return await self._get(
            "/ollama/api/ps",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def show_info(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Show Model Info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ollama/api/show",
            body=await async_maybe_transform({"name": name}, api_show_info_params.APIShowInfoParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class APIResourceWithRawResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

        self.get_loaded_models = to_raw_response_wrapper(
            api.get_loaded_models,
        )
        self.show_info = to_raw_response_wrapper(
            api.show_info,
        )

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._api.tags)

    @cached_property
    def version(self) -> VersionResourceWithRawResponse:
        return VersionResourceWithRawResponse(self._api.version)

    @cached_property
    def pull(self) -> PullResourceWithRawResponse:
        return PullResourceWithRawResponse(self._api.pull)

    @cached_property
    def push(self) -> PushResourceWithRawResponse:
        return PushResourceWithRawResponse(self._api.push)

    @cached_property
    def create(self) -> CreateResourceWithRawResponse:
        return CreateResourceWithRawResponse(self._api.create)

    @cached_property
    def copy(self) -> CopyResourceWithRawResponse:
        return CopyResourceWithRawResponse(self._api.copy)

    @cached_property
    def delete(self) -> DeleteResourceWithRawResponse:
        return DeleteResourceWithRawResponse(self._api.delete)

    @cached_property
    def embed(self) -> EmbedResourceWithRawResponse:
        return EmbedResourceWithRawResponse(self._api.embed)

    @cached_property
    def embeddings(self) -> EmbeddingsResourceWithRawResponse:
        return EmbeddingsResourceWithRawResponse(self._api.embeddings)

    @cached_property
    def generate(self) -> GenerateResourceWithRawResponse:
        return GenerateResourceWithRawResponse(self._api.generate)

    @cached_property
    def chat(self) -> ChatResourceWithRawResponse:
        return ChatResourceWithRawResponse(self._api.chat)


class AsyncAPIResourceWithRawResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

        self.get_loaded_models = async_to_raw_response_wrapper(
            api.get_loaded_models,
        )
        self.show_info = async_to_raw_response_wrapper(
            api.show_info,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._api.tags)

    @cached_property
    def version(self) -> AsyncVersionResourceWithRawResponse:
        return AsyncVersionResourceWithRawResponse(self._api.version)

    @cached_property
    def pull(self) -> AsyncPullResourceWithRawResponse:
        return AsyncPullResourceWithRawResponse(self._api.pull)

    @cached_property
    def push(self) -> AsyncPushResourceWithRawResponse:
        return AsyncPushResourceWithRawResponse(self._api.push)

    @cached_property
    def create(self) -> AsyncCreateResourceWithRawResponse:
        return AsyncCreateResourceWithRawResponse(self._api.create)

    @cached_property
    def copy(self) -> AsyncCopyResourceWithRawResponse:
        return AsyncCopyResourceWithRawResponse(self._api.copy)

    @cached_property
    def delete(self) -> AsyncDeleteResourceWithRawResponse:
        return AsyncDeleteResourceWithRawResponse(self._api.delete)

    @cached_property
    def embed(self) -> AsyncEmbedResourceWithRawResponse:
        return AsyncEmbedResourceWithRawResponse(self._api.embed)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResourceWithRawResponse:
        return AsyncEmbeddingsResourceWithRawResponse(self._api.embeddings)

    @cached_property
    def generate(self) -> AsyncGenerateResourceWithRawResponse:
        return AsyncGenerateResourceWithRawResponse(self._api.generate)

    @cached_property
    def chat(self) -> AsyncChatResourceWithRawResponse:
        return AsyncChatResourceWithRawResponse(self._api.chat)


class APIResourceWithStreamingResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

        self.get_loaded_models = to_streamed_response_wrapper(
            api.get_loaded_models,
        )
        self.show_info = to_streamed_response_wrapper(
            api.show_info,
        )

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._api.tags)

    @cached_property
    def version(self) -> VersionResourceWithStreamingResponse:
        return VersionResourceWithStreamingResponse(self._api.version)

    @cached_property
    def pull(self) -> PullResourceWithStreamingResponse:
        return PullResourceWithStreamingResponse(self._api.pull)

    @cached_property
    def push(self) -> PushResourceWithStreamingResponse:
        return PushResourceWithStreamingResponse(self._api.push)

    @cached_property
    def create(self) -> CreateResourceWithStreamingResponse:
        return CreateResourceWithStreamingResponse(self._api.create)

    @cached_property
    def copy(self) -> CopyResourceWithStreamingResponse:
        return CopyResourceWithStreamingResponse(self._api.copy)

    @cached_property
    def delete(self) -> DeleteResourceWithStreamingResponse:
        return DeleteResourceWithStreamingResponse(self._api.delete)

    @cached_property
    def embed(self) -> EmbedResourceWithStreamingResponse:
        return EmbedResourceWithStreamingResponse(self._api.embed)

    @cached_property
    def embeddings(self) -> EmbeddingsResourceWithStreamingResponse:
        return EmbeddingsResourceWithStreamingResponse(self._api.embeddings)

    @cached_property
    def generate(self) -> GenerateResourceWithStreamingResponse:
        return GenerateResourceWithStreamingResponse(self._api.generate)

    @cached_property
    def chat(self) -> ChatResourceWithStreamingResponse:
        return ChatResourceWithStreamingResponse(self._api.chat)


class AsyncAPIResourceWithStreamingResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

        self.get_loaded_models = async_to_streamed_response_wrapper(
            api.get_loaded_models,
        )
        self.show_info = async_to_streamed_response_wrapper(
            api.show_info,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._api.tags)

    @cached_property
    def version(self) -> AsyncVersionResourceWithStreamingResponse:
        return AsyncVersionResourceWithStreamingResponse(self._api.version)

    @cached_property
    def pull(self) -> AsyncPullResourceWithStreamingResponse:
        return AsyncPullResourceWithStreamingResponse(self._api.pull)

    @cached_property
    def push(self) -> AsyncPushResourceWithStreamingResponse:
        return AsyncPushResourceWithStreamingResponse(self._api.push)

    @cached_property
    def create(self) -> AsyncCreateResourceWithStreamingResponse:
        return AsyncCreateResourceWithStreamingResponse(self._api.create)

    @cached_property
    def copy(self) -> AsyncCopyResourceWithStreamingResponse:
        return AsyncCopyResourceWithStreamingResponse(self._api.copy)

    @cached_property
    def delete(self) -> AsyncDeleteResourceWithStreamingResponse:
        return AsyncDeleteResourceWithStreamingResponse(self._api.delete)

    @cached_property
    def embed(self) -> AsyncEmbedResourceWithStreamingResponse:
        return AsyncEmbedResourceWithStreamingResponse(self._api.embed)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResourceWithStreamingResponse:
        return AsyncEmbeddingsResourceWithStreamingResponse(self._api.embeddings)

    @cached_property
    def generate(self) -> AsyncGenerateResourceWithStreamingResponse:
        return AsyncGenerateResourceWithStreamingResponse(self._api.generate)

    @cached_property
    def chat(self) -> AsyncChatResourceWithStreamingResponse:
        return AsyncChatResourceWithStreamingResponse(self._api.chat)
