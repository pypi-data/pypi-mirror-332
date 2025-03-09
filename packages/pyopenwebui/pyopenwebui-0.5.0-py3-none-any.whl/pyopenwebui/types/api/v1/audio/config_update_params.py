# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ConfigUpdateParams", "Stt", "Tts"]


class ConfigUpdateParams(TypedDict, total=False):
    stt: Required[Stt]

    tts: Required[Tts]


class Stt(TypedDict, total=False):
    deepgram_api_key: Required[Annotated[str, PropertyInfo(alias="DEEPGRAM_API_KEY")]]

    engine: Required[Annotated[str, PropertyInfo(alias="ENGINE")]]

    model: Required[Annotated[str, PropertyInfo(alias="MODEL")]]

    openai_api_base_url: Required[Annotated[str, PropertyInfo(alias="OPENAI_API_BASE_URL")]]

    openai_api_key: Required[Annotated[str, PropertyInfo(alias="OPENAI_API_KEY")]]

    whisper_model: Required[Annotated[str, PropertyInfo(alias="WHISPER_MODEL")]]


class Tts(TypedDict, total=False):
    api_key: Required[Annotated[str, PropertyInfo(alias="API_KEY")]]

    azure_speech_output_format: Required[Annotated[str, PropertyInfo(alias="AZURE_SPEECH_OUTPUT_FORMAT")]]

    azure_speech_region: Required[Annotated[str, PropertyInfo(alias="AZURE_SPEECH_REGION")]]

    engine: Required[Annotated[str, PropertyInfo(alias="ENGINE")]]

    model: Required[Annotated[str, PropertyInfo(alias="MODEL")]]

    openai_api_base_url: Required[Annotated[str, PropertyInfo(alias="OPENAI_API_BASE_URL")]]

    openai_api_key: Required[Annotated[str, PropertyInfo(alias="OPENAI_API_KEY")]]

    split_on: Required[Annotated[str, PropertyInfo(alias="SPLIT_ON")]]

    voice: Required[Annotated[str, PropertyInfo(alias="VOICE")]]
