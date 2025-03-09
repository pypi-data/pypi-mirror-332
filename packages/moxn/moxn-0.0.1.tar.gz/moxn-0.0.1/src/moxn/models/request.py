from typing import Literal, overload, Any, cast, Sequence, Optional
from uuid import UUID

from anthropic.types import Message
from openai.types.chat import ChatCompletion
from pydantic import BaseModel, Field

from moxn import base_models
from moxn.models import prompt as pr
from moxn.telemetry.utils import unpack_llm_response_content
from moxn.base_models.content import AnthropicMessagesParam, OpenAIMessagesParam
from moxn.base_models.telemetry import LLMEvent


# Add these Pydantic models for image handling
class ImageProviderOptions(BaseModel):
    mime: str
    key: str | None = None


class ImageData(BaseModel):
    format: str
    base64: str
    url: str | None = None
    providerOptions: ImageProviderOptions


class ImageMetadata(BaseModel):
    type: str
    mime: str
    key: Optional[str] = None
    src: Optional[str] = None
    imageData: ImageData


class ContentBlock(BaseModel):
    content: str
    metadata: ImageMetadata


class Request(base_models._Request):
    """Immutable representation of a stored request configuration."""

    prompts: Sequence[pr.Prompt] = Field(default_factory=list)

    # Keep only the core data access methods
    def get_prompt_by_role(
        self, role: str | base_models.PromptRole
    ) -> pr.Prompt | None:
        """Get the first prompt with the specified role."""
        role = base_models.PromptRole(role) if isinstance(role, str) else role
        prompts = [p for p in self.prompts if p.role == role]
        if len(prompts) == 1:
            return prompts[0]
        elif len(prompts) == 0:
            return None
        else:
            raise ValueError(
                f"get prompt is not deterministic, there are {len(prompts)} {role.value} prompts in the request"
            )

    def get_prompts_by_role(
        self, role: str | base_models.PromptRole
    ) -> list[pr.Prompt]:
        """Get all prompts with the specified role."""
        role = base_models.PromptRole(role) if isinstance(role, str) else role
        return [p for p in self.prompts if p.role == role]

    def get_prompt_by_name(self, name: str) -> pr.Prompt:
        """Helper to get prompt by name"""
        matching = [p for p in self.prompts if p.name == name]
        if not matching:
            raise ValueError(f"No prompt found with name: {name}")
        if len(matching) > 1:
            raise ValueError(f"Multiple prompts found with name: {name}")
        return matching[0]

    def _get_selected_prompts(
        self,
        prompt_names: list[str] | None = None,
        prompts: list[pr.Prompt] | None = None,
    ) -> list[pr.Prompt]:
        """Internal method to get selected prompts based on various criteria."""
        if prompt_names:
            return [self.get_prompt_by_name(name) for name in prompt_names]
        elif prompts:
            return prompts
        else:
            # Use prompt_order if available, otherwise fall back to default role ordering
            if self.prompt_order:
                prompt_map = {str(p.id): p for p in self.prompts}
                return [
                    prompt_map[str(pid)]
                    for pid in self.prompt_order
                    if str(pid) in prompt_map
                ]
            else:
                # Fall back to default role ordering
                selected_prompts = []
                for role in [
                    base_models.PromptRole.SYSTEM,
                    base_models.PromptRole.USER,
                    base_models.PromptRole.ASSISTANT,
                ]:
                    prompt = self.get_prompt_by_role(role)
                    if prompt:
                        selected_prompts.append(prompt)
                return selected_prompts

    def create_instance(
        self,
        prompt_names: list[str] | None = None,
        prompts: list[pr.Prompt] | None = None,
        **variables,
    ) -> "RequestInstance":
        """Create a new RequestInstance for managing runtime state."""
        return RequestInstance.from_request(
            self, prompt_names=prompt_names, prompts=prompts, **variables
        )


class RequestInstance:
    """Manages the runtime state and operations for a request execution."""

    def __init__(
        self,
        base_request: Request,
        selected_prompts: list[pr.Prompt],
        variables: dict | None = None,
    ):
        self.base_request = base_request
        self.prompts = selected_prompts
        self.variables = variables or {}
        self.conversation_history: list[pr.Prompt] = []

    @property
    def request_id(self) -> UUID:
        return self.base_request.id

    @property
    def request_version_id(self) -> UUID:
        return self.base_request.version_id

    @classmethod
    def from_request(
        cls,
        request: Request,
        prompt_names: list[str] | None = None,
        prompts: list[pr.Prompt] | None = None,
        **variables,
    ) -> "RequestInstance":
        """Create a RequestInstance from a base Request."""
        if prompt_names and prompts:
            raise ValueError("Cannot specify both prompt_names and prompts")

        selected_prompts = request._get_selected_prompts(prompt_names, prompts)
        return cls(request, selected_prompts, variables)

    @overload
    def append_message(
        self,
        content: Message,
        provider: Literal[base_models.Provider.ANTHROPIC],
        name: str = "",
        description: str = "",
        author=base_models.Author.MACHINE,
        role=base_models.PromptRole.ASSISTANT,
    ) -> None: ...

    @overload
    def append_message(
        self,
        content: ChatCompletion,
        provider: Literal[base_models.Provider.OPENAI],
        name: str = "",
        description: str = "",
        author=base_models.Author.MACHINE,
        role=base_models.PromptRole.ASSISTANT,
    ) -> None: ...

    def append_message(
        self,
        content: ChatCompletion | Message,
        provider: base_models.Provider,
        name: str = "",
        description: str = "",
        author=base_models.Author.MACHINE,
        role=base_models.PromptRole.ASSISTANT,
    ) -> None:
        """Append a message to the conversation history."""
        new_prompt = pr.Prompt.from_provider_response(
            content=content,
            provider=provider,
            name=name,
            description=description,
            author=author,
            role=role,
        )
        self.conversation_history.append(new_prompt)

    def append_text(
        self,
        text: str,
        name: str = "",
        description: str = "",
        author=base_models.Author.HUMAN,
        role=base_models.PromptRole.USER,
    ) -> None:
        """
        Append a text message to the conversation history.

        Args:
            text: The text content to add
            name: Optional name for the prompt
            description: Optional description for the prompt
            author: Who created this content (default: HUMAN)
            role: The role of this content (default: USER)
        """
        # Create blocks structure for text content
        blocks = {
            "blocks": [
                {
                    "content": text,
                    "metadata": {
                        "type": "text",
                    },
                }
            ]
        }

        new_prompt = pr.Prompt(
            id=None,
            versionId=None,
            name=name,
            description=description,
            author=author,
            role=role,
            blocks=blocks,
        )
        self.conversation_history.append(new_prompt)

    def append_image(
        self,
        image_data: str,
        media_type: Literal["image/png", "image/jpeg"],
        image_url: str | None = None,
        key: str | None = None,
        name: str = "",
        description: str = "",
        author=base_models.Author.HUMAN,
        role=base_models.PromptRole.USER,
    ) -> None:
        """
        Append an image to the conversation history.

        Args:
            image_data: Base64-encoded image data (without the "data:image/..." prefix)
            media_type: The MIME type of the image ("image/png" or "image/jpeg")
            image_url: Optional URL to the image
            key: Optional unique identifier for the image
            name: Optional name for the prompt
            description: Optional description for the prompt
            author: Who created this content (default: HUMAN)
            role: The role of this content (default: USER)
        """
        # Format the image content as markdown
        image_markdown = "![]("
        if image_url:
            image_markdown += image_url
        image_markdown += ")\n\n"

        provider_options = ImageProviderOptions(
            mime=media_type, key=key if key else None
        )

        image_data_obj = ImageData(
            format="base64",
            base64=f"data:{media_type};base64,{image_data}",
            url=image_url,
            providerOptions=provider_options,
        )

        metadata = ImageMetadata(
            type="image",
            mime=media_type,
            key=key,
            src=image_url,
            imageData=image_data_obj,
        )

        content_block = ContentBlock(content=image_markdown, metadata=metadata)

        # Convert to dictionary for the blocks structure
        blocks = {"blocks": [content_block.model_dump(exclude_none=True)]}

        new_prompt = pr.Prompt(
            id=None,
            versionId=None,
            name=name,
            description=description,
            author=author,
            role=role,
            blocks=blocks,
        )
        self.conversation_history.append(new_prompt)

    def append_content(
        self,
        blocks: list[dict],
        name: str = "",
        description: str = "",
        author=base_models.Author.HUMAN,
        role=base_models.PromptRole.USER,
    ) -> None:
        """
        Append mixed content (text and/or images) to the conversation history.

        This method accepts pre-formatted blocks that match the internal block structure.
        For simpler use cases, consider using append_text() or append_image().

        Args:
            blocks: List of properly formatted content blocks
            name: Optional name for the prompt
            description: Optional description for the prompt
            author: Who created this content (default: HUMAN)
            role: The role of this content (default: USER)
        """
        # Create blocks structure
        blocks_data = {"blocks": blocks}

        new_prompt = pr.Prompt(
            id=None,
            versionId=None,
            name=name,
            description=description,
            author=author,
            role=role,
            blocks=blocks_data,
        )
        self.conversation_history.append(new_prompt)

    @overload
    def to_provider_messages(
        self,
        provider: Literal[base_models.Provider.ANTHROPIC],
    ) -> AnthropicMessagesParam: ...

    @overload
    def to_provider_messages(
        self,
        provider: Literal[base_models.Provider.OPENAI],
    ) -> OpenAIMessagesParam: ...

    def to_provider_messages(
        self,
        provider: base_models.Provider,
    ) -> AnthropicMessagesParam | OpenAIMessagesParam:
        """Convert current state to provider-specific messages."""
        all_prompts = self.prompts + self.conversation_history

        if provider == base_models.Provider.ANTHROPIC:
            # Handle Anthropic's special system message format
            if all_prompts and all_prompts[0].role == base_models.PromptRole.SYSTEM:
                # Explicitly request a TextBlockParam for the system message
                system = [
                    all_prompts[0].to_provider_message_param(
                        base_models.Provider.ANTHROPIC,
                        role=base_models.PromptRole.SYSTEM,
                        **self.variables,
                    )
                ]

                # Get messages from remaining prompts
                messages = [
                    p.to_provider_message_param(
                        base_models.Provider.ANTHROPIC, **self.variables
                    )
                    for p in all_prompts[1:]
                ]

                # Create properly typed AnthropicMessagesParam
                return AnthropicMessagesParam(system=system, messages=messages)
            else:
                # No system message, just regular messages
                messages = [
                    p.to_provider_message_param(
                        base_models.Provider.ANTHROPIC, **self.variables
                    )
                    for p in all_prompts
                ]

                # Create properly typed AnthropicMessagesParam with no system
                return AnthropicMessagesParam(system=None, messages=messages)

        elif provider == base_models.Provider.OPENAI:
            # For OpenAI, convert all prompts to messages
            messages = [
                p.to_provider_message_param(
                    base_models.Provider.OPENAI, **self.variables
                )
                for p in all_prompts
            ]

            # Create properly typed OpenAIMessagesParam
            return OpenAIMessagesParam(messages=messages)

        else:
            raise ValueError(f"Unsupported provider: {provider}")

    @overload
    def to_provider_payload(
        self,
        provider: Literal[base_models.Provider.ANTHROPIC],
    ) -> dict[str, str | list[dict[str, Any]]]: ...

    @overload
    def to_provider_payload(
        self,
        provider: Literal[base_models.Provider.OPENAI],
    ) -> dict[str, list[dict[str, Any]]]: ...

    def to_provider_payload(
        self,
        provider: base_models.Provider,
    ) -> dict[str, Any]:
        """Convert current state to provider-specific payload"""
        if provider == base_models.Provider.ANTHROPIC:
            return cast(
                dict[str, Any],
                self.to_provider_messages(base_models.Provider.ANTHROPIC).model_dump(
                    by_alias=True
                ),
            )
        elif provider == base_models.Provider.OPENAI:
            return cast(
                dict[str, Any],
                self.to_provider_messages(base_models.Provider.OPENAI).model_dump(
                    by_alias=True
                ),
            )
        else:
            raise ValueError(f"Unsupported provider: {provider}")

    @overload
    async def create_llm_event(
        self,
        response: Message,
        provider: Literal[base_models.Provider.ANTHROPIC],
        raw_input: BaseModel | None,
        rendered_input: dict[str, Any] | None,
        attributes: dict | None = None,
    ) -> LLMEvent: ...

    @overload
    async def create_llm_event(
        self,
        response: ChatCompletion,
        provider: Literal[base_models.Provider.OPENAI],
        raw_input: BaseModel | None,
        rendered_input: dict[str, Any] | None,
        attributes: dict | None = None,
    ) -> LLMEvent: ...

    async def create_llm_event(
        self,
        response: ChatCompletion | Message,
        provider: base_models.Provider,
        raw_input: BaseModel | None,
        rendered_input: dict[str, Any] | None,
        attributes: dict | None = None,
    ) -> LLMEvent:
        """Creates an LLM event from the current state."""
        parsed_response = unpack_llm_response_content(response, provider)
        return LLMEvent(
            prompts=[
                (
                    {"id": p.id, "version_id": p.version_id}
                    if p.id
                    else p.model_dump(mode="json", by_alias=True)
                )
                for p in self.prompts + self.conversation_history
            ],
            provider=provider,
            llm_response_content=parsed_response.content,
            llm_response_tool_calls=[
                tool_call.model_dump(by_alias=True)
                for tool_call in parsed_response.tool_calls
            ],
            raw_input=raw_input.model_dump(by_alias=True) if raw_input else None,
            rendered_input=rendered_input,
            attributes=attributes,
        )
