# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .permissions import (
    PermissionsResource,
    AsyncPermissionsResource,
    PermissionsResourceWithRawResponse,
    AsyncPermissionsResourceWithRawResponse,
    PermissionsResourceWithStreamingResponse,
    AsyncPermissionsResourceWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DefaultResource", "AsyncDefaultResource"]


class DefaultResource(SyncAPIResource):
    @cached_property
    def permissions(self) -> PermissionsResource:
        return PermissionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DefaultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return DefaultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefaultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return DefaultResourceWithStreamingResponse(self)


class AsyncDefaultResource(AsyncAPIResource):
    @cached_property
    def permissions(self) -> AsyncPermissionsResource:
        return AsyncPermissionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDefaultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefaultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefaultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncDefaultResourceWithStreamingResponse(self)


class DefaultResourceWithRawResponse:
    def __init__(self, default: DefaultResource) -> None:
        self._default = default

    @cached_property
    def permissions(self) -> PermissionsResourceWithRawResponse:
        return PermissionsResourceWithRawResponse(self._default.permissions)


class AsyncDefaultResourceWithRawResponse:
    def __init__(self, default: AsyncDefaultResource) -> None:
        self._default = default

    @cached_property
    def permissions(self) -> AsyncPermissionsResourceWithRawResponse:
        return AsyncPermissionsResourceWithRawResponse(self._default.permissions)


class DefaultResourceWithStreamingResponse:
    def __init__(self, default: DefaultResource) -> None:
        self._default = default

    @cached_property
    def permissions(self) -> PermissionsResourceWithStreamingResponse:
        return PermissionsResourceWithStreamingResponse(self._default.permissions)


class AsyncDefaultResourceWithStreamingResponse:
    def __init__(self, default: AsyncDefaultResource) -> None:
        self._default = default

    @cached_property
    def permissions(self) -> AsyncPermissionsResourceWithStreamingResponse:
        return AsyncPermissionsResourceWithStreamingResponse(self._default.permissions)
