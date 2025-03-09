# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "ConfigUpdateParams",
    "Chunk",
    "ContentExtraction",
    "ContentExtractionDocumentIntelligenceConfig",
    "File",
    "Web",
    "WebSearch",
    "Youtube",
]


class ConfigUpdateParams(TypedDict, total=False):
    bypass_embedding_and_retrieval: Annotated[Optional[bool], PropertyInfo(alias="BYPASS_EMBEDDING_AND_RETRIEVAL")]

    chunk: Optional[Chunk]

    content_extraction: Optional[ContentExtraction]

    enable_google_drive_integration: Optional[bool]

    enable_onedrive_integration: Optional[bool]

    file: Optional[File]

    pdf_extract_images: Optional[bool]

    rag_full_context: Annotated[Optional[bool], PropertyInfo(alias="RAG_FULL_CONTEXT")]

    web: Optional[Web]

    youtube: Optional[Youtube]


class Chunk(TypedDict, total=False):
    chunk_overlap: Required[int]

    chunk_size: Required[int]

    text_splitter: Optional[str]


class ContentExtractionDocumentIntelligenceConfig(TypedDict, total=False):
    endpoint: Required[str]

    key: Required[str]


class ContentExtraction(TypedDict, total=False):
    document_intelligence_config: Optional[ContentExtractionDocumentIntelligenceConfig]

    engine: str

    tika_server_url: Optional[str]


class File(TypedDict, total=False):
    max_count: Optional[int]

    max_size: Optional[int]


class WebSearch(TypedDict, total=False):
    enabled: Required[bool]

    bing_search_v7_endpoint: Optional[str]

    bing_search_v7_subscription_key: Optional[str]

    bocha_search_api_key: Optional[str]

    brave_search_api_key: Optional[str]

    concurrent_requests: Optional[int]

    domain_filter_list: Optional[List[str]]

    engine: Optional[str]

    exa_api_key: Optional[str]

    google_pse_api_key: Optional[str]

    google_pse_engine_id: Optional[str]

    jina_api_key: Optional[str]

    kagi_search_api_key: Optional[str]

    mojeek_search_api_key: Optional[str]

    perplexity_api_key: Optional[str]

    result_count: Optional[int]

    searchapi_api_key: Optional[str]

    searchapi_engine: Optional[str]

    searxng_query_url: Optional[str]

    serpapi_api_key: Optional[str]

    serpapi_engine: Optional[str]

    serper_api_key: Optional[str]

    serply_api_key: Optional[str]

    serpstack_api_key: Optional[str]

    serpstack_https: Optional[bool]

    tavily_api_key: Optional[str]

    trust_env: Optional[bool]


class Web(TypedDict, total=False):
    search: Required[WebSearch]

    bypass_web_search_embedding_and_retrieval: Annotated[
        Optional[bool], PropertyInfo(alias="BYPASS_WEB_SEARCH_EMBEDDING_AND_RETRIEVAL")
    ]

    enable_rag_web_loader_ssl_verification: Annotated[
        Optional[bool], PropertyInfo(alias="ENABLE_RAG_WEB_LOADER_SSL_VERIFICATION")
    ]


class Youtube(TypedDict, total=False):
    language: Required[List[str]]

    proxy_url: str

    translation: Optional[str]
