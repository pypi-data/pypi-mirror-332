# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EmbeddingUpdateConfigParams", "OllamaConfig", "OpenAIConfig"]


class EmbeddingUpdateConfigParams(TypedDict, total=False):
    embedding_engine: Required[str]

    embedding_model: Required[str]

    embedding_batch_size: Optional[int]

    ollama_config: Optional[OllamaConfig]

    openai_config: Optional[OpenAIConfig]


class OllamaConfig(TypedDict, total=False):
    key: Required[str]

    url: Required[str]


class OpenAIConfig(TypedDict, total=False):
    key: Required[str]

    url: Required[str]
