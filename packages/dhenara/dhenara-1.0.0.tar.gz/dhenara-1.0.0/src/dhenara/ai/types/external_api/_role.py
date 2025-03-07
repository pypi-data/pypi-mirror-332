# -----------------------------------------------------------------------------
from dhenara.ai.types.shared.base import BaseEnum


class OpenAiMessageRoleEnum(BaseEnum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class GoogleAiMessageRoleEnum(BaseEnum):
    USER = "user"
    MODEL = "model"


class AnthropicMessageRoleEnum(BaseEnum):
    USER = "user"
    ASSISTANT = "assistant"
    # NOTE:  To include a system prompt, you can use the top-level system parameter — there is no "system" role for input messages in the Messages API.
    # SYSTEM = "system"
