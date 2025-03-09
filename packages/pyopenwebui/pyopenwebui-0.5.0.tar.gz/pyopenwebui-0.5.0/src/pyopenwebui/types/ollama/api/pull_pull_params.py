# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PullPullParams"]


class PullPullParams(TypedDict, total=False):
    name: Required[str]

    url_idx: int
