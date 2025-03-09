from enum import Enum
from typing import Any, Optional
from pydantic import BaseModel, Field, ConfigDict
from moxn.base_models import NOT_GIVEN, NotGivenOr, BaseModelWithOptionalFields


# Define your Schema types in Python for reference
SchemaPropertyType = str  # 'string' | 'number' | 'boolean' | 'object' | 'array'
SchemaPropertyFormat = str  # 'text' | 'date' | 'date-time' | 'email' | 'uri' | 'uuid'
SchemaReference = dict[str, str]


# Align these with backend via NOT_GIVEN - backend needs tests and validation to support
class SchemaPropertyConstraints(BaseModel):
    # String constraints
    minLength: int | None = None
    maxLength: int | None = None
    pattern: str | None = None
    format: Optional[SchemaPropertyFormat] = None
    enum: list[str | int | bool] | None = None

    # Number constraints
    minimum: int | float | None = None
    maximum: int | float | None = None
    multipleOf: int | float | None = None

    # Array constraints
    minItems: int | None = None
    maxItems: int | None = None
    uniqueItems: bool | None = None

    # Object constraints
    additionalProperties: bool | None = None

    # Common
    nullable: bool | None = None

    # Variable Display
    displayMode: str | None = None  # 'inline' | 'block'


class SchemaProperty(BaseModelWithOptionalFields):
    name: str
    type: SchemaPropertyType
    description: str
    properties: NotGivenOr[list["SchemaProperty"]] = NOT_GIVEN  # For object type
    items: NotGivenOr[Optional["SchemaProperty"]] = NOT_GIVEN  # For array type
    constraints: NotGivenOr[SchemaPropertyConstraints] = NOT_GIVEN
    schemaRef: NotGivenOr[SchemaReference] = NOT_GIVEN
    defaultContent: NotGivenOr[Any] = NOT_GIVEN


class Schema(BaseModel):
    name: str
    description: str | None = None
    properties: list[SchemaProperty]
    strict: bool = False


class SchemaRequestType(str, Enum):
    ALL = "all"
    INPUT = "input"
    OUTPUT = "output"


class PromptType(str, Enum):
    PROMPT = "prompt"
    SCHEMA_INPUT = "input"
    SCHEMA_OUTPUT = "output"


class SchemaWithMetadata(BaseModel):
    moxn_schema: Schema = Field(alias="schema")
    created_at: str = Field(alias="createdAt")
    updated_at: str = Field(alias="updatedAt")
    prompt_id: str = Field(alias="promptId")
    prompt_version_id: str = Field(alias="promptVersionId")
    request_id: str = Field(alias="requestId")
    request_version_id: str = Field(alias="requestVersionId")
    prompt_type: PromptType = Field(alias="schemaType")

    model_config = ConfigDict(
        populate_by_name=True,  # Allow both alias and Python names
        alias_generator=lambda s: "".join(
            word.capitalize() if i > 0 else word for i, word in enumerate(s.split("_"))
        ),
    )


class RequestSchemas(BaseModel):
    input: SchemaWithMetadata | None = None
    outputs: list[SchemaWithMetadata] = Field(default_factory=list)

    model_config = ConfigDict(populate_by_name=True)


class MoxnPromptMetadata(BaseModel):
    prompt_id: str
    prompt_version_id: str
    request_id: str
    request_version_id: str
    prompt_type: PromptType

    model_config = ConfigDict(use_enum_values=True)


class MoxnBaseModel(BaseModel):
    """Base model that includes prompt metadata configuration"""

    model_version_config: dict[str, MoxnPromptMetadata | None] = {
        "metadata": None  # Initially None, must be set before model instantiation
    }

    @classmethod
    def set_metadata(cls, metadata: MoxnPromptMetadata) -> None:
        """Set the metadata for this model class"""
        cls.model_version_config["metadata"] = metadata


class CodegenResponse(BaseModel):
    """Response model for code generation requests"""

    files: dict[str, str]


SchemaProperty.model_rebuild()
