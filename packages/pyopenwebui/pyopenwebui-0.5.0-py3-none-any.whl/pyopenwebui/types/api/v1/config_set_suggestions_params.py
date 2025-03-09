# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...configs.default.prompt_suggestion_param import PromptSuggestionParam

__all__ = ["ConfigSetSuggestionsParams"]


class ConfigSetSuggestionsParams(TypedDict, total=False):
    suggestions: Required[Iterable[PromptSuggestionParam]]
