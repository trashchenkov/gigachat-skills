# Chat

Use this file for the default direct-SDK chat path.

## Default path

1. For the current stable PyPI SDK line, pass a string or `Chat(messages=[...])` to `client.chat(...)`.
2. For incremental UX, use `client.stream(...)`.
3. For async, use `client.achat(...)` and `client.astream(...)`.
4. For message history or richer payloads, use `Chat`, `Messages`, and `MessagesRole`.
5. Re-check the installed SDK before using newer `client.chat.create(...)` examples; upstream README/docs mention a primary `chat/completions` surface, but the inspected stable `gigachat==0.2.1` package does not expose that API.

Status: `smoke-covered`

## Minimal usage

```python
from gigachat import GigaChat

# GigaChat() automatically uses standard GIGACHAT_* environment variables
# such as GIGACHAT_CREDENTIALS when they are already loaded.
with GigaChat() as client:
    response = client.chat("Hello, GigaChat!")
    print(response.choices[0].message.content)
```

Status: `smoke-covered`

## Explicit message history

The API does not keep ordinary chat history for you. Send the full history in every request.

```python
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

payload = Chat(
    messages=[
        Messages(role=MessagesRole.SYSTEM, content="Reply briefly."),
        Messages(role=MessagesRole.USER, content="My name is Alex."),
        Messages(role=MessagesRole.ASSISTANT, content="Hi Alex."),
        Messages(role=MessagesRole.USER, content="What is my name?"),
    ]
)

with GigaChat() as client:
    response = client.chat(payload)
    print(response.choices[0].message.content)
```

Status: `smoke-covered`

## Request-shaping rules

- use one `system` message at the start for durable behavior instructions
- keep `user` and `assistant` turns explicit
- pass attachments at the message level when the model should inspect uploaded files
- switch to typed payloads once the request includes history, attachments, functions, response format, or reasoning settings

Status: `source-backed`

## Generation parameters

Common request parameters include:

- `temperature`
- `top_p`
- `max_tokens`
- `repetition_penalty`
- `n`
- `reasoning_effort` where supported by the selected model

Default rule:

- lower `temperature` first when you need more deterministic output

Status: `source-backed`

## Streaming

```python
from gigachat import GigaChat

with GigaChat() as client:
    for chunk in client.stream("Write a short poem about code."):
        print(chunk.choices[0].delta.content, end="", flush=True)
```

Status: `smoke-covered`

## Async

```python
import asyncio
from gigachat import GigaChat

async def main():
    async with GigaChat() as client:
        result = await client.achat("Summarize recursion in one sentence.")
        print(result.choices[0].message.content)

asyncio.run(main())
```

Status: `source-backed`

## Forward-looking `chat/completions` note

Upstream README/docs mention a newer primary surface:

- `client.chat.create(...)`
- `client.chat.stream(...)`
- `client.chat.parse(...)`
- async analogs under `client.achat`
- primary models such as `ChatCompletionRequest` and `ChatMessage`

However, a review against stable PyPI `gigachat==0.2.1` found that `client.chat` is still a method and `gigachat.models` does not expose those primary model names. Do not use these snippets as the default until the installed SDK version actually exposes them.

Status: `source-backed caution`

## Streaming behavior

- the underlying API uses SSE
- chunks arrive in `choices[0].delta.content`
- concatenate deltas in UI code

Status: `source-backed`

## When to switch away from plain chat

- need tools -> `gigachat-sdk-functions`
- need embeddings or file workflows -> `gigachat-sdk-files-embeddings`
- need LangChain abstractions -> `langchain-gigachat`
- need OpenAI-compatible or Anthropic-compatible clients -> `gpt2giga`
- need Deep Agents harness/profile behavior -> `deepagents-gigachat`

Status: `source-backed`
