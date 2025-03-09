# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .upload import (
    UploadResource,
    AsyncUploadResource,
    UploadResourceWithRawResponse,
    AsyncUploadResourceWithRawResponse,
    UploadResourceWithStreamingResponse,
    AsyncUploadResourceWithStreamingResponse,
)
from .download import (
    DownloadResource,
    AsyncDownloadResource,
    DownloadResourceWithRawResponse,
    AsyncDownloadResourceWithRawResponse,
    DownloadResourceWithStreamingResponse,
    AsyncDownloadResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ModelsResource", "AsyncModelsResource"]


class ModelsResource(SyncAPIResource):
    @cached_property
    def download(self) -> DownloadResource:
        return DownloadResource(self._client)

    @cached_property
    def upload(self) -> UploadResource:
        return UploadResource(self._client)

    @cached_property
    def with_raw_response(self) -> ModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return ModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return ModelsResourceWithStreamingResponse(self)


class AsyncModelsResource(AsyncAPIResource):
    @cached_property
    def download(self) -> AsyncDownloadResource:
        return AsyncDownloadResource(self._client)

    @cached_property
    def upload(self) -> AsyncUploadResource:
        return AsyncUploadResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncModelsResourceWithStreamingResponse(self)


class ModelsResourceWithRawResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

    @cached_property
    def download(self) -> DownloadResourceWithRawResponse:
        return DownloadResourceWithRawResponse(self._models.download)

    @cached_property
    def upload(self) -> UploadResourceWithRawResponse:
        return UploadResourceWithRawResponse(self._models.upload)


class AsyncModelsResourceWithRawResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

    @cached_property
    def download(self) -> AsyncDownloadResourceWithRawResponse:
        return AsyncDownloadResourceWithRawResponse(self._models.download)

    @cached_property
    def upload(self) -> AsyncUploadResourceWithRawResponse:
        return AsyncUploadResourceWithRawResponse(self._models.upload)


class ModelsResourceWithStreamingResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

    @cached_property
    def download(self) -> DownloadResourceWithStreamingResponse:
        return DownloadResourceWithStreamingResponse(self._models.download)

    @cached_property
    def upload(self) -> UploadResourceWithStreamingResponse:
        return UploadResourceWithStreamingResponse(self._models.upload)


class AsyncModelsResourceWithStreamingResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

    @cached_property
    def download(self) -> AsyncDownloadResourceWithStreamingResponse:
        return AsyncDownloadResourceWithStreamingResponse(self._models.download)

    @cached_property
    def upload(self) -> AsyncUploadResourceWithStreamingResponse:
        return AsyncUploadResourceWithStreamingResponse(self._models.upload)
