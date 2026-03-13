# Chat

Use this file for the default direct-SDK chat path.

## Default path

1. For a trivial one-shot prompt, pass a string to `client.chat(...)`.
2. For message history or richer payloads, use `Chat(messages=[...])`.
3. For incremental UX, use `client.stream(...)`.
4. For concurrency-sensitive code, use async only when it is actually needed.

Status: `verified`

## Minimal usage

```python
from gigachat import GigaChat

with GigaChat() as client:
    response = client.chat("Hello, GigaChat!")
    print(response.choices[0].message.content)
```

Status: `verified`

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

Status: `docs/code-backed`

## Request-shaping rules

- use one `system` message at the start for durable behavior instructions
- keep `user` and `assistant` turns explicit
- pass attachments at the payload level when the model should inspect uploaded files
- switch to typed payloads once the request includes history, attachments, or functions

Status: `verified`

## Generation parameters

- `temperature`
- `top_p`
- `max_tokens`
- `repetition_penalty`
- `n`

Default rule:

- lower `temperature` first when you need more deterministic output

Status: `docs/code-backed`

## Streaming

```python
from gigachat import GigaChat

with GigaChat() as client:
    for chunk in client.stream("Write a short poem about code."):
        print(chunk.choices[0].delta.content, end="", flush=True)
```

Status: `verified`

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

Status: `docs/code-backed`

## Streaming behavior

- the underlying API uses SSE
- chunks arrive in `choices[0].delta.content`
- concatenate deltas in UI code

Status: `docs/code-backed`

## When to switch away from plain chat

- need tools -> `gigachat-sdk-functions`
- need embeddings or file workflows -> `gigachat-sdk-files-embeddings`
- need LangChain abstractions -> `langchain-gigachat`
- need OpenAI-compatible or Anthropic-compatible clients -> `gpt2giga`

Status: `verified`
