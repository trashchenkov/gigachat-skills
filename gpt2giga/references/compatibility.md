# Compatibility

Use this file when preserving an OpenAI-style or Anthropic-style client matters more than native GigaChat control.

## Default rule

Treat `gpt2giga` as a compatibility layer, not as a byte-for-byte replacement for OpenAI or Anthropic behavior.

Status: `source-backed`

## Stable API families

Current stable documentation describes support for:

- OpenAI-compatible `GET /models`
- OpenAI-compatible `POST /chat/completions`
- OpenAI-compatible `POST /responses`
- OpenAI-compatible `POST /embeddings`
- Anthropic-compatible `POST /messages`
- Anthropic-compatible `POST /messages/count_tokens`
- LiteLLM-compatible `GET /model/info`
- system endpoints such as `/health` and `/ping`

Status: `source-backed`

## Disabled or out-of-scope APIs

Stable docs describe Files and Batches routes as disabled until the required GigaChat SDK/backend support is available end-to-end.

Not a project goal:

- full OpenAI parity for audio, image generation/editing, fine-tuning, assistants, threads, runs, vector stores, uploads, moderations, or realtime
- full Anthropic parity for Files beta, Skills beta, Agents beta, Sessions, Environments, or Admin API

Status: `source-backed caution`

## Important mapping behavior

- client payloads are transformed into normalized internal messages and then into GigaChat requests
- tool/function schemas are mapped into GigaChat-compatible structures
- structured output is supported where it can be mapped safely
- reasoning flags and unsupported optional parameters may be accepted, mapped, or safely ignored depending on route/support
- transport headers, client API keys, cookies, and unsafe metadata are filtered before upstream calls

Status: `source-backed`

## Model handling

When model pass-through is enabled or defaulted by the deployed config, client model names can affect GigaChat model selection. Otherwise, proxy configuration decides the upstream model. Always check the proxy configuration before assuming the client-side `model` field wins.

Status: `source-backed`

## Typical OpenAI client example

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8090/v1", api_key="<GPT2GIGA_API_KEY>")

response = client.chat.completions.create(
    model="GigaChat-2-Max",
    messages=[{"role": "user", "content": "Привет"}],
)
print(response.choices[0].message.content)
```

Status: `source-backed`

## Typical Anthropic client example

```python
from anthropic import Anthropic

client = Anthropic(base_url="http://localhost:8090", api_key="<GPT2GIGA_API_KEY>")

response = client.messages.create(
    model="GigaChat-2-Max",
    max_tokens=256,
    messages=[{"role": "user", "content": "Привет"}],
)
print(response.content[0].text)
```

Status: `source-backed`

## Practical rules

- use `gpt2giga` only when preserving client compatibility is a real requirement
- explain mapping gaps instead of hiding them
- do not route native GigaChat apps through the proxy by default
- do not use `gpt2giga` for Deep Agents harness profiles; use `deepagents-gigachat`

Status: `source-backed`
