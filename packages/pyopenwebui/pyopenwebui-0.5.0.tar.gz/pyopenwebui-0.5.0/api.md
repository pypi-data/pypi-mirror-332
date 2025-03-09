# Shared Types

```python
from pyopenwebui.types import FileModel, PromptModel
```

# Configs

## Default

### Suggestions

Types:

```python
from pyopenwebui.types.configs.default import PromptSuggestion
```

## Banners

Types:

```python
from pyopenwebui.types.configs import BannerModel
```

# Auths

Types:

```python
from pyopenwebui.types import APIKey, SigninResponse
```

# Users

Types:

```python
from pyopenwebui.types import UserModel
```

## User

Types:

```python
from pyopenwebui.types.users import UserSettings
```

# Chats

Types:

```python
from pyopenwebui.types import ChatResponse, ChatTitleIDResponse
```

## Tags

Types:

```python
from pyopenwebui.types.chats import TagModel
```

# Models

Types:

```python
from pyopenwebui.types import ModelModel
```

# Memories

Types:

```python
from pyopenwebui.types import MemoryModel
```

# Tools

Types:

```python
from pyopenwebui.types import ToolModel, ToolResponse
```

# Functions

Types:

```python
from pyopenwebui.types import FunctionModel, FunctionResponse, FunctionModel
```

# Ollama

Types:

```python
from pyopenwebui.types import OllamaGetStatusResponse, OllamaVerifyConnectionResponse
```

Methods:

- <code title="get /ollama/">client.ollama.<a href="./src/pyopenwebui/resources/ollama/ollama.py">get_status</a>() -> <a href="./src/pyopenwebui/types/ollama_get_status_response.py">object</a></code>
- <code title="post /ollama/verify">client.ollama.<a href="./src/pyopenwebui/resources/ollama/ollama.py">verify_connection</a>(\*\*<a href="src/pyopenwebui/types/ollama_verify_connection_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama_verify_connection_response.py">object</a></code>

## Config

Types:

```python
from pyopenwebui.types.ollama import ConfigUpdateResponse, ConfigGetResponse
```

Methods:

- <code title="post /ollama/config/update">client.ollama.config.<a href="./src/pyopenwebui/resources/ollama/config.py">update</a>(\*\*<a href="src/pyopenwebui/types/ollama/config_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/config_update_response.py">object</a></code>
- <code title="get /ollama/config">client.ollama.config.<a href="./src/pyopenwebui/resources/ollama/config.py">get</a>() -> <a href="./src/pyopenwebui/types/ollama/config_get_response.py">object</a></code>

## API

Types:

```python
from pyopenwebui.types.ollama import APIGetLoadedModelsResponse, APIShowInfoResponse
```

Methods:

- <code title="get /ollama/api/ps">client.ollama.api.<a href="./src/pyopenwebui/resources/ollama/api/api.py">get_loaded_models</a>() -> <a href="./src/pyopenwebui/types/ollama/api_get_loaded_models_response.py">object</a></code>
- <code title="post /ollama/api/show">client.ollama.api.<a href="./src/pyopenwebui/resources/ollama/api/api.py">show_info</a>(\*\*<a href="src/pyopenwebui/types/ollama/api_show_info_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api_show_info_response.py">object</a></code>

### Tags

Types:

```python
from pyopenwebui.types.ollama.api import TagListResponse, TagGetByIndexResponse
```

Methods:

- <code title="get /ollama/api/tags">client.ollama.api.tags.<a href="./src/pyopenwebui/resources/ollama/api/tags.py">list</a>(\*\*<a href="src/pyopenwebui/types/ollama/api/tag_list_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/tag_list_response.py">object</a></code>
- <code title="get /ollama/api/tags/{url_idx}">client.ollama.api.tags.<a href="./src/pyopenwebui/resources/ollama/api/tags.py">get_by_index</a>(url_idx) -> <a href="./src/pyopenwebui/types/ollama/api/tag_get_by_index_response.py">object</a></code>

### Version

Types:

```python
from pyopenwebui.types.ollama.api import VersionListResponse, VersionGetByIndexResponse
```

Methods:

- <code title="get /ollama/api/version">client.ollama.api.version.<a href="./src/pyopenwebui/resources/ollama/api/version.py">list</a>(\*\*<a href="src/pyopenwebui/types/ollama/api/version_list_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/version_list_response.py">object</a></code>
- <code title="get /ollama/api/version/{url_idx}">client.ollama.api.version.<a href="./src/pyopenwebui/resources/ollama/api/version.py">get_by_index</a>(url_idx) -> <a href="./src/pyopenwebui/types/ollama/api/version_get_by_index_response.py">object</a></code>

### Pull

Types:

```python
from pyopenwebui.types.ollama.api import PullPullResponse, PullPullByIndexResponse
```

Methods:

- <code title="post /ollama/api/pull">client.ollama.api.pull.<a href="./src/pyopenwebui/resources/ollama/api/pull.py">pull</a>(\*\*<a href="src/pyopenwebui/types/ollama/api/pull_pull_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/pull_pull_response.py">object</a></code>
- <code title="post /ollama/api/pull/{url_idx}">client.ollama.api.pull.<a href="./src/pyopenwebui/resources/ollama/api/pull.py">pull_by_index</a>(url_idx, \*\*<a href="src/pyopenwebui/types/ollama/api/pull_pull_by_index_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/pull_pull_by_index_response.py">object</a></code>

### Push

Types:

```python
from pyopenwebui.types.ollama.api import PushPushResponse, PushPushByIndexResponse
```

Methods:

- <code title="delete /ollama/api/push">client.ollama.api.push.<a href="./src/pyopenwebui/resources/ollama/api/push.py">push</a>(\*\*<a href="src/pyopenwebui/types/ollama/api/push_push_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/push_push_response.py">object</a></code>
- <code title="delete /ollama/api/push/{url_idx}">client.ollama.api.push.<a href="./src/pyopenwebui/resources/ollama/api/push.py">push_by_index</a>(url_idx, \*\*<a href="src/pyopenwebui/types/ollama/api/push_push_by_index_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/push_push_by_index_response.py">object</a></code>

### Create

Types:

```python
from pyopenwebui.types.ollama.api import CreateCreateResponse, CreateCreateByIndexResponse
```

Methods:

- <code title="post /ollama/api/create">client.ollama.api.create.<a href="./src/pyopenwebui/resources/ollama/api/create.py">create</a>(\*\*<a href="src/pyopenwebui/types/ollama/api/create_create_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/create_create_response.py">object</a></code>
- <code title="post /ollama/api/create/{url_idx}">client.ollama.api.create.<a href="./src/pyopenwebui/resources/ollama/api/create.py">create_by_index</a>(url_idx, \*\*<a href="src/pyopenwebui/types/ollama/api/create_create_by_index_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/create_create_by_index_response.py">object</a></code>

### Copy

Types:

```python
from pyopenwebui.types.ollama.api import CopyCopyResponse, CopyCopyByIndexResponse
```

Methods:

- <code title="post /ollama/api/copy">client.ollama.api.copy.<a href="./src/pyopenwebui/resources/ollama/api/copy.py">copy</a>(\*\*<a href="src/pyopenwebui/types/ollama/api/copy_copy_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/copy_copy_response.py">object</a></code>
- <code title="post /ollama/api/copy/{url_idx}">client.ollama.api.copy.<a href="./src/pyopenwebui/resources/ollama/api/copy.py">copy_by_index</a>(url_idx, \*\*<a href="src/pyopenwebui/types/ollama/api/copy_copy_by_index_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/copy_copy_by_index_response.py">object</a></code>

### Delete

Types:

```python
from pyopenwebui.types.ollama.api import DeleteDeleteResponse, DeleteDeleteByIndexResponse
```

Methods:

- <code title="delete /ollama/api/delete">client.ollama.api.delete.<a href="./src/pyopenwebui/resources/ollama/api/delete.py">delete</a>(\*\*<a href="src/pyopenwebui/types/ollama/api/delete_delete_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/delete_delete_response.py">object</a></code>
- <code title="delete /ollama/api/delete/{url_idx}">client.ollama.api.delete.<a href="./src/pyopenwebui/resources/ollama/api/delete.py">delete_by_index</a>(url_idx, \*\*<a href="src/pyopenwebui/types/ollama/api/delete_delete_by_index_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/delete_delete_by_index_response.py">object</a></code>

### Embed

Types:

```python
from pyopenwebui.types.ollama.api import EmbedEmbedResponse, EmbedEmbedByIndexResponse
```

Methods:

- <code title="post /ollama/api/embed">client.ollama.api.embed.<a href="./src/pyopenwebui/resources/ollama/api/embed.py">embed</a>(\*\*<a href="src/pyopenwebui/types/ollama/api/embed_embed_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/embed_embed_response.py">object</a></code>
- <code title="post /ollama/api/embed/{url_idx}">client.ollama.api.embed.<a href="./src/pyopenwebui/resources/ollama/api/embed.py">embed_by_index</a>(url_idx, \*\*<a href="src/pyopenwebui/types/ollama/api/embed_embed_by_index_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/embed_embed_by_index_response.py">object</a></code>

### Embeddings

Types:

```python
from pyopenwebui.types.ollama.api import (
    EmbeddingEmbeddingsResponse,
    EmbeddingEmbeddingsByIndexResponse,
)
```

Methods:

- <code title="post /ollama/api/embeddings">client.ollama.api.embeddings.<a href="./src/pyopenwebui/resources/ollama/api/embeddings.py">embeddings</a>(\*\*<a href="src/pyopenwebui/types/ollama/api/embedding_embeddings_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/embedding_embeddings_response.py">object</a></code>
- <code title="post /ollama/api/embeddings/{url_idx}">client.ollama.api.embeddings.<a href="./src/pyopenwebui/resources/ollama/api/embeddings.py">embeddings_by_index</a>(url_idx, \*\*<a href="src/pyopenwebui/types/ollama/api/embedding_embeddings_by_index_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/embedding_embeddings_by_index_response.py">object</a></code>

### Generate

Types:

```python
from pyopenwebui.types.ollama.api import GenerateGenerateResponse, GenerateGenerateByIndexResponse
```

Methods:

- <code title="post /ollama/api/generate">client.ollama.api.generate.<a href="./src/pyopenwebui/resources/ollama/api/generate.py">generate</a>(\*\*<a href="src/pyopenwebui/types/ollama/api/generate_generate_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/generate_generate_response.py">object</a></code>
- <code title="post /ollama/api/generate/{url_idx}">client.ollama.api.generate.<a href="./src/pyopenwebui/resources/ollama/api/generate.py">generate_by_index</a>(url_idx, \*\*<a href="src/pyopenwebui/types/ollama/api/generate_generate_by_index_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/generate_generate_by_index_response.py">object</a></code>

### Chat

Types:

```python
from pyopenwebui.types.ollama.api import ChatChatResponse, ChatChatByIndexResponse
```

Methods:

- <code title="post /ollama/api/chat">client.ollama.api.chat.<a href="./src/pyopenwebui/resources/ollama/api/chat.py">chat</a>(\*\*<a href="src/pyopenwebui/types/ollama/api/chat_chat_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/chat_chat_response.py">object</a></code>
- <code title="post /ollama/api/chat/{url_idx}">client.ollama.api.chat.<a href="./src/pyopenwebui/resources/ollama/api/chat.py">chat_by_index</a>(url_idx, \*\*<a href="src/pyopenwebui/types/ollama/api/chat_chat_by_index_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/api/chat_chat_by_index_response.py">object</a></code>

## V1

### Completions

Types:

```python
from pyopenwebui.types.ollama.v1 import (
    CompletionGenerateResponse,
    CompletionGenerateByIndexResponse,
)
```

Methods:

- <code title="post /ollama/v1/completions">client.ollama.v1.completions.<a href="./src/pyopenwebui/resources/ollama/v1/completions.py">generate</a>(\*\*<a href="src/pyopenwebui/types/ollama/v1/completion_generate_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/v1/completion_generate_response.py">object</a></code>
- <code title="post /ollama/v1/completions/{url_idx}">client.ollama.v1.completions.<a href="./src/pyopenwebui/resources/ollama/v1/completions.py">generate_by_index</a>(url_idx, \*\*<a href="src/pyopenwebui/types/ollama/v1/completion_generate_by_index_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/v1/completion_generate_by_index_response.py">object</a></code>

### Chat

#### Completions

Types:

```python
from pyopenwebui.types.ollama.v1.chat import (
    CompletionGenerateResponse,
    CompletionGenerateByIndexResponse,
)
```

Methods:

- <code title="post /ollama/v1/chat/completions">client.ollama.v1.chat.completions.<a href="./src/pyopenwebui/resources/ollama/v1/chat/completions.py">generate</a>(\*\*<a href="src/pyopenwebui/types/ollama/v1/chat/completion_generate_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/v1/chat/completion_generate_response.py">object</a></code>
- <code title="post /ollama/v1/chat/completions/{url_idx}">client.ollama.v1.chat.completions.<a href="./src/pyopenwebui/resources/ollama/v1/chat/completions.py">generate_by_index</a>(url_idx, \*\*<a href="src/pyopenwebui/types/ollama/v1/chat/completion_generate_by_index_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/v1/chat/completion_generate_by_index_response.py">object</a></code>

### Models

Types:

```python
from pyopenwebui.types.ollama.v1 import ModelListResponse, ModelGetByIndexResponse
```

Methods:

- <code title="get /ollama/v1/models">client.ollama.v1.models.<a href="./src/pyopenwebui/resources/ollama/v1/models.py">list</a>(\*\*<a href="src/pyopenwebui/types/ollama/v1/model_list_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/v1/model_list_response.py">object</a></code>
- <code title="get /ollama/v1/models/{url_idx}">client.ollama.v1.models.<a href="./src/pyopenwebui/resources/ollama/v1/models.py">get_by_index</a>(url_idx) -> <a href="./src/pyopenwebui/types/ollama/v1/model_get_by_index_response.py">object</a></code>

## Models

### Download

Types:

```python
from pyopenwebui.types.ollama.models import (
    DownloadDownloadResponse,
    DownloadDownloadByIndexResponse,
)
```

Methods:

- <code title="post /ollama/models/download">client.ollama.models.download.<a href="./src/pyopenwebui/resources/ollama/models/download.py">download</a>(\*\*<a href="src/pyopenwebui/types/ollama/models/download_download_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/models/download_download_response.py">object</a></code>
- <code title="post /ollama/models/download/{url_idx}">client.ollama.models.download.<a href="./src/pyopenwebui/resources/ollama/models/download.py">download_by_index</a>(url_idx, \*\*<a href="src/pyopenwebui/types/ollama/models/download_download_by_index_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/models/download_download_by_index_response.py">object</a></code>

### Upload

Types:

```python
from pyopenwebui.types.ollama.models import UploadUploadResponse, UploadUploadByIndexResponse
```

Methods:

- <code title="post /ollama/models/upload">client.ollama.models.upload.<a href="./src/pyopenwebui/resources/ollama/models/upload.py">upload</a>(\*\*<a href="src/pyopenwebui/types/ollama/models/upload_upload_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/models/upload_upload_response.py">object</a></code>
- <code title="post /ollama/models/upload/{url_idx}">client.ollama.models.upload.<a href="./src/pyopenwebui/resources/ollama/models/upload.py">upload_by_index</a>(url_idx, \*\*<a href="src/pyopenwebui/types/ollama/models/upload_upload_by_index_params.py">params</a>) -> <a href="./src/pyopenwebui/types/ollama/models/upload_upload_by_index_response.py">object</a></code>

# OpenAI

Types:

```python
from pyopenwebui.types import (
    OpenAIProxyDeleteResponse,
    OpenAIProxyGetResponse,
    OpenAIProxyPostResponse,
    OpenAIProxyPutResponse,
    OpenAIVerifyConnectionResponse,
)
```

Methods:

- <code title="delete /openai/{path}">client.openai.<a href="./src/pyopenwebui/resources/openai/openai.py">proxy_delete</a>(path) -> <a href="./src/pyopenwebui/types/openai_proxy_delete_response.py">object</a></code>
- <code title="get /openai/{path}">client.openai.<a href="./src/pyopenwebui/resources/openai/openai.py">proxy_get</a>(path) -> <a href="./src/pyopenwebui/types/openai_proxy_get_response.py">object</a></code>
- <code title="post /openai/{path}">client.openai.<a href="./src/pyopenwebui/resources/openai/openai.py">proxy_post</a>(path) -> <a href="./src/pyopenwebui/types/openai_proxy_post_response.py">object</a></code>
- <code title="put /openai/{path}">client.openai.<a href="./src/pyopenwebui/resources/openai/openai.py">proxy_put</a>(path) -> <a href="./src/pyopenwebui/types/openai_proxy_put_response.py">object</a></code>
- <code title="post /openai/verify">client.openai.<a href="./src/pyopenwebui/resources/openai/openai.py">verify_connection</a>(\*\*<a href="src/pyopenwebui/types/openai_verify_connection_params.py">params</a>) -> <a href="./src/pyopenwebui/types/openai_verify_connection_response.py">object</a></code>

## Config

Types:

```python
from pyopenwebui.types.openai import ConfigRetrieveResponse, ConfigUpdateResponse
```

Methods:

- <code title="get /openai/config">client.openai.config.<a href="./src/pyopenwebui/resources/openai/config.py">retrieve</a>() -> <a href="./src/pyopenwebui/types/openai/config_retrieve_response.py">object</a></code>
- <code title="post /openai/config/update">client.openai.config.<a href="./src/pyopenwebui/resources/openai/config.py">update</a>(\*\*<a href="src/pyopenwebui/types/openai/config_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/openai/config_update_response.py">object</a></code>

## Audio

Types:

```python
from pyopenwebui.types.openai import AudioSpeechResponse
```

Methods:

- <code title="post /openai/audio/speech">client.openai.audio.<a href="./src/pyopenwebui/resources/openai/audio.py">speech</a>() -> <a href="./src/pyopenwebui/types/openai/audio_speech_response.py">object</a></code>

## Models

Types:

```python
from pyopenwebui.types.openai import ModelRetrieveResponse, ModelListResponse
```

Methods:

- <code title="get /openai/models/{url_idx}">client.openai.models.<a href="./src/pyopenwebui/resources/openai/models.py">retrieve</a>(url_idx) -> <a href="./src/pyopenwebui/types/openai/model_retrieve_response.py">object</a></code>
- <code title="get /openai/models">client.openai.models.<a href="./src/pyopenwebui/resources/openai/models.py">list</a>(\*\*<a href="src/pyopenwebui/types/openai/model_list_params.py">params</a>) -> <a href="./src/pyopenwebui/types/openai/model_list_response.py">object</a></code>

## Chat

Types:

```python
from pyopenwebui.types.openai import ChatGenerateCompletionResponse
```

Methods:

- <code title="post /openai/chat/completions">client.openai.chat.<a href="./src/pyopenwebui/resources/openai/chat.py">generate_completion</a>(\*\*<a href="src/pyopenwebui/types/openai/chat_generate_completion_params.py">params</a>) -> <a href="./src/pyopenwebui/types/openai/chat_generate_completion_response.py">object</a></code>

# API

Types:

```python
from pyopenwebui.types import APIGetChangelogResponse, APIGetConfigResponse
```

Methods:

- <code title="get /api/changelog">client.api.<a href="./src/pyopenwebui/resources/api/api.py">get_changelog</a>() -> <a href="./src/pyopenwebui/types/api_get_changelog_response.py">object</a></code>
- <code title="get /api/config">client.api.<a href="./src/pyopenwebui/resources/api/api.py">get_config</a>() -> <a href="./src/pyopenwebui/types/api_get_config_response.py">object</a></code>

## V1

### Pipelines

Types:

```python
from pyopenwebui.types.api.v1 import (
    PipelineListResponse,
    PipelineDeleteResponse,
    PipelineAddResponse,
    PipelineGetResponse,
    PipelineUploadResponse,
)
```

Methods:

- <code title="get /api/v1/pipelines/list">client.api.v1.pipelines.<a href="./src/pyopenwebui/resources/api/v1/pipelines/pipelines.py">list</a>() -> <a href="./src/pyopenwebui/types/api/v1/pipeline_list_response.py">object</a></code>
- <code title="delete /api/v1/pipelines/delete">client.api.v1.pipelines.<a href="./src/pyopenwebui/resources/api/v1/pipelines/pipelines.py">delete</a>(\*\*<a href="src/pyopenwebui/types/api/v1/pipeline_delete_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/pipeline_delete_response.py">object</a></code>
- <code title="post /api/v1/pipelines/add">client.api.v1.pipelines.<a href="./src/pyopenwebui/resources/api/v1/pipelines/pipelines.py">add</a>(\*\*<a href="src/pyopenwebui/types/api/v1/pipeline_add_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/pipeline_add_response.py">object</a></code>
- <code title="get /api/v1/pipelines/">client.api.v1.pipelines.<a href="./src/pyopenwebui/resources/api/v1/pipelines/pipelines.py">get</a>(\*\*<a href="src/pyopenwebui/types/api/v1/pipeline_get_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/pipeline_get_response.py">object</a></code>
- <code title="post /api/v1/pipelines/upload">client.api.v1.pipelines.<a href="./src/pyopenwebui/resources/api/v1/pipelines/pipelines.py">upload</a>(\*\*<a href="src/pyopenwebui/types/api/v1/pipeline_upload_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/pipeline_upload_response.py">object</a></code>

#### Valves

Types:

```python
from pyopenwebui.types.api.v1.pipelines import (
    ValveUpdateResponse,
    ValveGetResponse,
    ValveGetSpecResponse,
)
```

Methods:

- <code title="post /api/v1/pipelines/{pipeline_id}/valves/update">client.api.v1.pipelines.valves.<a href="./src/pyopenwebui/resources/api/v1/pipelines/valves.py">update</a>(pipeline_id, \*\*<a href="src/pyopenwebui/types/api/v1/pipelines/valve_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/pipelines/valve_update_response.py">object</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/valves">client.api.v1.pipelines.valves.<a href="./src/pyopenwebui/resources/api/v1/pipelines/valves.py">get</a>(pipeline_id, \*\*<a href="src/pyopenwebui/types/api/v1/pipelines/valve_get_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/pipelines/valve_get_response.py">object</a></code>
- <code title="get /api/v1/pipelines/{pipeline_id}/valves/spec">client.api.v1.pipelines.valves.<a href="./src/pyopenwebui/resources/api/v1/pipelines/valves.py">get_spec</a>(pipeline_id, \*\*<a href="src/pyopenwebui/types/api/v1/pipelines/valve_get_spec_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/pipelines/valve_get_spec_response.py">object</a></code>

### Tasks

#### Config

Types:

```python
from pyopenwebui.types.api.v1.tasks import ConfigUpdateResponse, ConfigGetResponse
```

Methods:

- <code title="post /api/v1/tasks/config/update">client.api.v1.tasks.config.<a href="./src/pyopenwebui/resources/api/v1/tasks/config.py">update</a>(\*\*<a href="src/pyopenwebui/types/api/v1/tasks/config_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/tasks/config_update_response.py">object</a></code>
- <code title="get /api/v1/tasks/config">client.api.v1.tasks.config.<a href="./src/pyopenwebui/resources/api/v1/tasks/config.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/tasks/config_get_response.py">object</a></code>

#### Title

Types:

```python
from pyopenwebui.types.api.v1.tasks import TitleGenerateResponse
```

Methods:

- <code title="post /api/v1/tasks/title/completions">client.api.v1.tasks.title.<a href="./src/pyopenwebui/resources/api/v1/tasks/title.py">generate</a>(\*\*<a href="src/pyopenwebui/types/api/v1/tasks/title_generate_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/tasks/title_generate_response.py">object</a></code>

#### Tags

Types:

```python
from pyopenwebui.types.api.v1.tasks import TagGenerateResponse
```

Methods:

- <code title="post /api/v1/tasks/tags/completions">client.api.v1.tasks.tags.<a href="./src/pyopenwebui/resources/api/v1/tasks/tags.py">generate</a>(\*\*<a href="src/pyopenwebui/types/api/v1/tasks/tag_generate_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/tasks/tag_generate_response.py">object</a></code>

#### ImagePrompt

Types:

```python
from pyopenwebui.types.api.v1.tasks import ImagePromptGenerateResponse
```

Methods:

- <code title="post /api/v1/tasks/image_prompt/completions">client.api.v1.tasks.image_prompt.<a href="./src/pyopenwebui/resources/api/v1/tasks/image_prompt.py">generate</a>(\*\*<a href="src/pyopenwebui/types/api/v1/tasks/image_prompt_generate_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/tasks/image_prompt_generate_response.py">object</a></code>

#### Queries

Types:

```python
from pyopenwebui.types.api.v1.tasks import QueryGenerateResponse
```

Methods:

- <code title="post /api/v1/tasks/queries/completions">client.api.v1.tasks.queries.<a href="./src/pyopenwebui/resources/api/v1/tasks/queries.py">generate</a>(\*\*<a href="src/pyopenwebui/types/api/v1/tasks/query_generate_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/tasks/query_generate_response.py">object</a></code>

#### Auto

Types:

```python
from pyopenwebui.types.api.v1.tasks import AutoGenerateResponse
```

Methods:

- <code title="post /api/v1/tasks/auto/completions">client.api.v1.tasks.auto.<a href="./src/pyopenwebui/resources/api/v1/tasks/auto.py">generate</a>(\*\*<a href="src/pyopenwebui/types/api/v1/tasks/auto_generate_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/tasks/auto_generate_response.py">object</a></code>

#### Emoji

Types:

```python
from pyopenwebui.types.api.v1.tasks import EmojiGenerateResponse
```

Methods:

- <code title="post /api/v1/tasks/emoji/completions">client.api.v1.tasks.emoji.<a href="./src/pyopenwebui/resources/api/v1/tasks/emoji.py">generate</a>(\*\*<a href="src/pyopenwebui/types/api/v1/tasks/emoji_generate_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/tasks/emoji_generate_response.py">object</a></code>

#### Moa

Types:

```python
from pyopenwebui.types.api.v1.tasks import MoaGenerateResponse
```

Methods:

- <code title="post /api/v1/tasks/moa/completions">client.api.v1.tasks.moa.<a href="./src/pyopenwebui/resources/api/v1/tasks/moa.py">generate</a>(\*\*<a href="src/pyopenwebui/types/api/v1/tasks/moa_generate_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/tasks/moa_generate_response.py">object</a></code>

### Images

Types:

```python
from pyopenwebui.types.api.v1 import ImageGenerateResponse, ImageGetModelsResponse
```

Methods:

- <code title="post /api/v1/images/generations">client.api.v1.images.<a href="./src/pyopenwebui/resources/api/v1/images/images.py">generate</a>(\*\*<a href="src/pyopenwebui/types/api/v1/image_generate_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/image_generate_response.py">object</a></code>
- <code title="get /api/v1/images/models">client.api.v1.images.<a href="./src/pyopenwebui/resources/api/v1/images/images.py">get_models</a>() -> <a href="./src/pyopenwebui/types/api/v1/image_get_models_response.py">object</a></code>

#### Config

Types:

```python
from pyopenwebui.types.api.v1.images import ConfigUpdateResponse, ConfigGetResponse
```

Methods:

- <code title="post /api/v1/images/config/update">client.api.v1.images.config.<a href="./src/pyopenwebui/resources/api/v1/images/config/config.py">update</a>(\*\*<a href="src/pyopenwebui/types/api/v1/images/config_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/images/config_update_response.py">object</a></code>
- <code title="get /api/v1/images/config">client.api.v1.images.config.<a href="./src/pyopenwebui/resources/api/v1/images/config/config.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/images/config_get_response.py">object</a></code>

##### URL

Types:

```python
from pyopenwebui.types.api.v1.images.config import URLVerifyResponse
```

Methods:

- <code title="get /api/v1/images/config/url/verify">client.api.v1.images.config.url.<a href="./src/pyopenwebui/resources/api/v1/images/config/url.py">verify</a>() -> <a href="./src/pyopenwebui/types/api/v1/images/config/url_verify_response.py">object</a></code>

#### Image

##### Config

Types:

```python
from pyopenwebui.types.api.v1.images.image import ConfigUpdateResponse, ConfigGetResponse
```

Methods:

- <code title="post /api/v1/images/image/config/update">client.api.v1.images.image.config.<a href="./src/pyopenwebui/resources/api/v1/images/image/config.py">update</a>(\*\*<a href="src/pyopenwebui/types/api/v1/images/image/config_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/images/image/config_update_response.py">object</a></code>
- <code title="get /api/v1/images/image/config">client.api.v1.images.image.config.<a href="./src/pyopenwebui/resources/api/v1/images/image/config.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/images/image/config_get_response.py">object</a></code>

### Audio

Types:

```python
from pyopenwebui.types.api.v1 import (
    AudioGetModelsResponse,
    AudioGetVoicesResponse,
    AudioSpeechResponse,
    AudioTranscribeResponse,
)
```

Methods:

- <code title="get /api/v1/audio/models">client.api.v1.audio.<a href="./src/pyopenwebui/resources/api/v1/audio/audio.py">get_models</a>() -> <a href="./src/pyopenwebui/types/api/v1/audio_get_models_response.py">object</a></code>
- <code title="get /api/v1/audio/voices">client.api.v1.audio.<a href="./src/pyopenwebui/resources/api/v1/audio/audio.py">get_voices</a>() -> <a href="./src/pyopenwebui/types/api/v1/audio_get_voices_response.py">object</a></code>
- <code title="post /api/v1/audio/speech">client.api.v1.audio.<a href="./src/pyopenwebui/resources/api/v1/audio/audio.py">speech</a>() -> <a href="./src/pyopenwebui/types/api/v1/audio_speech_response.py">object</a></code>
- <code title="post /api/v1/audio/transcriptions">client.api.v1.audio.<a href="./src/pyopenwebui/resources/api/v1/audio/audio.py">transcribe</a>(\*\*<a href="src/pyopenwebui/types/api/v1/audio_transcribe_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/audio_transcribe_response.py">object</a></code>

#### Config

Types:

```python
from pyopenwebui.types.api.v1.audio import ConfigUpdateResponse, ConfigGetResponse
```

Methods:

- <code title="post /api/v1/audio/config/update">client.api.v1.audio.config.<a href="./src/pyopenwebui/resources/api/v1/audio/config.py">update</a>(\*\*<a href="src/pyopenwebui/types/api/v1/audio/config_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/audio/config_update_response.py">object</a></code>
- <code title="get /api/v1/audio/config">client.api.v1.audio.config.<a href="./src/pyopenwebui/resources/api/v1/audio/config.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/audio/config_get_response.py">object</a></code>

### Retrieval

Types:

```python
from pyopenwebui.types.api.v1 import (
    RetrievalDeleteEntriesResponse,
    RetrievalGetEmbeddingsResponse,
    RetrievalGetStatusResponse,
    RetrievalGetTemplateResponse,
)
```

Methods:

- <code title="post /api/v1/retrieval/delete">client.api.v1.retrieval.<a href="./src/pyopenwebui/resources/api/v1/retrieval/retrieval.py">delete_entries</a>(\*\*<a href="src/pyopenwebui/types/api/v1/retrieval_delete_entries_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/retrieval_delete_entries_response.py">object</a></code>
- <code title="get /api/v1/retrieval/ef/{text}">client.api.v1.retrieval.<a href="./src/pyopenwebui/resources/api/v1/retrieval/retrieval.py">get_embeddings</a>(text) -> <a href="./src/pyopenwebui/types/api/v1/retrieval_get_embeddings_response.py">object</a></code>
- <code title="get /api/v1/retrieval/">client.api.v1.retrieval.<a href="./src/pyopenwebui/resources/api/v1/retrieval/retrieval.py">get_status</a>() -> <a href="./src/pyopenwebui/types/api/v1/retrieval_get_status_response.py">object</a></code>
- <code title="get /api/v1/retrieval/template">client.api.v1.retrieval.<a href="./src/pyopenwebui/resources/api/v1/retrieval/retrieval.py">get_template</a>() -> <a href="./src/pyopenwebui/types/api/v1/retrieval_get_template_response.py">object</a></code>

#### Embedding

Types:

```python
from pyopenwebui.types.api.v1.retrieval import (
    EmbeddingGetConfigResponse,
    EmbeddingUpdateConfigResponse,
)
```

Methods:

- <code title="get /api/v1/retrieval/embedding">client.api.v1.retrieval.embedding.<a href="./src/pyopenwebui/resources/api/v1/retrieval/embedding.py">get_config</a>() -> <a href="./src/pyopenwebui/types/api/v1/retrieval/embedding_get_config_response.py">object</a></code>
- <code title="post /api/v1/retrieval/embedding/update">client.api.v1.retrieval.embedding.<a href="./src/pyopenwebui/resources/api/v1/retrieval/embedding.py">update_config</a>(\*\*<a href="src/pyopenwebui/types/api/v1/retrieval/embedding_update_config_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/retrieval/embedding_update_config_response.py">object</a></code>

#### Reranking

Types:

```python
from pyopenwebui.types.api.v1.retrieval import (
    RerankingGetConfigResponse,
    RerankingUpdateConfigResponse,
)
```

Methods:

- <code title="get /api/v1/retrieval/reranking">client.api.v1.retrieval.reranking.<a href="./src/pyopenwebui/resources/api/v1/retrieval/reranking.py">get_config</a>() -> <a href="./src/pyopenwebui/types/api/v1/retrieval/reranking_get_config_response.py">object</a></code>
- <code title="post /api/v1/retrieval/reranking/update">client.api.v1.retrieval.reranking.<a href="./src/pyopenwebui/resources/api/v1/retrieval/reranking.py">update_config</a>(\*\*<a href="src/pyopenwebui/types/api/v1/retrieval/reranking_update_config_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/retrieval/reranking_update_config_response.py">object</a></code>

#### Config

Types:

```python
from pyopenwebui.types.api.v1.retrieval import ConfigUpdateResponse, ConfigGetResponse
```

Methods:

- <code title="post /api/v1/retrieval/config/update">client.api.v1.retrieval.config.<a href="./src/pyopenwebui/resources/api/v1/retrieval/config.py">update</a>(\*\*<a href="src/pyopenwebui/types/api/v1/retrieval/config_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/retrieval/config_update_response.py">object</a></code>
- <code title="get /api/v1/retrieval/config">client.api.v1.retrieval.config.<a href="./src/pyopenwebui/resources/api/v1/retrieval/config.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/retrieval/config_get_response.py">object</a></code>

#### Query

Types:

```python
from pyopenwebui.types.api.v1.retrieval import QueryCollectionResponse, QueryDocResponse
```

Methods:

- <code title="post /api/v1/retrieval/query/collection">client.api.v1.retrieval.query.<a href="./src/pyopenwebui/resources/api/v1/retrieval/query/query.py">collection</a>(\*\*<a href="src/pyopenwebui/types/api/v1/retrieval/query_collection_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/retrieval/query_collection_response.py">object</a></code>
- <code title="post /api/v1/retrieval/query/doc">client.api.v1.retrieval.query.<a href="./src/pyopenwebui/resources/api/v1/retrieval/query/query.py">doc</a>(\*\*<a href="src/pyopenwebui/types/api/v1/retrieval/query_doc_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/retrieval/query_doc_response.py">object</a></code>

##### Settings

Types:

```python
from pyopenwebui.types.api.v1.retrieval.query import SettingUpdateResponse, SettingGetResponse
```

Methods:

- <code title="post /api/v1/retrieval/query/settings/update">client.api.v1.retrieval.query.settings.<a href="./src/pyopenwebui/resources/api/v1/retrieval/query/settings.py">update</a>(\*\*<a href="src/pyopenwebui/types/api/v1/retrieval/query/setting_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/retrieval/query/setting_update_response.py">object</a></code>
- <code title="get /api/v1/retrieval/query/settings">client.api.v1.retrieval.query.settings.<a href="./src/pyopenwebui/resources/api/v1/retrieval/query/settings.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/retrieval/query/setting_get_response.py">object</a></code>

#### Process

Types:

```python
from pyopenwebui.types.api.v1.retrieval import (
    ProcessFileResponse,
    ProcessTextResponse,
    ProcessYoutubeResponse,
)
```

Methods:

- <code title="post /api/v1/retrieval/process/file">client.api.v1.retrieval.process.<a href="./src/pyopenwebui/resources/api/v1/retrieval/process/process.py">file</a>(\*\*<a href="src/pyopenwebui/types/api/v1/retrieval/process_file_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/retrieval/process_file_response.py">object</a></code>
- <code title="post /api/v1/retrieval/process/text">client.api.v1.retrieval.process.<a href="./src/pyopenwebui/resources/api/v1/retrieval/process/process.py">text</a>(\*\*<a href="src/pyopenwebui/types/api/v1/retrieval/process_text_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/retrieval/process_text_response.py">object</a></code>
- <code title="post /api/v1/retrieval/process/youtube">client.api.v1.retrieval.process.<a href="./src/pyopenwebui/resources/api/v1/retrieval/process/process.py">youtube</a>(\*\*<a href="src/pyopenwebui/types/api/v1/retrieval/process_youtube_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/retrieval/process_youtube_response.py">object</a></code>

##### Web

Types:

```python
from pyopenwebui.types.api.v1.retrieval.process import WebSearchResponse
```

Methods:

- <code title="post /api/v1/retrieval/process/web/search">client.api.v1.retrieval.process.web.<a href="./src/pyopenwebui/resources/api/v1/retrieval/process/web.py">search</a>(\*\*<a href="src/pyopenwebui/types/api/v1/retrieval/process/web_search_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/retrieval/process/web_search_response.py">object</a></code>

##### Files

Types:

```python
from pyopenwebui.types.api.v1.retrieval.process import FileBatchResponse
```

Methods:

- <code title="post /api/v1/retrieval/process/files/batch">client.api.v1.retrieval.process.files.<a href="./src/pyopenwebui/resources/api/v1/retrieval/process/files.py">batch</a>(\*\*<a href="src/pyopenwebui/types/api/v1/retrieval/process/file_batch_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/retrieval/process/file_batch_response.py">FileBatchResponse</a></code>

#### Reset

Types:

```python
from pyopenwebui.types.api.v1.retrieval import ResetDBResponse, ResetUploadsResponse
```

Methods:

- <code title="post /api/v1/retrieval/reset/db">client.api.v1.retrieval.reset.<a href="./src/pyopenwebui/resources/api/v1/retrieval/reset.py">db</a>() -> <a href="./src/pyopenwebui/types/api/v1/retrieval/reset_db_response.py">object</a></code>
- <code title="post /api/v1/retrieval/reset/uploads">client.api.v1.retrieval.reset.<a href="./src/pyopenwebui/resources/api/v1/retrieval/reset.py">uploads</a>() -> <a href="./src/pyopenwebui/types/api/v1/retrieval/reset_uploads_response.py">ResetUploadsResponse</a></code>

### Configs

Types:

```python
from pyopenwebui.types.api.v1 import (
    ConfigExportResponse,
    ConfigImportResponse,
    ConfigSetSuggestionsResponse,
)
```

Methods:

- <code title="get /api/v1/configs/export">client.api.v1.configs.<a href="./src/pyopenwebui/resources/api/v1/configs/configs.py">export</a>() -> <a href="./src/pyopenwebui/types/api/v1/config_export_response.py">object</a></code>
- <code title="post /api/v1/configs/import">client.api.v1.configs.<a href="./src/pyopenwebui/resources/api/v1/configs/configs.py">import\_</a>(\*\*<a href="src/pyopenwebui/types/api/v1/config_import_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/config_import_response.py">object</a></code>
- <code title="post /api/v1/configs/suggestions">client.api.v1.configs.<a href="./src/pyopenwebui/resources/api/v1/configs/configs.py">set_suggestions</a>(\*\*<a href="src/pyopenwebui/types/api/v1/config_set_suggestions_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/config_set_suggestions_response.py">ConfigSetSuggestionsResponse</a></code>

#### DirectConnections

Types:

```python
from pyopenwebui.types.api.v1.configs import (
    DirectConnectionGetResponse,
    DirectConnectionSetResponse,
)
```

Methods:

- <code title="get /api/v1/configs/direct_connections">client.api.v1.configs.direct_connections.<a href="./src/pyopenwebui/resources/api/v1/configs/direct_connections.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/configs/direct_connection_get_response.py">DirectConnectionGetResponse</a></code>
- <code title="post /api/v1/configs/direct_connections">client.api.v1.configs.direct_connections.<a href="./src/pyopenwebui/resources/api/v1/configs/direct_connections.py">set</a>(\*\*<a href="src/pyopenwebui/types/api/v1/configs/direct_connection_set_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/configs/direct_connection_set_response.py">DirectConnectionSetResponse</a></code>

#### CodeExecution

Types:

```python
from pyopenwebui.types.api.v1.configs import CodeExecutionGetResponse, CodeExecutionSetResponse
```

Methods:

- <code title="get /api/v1/configs/code_execution">client.api.v1.configs.code_execution.<a href="./src/pyopenwebui/resources/api/v1/configs/code_execution.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/configs/code_execution_get_response.py">CodeExecutionGetResponse</a></code>
- <code title="post /api/v1/configs/code_execution">client.api.v1.configs.code_execution.<a href="./src/pyopenwebui/resources/api/v1/configs/code_execution.py">set</a>(\*\*<a href="src/pyopenwebui/types/api/v1/configs/code_execution_set_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/configs/code_execution_set_response.py">CodeExecutionSetResponse</a></code>

#### Models

Types:

```python
from pyopenwebui.types.api.v1.configs import ModelGetResponse, ModelSetResponse
```

Methods:

- <code title="get /api/v1/configs/models">client.api.v1.configs.models.<a href="./src/pyopenwebui/resources/api/v1/configs/models.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/configs/model_get_response.py">ModelGetResponse</a></code>
- <code title="post /api/v1/configs/models">client.api.v1.configs.models.<a href="./src/pyopenwebui/resources/api/v1/configs/models.py">set</a>(\*\*<a href="src/pyopenwebui/types/api/v1/configs/model_set_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/configs/model_set_response.py">ModelSetResponse</a></code>

#### Banners

Types:

```python
from pyopenwebui.types.api.v1.configs import BannerGetResponse, BannerSetResponse
```

Methods:

- <code title="get /api/v1/configs/banners">client.api.v1.configs.banners.<a href="./src/pyopenwebui/resources/api/v1/configs/banners.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/configs/banner_get_response.py">BannerGetResponse</a></code>
- <code title="post /api/v1/configs/banners">client.api.v1.configs.banners.<a href="./src/pyopenwebui/resources/api/v1/configs/banners.py">set</a>(\*\*<a href="src/pyopenwebui/types/api/v1/configs/banner_set_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/configs/banner_set_response.py">BannerSetResponse</a></code>

### Auths

Types:

```python
from pyopenwebui.types.api.v1 import (
    AuthGetSessionUserResponse,
    AuthLdapAuthResponse,
    AuthSigninResponse,
    AuthSignoutResponse,
    AuthSignupResponse,
)
```

Methods:

- <code title="post /api/v1/auths/add">client.api.v1.auths.<a href="./src/pyopenwebui/resources/api/v1/auths/auths.py">add_user</a>(\*\*<a href="src/pyopenwebui/types/api/v1/auth_add_user_params.py">params</a>) -> <a href="./src/pyopenwebui/types/signin_response.py">SigninResponse</a></code>
- <code title="get /api/v1/auths/">client.api.v1.auths.<a href="./src/pyopenwebui/resources/api/v1/auths/auths.py">get_session_user</a>() -> <a href="./src/pyopenwebui/types/api/v1/auth_get_session_user_response.py">AuthGetSessionUserResponse</a></code>
- <code title="post /api/v1/auths/ldap">client.api.v1.auths.<a href="./src/pyopenwebui/resources/api/v1/auths/auths.py">ldap_auth</a>(\*\*<a href="src/pyopenwebui/types/api/v1/auth_ldap_auth_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/auth_ldap_auth_response.py">AuthLdapAuthResponse</a></code>
- <code title="post /api/v1/auths/signin">client.api.v1.auths.<a href="./src/pyopenwebui/resources/api/v1/auths/auths.py">signin</a>(\*\*<a href="src/pyopenwebui/types/api/v1/auth_signin_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/auth_signin_response.py">AuthSigninResponse</a></code>
- <code title="get /api/v1/auths/signout">client.api.v1.auths.<a href="./src/pyopenwebui/resources/api/v1/auths/auths.py">signout</a>() -> <a href="./src/pyopenwebui/types/api/v1/auth_signout_response.py">object</a></code>
- <code title="post /api/v1/auths/signup">client.api.v1.auths.<a href="./src/pyopenwebui/resources/api/v1/auths/auths.py">signup</a>(\*\*<a href="src/pyopenwebui/types/api/v1/auth_signup_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/auth_signup_response.py">AuthSignupResponse</a></code>

#### Update

Types:

```python
from pyopenwebui.types.api.v1.auths import UpdatePasswordResponse, UpdateProfileResponse
```

Methods:

- <code title="post /api/v1/auths/update/password">client.api.v1.auths.update.<a href="./src/pyopenwebui/resources/api/v1/auths/update.py">password</a>(\*\*<a href="src/pyopenwebui/types/api/v1/auths/update_password_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/auths/update_password_response.py">UpdatePasswordResponse</a></code>
- <code title="post /api/v1/auths/update/profile">client.api.v1.auths.update.<a href="./src/pyopenwebui/resources/api/v1/auths/update.py">profile</a>(\*\*<a href="src/pyopenwebui/types/api/v1/auths/update_profile_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/auths/update_profile_response.py">UpdateProfileResponse</a></code>

#### Admin

Types:

```python
from pyopenwebui.types.api.v1.auths import AdminGetDetailsResponse
```

Methods:

- <code title="get /api/v1/auths/admin/details">client.api.v1.auths.admin.<a href="./src/pyopenwebui/resources/api/v1/auths/admin/admin.py">get_details</a>() -> <a href="./src/pyopenwebui/types/api/v1/auths/admin_get_details_response.py">object</a></code>

##### Config

Types:

```python
from pyopenwebui.types.api.v1.auths.admin import ConfigUpdateResponse, ConfigGetResponse
```

Methods:

- <code title="post /api/v1/auths/admin/config">client.api.v1.auths.admin.config.<a href="./src/pyopenwebui/resources/api/v1/auths/admin/config/config.py">update</a>(\*\*<a href="src/pyopenwebui/types/api/v1/auths/admin/config_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/auths/admin/config_update_response.py">object</a></code>
- <code title="get /api/v1/auths/admin/config">client.api.v1.auths.admin.config.<a href="./src/pyopenwebui/resources/api/v1/auths/admin/config/config.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/auths/admin/config_get_response.py">object</a></code>

###### Ldap

Types:

```python
from pyopenwebui.types.api.v1.auths.admin.config import LdapUpdateResponse, LdapGetResponse
```

Methods:

- <code title="post /api/v1/auths/admin/config/ldap">client.api.v1.auths.admin.config.ldap.<a href="./src/pyopenwebui/resources/api/v1/auths/admin/config/ldap/ldap.py">update</a>(\*\*<a href="src/pyopenwebui/types/api/v1/auths/admin/config/ldap_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/auths/admin/config/ldap_update_response.py">object</a></code>
- <code title="get /api/v1/auths/admin/config/ldap">client.api.v1.auths.admin.config.ldap.<a href="./src/pyopenwebui/resources/api/v1/auths/admin/config/ldap/ldap.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/auths/admin/config/ldap_get_response.py">object</a></code>
  ####### Server
  Types:

```python
from pyopenwebui.types.api.v1.auths.admin.config.ldap import ServerUpdateResponse, ServerGetResponse
```

Methods:

- <code title="post /api/v1/auths/admin/config/ldap/server">client.api.v1.auths.admin.config.ldap.server.<a href="./src/pyopenwebui/resources/api/v1/auths/admin/config/ldap/server.py">update</a>(\*\*<a href="src/pyopenwebui/types/api/v1/auths/admin/config/ldap/server_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/auths/admin/config/ldap/server_update_response.py">object</a></code>
- <code title="get /api/v1/auths/admin/config/ldap/server">client.api.v1.auths.admin.config.ldap.server.<a href="./src/pyopenwebui/resources/api/v1/auths/admin/config/ldap/server.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/auths/admin/config/ldap/server_get_response.py">ServerGetResponse</a></code>

#### APIKey

Types:

```python
from pyopenwebui.types.api.v1.auths import APIKeyDeleteResponse
```

Methods:

- <code title="delete /api/v1/auths/api_key">client.api.v1.auths.api_key.<a href="./src/pyopenwebui/resources/api/v1/auths/api_key.py">delete</a>() -> <a href="./src/pyopenwebui/types/api/v1/auths/api_key_delete_response.py">APIKeyDeleteResponse</a></code>
- <code title="post /api/v1/auths/api_key">client.api.v1.auths.api_key.<a href="./src/pyopenwebui/resources/api/v1/auths/api_key.py">generate</a>() -> <a href="./src/pyopenwebui/types/api_key.py">APIKey</a></code>
- <code title="get /api/v1/auths/api_key">client.api.v1.auths.api_key.<a href="./src/pyopenwebui/resources/api/v1/auths/api_key.py">get</a>() -> <a href="./src/pyopenwebui/types/api_key.py">APIKey</a></code>

### Users

Types:

```python
from pyopenwebui.types.api.v1 import (
    UserDeleteByIDResponse,
    UserGetResponse,
    UserGetByIDResponse,
    UserGetGroupsResponse,
    UserGetPermissionsResponse,
)
```

Methods:

- <code title="delete /api/v1/users/{user_id}">client.api.v1.users.<a href="./src/pyopenwebui/resources/api/v1/users/users.py">delete_by_id</a>(user_id) -> <a href="./src/pyopenwebui/types/api/v1/user_delete_by_id_response.py">UserDeleteByIDResponse</a></code>
- <code title="get /api/v1/users/">client.api.v1.users.<a href="./src/pyopenwebui/resources/api/v1/users/users.py">get</a>(\*\*<a href="src/pyopenwebui/types/api/v1/user_get_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/user_get_response.py">UserGetResponse</a></code>
- <code title="get /api/v1/users/{user_id}">client.api.v1.users.<a href="./src/pyopenwebui/resources/api/v1/users/users.py">get_by_id</a>(user_id) -> <a href="./src/pyopenwebui/types/api/v1/user_get_by_id_response.py">UserGetByIDResponse</a></code>
- <code title="get /api/v1/users/groups">client.api.v1.users.<a href="./src/pyopenwebui/resources/api/v1/users/users.py">get_groups</a>() -> <a href="./src/pyopenwebui/types/api/v1/user_get_groups_response.py">object</a></code>
- <code title="get /api/v1/users/permissions">client.api.v1.users.<a href="./src/pyopenwebui/resources/api/v1/users/users.py">get_permissions</a>() -> <a href="./src/pyopenwebui/types/api/v1/user_get_permissions_response.py">object</a></code>

#### Default

##### Permissions

Types:

```python
from pyopenwebui.types.api.v1.users.default import PermissionUpdateResponse, PermissionGetResponse
```

Methods:

- <code title="post /api/v1/users/default/permissions">client.api.v1.users.default.permissions.<a href="./src/pyopenwebui/resources/api/v1/users/default/permissions.py">update</a>(\*\*<a href="src/pyopenwebui/types/api/v1/users/default/permission_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/users/default/permission_update_response.py">object</a></code>
- <code title="get /api/v1/users/default/permissions">client.api.v1.users.default.permissions.<a href="./src/pyopenwebui/resources/api/v1/users/default/permissions.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/users/default/permission_get_response.py">PermissionGetResponse</a></code>

#### Update

Methods:

- <code title="post /api/v1/users/update/role">client.api.v1.users.update.<a href="./src/pyopenwebui/resources/api/v1/users/update.py">role</a>(\*\*<a href="src/pyopenwebui/types/api/v1/users/update_role_params.py">params</a>) -> <a href="./src/pyopenwebui/types/user_model.py">Optional[UserModel]</a></code>

#### User

##### Settings

Methods:

- <code title="post /api/v1/users/user/settings/update">client.api.v1.users.user.settings.<a href="./src/pyopenwebui/resources/api/v1/users/user/settings.py">update</a>(\*\*<a href="src/pyopenwebui/types/api/v1/users/user/setting_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/users/user_settings.py">UserSettings</a></code>
- <code title="get /api/v1/users/user/settings">client.api.v1.users.user.settings.<a href="./src/pyopenwebui/resources/api/v1/users/user/settings.py">get</a>() -> <a href="./src/pyopenwebui/types/users/user_settings.py">Optional[UserSettings]</a></code>

##### Info

Types:

```python
from pyopenwebui.types.api.v1.users.user import InfoUpdateResponse, InfoGetResponse
```

Methods:

- <code title="post /api/v1/users/user/info/update">client.api.v1.users.user.info.<a href="./src/pyopenwebui/resources/api/v1/users/user/info.py">update</a>(\*\*<a href="src/pyopenwebui/types/api/v1/users/user/info_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/users/user/info_update_response.py">object</a></code>
- <code title="get /api/v1/users/user/info">client.api.v1.users.user.info.<a href="./src/pyopenwebui/resources/api/v1/users/user/info.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/users/user/info_get_response.py">object</a></code>

### Channels

Types:

```python
from pyopenwebui.types.api.v1 import (
    ChannelCreateResponse,
    ChannelDeleteByIDResponse,
    ChannelGetResponse,
    ChannelGetByIDResponse,
    ChannelUpdateByIDResponse,
)
```

Methods:

- <code title="post /api/v1/channels/create">client.api.v1.channels.<a href="./src/pyopenwebui/resources/api/v1/channels/channels.py">create</a>(\*\*<a href="src/pyopenwebui/types/api/v1/channel_create_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/channel_create_response.py">Optional[ChannelCreateResponse]</a></code>
- <code title="delete /api/v1/channels/{id}/delete">client.api.v1.channels.<a href="./src/pyopenwebui/resources/api/v1/channels/channels.py">delete_by_id</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/channel_delete_by_id_response.py">ChannelDeleteByIDResponse</a></code>
- <code title="get /api/v1/channels/">client.api.v1.channels.<a href="./src/pyopenwebui/resources/api/v1/channels/channels.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/channel_get_response.py">ChannelGetResponse</a></code>
- <code title="get /api/v1/channels/{id}">client.api.v1.channels.<a href="./src/pyopenwebui/resources/api/v1/channels/channels.py">get_by_id</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/channel_get_by_id_response.py">Optional[ChannelGetByIDResponse]</a></code>
- <code title="post /api/v1/channels/{id}/update">client.api.v1.channels.<a href="./src/pyopenwebui/resources/api/v1/channels/channels.py">update_by_id</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/channel_update_by_id_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/channel_update_by_id_response.py">Optional[ChannelUpdateByIDResponse]</a></code>

#### Messages

Types:

```python
from pyopenwebui.types.api.v1.channels import (
    MessageDeleteByIDResponse,
    MessageGetResponse,
    MessageGetByIDResponse,
    MessageGetThreadResponse,
    MessagePostResponse,
    MessageUpdateByIDResponse,
)
```

Methods:

- <code title="delete /api/v1/channels/{id}/messages/{message_id}/delete">client.api.v1.channels.messages.<a href="./src/pyopenwebui/resources/api/v1/channels/messages/messages.py">delete_by_id</a>(message_id, \*, id) -> <a href="./src/pyopenwebui/types/api/v1/channels/message_delete_by_id_response.py">MessageDeleteByIDResponse</a></code>
- <code title="get /api/v1/channels/{id}/messages">client.api.v1.channels.messages.<a href="./src/pyopenwebui/resources/api/v1/channels/messages/messages.py">get</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/channels/message_get_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/channels/message_get_response.py">MessageGetResponse</a></code>
- <code title="get /api/v1/channels/{id}/messages/{message_id}">client.api.v1.channels.messages.<a href="./src/pyopenwebui/resources/api/v1/channels/messages/messages.py">get_by_id</a>(message_id, \*, id) -> <a href="./src/pyopenwebui/types/api/v1/channels/message_get_by_id_response.py">Optional[MessageGetByIDResponse]</a></code>
- <code title="get /api/v1/channels/{id}/messages/{message_id}/thread">client.api.v1.channels.messages.<a href="./src/pyopenwebui/resources/api/v1/channels/messages/messages.py">get_thread</a>(message_id, \*, id, \*\*<a href="src/pyopenwebui/types/api/v1/channels/message_get_thread_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/channels/message_get_thread_response.py">MessageGetThreadResponse</a></code>
- <code title="post /api/v1/channels/{id}/messages/post">client.api.v1.channels.messages.<a href="./src/pyopenwebui/resources/api/v1/channels/messages/messages.py">post</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/channels/message_post_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/channels/message_post_response.py">Optional[MessagePostResponse]</a></code>
- <code title="post /api/v1/channels/{id}/messages/{message_id}/update">client.api.v1.channels.messages.<a href="./src/pyopenwebui/resources/api/v1/channels/messages/messages.py">update_by_id</a>(message_id, \*, id, \*\*<a href="src/pyopenwebui/types/api/v1/channels/message_update_by_id_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/channels/message_update_by_id_response.py">Optional[MessageUpdateByIDResponse]</a></code>

##### Reactions

Types:

```python
from pyopenwebui.types.api.v1.channels.messages import ReactionAddResponse, ReactionRemoveResponse
```

Methods:

- <code title="post /api/v1/channels/{id}/messages/{message_id}/reactions/add">client.api.v1.channels.messages.reactions.<a href="./src/pyopenwebui/resources/api/v1/channels/messages/reactions.py">add</a>(message_id, \*, id, \*\*<a href="src/pyopenwebui/types/api/v1/channels/messages/reaction_add_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/channels/messages/reaction_add_response.py">ReactionAddResponse</a></code>
- <code title="post /api/v1/channels/{id}/messages/{message_id}/reactions/remove">client.api.v1.channels.messages.reactions.<a href="./src/pyopenwebui/resources/api/v1/channels/messages/reactions.py">remove</a>(message_id, \*, id, \*\*<a href="src/pyopenwebui/types/api/v1/channels/messages/reaction_remove_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/channels/messages/reaction_remove_response.py">ReactionRemoveResponse</a></code>

### Chats

Types:

```python
from pyopenwebui.types.api.v1 import (
    ChatListResponse,
    ChatDeleteAllResponse,
    ChatDeleteByIDResponse,
    ChatGetResponse,
    ChatGetArchivedListResponse,
    ChatSearchResponse,
)
```

Methods:

- <code title="post /api/v1/chats/new">client.api.v1.chats.<a href="./src/pyopenwebui/resources/api/v1/chats/chats.py">create</a>(\*\*<a href="src/pyopenwebui/types/api/v1/chat_create_params.py">params</a>) -> <a href="./src/pyopenwebui/types/chat_response.py">Optional[ChatResponse]</a></code>
- <code title="get /api/v1/chats/list/user/{user_id}">client.api.v1.chats.<a href="./src/pyopenwebui/resources/api/v1/chats/chats.py">list</a>(user_id, \*\*<a href="src/pyopenwebui/types/api/v1/chat_list_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/chat_list_response.py">ChatListResponse</a></code>
- <code title="post /api/v1/chats/{id}/archive">client.api.v1.chats.<a href="./src/pyopenwebui/resources/api/v1/chats/chats.py">archive</a>(id) -> <a href="./src/pyopenwebui/types/chat_response.py">Optional[ChatResponse]</a></code>
- <code title="delete /api/v1/chats/">client.api.v1.chats.<a href="./src/pyopenwebui/resources/api/v1/chats/chats.py">delete_all</a>() -> <a href="./src/pyopenwebui/types/api/v1/chat_delete_all_response.py">ChatDeleteAllResponse</a></code>
- <code title="delete /api/v1/chats/{id}">client.api.v1.chats.<a href="./src/pyopenwebui/resources/api/v1/chats/chats.py">delete_by_id</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/chat_delete_by_id_response.py">ChatDeleteByIDResponse</a></code>
- <code title="get /api/v1/chats/">client.api.v1.chats.<a href="./src/pyopenwebui/resources/api/v1/chats/chats.py">get</a>(\*\*<a href="src/pyopenwebui/types/api/v1/chat_get_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/chat_get_response.py">ChatGetResponse</a></code>
- <code title="get /api/v1/chats/archived">client.api.v1.chats.<a href="./src/pyopenwebui/resources/api/v1/chats/chats.py">get_archived_list</a>(\*\*<a href="src/pyopenwebui/types/api/v1/chat_get_archived_list_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/chat_get_archived_list_response.py">ChatGetArchivedListResponse</a></code>
- <code title="get /api/v1/chats/{id}">client.api.v1.chats.<a href="./src/pyopenwebui/resources/api/v1/chats/chats.py">get_by_id</a>(id) -> <a href="./src/pyopenwebui/types/chat_response.py">Optional[ChatResponse]</a></code>
- <code title="post /api/v1/chats/import">client.api.v1.chats.<a href="./src/pyopenwebui/resources/api/v1/chats/chats.py">import\_</a>(\*\*<a href="src/pyopenwebui/types/api/v1/chat_import_params.py">params</a>) -> <a href="./src/pyopenwebui/types/chat_response.py">Optional[ChatResponse]</a></code>
- <code title="post /api/v1/chats/{id}/pin">client.api.v1.chats.<a href="./src/pyopenwebui/resources/api/v1/chats/chats.py">pin_by_id</a>(id) -> <a href="./src/pyopenwebui/types/chat_response.py">Optional[ChatResponse]</a></code>
- <code title="get /api/v1/chats/search">client.api.v1.chats.<a href="./src/pyopenwebui/resources/api/v1/chats/chats.py">search</a>(\*\*<a href="src/pyopenwebui/types/api/v1/chat_search_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/chat_search_response.py">ChatSearchResponse</a></code>
- <code title="post /api/v1/chats/{id}">client.api.v1.chats.<a href="./src/pyopenwebui/resources/api/v1/chats/chats.py">update_by_id</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/chat_update_by_id_params.py">params</a>) -> <a href="./src/pyopenwebui/types/chat_response.py">Optional[ChatResponse]</a></code>

#### Folder

Types:

```python
from pyopenwebui.types.api.v1.chats import FolderGetResponse
```

Methods:

- <code title="post /api/v1/chats/{id}/folder">client.api.v1.chats.folder.<a href="./src/pyopenwebui/resources/api/v1/chats/folder.py">update</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/chats/folder_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/chat_response.py">Optional[ChatResponse]</a></code>
- <code title="get /api/v1/chats/folder/{folder_id}">client.api.v1.chats.folder.<a href="./src/pyopenwebui/resources/api/v1/chats/folder.py">get</a>(folder_id) -> <a href="./src/pyopenwebui/types/api/v1/chats/folder_get_response.py">FolderGetResponse</a></code>

#### Pinned

Types:

```python
from pyopenwebui.types.api.v1.chats import PinnedGetResponse, PinnedGetByIDResponse
```

Methods:

- <code title="get /api/v1/chats/pinned">client.api.v1.chats.pinned.<a href="./src/pyopenwebui/resources/api/v1/chats/pinned.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/chats/pinned_get_response.py">PinnedGetResponse</a></code>
- <code title="get /api/v1/chats/{id}/pinned">client.api.v1.chats.pinned.<a href="./src/pyopenwebui/resources/api/v1/chats/pinned.py">get_by_id</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/chats/pinned_get_by_id_response.py">Optional[PinnedGetByIDResponse]</a></code>

#### All

Types:

```python
from pyopenwebui.types.api.v1.chats import (
    AllGetResponse,
    AllGetArchivedResponse,
    AllGetDBResponse,
    AllGetTagsResponse,
)
```

Methods:

- <code title="get /api/v1/chats/all">client.api.v1.chats.all.<a href="./src/pyopenwebui/resources/api/v1/chats/all.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/chats/all_get_response.py">AllGetResponse</a></code>
- <code title="get /api/v1/chats/all/archived">client.api.v1.chats.all.<a href="./src/pyopenwebui/resources/api/v1/chats/all.py">get_archived</a>() -> <a href="./src/pyopenwebui/types/api/v1/chats/all_get_archived_response.py">AllGetArchivedResponse</a></code>
- <code title="get /api/v1/chats/all/db">client.api.v1.chats.all.<a href="./src/pyopenwebui/resources/api/v1/chats/all.py">get_db</a>() -> <a href="./src/pyopenwebui/types/api/v1/chats/all_get_db_response.py">AllGetDBResponse</a></code>
- <code title="get /api/v1/chats/all/tags">client.api.v1.chats.all.<a href="./src/pyopenwebui/resources/api/v1/chats/all.py">get_tags</a>() -> <a href="./src/pyopenwebui/types/api/v1/chats/all_get_tags_response.py">AllGetTagsResponse</a></code>

#### Share

Types:

```python
from pyopenwebui.types.api.v1.chats import ShareDeleteResponse
```

Methods:

- <code title="delete /api/v1/chats/{id}/share">client.api.v1.chats.share.<a href="./src/pyopenwebui/resources/api/v1/chats/share.py">delete</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/chats/share_delete_response.py">Optional[ShareDeleteResponse]</a></code>
- <code title="get /api/v1/chats/share/{share_id}">client.api.v1.chats.share.<a href="./src/pyopenwebui/resources/api/v1/chats/share.py">get</a>(share_id) -> <a href="./src/pyopenwebui/types/chat_response.py">Optional[ChatResponse]</a></code>

#### Tags

Types:

```python
from pyopenwebui.types.api.v1.chats import (
    TagDeleteResponse,
    TagAddResponse,
    TagDeleteAllResponse,
    TagGetResponse,
    TagGetByIDResponse,
)
```

Methods:

- <code title="delete /api/v1/chats/{id}/tags">client.api.v1.chats.tags.<a href="./src/pyopenwebui/resources/api/v1/chats/tags.py">delete</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/chats/tag_delete_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/chats/tag_delete_response.py">TagDeleteResponse</a></code>
- <code title="post /api/v1/chats/{id}/tags">client.api.v1.chats.tags.<a href="./src/pyopenwebui/resources/api/v1/chats/tags.py">add</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/chats/tag_add_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/chats/tag_add_response.py">TagAddResponse</a></code>
- <code title="delete /api/v1/chats/{id}/tags/all">client.api.v1.chats.tags.<a href="./src/pyopenwebui/resources/api/v1/chats/tags.py">delete_all</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/chats/tag_delete_all_response.py">Optional[TagDeleteAllResponse]</a></code>
- <code title="post /api/v1/chats/tags">client.api.v1.chats.tags.<a href="./src/pyopenwebui/resources/api/v1/chats/tags.py">get</a>(\*\*<a href="src/pyopenwebui/types/api/v1/chats/tag_get_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/chats/tag_get_response.py">TagGetResponse</a></code>
- <code title="get /api/v1/chats/{id}/tags">client.api.v1.chats.tags.<a href="./src/pyopenwebui/resources/api/v1/chats/tags.py">get_by_id</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/chats/tag_get_by_id_response.py">TagGetByIDResponse</a></code>

#### Clone

Methods:

- <code title="post /api/v1/chats/{id}/clone/shared">client.api.v1.chats.clone.<a href="./src/pyopenwebui/resources/api/v1/chats/clone.py">shared</a>(id) -> <a href="./src/pyopenwebui/types/chat_response.py">Optional[ChatResponse]</a></code>

### Models

Types:

```python
from pyopenwebui.types.api.v1 import ModelDeleteResponse, ModelGetResponse, ModelGetBaseResponse
```

Methods:

- <code title="post /api/v1/models/create">client.api.v1.models.<a href="./src/pyopenwebui/resources/api/v1/models/models.py">create</a>(\*\*<a href="src/pyopenwebui/types/api/v1/model_create_params.py">params</a>) -> <a href="./src/pyopenwebui/types/model_model.py">Optional[ModelModel]</a></code>
- <code title="delete /api/v1/models/delete/all">client.api.v1.models.<a href="./src/pyopenwebui/resources/api/v1/models/models.py">delete</a>() -> <a href="./src/pyopenwebui/types/api/v1/model_delete_response.py">ModelDeleteResponse</a></code>
- <code title="get /api/v1/models/">client.api.v1.models.<a href="./src/pyopenwebui/resources/api/v1/models/models.py">get</a>(\*\*<a href="src/pyopenwebui/types/api/v1/model_get_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/model_get_response.py">ModelGetResponse</a></code>
- <code title="get /api/v1/models/base">client.api.v1.models.<a href="./src/pyopenwebui/resources/api/v1/models/models.py">get_base</a>() -> <a href="./src/pyopenwebui/types/api/v1/model_get_base_response.py">ModelGetBaseResponse</a></code>

#### Model

Types:

```python
from pyopenwebui.types.api.v1.models import (
    ModelDeleteResponse,
    ModelGetResponse,
    ModelToggleResponse,
)
```

Methods:

- <code title="post /api/v1/models/model/update">client.api.v1.models.model.<a href="./src/pyopenwebui/resources/api/v1/models/model.py">update</a>(\*\*<a href="src/pyopenwebui/types/api/v1/models/model_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/model_model.py">Optional[ModelModel]</a></code>
- <code title="delete /api/v1/models/model/delete">client.api.v1.models.model.<a href="./src/pyopenwebui/resources/api/v1/models/model.py">delete</a>(\*\*<a href="src/pyopenwebui/types/api/v1/models/model_delete_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/models/model_delete_response.py">ModelDeleteResponse</a></code>
- <code title="get /api/v1/models/model">client.api.v1.models.model.<a href="./src/pyopenwebui/resources/api/v1/models/model.py">get</a>(\*\*<a href="src/pyopenwebui/types/api/v1/models/model_get_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/models/model_get_response.py">Optional[ModelGetResponse]</a></code>
- <code title="post /api/v1/models/model/toggle">client.api.v1.models.model.<a href="./src/pyopenwebui/resources/api/v1/models/model.py">toggle</a>(\*\*<a href="src/pyopenwebui/types/api/v1/models/model_toggle_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/models/model_toggle_response.py">Optional[ModelToggleResponse]</a></code>

### Knowledge

Types:

```python
from pyopenwebui.types.api.v1 import (
    KnowledgeCreateResponse,
    KnowledgeDeleteByIDResponse,
    KnowledgeGetResponse,
    KnowledgeGetByIDResponse,
    KnowledgeGetListResponse,
    KnowledgeResetByIDResponse,
    KnowledgeUpdateByIDResponse,
)
```

Methods:

- <code title="post /api/v1/knowledge/create">client.api.v1.knowledge.<a href="./src/pyopenwebui/resources/api/v1/knowledge/knowledge.py">create</a>(\*\*<a href="src/pyopenwebui/types/api/v1/knowledge_create_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/knowledge_create_response.py">Optional[KnowledgeCreateResponse]</a></code>
- <code title="delete /api/v1/knowledge/{id}/delete">client.api.v1.knowledge.<a href="./src/pyopenwebui/resources/api/v1/knowledge/knowledge.py">delete_by_id</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/knowledge_delete_by_id_response.py">KnowledgeDeleteByIDResponse</a></code>
- <code title="get /api/v1/knowledge/">client.api.v1.knowledge.<a href="./src/pyopenwebui/resources/api/v1/knowledge/knowledge.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/knowledge_get_response.py">KnowledgeGetResponse</a></code>
- <code title="get /api/v1/knowledge/{id}">client.api.v1.knowledge.<a href="./src/pyopenwebui/resources/api/v1/knowledge/knowledge.py">get_by_id</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/knowledge_get_by_id_response.py">Optional[KnowledgeGetByIDResponse]</a></code>
- <code title="get /api/v1/knowledge/list">client.api.v1.knowledge.<a href="./src/pyopenwebui/resources/api/v1/knowledge/knowledge.py">get_list</a>() -> <a href="./src/pyopenwebui/types/api/v1/knowledge_get_list_response.py">KnowledgeGetListResponse</a></code>
- <code title="post /api/v1/knowledge/{id}/reset">client.api.v1.knowledge.<a href="./src/pyopenwebui/resources/api/v1/knowledge/knowledge.py">reset_by_id</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/knowledge_reset_by_id_response.py">Optional[KnowledgeResetByIDResponse]</a></code>
- <code title="post /api/v1/knowledge/{id}/update">client.api.v1.knowledge.<a href="./src/pyopenwebui/resources/api/v1/knowledge/knowledge.py">update_by_id</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/knowledge_update_by_id_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/knowledge_update_by_id_response.py">Optional[KnowledgeUpdateByIDResponse]</a></code>

#### File

Types:

```python
from pyopenwebui.types.api.v1.knowledge import (
    FileUpdateResponse,
    FileAddResponse,
    FileRemoveResponse,
)
```

Methods:

- <code title="post /api/v1/knowledge/{id}/file/update">client.api.v1.knowledge.file.<a href="./src/pyopenwebui/resources/api/v1/knowledge/file.py">update</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/knowledge/file_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/knowledge/file_update_response.py">Optional[FileUpdateResponse]</a></code>
- <code title="post /api/v1/knowledge/{id}/file/add">client.api.v1.knowledge.file.<a href="./src/pyopenwebui/resources/api/v1/knowledge/file.py">add</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/knowledge/file_add_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/knowledge/file_add_response.py">Optional[FileAddResponse]</a></code>
- <code title="post /api/v1/knowledge/{id}/file/remove">client.api.v1.knowledge.file.<a href="./src/pyopenwebui/resources/api/v1/knowledge/file.py">remove</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/knowledge/file_remove_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/knowledge/file_remove_response.py">Optional[FileRemoveResponse]</a></code>

#### Files

##### Batch

Types:

```python
from pyopenwebui.types.api.v1.knowledge.files import BatchAddResponse
```

Methods:

- <code title="post /api/v1/knowledge/{id}/files/batch/add">client.api.v1.knowledge.files.batch.<a href="./src/pyopenwebui/resources/api/v1/knowledge/files/batch.py">add</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/knowledge/files/batch_add_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/knowledge/files/batch_add_response.py">Optional[BatchAddResponse]</a></code>

### Prompts

Types:

```python
from pyopenwebui.types.api.v1 import PromptGetResponse, PromptGetListResponse
```

Methods:

- <code title="post /api/v1/prompts/create">client.api.v1.prompts.<a href="./src/pyopenwebui/resources/api/v1/prompts/prompts.py">create</a>(\*\*<a href="src/pyopenwebui/types/api/v1/prompt_create_params.py">params</a>) -> <a href="./src/pyopenwebui/types/shared/prompt_model.py">Optional[PromptModel]</a></code>
- <code title="get /api/v1/prompts/">client.api.v1.prompts.<a href="./src/pyopenwebui/resources/api/v1/prompts/prompts.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/prompt_get_response.py">PromptGetResponse</a></code>
- <code title="get /api/v1/prompts/list">client.api.v1.prompts.<a href="./src/pyopenwebui/resources/api/v1/prompts/prompts.py">get_list</a>() -> <a href="./src/pyopenwebui/types/api/v1/prompt_get_list_response.py">PromptGetListResponse</a></code>

#### Command

Types:

```python
from pyopenwebui.types.api.v1.prompts import CommandDeleteByCommandResponse
```

Methods:

- <code title="delete /api/v1/prompts/command/{command}/delete">client.api.v1.prompts.command.<a href="./src/pyopenwebui/resources/api/v1/prompts/command.py">delete_by_command</a>(command) -> <a href="./src/pyopenwebui/types/api/v1/prompts/command_delete_by_command_response.py">CommandDeleteByCommandResponse</a></code>
- <code title="get /api/v1/prompts/command/{command}">client.api.v1.prompts.command.<a href="./src/pyopenwebui/resources/api/v1/prompts/command.py">get_by_command</a>(command) -> <a href="./src/pyopenwebui/types/shared/prompt_model.py">Optional[PromptModel]</a></code>
- <code title="post /api/v1/prompts/command/{command}/update">client.api.v1.prompts.command.<a href="./src/pyopenwebui/resources/api/v1/prompts/command.py">update_by_command</a>(command_1, \*\*<a href="src/pyopenwebui/types/api/v1/prompts/command_update_by_command_params.py">params</a>) -> <a href="./src/pyopenwebui/types/shared/prompt_model.py">Optional[PromptModel]</a></code>

### Tools

Types:

```python
from pyopenwebui.types.api.v1 import ToolExportResponse, ToolGetResponse, ToolGetListResponse
```

Methods:

- <code title="post /api/v1/tools/create">client.api.v1.tools.<a href="./src/pyopenwebui/resources/api/v1/tools/tools.py">create</a>(\*\*<a href="src/pyopenwebui/types/api/v1/tool_create_params.py">params</a>) -> <a href="./src/pyopenwebui/types/tool_response.py">Optional[ToolResponse]</a></code>
- <code title="get /api/v1/tools/export">client.api.v1.tools.<a href="./src/pyopenwebui/resources/api/v1/tools/tools.py">export</a>() -> <a href="./src/pyopenwebui/types/api/v1/tool_export_response.py">ToolExportResponse</a></code>
- <code title="get /api/v1/tools/">client.api.v1.tools.<a href="./src/pyopenwebui/resources/api/v1/tools/tools.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/tool_get_response.py">ToolGetResponse</a></code>
- <code title="get /api/v1/tools/list">client.api.v1.tools.<a href="./src/pyopenwebui/resources/api/v1/tools/tools.py">get_list</a>() -> <a href="./src/pyopenwebui/types/api/v1/tool_get_list_response.py">ToolGetListResponse</a></code>

#### ID

Types:

```python
from pyopenwebui.types.api.v1.tools import IDDeleteResponse
```

Methods:

- <code title="post /api/v1/tools/id/{id}/update">client.api.v1.tools.id.<a href="./src/pyopenwebui/resources/api/v1/tools/id/id.py">update</a>(id_1, \*\*<a href="src/pyopenwebui/types/api/v1/tools/id_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/tool_model.py">Optional[ToolModel]</a></code>
- <code title="delete /api/v1/tools/id/{id}/delete">client.api.v1.tools.id.<a href="./src/pyopenwebui/resources/api/v1/tools/id/id.py">delete</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/tools/id_delete_response.py">IDDeleteResponse</a></code>
- <code title="get /api/v1/tools/id/{id}">client.api.v1.tools.id.<a href="./src/pyopenwebui/resources/api/v1/tools/id/id.py">get</a>(id) -> <a href="./src/pyopenwebui/types/tool_model.py">Optional[ToolModel]</a></code>

##### Valves

Types:

```python
from pyopenwebui.types.api.v1.tools.id import (
    ValveUpdateResponse,
    ValveGetResponse,
    ValveGetSpecResponse,
)
```

Methods:

- <code title="post /api/v1/tools/id/{id}/valves/update">client.api.v1.tools.id.valves.<a href="./src/pyopenwebui/resources/api/v1/tools/id/valves/valves.py">update</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/tools/id/valve_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/tools/id/valve_update_response.py">object</a></code>
- <code title="get /api/v1/tools/id/{id}/valves">client.api.v1.tools.id.valves.<a href="./src/pyopenwebui/resources/api/v1/tools/id/valves/valves.py">get</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/tools/id/valve_get_response.py">object</a></code>
- <code title="get /api/v1/tools/id/{id}/valves/spec">client.api.v1.tools.id.valves.<a href="./src/pyopenwebui/resources/api/v1/tools/id/valves/valves.py">get_spec</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/tools/id/valve_get_spec_response.py">object</a></code>

###### User

Types:

```python
from pyopenwebui.types.api.v1.tools.id.valves import (
    UserUpdateResponse,
    UserGetResponse,
    UserGetSpecResponse,
)
```

Methods:

- <code title="post /api/v1/tools/id/{id}/valves/user/update">client.api.v1.tools.id.valves.user.<a href="./src/pyopenwebui/resources/api/v1/tools/id/valves/user.py">update</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/tools/id/valves/user_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/tools/id/valves/user_update_response.py">object</a></code>
- <code title="get /api/v1/tools/id/{id}/valves/user">client.api.v1.tools.id.valves.user.<a href="./src/pyopenwebui/resources/api/v1/tools/id/valves/user.py">get</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/tools/id/valves/user_get_response.py">object</a></code>
- <code title="get /api/v1/tools/id/{id}/valves/user/spec">client.api.v1.tools.id.valves.user.<a href="./src/pyopenwebui/resources/api/v1/tools/id/valves/user.py">get_spec</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/tools/id/valves/user_get_spec_response.py">object</a></code>

### Memories

Types:

```python
from pyopenwebui.types.api.v1 import (
    MemoryDeleteResponse,
    MemoryDeleteByIDResponse,
    MemoryGetResponse,
    MemoryGetEmbeddingsResponse,
    MemoryQueryResponse,
    MemoryResetResponse,
)
```

Methods:

- <code title="delete /api/v1/memories/delete/user">client.api.v1.memories.<a href="./src/pyopenwebui/resources/api/v1/memories.py">delete</a>() -> <a href="./src/pyopenwebui/types/api/v1/memory_delete_response.py">MemoryDeleteResponse</a></code>
- <code title="post /api/v1/memories/add">client.api.v1.memories.<a href="./src/pyopenwebui/resources/api/v1/memories.py">add</a>(\*\*<a href="src/pyopenwebui/types/api/v1/memory_add_params.py">params</a>) -> <a href="./src/pyopenwebui/types/memory_model.py">Optional[MemoryModel]</a></code>
- <code title="delete /api/v1/memories/{memory_id}">client.api.v1.memories.<a href="./src/pyopenwebui/resources/api/v1/memories.py">delete_by_id</a>(memory_id) -> <a href="./src/pyopenwebui/types/api/v1/memory_delete_by_id_response.py">MemoryDeleteByIDResponse</a></code>
- <code title="get /api/v1/memories/">client.api.v1.memories.<a href="./src/pyopenwebui/resources/api/v1/memories.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/memory_get_response.py">MemoryGetResponse</a></code>
- <code title="get /api/v1/memories/ef">client.api.v1.memories.<a href="./src/pyopenwebui/resources/api/v1/memories.py">get_embeddings</a>() -> <a href="./src/pyopenwebui/types/api/v1/memory_get_embeddings_response.py">object</a></code>
- <code title="post /api/v1/memories/query">client.api.v1.memories.<a href="./src/pyopenwebui/resources/api/v1/memories.py">query</a>(\*\*<a href="src/pyopenwebui/types/api/v1/memory_query_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/memory_query_response.py">object</a></code>
- <code title="post /api/v1/memories/reset">client.api.v1.memories.<a href="./src/pyopenwebui/resources/api/v1/memories.py">reset</a>() -> <a href="./src/pyopenwebui/types/api/v1/memory_reset_response.py">MemoryResetResponse</a></code>
- <code title="post /api/v1/memories/{memory_id}/update">client.api.v1.memories.<a href="./src/pyopenwebui/resources/api/v1/memories.py">update_by_id</a>(memory_id, \*\*<a href="src/pyopenwebui/types/api/v1/memory_update_by_id_params.py">params</a>) -> <a href="./src/pyopenwebui/types/memory_model.py">Optional[MemoryModel]</a></code>

### Folders

Types:

```python
from pyopenwebui.types.api.v1 import (
    FolderCreateResponse,
    FolderUpdateResponse,
    FolderDeleteByIDResponse,
    FolderGetResponse,
    FolderGetByIDResponse,
)
```

Methods:

- <code title="post /api/v1/folders/">client.api.v1.folders.<a href="./src/pyopenwebui/resources/api/v1/folders.py">create</a>(\*\*<a href="src/pyopenwebui/types/api/v1/folder_create_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/folder_create_response.py">object</a></code>
- <code title="post /api/v1/folders/{id}/update/expanded">client.api.v1.folders.<a href="./src/pyopenwebui/resources/api/v1/folders.py">update</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/folder_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/folder_update_response.py">object</a></code>
- <code title="delete /api/v1/folders/{id}">client.api.v1.folders.<a href="./src/pyopenwebui/resources/api/v1/folders.py">delete_by_id</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/folder_delete_by_id_response.py">object</a></code>
- <code title="get /api/v1/folders/">client.api.v1.folders.<a href="./src/pyopenwebui/resources/api/v1/folders.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/folder_get_response.py">FolderGetResponse</a></code>
- <code title="get /api/v1/folders/{id}">client.api.v1.folders.<a href="./src/pyopenwebui/resources/api/v1/folders.py">get_by_id</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/folder_get_by_id_response.py">Optional[FolderGetByIDResponse]</a></code>

### Groups

Types:

```python
from pyopenwebui.types.api.v1 import GroupCreateResponse, GroupGetResponse
```

Methods:

- <code title="post /api/v1/groups/create">client.api.v1.groups.<a href="./src/pyopenwebui/resources/api/v1/groups/groups.py">create</a>(\*\*<a href="src/pyopenwebui/types/api/v1/group_create_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/group_create_response.py">Optional[GroupCreateResponse]</a></code>
- <code title="get /api/v1/groups/">client.api.v1.groups.<a href="./src/pyopenwebui/resources/api/v1/groups/groups.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/group_get_response.py">GroupGetResponse</a></code>

#### ID

Types:

```python
from pyopenwebui.types.api.v1.groups import IDUpdateResponse, IDDeleteResponse, IDGetResponse
```

Methods:

- <code title="post /api/v1/groups/id/{id}/update">client.api.v1.groups.id.<a href="./src/pyopenwebui/resources/api/v1/groups/id.py">update</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/groups/id_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/groups/id_update_response.py">Optional[IDUpdateResponse]</a></code>
- <code title="delete /api/v1/groups/id/{id}/delete">client.api.v1.groups.id.<a href="./src/pyopenwebui/resources/api/v1/groups/id.py">delete</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/groups/id_delete_response.py">IDDeleteResponse</a></code>
- <code title="get /api/v1/groups/id/{id}">client.api.v1.groups.id.<a href="./src/pyopenwebui/resources/api/v1/groups/id.py">get</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/groups/id_get_response.py">Optional[IDGetResponse]</a></code>

### Files

Types:

```python
from pyopenwebui.types.api.v1 import (
    FileListResponse,
    FileDeleteAllResponse,
    FileDeleteByIDResponse,
    FileUploadResponse,
)
```

Methods:

- <code title="get /api/v1/files/">client.api.v1.files.<a href="./src/pyopenwebui/resources/api/v1/files/files.py">list</a>() -> <a href="./src/pyopenwebui/types/api/v1/file_list_response.py">FileListResponse</a></code>
- <code title="delete /api/v1/files/all">client.api.v1.files.<a href="./src/pyopenwebui/resources/api/v1/files/files.py">delete_all</a>() -> <a href="./src/pyopenwebui/types/api/v1/file_delete_all_response.py">object</a></code>
- <code title="delete /api/v1/files/{id}">client.api.v1.files.<a href="./src/pyopenwebui/resources/api/v1/files/files.py">delete_by_id</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/file_delete_by_id_response.py">object</a></code>
- <code title="get /api/v1/files/{id}">client.api.v1.files.<a href="./src/pyopenwebui/resources/api/v1/files/files.py">get_by_id</a>(id) -> <a href="./src/pyopenwebui/types/shared/file_model.py">Optional[FileModel]</a></code>
- <code title="post /api/v1/files/">client.api.v1.files.<a href="./src/pyopenwebui/resources/api/v1/files/files.py">upload</a>(\*\*<a href="src/pyopenwebui/types/api/v1/file_upload_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/file_upload_response.py">FileUploadResponse</a></code>

#### Data

##### Content

Types:

```python
from pyopenwebui.types.api.v1.files.data import ContentUpdateResponse, ContentGetResponse
```

Methods:

- <code title="post /api/v1/files/{id}/data/content/update">client.api.v1.files.data.content.<a href="./src/pyopenwebui/resources/api/v1/files/data/content.py">update</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/files/data/content_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/files/data/content_update_response.py">object</a></code>
- <code title="get /api/v1/files/{id}/data/content">client.api.v1.files.data.content.<a href="./src/pyopenwebui/resources/api/v1/files/data/content.py">get</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/files/data/content_get_response.py">object</a></code>

#### Content

Types:

```python
from pyopenwebui.types.api.v1.files import (
    ContentGetResponse,
    ContentGetByNameResponse,
    ContentGetHTMLResponse,
)
```

Methods:

- <code title="get /api/v1/files/{id}/content">client.api.v1.files.content.<a href="./src/pyopenwebui/resources/api/v1/files/content.py">get</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/files/content_get_response.py">object</a></code>
- <code title="get /api/v1/files/{id}/content/{file_name}">client.api.v1.files.content.<a href="./src/pyopenwebui/resources/api/v1/files/content.py">get_by_name</a>(file_name, \*, id) -> <a href="./src/pyopenwebui/types/api/v1/files/content_get_by_name_response.py">object</a></code>
- <code title="get /api/v1/files/{id}/content/html">client.api.v1.files.content.<a href="./src/pyopenwebui/resources/api/v1/files/content.py">get_html</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/files/content_get_html_response.py">object</a></code>

### Functions

Types:

```python
from pyopenwebui.types.api.v1 import FunctionGetResponse, FunctionGetExportResponse
```

Methods:

- <code title="post /api/v1/functions/create">client.api.v1.functions.<a href="./src/pyopenwebui/resources/api/v1/functions/functions.py">create</a>(\*\*<a href="src/pyopenwebui/types/api/v1/function_create_params.py">params</a>) -> <a href="./src/pyopenwebui/types/function_response.py">Optional[FunctionResponse]</a></code>
- <code title="get /api/v1/functions/">client.api.v1.functions.<a href="./src/pyopenwebui/resources/api/v1/functions/functions.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/function_get_response.py">FunctionGetResponse</a></code>
- <code title="get /api/v1/functions/export">client.api.v1.functions.<a href="./src/pyopenwebui/resources/api/v1/functions/functions.py">get_export</a>() -> <a href="./src/pyopenwebui/types/api/v1/function_get_export_response.py">FunctionGetExportResponse</a></code>

#### ID

Types:

```python
from pyopenwebui.types.api.v1.functions import IDDeleteResponse
```

Methods:

- <code title="post /api/v1/functions/id/{id}/update">client.api.v1.functions.id.<a href="./src/pyopenwebui/resources/api/v1/functions/id/id.py">update</a>(id_1, \*\*<a href="src/pyopenwebui/types/api/v1/functions/id_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/function_model.py">Optional[FunctionModel]</a></code>
- <code title="delete /api/v1/functions/id/{id}/delete">client.api.v1.functions.id.<a href="./src/pyopenwebui/resources/api/v1/functions/id/id.py">delete</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/functions/id_delete_response.py">IDDeleteResponse</a></code>
- <code title="get /api/v1/functions/id/{id}">client.api.v1.functions.id.<a href="./src/pyopenwebui/resources/api/v1/functions/id/id.py">get</a>(id) -> <a href="./src/pyopenwebui/types/function_model.py">Optional[FunctionModel]</a></code>

##### Toggle

Methods:

- <code title="post /api/v1/functions/id/{id}/toggle/global">client.api.v1.functions.id.toggle.<a href="./src/pyopenwebui/resources/api/v1/functions/id/toggle.py">global\_</a>(id) -> <a href="./src/pyopenwebui/types/function_model.py">Optional[FunctionModel]</a></code>

##### Valves

Types:

```python
from pyopenwebui.types.api.v1.functions.id import (
    ValveUpdateResponse,
    ValveGetResponse,
    ValveGetSpecResponse,
)
```

Methods:

- <code title="post /api/v1/functions/id/{id}/valves/update">client.api.v1.functions.id.valves.<a href="./src/pyopenwebui/resources/api/v1/functions/id/valves/valves.py">update</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/functions/id/valve_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/functions/id/valve_update_response.py">object</a></code>
- <code title="get /api/v1/functions/id/{id}/valves">client.api.v1.functions.id.valves.<a href="./src/pyopenwebui/resources/api/v1/functions/id/valves/valves.py">get</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/functions/id/valve_get_response.py">object</a></code>
- <code title="get /api/v1/functions/id/{id}/valves/spec">client.api.v1.functions.id.valves.<a href="./src/pyopenwebui/resources/api/v1/functions/id/valves/valves.py">get_spec</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/functions/id/valve_get_spec_response.py">object</a></code>

###### User

Types:

```python
from pyopenwebui.types.api.v1.functions.id.valves import (
    UserUpdateResponse,
    UserGetResponse,
    UserGetSpecResponse,
)
```

Methods:

- <code title="post /api/v1/functions/id/{id}/valves/user/update">client.api.v1.functions.id.valves.user.<a href="./src/pyopenwebui/resources/api/v1/functions/id/valves/user.py">update</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/functions/id/valves/user_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/functions/id/valves/user_update_response.py">object</a></code>
- <code title="get /api/v1/functions/id/{id}/valves/user">client.api.v1.functions.id.valves.user.<a href="./src/pyopenwebui/resources/api/v1/functions/id/valves/user.py">get</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/functions/id/valves/user_get_response.py">object</a></code>
- <code title="get /api/v1/functions/id/{id}/valves/user/spec">client.api.v1.functions.id.valves.user.<a href="./src/pyopenwebui/resources/api/v1/functions/id/valves/user.py">get_spec</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/functions/id/valves/user_get_spec_response.py">object</a></code>

### Evaluations

#### Config

Types:

```python
from pyopenwebui.types.api.v1.evaluations import ConfigUpdateResponse, ConfigGetResponse
```

Methods:

- <code title="post /api/v1/evaluations/config">client.api.v1.evaluations.config.<a href="./src/pyopenwebui/resources/api/v1/evaluations/config.py">update</a>(\*\*<a href="src/pyopenwebui/types/api/v1/evaluations/config_update_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/evaluations/config_update_response.py">object</a></code>
- <code title="get /api/v1/evaluations/config">client.api.v1.evaluations.config.<a href="./src/pyopenwebui/resources/api/v1/evaluations/config.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/evaluations/config_get_response.py">object</a></code>

#### Feedbacks

Types:

```python
from pyopenwebui.types.api.v1.evaluations import FeedbackDeleteResponse, FeedbackGetResponse
```

Methods:

- <code title="delete /api/v1/evaluations/feedbacks">client.api.v1.evaluations.feedbacks.<a href="./src/pyopenwebui/resources/api/v1/evaluations/feedbacks/feedbacks.py">delete</a>() -> <a href="./src/pyopenwebui/types/api/v1/evaluations/feedback_delete_response.py">FeedbackDeleteResponse</a></code>
- <code title="get /api/v1/evaluations/feedbacks/user">client.api.v1.evaluations.feedbacks.<a href="./src/pyopenwebui/resources/api/v1/evaluations/feedbacks/feedbacks.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/evaluations/feedback_get_response.py">FeedbackGetResponse</a></code>

##### All

Types:

```python
from pyopenwebui.types.api.v1.evaluations.feedbacks import (
    AllDeleteResponse,
    AllExportResponse,
    AllGetResponse,
)
```

Methods:

- <code title="delete /api/v1/evaluations/feedbacks/all">client.api.v1.evaluations.feedbacks.all.<a href="./src/pyopenwebui/resources/api/v1/evaluations/feedbacks/all.py">delete</a>() -> <a href="./src/pyopenwebui/types/api/v1/evaluations/feedbacks/all_delete_response.py">object</a></code>
- <code title="get /api/v1/evaluations/feedbacks/all/export">client.api.v1.evaluations.feedbacks.all.<a href="./src/pyopenwebui/resources/api/v1/evaluations/feedbacks/all.py">export</a>() -> <a href="./src/pyopenwebui/types/api/v1/evaluations/feedbacks/all_export_response.py">AllExportResponse</a></code>
- <code title="get /api/v1/evaluations/feedbacks/all">client.api.v1.evaluations.feedbacks.all.<a href="./src/pyopenwebui/resources/api/v1/evaluations/feedbacks/all.py">get</a>() -> <a href="./src/pyopenwebui/types/api/v1/evaluations/feedbacks/all_get_response.py">AllGetResponse</a></code>

#### Feedback

Types:

```python
from pyopenwebui.types.api.v1.evaluations import (
    FeedbackCreateResponse,
    FeedbackDeleteByIDResponse,
    FeedbackGetByIDResponse,
    FeedbackUpdateByIDResponse,
)
```

Methods:

- <code title="post /api/v1/evaluations/feedback">client.api.v1.evaluations.feedback.<a href="./src/pyopenwebui/resources/api/v1/evaluations/feedback.py">create</a>(\*\*<a href="src/pyopenwebui/types/api/v1/evaluations/feedback_create_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/evaluations/feedback_create_response.py">FeedbackCreateResponse</a></code>
- <code title="delete /api/v1/evaluations/feedback/{id}">client.api.v1.evaluations.feedback.<a href="./src/pyopenwebui/resources/api/v1/evaluations/feedback.py">delete_by_id</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/evaluations/feedback_delete_by_id_response.py">object</a></code>
- <code title="get /api/v1/evaluations/feedback/{id}">client.api.v1.evaluations.feedback.<a href="./src/pyopenwebui/resources/api/v1/evaluations/feedback.py">get_by_id</a>(id) -> <a href="./src/pyopenwebui/types/api/v1/evaluations/feedback_get_by_id_response.py">FeedbackGetByIDResponse</a></code>
- <code title="post /api/v1/evaluations/feedback/{id}">client.api.v1.evaluations.feedback.<a href="./src/pyopenwebui/resources/api/v1/evaluations/feedback.py">update_by_id</a>(id, \*\*<a href="src/pyopenwebui/types/api/v1/evaluations/feedback_update_by_id_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/evaluations/feedback_update_by_id_response.py">FeedbackUpdateByIDResponse</a></code>

### Utils

Types:

```python
from pyopenwebui.types.api.v1 import (
    UtilDownloadChatAsPdfResponse,
    UtilGetGravatarResponse,
    UtilMarkdownResponse,
)
```

Methods:

- <code title="post /api/v1/utils/pdf">client.api.v1.utils.<a href="./src/pyopenwebui/resources/api/v1/utils/utils.py">download_chat_as_pdf</a>(\*\*<a href="src/pyopenwebui/types/api/v1/util_download_chat_as_pdf_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/util_download_chat_as_pdf_response.py">object</a></code>
- <code title="get /api/v1/utils/gravatar">client.api.v1.utils.<a href="./src/pyopenwebui/resources/api/v1/utils/utils.py">get_gravatar</a>(\*\*<a href="src/pyopenwebui/types/api/v1/util_get_gravatar_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/util_get_gravatar_response.py">object</a></code>
- <code title="post /api/v1/utils/markdown">client.api.v1.utils.<a href="./src/pyopenwebui/resources/api/v1/utils/utils.py">markdown</a>(\*\*<a href="src/pyopenwebui/types/api/v1/util_markdown_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/util_markdown_response.py">object</a></code>

#### Code

Types:

```python
from pyopenwebui.types.api.v1.utils import CodeExecuteResponse, CodeFormatResponse
```

Methods:

- <code title="post /api/v1/utils/code/execute">client.api.v1.utils.code.<a href="./src/pyopenwebui/resources/api/v1/utils/code.py">execute</a>(\*\*<a href="src/pyopenwebui/types/api/v1/utils/code_execute_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/utils/code_execute_response.py">object</a></code>
- <code title="post /api/v1/utils/code/format">client.api.v1.utils.code.<a href="./src/pyopenwebui/resources/api/v1/utils/code.py">format</a>(\*\*<a href="src/pyopenwebui/types/api/v1/utils/code_format_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/v1/utils/code_format_response.py">object</a></code>

#### DB

Types:

```python
from pyopenwebui.types.api.v1.utils import DBDownloadResponse
```

Methods:

- <code title="get /api/v1/utils/db/download">client.api.v1.utils.db.<a href="./src/pyopenwebui/resources/api/v1/utils/db.py">download</a>() -> <a href="./src/pyopenwebui/types/api/v1/utils/db_download_response.py">object</a></code>

#### Litellm

Types:

```python
from pyopenwebui.types.api.v1.utils import LitellmGetConfigResponse
```

Methods:

- <code title="get /api/v1/utils/litellm/config">client.api.v1.utils.litellm.<a href="./src/pyopenwebui/resources/api/v1/utils/litellm.py">get_config</a>() -> <a href="./src/pyopenwebui/types/api/v1/utils/litellm_get_config_response.py">object</a></code>

## Models

Types:

```python
from pyopenwebui.types.api import ModelListResponse, ModelListBaseResponse
```

Methods:

- <code title="get /api/models">client.api.models.<a href="./src/pyopenwebui/resources/api/models.py">list</a>() -> <a href="./src/pyopenwebui/types/api/model_list_response.py">object</a></code>
- <code title="get /api/models/base">client.api.models.<a href="./src/pyopenwebui/resources/api/models.py">list_base</a>() -> <a href="./src/pyopenwebui/types/api/model_list_base_response.py">object</a></code>

## Chat

Types:

```python
from pyopenwebui.types.api import (
    ChatCompleteResponse,
    ChatCreateCompletionResponse,
    ChatPerformActionResponse,
)
```

Methods:

- <code title="post /api/chat/completed">client.api.chat.<a href="./src/pyopenwebui/resources/api/chat.py">complete</a>(\*\*<a href="src/pyopenwebui/types/api/chat_complete_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/chat_complete_response.py">object</a></code>
- <code title="post /api/chat/completions">client.api.chat.<a href="./src/pyopenwebui/resources/api/chat.py">create_completion</a>(\*\*<a href="src/pyopenwebui/types/api/chat_create_completion_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/chat_create_completion_response.py">object</a></code>
- <code title="post /api/chat/actions/{action_id}">client.api.chat.<a href="./src/pyopenwebui/resources/api/chat.py">perform_action</a>(action_id, \*\*<a href="src/pyopenwebui/types/api/chat_perform_action_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/chat_perform_action_response.py">object</a></code>

## Tasks

Types:

```python
from pyopenwebui.types.api import TaskListResponse, TaskStopResponse
```

Methods:

- <code title="get /api/tasks">client.api.tasks.<a href="./src/pyopenwebui/resources/api/tasks.py">list</a>() -> <a href="./src/pyopenwebui/types/api/task_list_response.py">object</a></code>
- <code title="post /api/tasks/stop/{task_id}">client.api.tasks.<a href="./src/pyopenwebui/resources/api/tasks.py">stop</a>(task_id) -> <a href="./src/pyopenwebui/types/api/task_stop_response.py">object</a></code>

## Webhook

Types:

```python
from pyopenwebui.types.api import WebhookGetURLResponse, WebhookUpdateURLResponse
```

Methods:

- <code title="get /api/webhook">client.api.webhook.<a href="./src/pyopenwebui/resources/api/webhook.py">get_url</a>() -> <a href="./src/pyopenwebui/types/api/webhook_get_url_response.py">object</a></code>
- <code title="post /api/webhook">client.api.webhook.<a href="./src/pyopenwebui/resources/api/webhook.py">update_url</a>(\*\*<a href="src/pyopenwebui/types/api/webhook_update_url_params.py">params</a>) -> <a href="./src/pyopenwebui/types/api/webhook_update_url_response.py">object</a></code>

## Version

Types:

```python
from pyopenwebui.types.api import VersionRetrieveResponse, VersionListUpdatesResponse
```

Methods:

- <code title="get /api/version">client.api.version.<a href="./src/pyopenwebui/resources/api/version.py">retrieve</a>() -> <a href="./src/pyopenwebui/types/api/version_retrieve_response.py">object</a></code>
- <code title="get /api/version/updates">client.api.version.<a href="./src/pyopenwebui/resources/api/version.py">list_updates</a>() -> <a href="./src/pyopenwebui/types/api/version_list_updates_response.py">object</a></code>

# OAuth

Types:

```python
from pyopenwebui.types import OAuthCallbackResponse, OAuthLoginResponse
```

Methods:

- <code title="get /oauth/{provider}/callback">client.oauth.<a href="./src/pyopenwebui/resources/oauth.py">callback</a>(provider) -> <a href="./src/pyopenwebui/types/oauth_callback_response.py">object</a></code>
- <code title="get /oauth/{provider}/login">client.oauth.<a href="./src/pyopenwebui/resources/oauth.py">login</a>(provider) -> <a href="./src/pyopenwebui/types/oauth_login_response.py">object</a></code>

# ManifestJson

Types:

```python
from pyopenwebui.types import ManifestJsonRetrieveResponse
```

Methods:

- <code title="get /manifest.json">client.manifest_json.<a href="./src/pyopenwebui/resources/manifest_json.py">retrieve</a>() -> <a href="./src/pyopenwebui/types/manifest_json_retrieve_response.py">object</a></code>

# OpensearchXml

Types:

```python
from pyopenwebui.types import OpensearchXmlRetrieveResponse
```

Methods:

- <code title="get /opensearch.xml">client.opensearch_xml.<a href="./src/pyopenwebui/resources/opensearch_xml.py">retrieve</a>() -> <a href="./src/pyopenwebui/types/opensearch_xml_retrieve_response.py">object</a></code>

# Health

Types:

```python
from pyopenwebui.types import HealthCheckResponse, HealthCheckDBResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/pyopenwebui/resources/health.py">check</a>() -> <a href="./src/pyopenwebui/types/health_check_response.py">object</a></code>
- <code title="get /health/db">client.health.<a href="./src/pyopenwebui/resources/health.py">check_db</a>() -> <a href="./src/pyopenwebui/types/health_check_db_response.py">object</a></code>
