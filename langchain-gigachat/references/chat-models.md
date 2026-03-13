# Chat Models

Use this file when the app already depends on LangChain abstractions.

## Default path

1. Keep auth and TLS config aligned with the native SDK.
2. Work with LangChain message objects, not raw GigaChat payloads.
3. Use wrapper-native chat, streaming, tools, and structured output where available.
4. Drop to raw SDK details only when debugging wrapper boundaries or when the wrapper lacks a required feature.

Status: `verified`

## Installation

```bash
pip install -U langchain-gigachat
```

Status: `docs/code-backed`

## Minimal initialization

```python
from langchain_gigachat.chat_models import GigaChat

llm = GigaChat(
    credentials="YOUR_AUTHORIZATION_KEY",
    verify_ssl_certs=False,
)
```

Status: `docs/code-backed`

## Basic invocation

```python
from langchain_core.messages import HumanMessage

response = llm.invoke([HumanMessage(content="Hello")])
print(response.content)
```

Status: `verified`

## Wrapper behavior

- LangChain messages are converted into GigaChat message structures
- tool calls are mapped between LangChain and GigaChat formats
- streaming works through LangChain streaming APIs and callbacks
- auth inputs mirror the native SDK

Status: `docs/code-backed`

## Tool and schema caveats

- complex JSON-schema constructs may need flattening
- prefer Pydantic models or plain object schemas
- if a tool/schema issue appears, inspect both the LangChain object and the final mapped payload

Status: `docs/code-backed`

## Practical rules

- stay inside LangChain message types unless debugging an adapter issue
- do not mix lower-level SDK code into normal LangChain application logic
- if raw SDK chat is not working yet, fix setup before debugging LangChain behavior

Status: `verified`
