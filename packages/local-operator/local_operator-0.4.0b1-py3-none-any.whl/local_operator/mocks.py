import asyncio

from langchain_core.messages import BaseMessage

from local_operator.types import ActionType, ConversationRole, ResponseJsonSchema

USER_MOCK_RESPONSES = {
    "hello": ResponseJsonSchema(
        response="Hello! I am the test model.",
        code="",
        action=ActionType.DONE,
        learnings="",
        content="",
        file_path="",
        replacements=[],
    ),
    "please proceed according to your plan": ResponseJsonSchema(
        response='I will execute a simple Python script to print "Hello World".',
        code='print("Hello World")',
        action=ActionType.CODE,
        learnings="",
        content="",
        file_path="",
        replacements=[],
    ),
    "think aloud about what you will need to do": (
        "I will need to print 'Hello World' to the console."
    ),
    "hello world": ResponseJsonSchema(
        response="I have printed 'Hello World' to the console.",
        code="",
        action=ActionType.DONE,
        learnings="",
        content="",
        file_path="",
        replacements=[],
    ),
}


class ChatMock:
    """A test model that returns predefined responses for specific inputs."""

    temperature: float | None
    model: str | None
    model_name: str | None
    api_key: str | None
    base_url: str | None
    max_tokens: int | None
    top_p: float | None
    frequency_penalty: float | None
    presence_penalty: float | None

    def __init__(self):
        self.temperature = 0.3
        self.model = "test-model"
        self.model_name = "test-model"
        self.api_key = None
        self.base_url = None
        self.max_tokens = 4096
        self.top_p = 0.9
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0

    async def ainvoke(self, messages):
        """Mock ainvoke method that returns predefined responses.

        Args:
            messages: List of message dicts with role and content

        Returns:
            BaseMessage instance containing the response
        """
        if not messages:
            raise ValueError("No messages provided to ChatMock")

        # Only consider the last message coming from the user
        user_message = ""
        for msg in reversed(list(messages)):
            if msg.get("role") == ConversationRole.USER.value:
                user_message = msg.get("content", "")
                break

        user_message_lower = user_message.lower()

        # Find closest matching response by partial string match
        closest_match = None
        max_match_length = 0
        for key in USER_MOCK_RESPONSES:
            key_lower = key.lower()
            if key_lower in user_message_lower and len(key_lower) > max_match_length:
                closest_match = key
                max_match_length = len(key_lower)

        if closest_match:
            response = USER_MOCK_RESPONSES[closest_match]
            return BaseMessage(
                content=(
                    response.model_dump_json()
                    if isinstance(response, ResponseJsonSchema)
                    else response
                ),
                type=ConversationRole.ASSISTANT.value,
            )

        # Pass through the last message if no match found
        return BaseMessage(
            content=ResponseJsonSchema(
                response=f"No mock response for message: {user_message}",
                code="",
                action=ActionType.DONE,
                learnings="",
                content="",
                file_path="",
                replacements=[],
            ).model_dump_json(),
            type=ConversationRole.ASSISTANT.value,
        )

    def invoke(self, messages):
        """Synchronous version of ainvoke."""
        return asyncio.run(self.ainvoke(messages))

    def stream(self, messages):
        """Mock stream method that yields chunks of the response."""
        response = self.invoke(messages)
        yield response

    async def astream(self, messages):
        """Mock astream method that asynchronously yields chunks of the response."""
        response = await self.ainvoke(messages)
        yield response


class ChatNoop:
    """A test model that returns an empty response."""

    temperature: float | None
    model: str | None
    model_name: str | None
    api_key: str | None
    base_url: str | None
    max_tokens: int | None
    top_p: float | None
    frequency_penalty: float | None
    presence_penalty: float | None

    def __init__(self):
        self.temperature = 0.3
        self.model = "noop-model"
        self.model_name = "noop-model"
        self.api_key = None
        self.base_url = None
        self.max_tokens = 4096
        self.top_p = 0.9
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0

    async def ainvoke(self, messages):
        """Async version that returns an empty response."""
        return BaseMessage(content="", type=ConversationRole.ASSISTANT.value)

    def invoke(self, messages):
        """Synchronous version that returns an empty response."""
        return asyncio.run(self.ainvoke(messages))

    def stream(self, messages):
        """Mock stream method that yields an empty response."""
        response = self.invoke(messages)
        yield response

    async def astream(self, messages):
        """Mock astream method that asynchronously yields an empty response."""
        response = await self.ainvoke(messages)
        yield response
