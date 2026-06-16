# Chat Models

Use this file when the app already depends on LangChain abstractions.

## Default path

1. Keep auth and TLS config aligned with the native SDK.
2. Work with LangChain message objects and runnables, not raw GigaChat payloads.
3. Use `invoke()` / `ainvoke()` and streaming APIs; do not use removed legacy `predict()` / `apredict()` patterns.
4. Use wrapper-native tools, structured output, multimodal inputs, and reasoning options where supported by the installed version.
5. Drop to raw SDK details only when debugging wrapper boundaries or when the wrapper lacks a required feature.

Status: `source-backed`

## Installation

```bash
pip install -U langchain-gigachat
```

Current 0.5.x releases require modern LangChain Core and Python 3.10+.

Status: `source-backed`

## Minimal initialization

```python
from langchain_gigachat import GigaChat

# Uses standard GIGACHAT_* environment variables when they are already loaded.
llm = GigaChat()
```

Pass constructor arguments only when overriding the environment for this instance:

```python
from langchain_gigachat import GigaChat

llm = GigaChat(verify_ssl_certs=True)
```

For local development with certificate issues, `verify_ssl_certs=False` can be used temporarily, but do not make it a production default.

Status: `source-backed`

## Basic invocation

```python
from langchain_core.messages import HumanMessage

response = llm.invoke([HumanMessage(content="Hello")])
print(response.content)
```

Status: `smoke-covered`

## Wrapper behavior

- LangChain messages are converted into GigaChat message structures
- tool calls are mapped between LangChain and GigaChat formats
- streaming works through LangChain streaming APIs and callbacks
- auth inputs mirror the native SDK
- 0.5.x supports LangChain Core 1.x and Pydantic V2

Status: `source-backed`

## Structured output

Use `with_structured_output(...)` for schema-bound responses when the installed version supports it. 0.5.x release notes describe native JSON Schema structured output and a restored `format_instructions` mode.

Status: `source-backed`

## Reasoning and multimodal notes

0.5.x release notes describe support for reasoning models and multimodal image/audio/document inputs through the wrapper and file APIs. Keep exact parameter names source-checked against the installed version before writing production snippets.

Status: `source-backed caution`

## Tool and schema caveats

- complex JSON-schema constructs may need flattening
- prefer Pydantic models or plain object schemas
- if a tool/schema issue appears, inspect both the LangChain object and the final mapped payload
- avoid double retries when LangChain and the SDK are both configured to retry

Status: `source-backed`

## Practical rules

- stay inside LangChain message types unless debugging an adapter issue
- do not mix lower-level SDK code into normal LangChain application logic
- if raw SDK chat is not working yet, fix setup before debugging LangChain behavior
- for Deep Agents harness profiles, switch to `deepagents-gigachat`

Status: `source-backed`
