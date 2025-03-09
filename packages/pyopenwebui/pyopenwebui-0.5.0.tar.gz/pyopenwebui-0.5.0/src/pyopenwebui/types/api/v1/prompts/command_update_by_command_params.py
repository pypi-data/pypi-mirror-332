# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CommandUpdateByCommandParams"]


class CommandUpdateByCommandParams(TypedDict, total=False):
    command_2: Required[Annotated[str, PropertyInfo(alias="command")]]

    content: Required[str]

    title: Required[str]

    access_control: Optional[object]
