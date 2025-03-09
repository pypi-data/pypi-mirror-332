# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ....configs.banner_model_param import BannerModelParam

__all__ = ["BannerSetParams"]


class BannerSetParams(TypedDict, total=False):
    banners: Required[Iterable[BannerModelParam]]
