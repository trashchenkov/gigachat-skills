---
name: gpt2giga
description: >-
  Runs and configures the gpt2giga proxy that maps OpenAI API and Anthropic
  Messages API requests to GigaChat. Use when plugging GigaChat into existing
  OpenAI-compatible or Anthropic-compatible applications without rewriting the
  client integration.
---

# gpt2giga

Use this skill when the task is compatibility, migration, or proxy deployment.

## What this skill covers

- local or Docker startup
- `.env` and CLI configuration
- OpenAI-compatible and Anthropic-compatible endpoints
- proxy auth and pass-through auth
- streaming and model routing behavior
- production hardening

## Workflow

1. Decide whether the user wants local development, Docker, or production deployment.
2. Configure proxy auth separately from GigaChat auth.
3. If the client must keep its OpenAI or Anthropic SDK, point it at the proxy base URL.
4. If the client should carry its own GigaChat credentials, use pass-token mode.
5. In production, enable proxy API-key auth and avoid DEV-only endpoints.
6. When behavior differs from native OpenAI or Anthropic APIs, explain the mapping rather than hiding it.
7. Prefer the smallest compatibility setup that preserves the client API the user already has.

## Read these references as needed

- For env vars, ports, auth, and startup: `references/config.md`
- For endpoint compatibility and client behavior: `references/compatibility.md`

## Default output

- treat `gpt2giga` as a compatibility layer, not as the default for new native apps
- state which API family is being preserved: OpenAI or Anthropic
- call out that outer orchestration still owns full multi-step tool execution

## Boundaries

- Do not teach raw SDK usage here; use `gigachat-sdk-*`.
