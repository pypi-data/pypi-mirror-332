# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ServerUpdateParams"]


class ServerUpdateParams(TypedDict, total=False):
    app_dn: Required[str]

    app_dn_password: Required[str]

    host: Required[str]

    label: Required[str]

    search_base: Required[str]

    attribute_for_mail: str

    attribute_for_username: str

    certificate_path: Optional[str]

    ciphers: Optional[str]

    port: Optional[int]

    search_filters: str

    use_tls: bool
