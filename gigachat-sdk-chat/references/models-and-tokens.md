# Models And Tokens

Use this file for model choice, token counting, retries, and prompt-size decisions.

## Confidence

- `verified`: exercised locally in this workspace
- `docs/code-backed`: supported by repository code or local docs
- `inference`: heuristic, not a guaranteed platform rule

## Main generation models

- `GigaChat-2`
- `GigaChat-2-Pro`
- `GigaChat-2-Max`

Practical default:

- start with `GigaChat-2`
- move to `Pro` or `Max` when instruction quality matters more than latency

Status: `docs/code-backed`

## Context-window guidance

- `GigaChat-2`: treated as a large-context option in local notes
- `GigaChat-2-Pro`: local notes indicate up to 128k tokens
- `GigaChat-2-Max`: local notes indicate up to 128k tokens

Do not rely on rough character counts near the limit. Use `tokens_count(...)`.

Status: `docs/code-backed`

## Token counting

```python
from gigachat import GigaChat

with GigaChat(model="GigaChat-2-Max") as client:
    counts = client.tokens_count(["Hello", "World"], model="GigaChat-2-Max")
    print(counts)
```

Status: `docs/code-backed`

## Session caching

You can reuse cached prompt context via `X-Session-ID`.

```python
import gigachat.context
from gigachat import GigaChat

with GigaChat() as client:
    gigachat.context.session_id_cvar.set("session-1")
    response = client.chat("Explain insurance pricing factors.")
```

Useful response field:

- `precached_prompt_tokens`

Status: `docs/code-backed`

## Retries

SDK supports retry settings such as:

- `max_retries`
- `retry_backoff_factor`
- `retry_on_status_codes`

Default rule:

- enable retries for raw SDK usage
- disable SDK retries when a higher-level framework already retries
- retry 429 and 5xx with backoff
- do not retry malformed schemas or bad auth

Status: `docs/code-backed`

## Throughput and batching heuristics

- call `tokens_count(...)` before large prompts or batch prompt generation
- reuse `X-Session-ID` for repeated long prefixes
- account type matters for concurrency

Status: `inference`

## Common exceptions

- `AuthenticationError`
- `RateLimitError`
- `BadRequestError`
- `ForbiddenError`
- `NotFoundError`
- `ServerError`

Status: `docs/code-backed`
