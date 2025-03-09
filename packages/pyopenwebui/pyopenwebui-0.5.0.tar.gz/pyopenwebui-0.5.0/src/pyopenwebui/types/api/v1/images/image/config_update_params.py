# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["ConfigUpdateParams"]


class ConfigUpdateParams(TypedDict, total=False):
    image_size: Required[Annotated[str, PropertyInfo(alias="IMAGE_SIZE")]]

    image_steps: Required[Annotated[int, PropertyInfo(alias="IMAGE_STEPS")]]

    model: Required[Annotated[str, PropertyInfo(alias="MODEL")]]
