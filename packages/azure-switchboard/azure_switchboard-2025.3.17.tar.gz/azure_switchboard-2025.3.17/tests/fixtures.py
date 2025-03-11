from openai.types.chat import ChatCompletion, ChatCompletionChunk
from openai.types.chat.chat_completion import Choice
from openai.types.chat.chat_completion_chunk import Choice as ChunkChoice
from openai.types.chat.chat_completion_chunk import ChoiceDelta
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from openai.types.completion_usage import CompletionUsage

from azure_switchboard import Deployment, ModelConfig


def _make_model_config() -> dict[str, ModelConfig]:
    return {
        "gpt-4o-mini": ModelConfig(
            model="gpt-4o-mini",
            tpm_ratelimit=10000,
            rpm_ratelimit=60,
        ),
        "gpt-4o": ModelConfig(
            model="gpt-4o",
            tpm_ratelimit=10000,
            rpm_ratelimit=60,
        ),
    }


TEST_DEPLOYMENT_1 = Deployment(
    name="test1",
    api_base="https://test1.openai.azure.com/",
    api_key="test1",
    models=_make_model_config(),
)

TEST_DEPLOYMENT_2 = Deployment(
    name="test2",
    api_base="https://test2.openai.azure.com/",
    api_key="test2",
    models=_make_model_config(),
)

TEST_DEPLOYMENT_3 = Deployment(
    name="test3",
    api_base="https://test3.openai.azure.com/",
    api_key="test3",
    models=_make_model_config(),
)


MOCK_STREAM_CHUNKS = [
    ChatCompletionChunk(
        id="test_chunk_1",
        choices=[
            ChunkChoice(
                delta=ChoiceDelta(content="Hello", role="assistant"),
                finish_reason=None,
                index=0,
            )
        ],
        created=1234567890,
        model="gpt-4o-mini",
        object="chat.completion.chunk",
        usage=None,
    ),
    ChatCompletionChunk(
        id="test_chunk_2",
        choices=[
            ChunkChoice(
                delta=ChoiceDelta(content=", "),
                finish_reason=None,
                index=0,
            )
        ],
        created=1234567890,
        model="gpt-4o-mini",
        object="chat.completion.chunk",
        usage=None,
    ),
    ChatCompletionChunk(
        id="test_chunk_3",
        choices=[
            ChunkChoice(
                delta=ChoiceDelta(content="world!"),
                finish_reason=None,
                index=0,
            )
        ],
        created=1234567890,
        model="gpt-4o-mini",
        object="chat.completion.chunk",
        usage=None,
    ),
    ChatCompletionChunk(
        id="test_chunk_4",
        choices=[
            ChunkChoice(
                delta=ChoiceDelta(),
                finish_reason="stop",
                index=0,
            )
        ],
        created=1234567890,
        model="gpt-4o-mini",
        object="chat.completion.chunk",
        usage=CompletionUsage(
            completion_tokens=5,
            prompt_tokens=15,
            total_tokens=20,
        ),
    ),
]

MOCK_COMPLETION = ChatCompletion(
    id="test",
    choices=[
        Choice(
            finish_reason="stop",
            index=0,
            message=ChatCompletionMessage(
                content="Hello, world!",
                role="assistant",
            ),
        )
    ],
    created=1234567890,
    model="gpt-4o-mini",
    object="chat.completion",
    usage=CompletionUsage(
        completion_tokens=3,
        prompt_tokens=8,
        total_tokens=11,
    ),
)

MOCK_COMPLETION_RAW = {
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": None,
            "message": {
                "content": "Hello! How can I assist you today?",
                "refusal": None,
                "role": "assistant",
            },
        }
    ],
    "created": 1741124380,
    "id": "chatcmpl-test",
    "model": "gpt-4o-mini",
    "object": "chat.completion",
    "service_tier": "default",
    "system_fingerprint": "fp_06737a9306",
    "usage": {
        "completion_tokens": 10,
        "completion_tokens_details": {
            "accepted_prediction_tokens": 0,
            "audio_tokens": 0,
            "reasoning_tokens": 0,
            "rejected_prediction_tokens": 0,
        },
        "prompt_tokens": 8,
        "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
        "total_tokens": 18,
    },
}

MOCK_COMPLETION_PARSED = ChatCompletion.model_validate(MOCK_COMPLETION_RAW)


BASIC_CHAT_COMPLETION_ARGS = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "Hello, world!"}],
}
