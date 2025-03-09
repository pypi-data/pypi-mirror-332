# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["FeedbackUpdateByIDParams", "Data", "Snapshot"]


class FeedbackUpdateByIDParams(TypedDict, total=False):
    type: Required[str]

    data: Optional[Data]

    meta: Optional[object]

    snapshot: Optional[Snapshot]


class DataTyped(TypedDict, total=False):
    comment: Optional[str]

    model_id: Optional[str]

    rating: Union[int, str, None]

    reason: Optional[str]

    sibling_model_ids: Optional[List[str]]


Data: TypeAlias = Union[DataTyped, Dict[str, object]]


class SnapshotTyped(TypedDict, total=False):
    chat: Optional[object]


Snapshot: TypeAlias = Union[SnapshotTyped, Dict[str, object]]
