# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["IDUpdateParams", "Meta"]


class IDUpdateParams(TypedDict, total=False):
    id_2: Required[Annotated[str, PropertyInfo(alias="id")]]

    content: Required[str]

    meta: Required[Meta]

    name: Required[str]

    access_control: Optional[object]


class Meta(TypedDict, total=False):
    description: Optional[str]

    manifest: Optional[object]
