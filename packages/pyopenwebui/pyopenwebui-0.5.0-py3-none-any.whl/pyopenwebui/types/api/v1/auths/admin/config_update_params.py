# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["ConfigUpdateParams"]


class ConfigUpdateParams(TypedDict, total=False):
    api_key_allowed_endpoints: Required[Annotated[str, PropertyInfo(alias="API_KEY_ALLOWED_ENDPOINTS")]]

    default_user_role: Required[Annotated[str, PropertyInfo(alias="DEFAULT_USER_ROLE")]]

    enable_api_key: Required[Annotated[bool, PropertyInfo(alias="ENABLE_API_KEY")]]

    enable_api_key_endpoint_restrictions: Required[
        Annotated[bool, PropertyInfo(alias="ENABLE_API_KEY_ENDPOINT_RESTRICTIONS")]
    ]

    enable_channels: Required[Annotated[bool, PropertyInfo(alias="ENABLE_CHANNELS")]]

    enable_community_sharing: Required[Annotated[bool, PropertyInfo(alias="ENABLE_COMMUNITY_SHARING")]]

    enable_message_rating: Required[Annotated[bool, PropertyInfo(alias="ENABLE_MESSAGE_RATING")]]

    enable_signup: Required[Annotated[bool, PropertyInfo(alias="ENABLE_SIGNUP")]]

    jwt_expires_in: Required[Annotated[str, PropertyInfo(alias="JWT_EXPIRES_IN")]]

    show_admin_details: Required[Annotated[bool, PropertyInfo(alias="SHOW_ADMIN_DETAILS")]]

    webui_url: Required[Annotated[str, PropertyInfo(alias="WEBUI_URL")]]
