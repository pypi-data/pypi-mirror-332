"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_ai_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class ListPromptVersionsRequestTypedDict(TypedDict):
    prompt_id: str
    limit: NotRequired[float]
    r"""A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10"""
    starting_after: NotRequired[str]
    r"""A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list."""
    ending_before: NotRequired[str]
    r"""A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list."""


class ListPromptVersionsRequest(BaseModel):
    prompt_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    limit: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10
    r"""A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10"""

    starting_after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list."""

    ending_before: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list."""


ListPromptVersionsObject = Literal["list"]

ListPromptVersionsType = Literal["prompt"]

ListPromptVersionsModelType = Literal[
    "chat",
    "completion",
    "embedding",
    "vision",
    "image",
    "tts",
    "stt",
    "rerank",
    "moderations",
]
r"""The type of the model"""

ListPromptVersionsFormat = Literal["url", "b64_json", "text", "json_object"]
r"""Only supported on `image` models."""

ListPromptVersionsQuality = Literal["standard", "hd"]
r"""Only supported on `image` models."""

ListPromptVersionsResponseFormatPromptsType = Literal["json_object"]


class ListPromptVersionsResponseFormat2TypedDict(TypedDict):
    type: ListPromptVersionsResponseFormatPromptsType


class ListPromptVersionsResponseFormat2(BaseModel):
    type: ListPromptVersionsResponseFormatPromptsType


ListPromptVersionsResponseFormatType = Literal["json_schema"]


class ListPromptVersionsResponseFormatJSONSchemaTypedDict(TypedDict):
    name: str
    strict: bool
    schema_: Dict[str, Any]


class ListPromptVersionsResponseFormatJSONSchema(BaseModel):
    name: str

    strict: bool

    schema_: Annotated[Dict[str, Any], pydantic.Field(alias="schema")]


class ListPromptVersionsResponseFormat1TypedDict(TypedDict):
    type: ListPromptVersionsResponseFormatType
    json_schema: ListPromptVersionsResponseFormatJSONSchemaTypedDict


class ListPromptVersionsResponseFormat1(BaseModel):
    type: ListPromptVersionsResponseFormatType

    json_schema: ListPromptVersionsResponseFormatJSONSchema


ListPromptVersionsResponseFormatTypedDict = TypeAliasType(
    "ListPromptVersionsResponseFormatTypedDict",
    Union[
        ListPromptVersionsResponseFormat2TypedDict,
        ListPromptVersionsResponseFormat1TypedDict,
    ],
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


ListPromptVersionsResponseFormat = TypeAliasType(
    "ListPromptVersionsResponseFormat",
    Union[ListPromptVersionsResponseFormat2, ListPromptVersionsResponseFormat1],
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


ListPromptVersionsPhotoRealVersion = Literal["v1", "v2"]
r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

ListPromptVersionsEncodingFormat = Literal["float", "base64"]
r"""The format to return the embeddings"""

ListPromptVersionsReasoningEffort = Literal["low", "medium", "high"]
r"""Constrains effort on reasoning for reasoning models. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response."""


class ListPromptVersionsModelParametersTypedDict(TypedDict):
    r"""Model Parameters: Not all parameters apply to every model"""

    temperature: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    max_tokens: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    top_k: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    top_p: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    frequency_penalty: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    presence_penalty: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    num_images: NotRequired[float]
    r"""Only supported on `image` models."""
    seed: NotRequired[float]
    r"""Best effort deterministic seed for the model. Currently only OpenAI models support these"""
    format_: NotRequired[ListPromptVersionsFormat]
    r"""Only supported on `image` models."""
    dimensions: NotRequired[str]
    r"""Only supported on `image` models."""
    quality: NotRequired[ListPromptVersionsQuality]
    r"""Only supported on `image` models."""
    style: NotRequired[str]
    r"""Only supported on `image` models."""
    response_format: NotRequired[Nullable[ListPromptVersionsResponseFormatTypedDict]]
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """
    photo_real_version: NotRequired[ListPromptVersionsPhotoRealVersion]
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""
    encoding_format: NotRequired[ListPromptVersionsEncodingFormat]
    r"""The format to return the embeddings"""
    reasoning_effort: NotRequired[ListPromptVersionsReasoningEffort]
    r"""Constrains effort on reasoning for reasoning models. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response."""
    budget_tokens: NotRequired[float]
    r"""Gives the model enhanced reasoning capabilities for complex tasks. A value of 0 disables thinking. The minimum budget tokens for thinking are 1024. The Budget Tokens should never exceed the Max Tokens parameter. Only supported by `Anthropic`"""


class ListPromptVersionsModelParameters(BaseModel):
    r"""Model Parameters: Not all parameters apply to every model"""

    temperature: Optional[float] = None
    r"""Only supported on `chat` and `completion` models."""

    max_tokens: Annotated[Optional[float], pydantic.Field(alias="maxTokens")] = None
    r"""Only supported on `chat` and `completion` models."""

    top_k: Annotated[Optional[float], pydantic.Field(alias="topK")] = None
    r"""Only supported on `chat` and `completion` models."""

    top_p: Annotated[Optional[float], pydantic.Field(alias="topP")] = None
    r"""Only supported on `chat` and `completion` models."""

    frequency_penalty: Annotated[
        Optional[float], pydantic.Field(alias="frequencyPenalty")
    ] = None
    r"""Only supported on `chat` and `completion` models."""

    presence_penalty: Annotated[
        Optional[float], pydantic.Field(alias="presencePenalty")
    ] = None
    r"""Only supported on `chat` and `completion` models."""

    num_images: Annotated[Optional[float], pydantic.Field(alias="numImages")] = None
    r"""Only supported on `image` models."""

    seed: Optional[float] = None
    r"""Best effort deterministic seed for the model. Currently only OpenAI models support these"""

    format_: Annotated[
        Optional[ListPromptVersionsFormat], pydantic.Field(alias="format")
    ] = None
    r"""Only supported on `image` models."""

    dimensions: Optional[str] = None
    r"""Only supported on `image` models."""

    quality: Optional[ListPromptVersionsQuality] = None
    r"""Only supported on `image` models."""

    style: Optional[str] = None
    r"""Only supported on `image` models."""

    response_format: Annotated[
        OptionalNullable[ListPromptVersionsResponseFormat],
        pydantic.Field(alias="responseFormat"),
    ] = UNSET
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """

    photo_real_version: Annotated[
        Optional[ListPromptVersionsPhotoRealVersion],
        pydantic.Field(alias="photoRealVersion"),
    ] = None
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

    encoding_format: Optional[ListPromptVersionsEncodingFormat] = None
    r"""The format to return the embeddings"""

    reasoning_effort: Annotated[
        Optional[ListPromptVersionsReasoningEffort],
        pydantic.Field(alias="reasoningEffort"),
    ] = None
    r"""Constrains effort on reasoning for reasoning models. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response."""

    budget_tokens: Annotated[Optional[float], pydantic.Field(alias="budgetTokens")] = (
        None
    )
    r"""Gives the model enhanced reasoning capabilities for complex tasks. A value of 0 disables thinking. The minimum budget tokens for thinking are 1024. The Budget Tokens should never exceed the Max Tokens parameter. Only supported by `Anthropic`"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "temperature",
            "maxTokens",
            "topK",
            "topP",
            "frequencyPenalty",
            "presencePenalty",
            "numImages",
            "seed",
            "format",
            "dimensions",
            "quality",
            "style",
            "responseFormat",
            "photoRealVersion",
            "encoding_format",
            "reasoningEffort",
            "budgetTokens",
        ]
        nullable_fields = ["responseFormat"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


ListPromptVersionsProvider = Literal[
    "cohere",
    "openai",
    "anthropic",
    "huggingface",
    "replicate",
    "google",
    "google-ai",
    "azure",
    "aws",
    "anyscale",
    "perplexity",
    "groq",
    "fal",
    "leonardoai",
    "nvidia",
    "jina",
    "togetherai",
    "elevenlabs",
]

ListPromptVersionsRole = Literal[
    "system",
    "assistant",
    "user",
    "exception",
    "tool",
    "prompt",
    "correction",
    "expected_output",
]
r"""The role of the prompt message"""

ListPromptVersions2PromptsType = Literal["image_url"]


class ListPromptVersions2ImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    id: NotRequired[str]
    r"""The orq.ai id of the image"""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class ListPromptVersions2ImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    id: Optional[str] = None
    r"""The orq.ai id of the image"""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class ListPromptVersions22TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: ListPromptVersions2PromptsType
    image_url: ListPromptVersions2ImageURLTypedDict


class ListPromptVersions22(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: ListPromptVersions2PromptsType

    image_url: ListPromptVersions2ImageURL


ListPromptVersions2Type = Literal["text"]


class ListPromptVersions21TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: ListPromptVersions2Type
    text: str


class ListPromptVersions21(BaseModel):
    r"""Text content part of a prompt message"""

    type: ListPromptVersions2Type

    text: str


ListPromptVersionsContent2TypedDict = TypeAliasType(
    "ListPromptVersionsContent2TypedDict",
    Union[ListPromptVersions21TypedDict, ListPromptVersions22TypedDict],
)


ListPromptVersionsContent2 = TypeAliasType(
    "ListPromptVersionsContent2", Union[ListPromptVersions21, ListPromptVersions22]
)


ListPromptVersionsContentTypedDict = TypeAliasType(
    "ListPromptVersionsContentTypedDict",
    Union[str, List[ListPromptVersionsContent2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


ListPromptVersionsContent = TypeAliasType(
    "ListPromptVersionsContent", Union[str, List[ListPromptVersionsContent2]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


ListPromptVersionsPromptsType = Literal["function"]


class ListPromptVersionsFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class ListPromptVersionsFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class ListPromptVersionsToolCallsTypedDict(TypedDict):
    type: ListPromptVersionsPromptsType
    function: ListPromptVersionsFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class ListPromptVersionsToolCalls(BaseModel):
    type: ListPromptVersionsPromptsType

    function: ListPromptVersionsFunction

    id: Optional[str] = None

    index: Optional[float] = None


class ListPromptVersionsMessagesTypedDict(TypedDict):
    role: ListPromptVersionsRole
    r"""The role of the prompt message"""
    content: ListPromptVersionsContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[ListPromptVersionsToolCallsTypedDict]]


class ListPromptVersionsMessages(BaseModel):
    role: ListPromptVersionsRole
    r"""The role of the prompt message"""

    content: ListPromptVersionsContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[ListPromptVersionsToolCalls]] = None


class ListPromptVersionsPromptConfigTypedDict(TypedDict):
    r"""A list of messages compatible with the openAI schema"""

    messages: List[ListPromptVersionsMessagesTypedDict]
    stream: NotRequired[bool]
    model: NotRequired[str]
    model_db_id: NotRequired[str]
    r"""The id of the resource"""
    model_type: NotRequired[ListPromptVersionsModelType]
    r"""The type of the model"""
    model_parameters: NotRequired[ListPromptVersionsModelParametersTypedDict]
    r"""Model Parameters: Not all parameters apply to every model"""
    provider: NotRequired[ListPromptVersionsProvider]
    integration_id: NotRequired[Nullable[str]]
    r"""The id of the resource"""
    version: NotRequired[str]


class ListPromptVersionsPromptConfig(BaseModel):
    r"""A list of messages compatible with the openAI schema"""

    messages: List[ListPromptVersionsMessages]

    stream: Optional[bool] = None

    model: Optional[str] = None

    model_db_id: Optional[str] = None
    r"""The id of the resource"""

    model_type: Optional[ListPromptVersionsModelType] = None
    r"""The type of the model"""

    model_parameters: Optional[ListPromptVersionsModelParameters] = None
    r"""Model Parameters: Not all parameters apply to every model"""

    provider: Optional[ListPromptVersionsProvider] = None

    integration_id: OptionalNullable[str] = UNSET
    r"""The id of the resource"""

    version: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "stream",
            "model",
            "model_db_id",
            "model_type",
            "model_parameters",
            "provider",
            "integration_id",
            "version",
        ]
        nullable_fields = ["integration_id"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


ListPromptVersionsUseCases = Literal[
    "Agents",
    "Agents simulations",
    "API interaction",
    "Autonomous Agents",
    "Chatbots",
    "Classification",
    "Code understanding",
    "Code writing",
    "Documents QA",
    "Conversation",
    "Extraction",
    "Multi-modal",
    "Self-checking",
    "SQL",
    "Summarization",
    "Tagging",
]

ListPromptVersionsLanguage = Literal[
    "Chinese", "Dutch", "English", "French", "German", "Russian", "Spanish"
]
r"""The language that the prompt is written in. Use this field to categorize the prompt for your own purpose"""


class ListPromptVersionsMetadataTypedDict(TypedDict):
    use_cases: NotRequired[List[ListPromptVersionsUseCases]]
    r"""A list of use cases that the prompt is meant to be used for. Use this field to categorize the prompt for your own purpose"""
    language: NotRequired[ListPromptVersionsLanguage]
    r"""The language that the prompt is written in. Use this field to categorize the prompt for your own purpose"""


class ListPromptVersionsMetadata(BaseModel):
    use_cases: Optional[List[ListPromptVersionsUseCases]] = None
    r"""A list of use cases that the prompt is meant to be used for. Use this field to categorize the prompt for your own purpose"""

    language: Optional[ListPromptVersionsLanguage] = None
    r"""The language that the prompt is written in. Use this field to categorize the prompt for your own purpose"""


class ListPromptVersionsDataTypedDict(TypedDict):
    id: str
    type: ListPromptVersionsType
    prompt_config: ListPromptVersionsPromptConfigTypedDict
    r"""A list of messages compatible with the openAI schema"""
    timestamp: str
    created_by_id: NotRequired[str]
    updated_by_id: NotRequired[str]
    description: NotRequired[Nullable[str]]
    r"""The prompt’s description, meant to be displayable in the UI. Use this field to optionally store a long form explanation of the prompt for your own purpose"""
    metadata: NotRequired[ListPromptVersionsMetadataTypedDict]


class ListPromptVersionsData(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]

    type: ListPromptVersionsType

    prompt_config: ListPromptVersionsPromptConfig
    r"""A list of messages compatible with the openAI schema"""

    timestamp: str

    created_by_id: Optional[str] = None

    updated_by_id: Optional[str] = None

    description: OptionalNullable[str] = UNSET
    r"""The prompt’s description, meant to be displayable in the UI. Use this field to optionally store a long form explanation of the prompt for your own purpose"""

    metadata: Optional[ListPromptVersionsMetadata] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["created_by_id", "updated_by_id", "description", "metadata"]
        nullable_fields = ["description"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class ListPromptVersionsResponseBodyTypedDict(TypedDict):
    r"""Prompt versions retrieved."""

    object: ListPromptVersionsObject
    data: List[ListPromptVersionsDataTypedDict]
    has_more: bool


class ListPromptVersionsResponseBody(BaseModel):
    r"""Prompt versions retrieved."""

    object: ListPromptVersionsObject

    data: List[ListPromptVersionsData]

    has_more: bool
