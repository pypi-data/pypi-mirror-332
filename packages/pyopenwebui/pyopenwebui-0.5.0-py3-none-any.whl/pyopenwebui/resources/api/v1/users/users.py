# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .update import (
    UpdateResource,
    AsyncUpdateResource,
    UpdateResourceWithRawResponse,
    AsyncUpdateResourceWithRawResponse,
    UpdateResourceWithStreamingResponse,
    AsyncUpdateResourceWithStreamingResponse,
)
from .user.user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
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
from .default.default import (
    DefaultResource,
    AsyncDefaultResource,
    DefaultResourceWithRawResponse,
    AsyncDefaultResourceWithRawResponse,
    DefaultResourceWithStreamingResponse,
    AsyncDefaultResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .....types.api.v1 import user_get_params
from .....types.api.v1.user_get_response import UserGetResponse
from .....types.api.v1.user_get_by_id_response import UserGetByIDResponse
from .....types.api.v1.user_delete_by_id_response import UserDeleteByIDResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def default(self) -> DefaultResource:
        return DefaultResource(self._client)

    @cached_property
    def update(self) -> UpdateResource:
        return UpdateResource(self._client)

    @cached_property
    def user(self) -> UserResource:
        return UserResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def delete_by_id(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserDeleteByIDResponse:
        """
        Delete User By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._delete(
            f"/api/v1/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDeleteByIDResponse,
        )

    def get(
        self,
        *,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        skip: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserGetResponse:
        """
        Get Users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/users/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    user_get_params.UserGetParams,
                ),
            ),
            cast_to=UserGetResponse,
        )

    def get_by_id(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserGetByIDResponse:
        """
        Get User By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/api/v1/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGetByIDResponse,
        )

    def get_groups(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get User Groups"""
        return self._get(
            "/api/v1/users/groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_permissions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get User Permissisions"""
        return self._get(
            "/api/v1/users/permissions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def default(self) -> AsyncDefaultResource:
        return AsyncDefaultResource(self._client)

    @cached_property
    def update(self) -> AsyncUpdateResource:
        return AsyncUpdateResource(self._client)

    @cached_property
    def user(self) -> AsyncUserResource:
        return AsyncUserResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def delete_by_id(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserDeleteByIDResponse:
        """
        Delete User By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._delete(
            f"/api/v1/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDeleteByIDResponse,
        )

    async def get(
        self,
        *,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        skip: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserGetResponse:
        """
        Get Users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/users/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    user_get_params.UserGetParams,
                ),
            ),
            cast_to=UserGetResponse,
        )

    async def get_by_id(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserGetByIDResponse:
        """
        Get User By Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/api/v1/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGetByIDResponse,
        )

    async def get_groups(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get User Groups"""
        return await self._get(
            "/api/v1/users/groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_permissions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get User Permissisions"""
        return await self._get(
            "/api/v1/users/permissions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.delete_by_id = to_raw_response_wrapper(
            users.delete_by_id,
        )
        self.get = to_raw_response_wrapper(
            users.get,
        )
        self.get_by_id = to_raw_response_wrapper(
            users.get_by_id,
        )
        self.get_groups = to_raw_response_wrapper(
            users.get_groups,
        )
        self.get_permissions = to_raw_response_wrapper(
            users.get_permissions,
        )

    @cached_property
    def default(self) -> DefaultResourceWithRawResponse:
        return DefaultResourceWithRawResponse(self._users.default)

    @cached_property
    def update(self) -> UpdateResourceWithRawResponse:
        return UpdateResourceWithRawResponse(self._users.update)

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self._users.user)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.delete_by_id = async_to_raw_response_wrapper(
            users.delete_by_id,
        )
        self.get = async_to_raw_response_wrapper(
            users.get,
        )
        self.get_by_id = async_to_raw_response_wrapper(
            users.get_by_id,
        )
        self.get_groups = async_to_raw_response_wrapper(
            users.get_groups,
        )
        self.get_permissions = async_to_raw_response_wrapper(
            users.get_permissions,
        )

    @cached_property
    def default(self) -> AsyncDefaultResourceWithRawResponse:
        return AsyncDefaultResourceWithRawResponse(self._users.default)

    @cached_property
    def update(self) -> AsyncUpdateResourceWithRawResponse:
        return AsyncUpdateResourceWithRawResponse(self._users.update)

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self._users.user)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.delete_by_id = to_streamed_response_wrapper(
            users.delete_by_id,
        )
        self.get = to_streamed_response_wrapper(
            users.get,
        )
        self.get_by_id = to_streamed_response_wrapper(
            users.get_by_id,
        )
        self.get_groups = to_streamed_response_wrapper(
            users.get_groups,
        )
        self.get_permissions = to_streamed_response_wrapper(
            users.get_permissions,
        )

    @cached_property
    def default(self) -> DefaultResourceWithStreamingResponse:
        return DefaultResourceWithStreamingResponse(self._users.default)

    @cached_property
    def update(self) -> UpdateResourceWithStreamingResponse:
        return UpdateResourceWithStreamingResponse(self._users.update)

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self._users.user)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.delete_by_id = async_to_streamed_response_wrapper(
            users.delete_by_id,
        )
        self.get = async_to_streamed_response_wrapper(
            users.get,
        )
        self.get_by_id = async_to_streamed_response_wrapper(
            users.get_by_id,
        )
        self.get_groups = async_to_streamed_response_wrapper(
            users.get_groups,
        )
        self.get_permissions = async_to_streamed_response_wrapper(
            users.get_permissions,
        )

    @cached_property
    def default(self) -> AsyncDefaultResourceWithStreamingResponse:
        return AsyncDefaultResourceWithStreamingResponse(self._users.default)

    @cached_property
    def update(self) -> AsyncUpdateResourceWithStreamingResponse:
        return AsyncUpdateResourceWithStreamingResponse(self._users.update)

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self._users.user)
