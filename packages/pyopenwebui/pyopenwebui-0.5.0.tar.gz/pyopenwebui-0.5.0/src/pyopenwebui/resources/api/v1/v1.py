# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .folders import (
    FoldersResource,
    AsyncFoldersResource,
    FoldersResourceWithRawResponse,
    AsyncFoldersResourceWithRawResponse,
    FoldersResourceWithStreamingResponse,
    AsyncFoldersResourceWithStreamingResponse,
)
from .memories import (
    MemoriesResource,
    AsyncMemoriesResource,
    MemoriesResourceWithRawResponse,
    AsyncMemoriesResourceWithRawResponse,
    MemoriesResourceWithStreamingResponse,
    AsyncMemoriesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .audio.audio import (
    AudioResource,
    AsyncAudioResource,
    AudioResourceWithRawResponse,
    AsyncAudioResourceWithRawResponse,
    AudioResourceWithStreamingResponse,
    AsyncAudioResourceWithStreamingResponse,
)
from .auths.auths import (
    AuthsResource,
    AsyncAuthsResource,
    AuthsResourceWithRawResponse,
    AsyncAuthsResourceWithRawResponse,
    AuthsResourceWithStreamingResponse,
    AsyncAuthsResourceWithStreamingResponse,
)
from .chats.chats import (
    ChatsResource,
    AsyncChatsResource,
    ChatsResourceWithRawResponse,
    AsyncChatsResourceWithRawResponse,
    ChatsResourceWithStreamingResponse,
    AsyncChatsResourceWithStreamingResponse,
)
from .files.files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from .tasks.tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from .tools.tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from .users.users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from .utils.utils import (
    UtilsResource,
    AsyncUtilsResource,
    UtilsResourceWithRawResponse,
    AsyncUtilsResourceWithRawResponse,
    UtilsResourceWithStreamingResponse,
    AsyncUtilsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .groups.groups import (
    GroupsResource,
    AsyncGroupsResource,
    GroupsResourceWithRawResponse,
    AsyncGroupsResourceWithRawResponse,
    GroupsResourceWithStreamingResponse,
    AsyncGroupsResourceWithStreamingResponse,
)
from .images.images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from .models.models import (
    ModelsResource,
    AsyncModelsResource,
    ModelsResourceWithRawResponse,
    AsyncModelsResourceWithRawResponse,
    ModelsResourceWithStreamingResponse,
    AsyncModelsResourceWithStreamingResponse,
)
from .configs.configs import (
    ConfigsResource,
    AsyncConfigsResource,
    ConfigsResourceWithRawResponse,
    AsyncConfigsResourceWithRawResponse,
    ConfigsResourceWithStreamingResponse,
    AsyncConfigsResourceWithStreamingResponse,
)
from .prompts.prompts import (
    PromptsResource,
    AsyncPromptsResource,
    PromptsResourceWithRawResponse,
    AsyncPromptsResourceWithRawResponse,
    PromptsResourceWithStreamingResponse,
    AsyncPromptsResourceWithStreamingResponse,
)
from .channels.channels import (
    ChannelsResource,
    AsyncChannelsResource,
    ChannelsResourceWithRawResponse,
    AsyncChannelsResourceWithRawResponse,
    ChannelsResourceWithStreamingResponse,
    AsyncChannelsResourceWithStreamingResponse,
)
from .functions.functions import (
    FunctionsResource,
    AsyncFunctionsResource,
    FunctionsResourceWithRawResponse,
    AsyncFunctionsResourceWithRawResponse,
    FunctionsResourceWithStreamingResponse,
    AsyncFunctionsResourceWithStreamingResponse,
)
from .knowledge.knowledge import (
    KnowledgeResource,
    AsyncKnowledgeResource,
    KnowledgeResourceWithRawResponse,
    AsyncKnowledgeResourceWithRawResponse,
    KnowledgeResourceWithStreamingResponse,
    AsyncKnowledgeResourceWithStreamingResponse,
)
from .pipelines.pipelines import (
    PipelinesResource,
    AsyncPipelinesResource,
    PipelinesResourceWithRawResponse,
    AsyncPipelinesResourceWithRawResponse,
    PipelinesResourceWithStreamingResponse,
    AsyncPipelinesResourceWithStreamingResponse,
)
from .retrieval.retrieval import (
    RetrievalResource,
    AsyncRetrievalResource,
    RetrievalResourceWithRawResponse,
    AsyncRetrievalResourceWithRawResponse,
    RetrievalResourceWithStreamingResponse,
    AsyncRetrievalResourceWithStreamingResponse,
)
from .evaluations.evaluations import (
    EvaluationsResource,
    AsyncEvaluationsResource,
    EvaluationsResourceWithRawResponse,
    AsyncEvaluationsResourceWithRawResponse,
    EvaluationsResourceWithStreamingResponse,
    AsyncEvaluationsResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def pipelines(self) -> PipelinesResource:
        return PipelinesResource(self._client)

    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def audio(self) -> AudioResource:
        return AudioResource(self._client)

    @cached_property
    def retrieval(self) -> RetrievalResource:
        return RetrievalResource(self._client)

    @cached_property
    def configs(self) -> ConfigsResource:
        return ConfigsResource(self._client)

    @cached_property
    def auths(self) -> AuthsResource:
        return AuthsResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def channels(self) -> ChannelsResource:
        return ChannelsResource(self._client)

    @cached_property
    def chats(self) -> ChatsResource:
        return ChatsResource(self._client)

    @cached_property
    def models(self) -> ModelsResource:
        return ModelsResource(self._client)

    @cached_property
    def knowledge(self) -> KnowledgeResource:
        return KnowledgeResource(self._client)

    @cached_property
    def prompts(self) -> PromptsResource:
        return PromptsResource(self._client)

    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def memories(self) -> MemoriesResource:
        return MemoriesResource(self._client)

    @cached_property
    def folders(self) -> FoldersResource:
        return FoldersResource(self._client)

    @cached_property
    def groups(self) -> GroupsResource:
        return GroupsResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def functions(self) -> FunctionsResource:
        return FunctionsResource(self._client)

    @cached_property
    def evaluations(self) -> EvaluationsResource:
        return EvaluationsResource(self._client)

    @cached_property
    def utils(self) -> UtilsResource:
        return UtilsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def pipelines(self) -> AsyncPipelinesResource:
        return AsyncPipelinesResource(self._client)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def audio(self) -> AsyncAudioResource:
        return AsyncAudioResource(self._client)

    @cached_property
    def retrieval(self) -> AsyncRetrievalResource:
        return AsyncRetrievalResource(self._client)

    @cached_property
    def configs(self) -> AsyncConfigsResource:
        return AsyncConfigsResource(self._client)

    @cached_property
    def auths(self) -> AsyncAuthsResource:
        return AsyncAuthsResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def channels(self) -> AsyncChannelsResource:
        return AsyncChannelsResource(self._client)

    @cached_property
    def chats(self) -> AsyncChatsResource:
        return AsyncChatsResource(self._client)

    @cached_property
    def models(self) -> AsyncModelsResource:
        return AsyncModelsResource(self._client)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResource:
        return AsyncKnowledgeResource(self._client)

    @cached_property
    def prompts(self) -> AsyncPromptsResource:
        return AsyncPromptsResource(self._client)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def memories(self) -> AsyncMemoriesResource:
        return AsyncMemoriesResource(self._client)

    @cached_property
    def folders(self) -> AsyncFoldersResource:
        return AsyncFoldersResource(self._client)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        return AsyncGroupsResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def functions(self) -> AsyncFunctionsResource:
        return AsyncFunctionsResource(self._client)

    @cached_property
    def evaluations(self) -> AsyncEvaluationsResource:
        return AsyncEvaluationsResource(self._client)

    @cached_property
    def utils(self) -> AsyncUtilsResource:
        return AsyncUtilsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/aigc-libs/pyopenwebui-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def pipelines(self) -> PipelinesResourceWithRawResponse:
        return PipelinesResourceWithRawResponse(self._v1.pipelines)

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._v1.tasks)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._v1.images)

    @cached_property
    def audio(self) -> AudioResourceWithRawResponse:
        return AudioResourceWithRawResponse(self._v1.audio)

    @cached_property
    def retrieval(self) -> RetrievalResourceWithRawResponse:
        return RetrievalResourceWithRawResponse(self._v1.retrieval)

    @cached_property
    def configs(self) -> ConfigsResourceWithRawResponse:
        return ConfigsResourceWithRawResponse(self._v1.configs)

    @cached_property
    def auths(self) -> AuthsResourceWithRawResponse:
        return AuthsResourceWithRawResponse(self._v1.auths)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._v1.users)

    @cached_property
    def channels(self) -> ChannelsResourceWithRawResponse:
        return ChannelsResourceWithRawResponse(self._v1.channels)

    @cached_property
    def chats(self) -> ChatsResourceWithRawResponse:
        return ChatsResourceWithRawResponse(self._v1.chats)

    @cached_property
    def models(self) -> ModelsResourceWithRawResponse:
        return ModelsResourceWithRawResponse(self._v1.models)

    @cached_property
    def knowledge(self) -> KnowledgeResourceWithRawResponse:
        return KnowledgeResourceWithRawResponse(self._v1.knowledge)

    @cached_property
    def prompts(self) -> PromptsResourceWithRawResponse:
        return PromptsResourceWithRawResponse(self._v1.prompts)

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._v1.tools)

    @cached_property
    def memories(self) -> MemoriesResourceWithRawResponse:
        return MemoriesResourceWithRawResponse(self._v1.memories)

    @cached_property
    def folders(self) -> FoldersResourceWithRawResponse:
        return FoldersResourceWithRawResponse(self._v1.folders)

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        return GroupsResourceWithRawResponse(self._v1.groups)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._v1.files)

    @cached_property
    def functions(self) -> FunctionsResourceWithRawResponse:
        return FunctionsResourceWithRawResponse(self._v1.functions)

    @cached_property
    def evaluations(self) -> EvaluationsResourceWithRawResponse:
        return EvaluationsResourceWithRawResponse(self._v1.evaluations)

    @cached_property
    def utils(self) -> UtilsResourceWithRawResponse:
        return UtilsResourceWithRawResponse(self._v1.utils)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def pipelines(self) -> AsyncPipelinesResourceWithRawResponse:
        return AsyncPipelinesResourceWithRawResponse(self._v1.pipelines)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._v1.tasks)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._v1.images)

    @cached_property
    def audio(self) -> AsyncAudioResourceWithRawResponse:
        return AsyncAudioResourceWithRawResponse(self._v1.audio)

    @cached_property
    def retrieval(self) -> AsyncRetrievalResourceWithRawResponse:
        return AsyncRetrievalResourceWithRawResponse(self._v1.retrieval)

    @cached_property
    def configs(self) -> AsyncConfigsResourceWithRawResponse:
        return AsyncConfigsResourceWithRawResponse(self._v1.configs)

    @cached_property
    def auths(self) -> AsyncAuthsResourceWithRawResponse:
        return AsyncAuthsResourceWithRawResponse(self._v1.auths)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._v1.users)

    @cached_property
    def channels(self) -> AsyncChannelsResourceWithRawResponse:
        return AsyncChannelsResourceWithRawResponse(self._v1.channels)

    @cached_property
    def chats(self) -> AsyncChatsResourceWithRawResponse:
        return AsyncChatsResourceWithRawResponse(self._v1.chats)

    @cached_property
    def models(self) -> AsyncModelsResourceWithRawResponse:
        return AsyncModelsResourceWithRawResponse(self._v1.models)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResourceWithRawResponse:
        return AsyncKnowledgeResourceWithRawResponse(self._v1.knowledge)

    @cached_property
    def prompts(self) -> AsyncPromptsResourceWithRawResponse:
        return AsyncPromptsResourceWithRawResponse(self._v1.prompts)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._v1.tools)

    @cached_property
    def memories(self) -> AsyncMemoriesResourceWithRawResponse:
        return AsyncMemoriesResourceWithRawResponse(self._v1.memories)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithRawResponse:
        return AsyncFoldersResourceWithRawResponse(self._v1.folders)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        return AsyncGroupsResourceWithRawResponse(self._v1.groups)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._v1.files)

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithRawResponse:
        return AsyncFunctionsResourceWithRawResponse(self._v1.functions)

    @cached_property
    def evaluations(self) -> AsyncEvaluationsResourceWithRawResponse:
        return AsyncEvaluationsResourceWithRawResponse(self._v1.evaluations)

    @cached_property
    def utils(self) -> AsyncUtilsResourceWithRawResponse:
        return AsyncUtilsResourceWithRawResponse(self._v1.utils)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def pipelines(self) -> PipelinesResourceWithStreamingResponse:
        return PipelinesResourceWithStreamingResponse(self._v1.pipelines)

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._v1.tasks)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._v1.images)

    @cached_property
    def audio(self) -> AudioResourceWithStreamingResponse:
        return AudioResourceWithStreamingResponse(self._v1.audio)

    @cached_property
    def retrieval(self) -> RetrievalResourceWithStreamingResponse:
        return RetrievalResourceWithStreamingResponse(self._v1.retrieval)

    @cached_property
    def configs(self) -> ConfigsResourceWithStreamingResponse:
        return ConfigsResourceWithStreamingResponse(self._v1.configs)

    @cached_property
    def auths(self) -> AuthsResourceWithStreamingResponse:
        return AuthsResourceWithStreamingResponse(self._v1.auths)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._v1.users)

    @cached_property
    def channels(self) -> ChannelsResourceWithStreamingResponse:
        return ChannelsResourceWithStreamingResponse(self._v1.channels)

    @cached_property
    def chats(self) -> ChatsResourceWithStreamingResponse:
        return ChatsResourceWithStreamingResponse(self._v1.chats)

    @cached_property
    def models(self) -> ModelsResourceWithStreamingResponse:
        return ModelsResourceWithStreamingResponse(self._v1.models)

    @cached_property
    def knowledge(self) -> KnowledgeResourceWithStreamingResponse:
        return KnowledgeResourceWithStreamingResponse(self._v1.knowledge)

    @cached_property
    def prompts(self) -> PromptsResourceWithStreamingResponse:
        return PromptsResourceWithStreamingResponse(self._v1.prompts)

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._v1.tools)

    @cached_property
    def memories(self) -> MemoriesResourceWithStreamingResponse:
        return MemoriesResourceWithStreamingResponse(self._v1.memories)

    @cached_property
    def folders(self) -> FoldersResourceWithStreamingResponse:
        return FoldersResourceWithStreamingResponse(self._v1.folders)

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        return GroupsResourceWithStreamingResponse(self._v1.groups)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._v1.files)

    @cached_property
    def functions(self) -> FunctionsResourceWithStreamingResponse:
        return FunctionsResourceWithStreamingResponse(self._v1.functions)

    @cached_property
    def evaluations(self) -> EvaluationsResourceWithStreamingResponse:
        return EvaluationsResourceWithStreamingResponse(self._v1.evaluations)

    @cached_property
    def utils(self) -> UtilsResourceWithStreamingResponse:
        return UtilsResourceWithStreamingResponse(self._v1.utils)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def pipelines(self) -> AsyncPipelinesResourceWithStreamingResponse:
        return AsyncPipelinesResourceWithStreamingResponse(self._v1.pipelines)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._v1.tasks)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._v1.images)

    @cached_property
    def audio(self) -> AsyncAudioResourceWithStreamingResponse:
        return AsyncAudioResourceWithStreamingResponse(self._v1.audio)

    @cached_property
    def retrieval(self) -> AsyncRetrievalResourceWithStreamingResponse:
        return AsyncRetrievalResourceWithStreamingResponse(self._v1.retrieval)

    @cached_property
    def configs(self) -> AsyncConfigsResourceWithStreamingResponse:
        return AsyncConfigsResourceWithStreamingResponse(self._v1.configs)

    @cached_property
    def auths(self) -> AsyncAuthsResourceWithStreamingResponse:
        return AsyncAuthsResourceWithStreamingResponse(self._v1.auths)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._v1.users)

    @cached_property
    def channels(self) -> AsyncChannelsResourceWithStreamingResponse:
        return AsyncChannelsResourceWithStreamingResponse(self._v1.channels)

    @cached_property
    def chats(self) -> AsyncChatsResourceWithStreamingResponse:
        return AsyncChatsResourceWithStreamingResponse(self._v1.chats)

    @cached_property
    def models(self) -> AsyncModelsResourceWithStreamingResponse:
        return AsyncModelsResourceWithStreamingResponse(self._v1.models)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResourceWithStreamingResponse:
        return AsyncKnowledgeResourceWithStreamingResponse(self._v1.knowledge)

    @cached_property
    def prompts(self) -> AsyncPromptsResourceWithStreamingResponse:
        return AsyncPromptsResourceWithStreamingResponse(self._v1.prompts)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._v1.tools)

    @cached_property
    def memories(self) -> AsyncMemoriesResourceWithStreamingResponse:
        return AsyncMemoriesResourceWithStreamingResponse(self._v1.memories)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithStreamingResponse:
        return AsyncFoldersResourceWithStreamingResponse(self._v1.folders)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        return AsyncGroupsResourceWithStreamingResponse(self._v1.groups)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._v1.files)

    @cached_property
    def functions(self) -> AsyncFunctionsResourceWithStreamingResponse:
        return AsyncFunctionsResourceWithStreamingResponse(self._v1.functions)

    @cached_property
    def evaluations(self) -> AsyncEvaluationsResourceWithStreamingResponse:
        return AsyncEvaluationsResourceWithStreamingResponse(self._v1.evaluations)

    @cached_property
    def utils(self) -> AsyncUtilsResourceWithStreamingResponse:
        return AsyncUtilsResourceWithStreamingResponse(self._v1.utils)
