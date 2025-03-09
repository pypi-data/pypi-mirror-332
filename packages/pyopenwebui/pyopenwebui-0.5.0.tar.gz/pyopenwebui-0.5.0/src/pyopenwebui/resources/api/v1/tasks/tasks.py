# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .moa import (
    MoaResource,
    AsyncMoaResource,
    MoaResourceWithRawResponse,
    AsyncMoaResourceWithRawResponse,
    MoaResourceWithStreamingResponse,
    AsyncMoaResourceWithStreamingResponse,
)
from .auto import (
    AutoResource,
    AsyncAutoResource,
    AutoResourceWithRawResponse,
    AsyncAutoResourceWithRawResponse,
    AutoResourceWithStreamingResponse,
    AsyncAutoResourceWithStreamingResponse,
)
from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from .emoji import (
    EmojiResource,
    AsyncEmojiResource,
    EmojiResourceWithRawResponse,
    AsyncEmojiResourceWithRawResponse,
    EmojiResourceWithStreamingResponse,
    AsyncEmojiResourceWithStreamingResponse,
)
from .title import (
    TitleResource,
    AsyncTitleResource,
    TitleResourceWithRawResponse,
    AsyncTitleResourceWithRawResponse,
    TitleResourceWithStreamingResponse,
    AsyncTitleResourceWithStreamingResponse,
)
from .config import (
    ConfigResource,
    AsyncConfigResource,
    ConfigResourceWithRawResponse,
    AsyncConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
    AsyncConfigResourceWithStreamingResponse,
)
from .queries import (
    QueriesResource,
    AsyncQueriesResource,
    QueriesResourceWithRawResponse,
    AsyncQueriesResourceWithRawResponse,
    QueriesResourceWithStreamingResponse,
    AsyncQueriesResourceWithStreamingResponse,
)
from ....._compat import cached_property
from .image_prompt import (
    ImagePromptResource,
    AsyncImagePromptResource,
    ImagePromptResourceWithRawResponse,
    AsyncImagePromptResourceWithRawResponse,
    ImagePromptResourceWithStreamingResponse,
    AsyncImagePromptResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def title(self) -> TitleResource:
        return TitleResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def image_prompt(self) -> ImagePromptResource:
        return ImagePromptResource(self._client)

    @cached_property
    def queries(self) -> QueriesResource:
        return QueriesResource(self._client)

    @cached_property
    def auto(self) -> AutoResource:
        return AutoResource(self._client)

    @cached_property
    def emoji(self) -> EmojiResource:
        return EmojiResource(self._client)

    @cached_property
    def moa(self) -> MoaResource:
        return MoaResource(self._client)

    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def title(self) -> AsyncTitleResource:
        return AsyncTitleResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def image_prompt(self) -> AsyncImagePromptResource:
        return AsyncImagePromptResource(self._client)

    @cached_property
    def queries(self) -> AsyncQueriesResource:
        return AsyncQueriesResource(self._client)

    @cached_property
    def auto(self) -> AsyncAutoResource:
        return AsyncAutoResource(self._client)

    @cached_property
    def emoji(self) -> AsyncEmojiResource:
        return AsyncEmojiResource(self._client)

    @cached_property
    def moa(self) -> AsyncMoaResource:
        return AsyncMoaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._tasks.config)

    @cached_property
    def title(self) -> TitleResourceWithRawResponse:
        return TitleResourceWithRawResponse(self._tasks.title)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._tasks.tags)

    @cached_property
    def image_prompt(self) -> ImagePromptResourceWithRawResponse:
        return ImagePromptResourceWithRawResponse(self._tasks.image_prompt)

    @cached_property
    def queries(self) -> QueriesResourceWithRawResponse:
        return QueriesResourceWithRawResponse(self._tasks.queries)

    @cached_property
    def auto(self) -> AutoResourceWithRawResponse:
        return AutoResourceWithRawResponse(self._tasks.auto)

    @cached_property
    def emoji(self) -> EmojiResourceWithRawResponse:
        return EmojiResourceWithRawResponse(self._tasks.emoji)

    @cached_property
    def moa(self) -> MoaResourceWithRawResponse:
        return MoaResourceWithRawResponse(self._tasks.moa)


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._tasks.config)

    @cached_property
    def title(self) -> AsyncTitleResourceWithRawResponse:
        return AsyncTitleResourceWithRawResponse(self._tasks.title)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._tasks.tags)

    @cached_property
    def image_prompt(self) -> AsyncImagePromptResourceWithRawResponse:
        return AsyncImagePromptResourceWithRawResponse(self._tasks.image_prompt)

    @cached_property
    def queries(self) -> AsyncQueriesResourceWithRawResponse:
        return AsyncQueriesResourceWithRawResponse(self._tasks.queries)

    @cached_property
    def auto(self) -> AsyncAutoResourceWithRawResponse:
        return AsyncAutoResourceWithRawResponse(self._tasks.auto)

    @cached_property
    def emoji(self) -> AsyncEmojiResourceWithRawResponse:
        return AsyncEmojiResourceWithRawResponse(self._tasks.emoji)

    @cached_property
    def moa(self) -> AsyncMoaResourceWithRawResponse:
        return AsyncMoaResourceWithRawResponse(self._tasks.moa)


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._tasks.config)

    @cached_property
    def title(self) -> TitleResourceWithStreamingResponse:
        return TitleResourceWithStreamingResponse(self._tasks.title)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._tasks.tags)

    @cached_property
    def image_prompt(self) -> ImagePromptResourceWithStreamingResponse:
        return ImagePromptResourceWithStreamingResponse(self._tasks.image_prompt)

    @cached_property
    def queries(self) -> QueriesResourceWithStreamingResponse:
        return QueriesResourceWithStreamingResponse(self._tasks.queries)

    @cached_property
    def auto(self) -> AutoResourceWithStreamingResponse:
        return AutoResourceWithStreamingResponse(self._tasks.auto)

    @cached_property
    def emoji(self) -> EmojiResourceWithStreamingResponse:
        return EmojiResourceWithStreamingResponse(self._tasks.emoji)

    @cached_property
    def moa(self) -> MoaResourceWithStreamingResponse:
        return MoaResourceWithStreamingResponse(self._tasks.moa)


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._tasks.config)

    @cached_property
    def title(self) -> AsyncTitleResourceWithStreamingResponse:
        return AsyncTitleResourceWithStreamingResponse(self._tasks.title)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._tasks.tags)

    @cached_property
    def image_prompt(self) -> AsyncImagePromptResourceWithStreamingResponse:
        return AsyncImagePromptResourceWithStreamingResponse(self._tasks.image_prompt)

    @cached_property
    def queries(self) -> AsyncQueriesResourceWithStreamingResponse:
        return AsyncQueriesResourceWithStreamingResponse(self._tasks.queries)

    @cached_property
    def auto(self) -> AsyncAutoResourceWithStreamingResponse:
        return AsyncAutoResourceWithStreamingResponse(self._tasks.auto)

    @cached_property
    def emoji(self) -> AsyncEmojiResourceWithStreamingResponse:
        return AsyncEmojiResourceWithStreamingResponse(self._tasks.emoji)

    @cached_property
    def moa(self) -> AsyncMoaResourceWithStreamingResponse:
        return AsyncMoaResourceWithStreamingResponse(self._tasks.moa)
