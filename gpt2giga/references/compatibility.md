# Compatibility

Use this file when preserving an OpenAI-style or Anthropic-style client matters more than native GigaChat control.

## Default rule

Treat `gpt2giga` as a compatibility layer, not as a byte-for-byte replacement for OpenAI or Anthropic behavior.

Status: `verified`

## Verified client paths

- OpenAI-style chat through the proxy
- Anthropic-style chat through the proxy
- embeddings through the proxy
- tool selection through the OpenAI-style API

Status: `verified`

## Exposed API families

- OpenAI-style `/v1/chat/completions`
- OpenAI-style `/v1/embeddings`
- OpenAI-style `/v1/responses`
- Anthropic-style `/v1/messages`

Status: `docs/code-backed`

## Important mapping behavior

- client payloads are transformed into GigaChat chat or embeddings requests
- responses are transformed back into the source API shape
- tool or function metadata may be mapped rather than preserved byte-for-byte
- streaming is exposed as SSE where appropriate
- some tool names may be remapped internally
- tools without JSON parameters may be skipped

Status: `docs/code-backed`

## Model handling

If `GPT2GIGA_PASS_MODEL=True`, the proxy forwards the client model name to GigaChat logic. Otherwise, the proxy default model wins.

Status: `docs/code-backed`

## Typical client example

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8090/v1",
    api_key="any",
)
```

Status: `verified`

## Anthropic compatibility notes

- `tool_use` and `tool_result` blocks are converted internally before reaching GigaChat
- image content may be converted into OpenAI-style image payloads on the proxy side
- finish reasons are mapped into Anthropic `stop_reason` values

Status: `docs/code-backed`

## Practical rules

- use `gpt2giga` only when preserving client compatibility is a real requirement
- do not route new native Python apps through the proxy by default
- assume outer orchestration still owns the full multi-step tool loop

Status: `verified`
