# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ........_models import BaseModel

__all__ = ["ServerGetResponse"]


class ServerGetResponse(BaseModel):
    app_dn: str

    app_dn_password: str

    host: str

    label: str

    search_base: str

    attribute_for_mail: Optional[str] = None

    attribute_for_username: Optional[str] = None

    certificate_path: Optional[str] = None

    ciphers: Optional[str] = None

    port: Optional[int] = None

    search_filters: Optional[str] = None

    use_tls: Optional[bool] = None
