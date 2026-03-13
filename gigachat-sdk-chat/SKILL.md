---
name: gigachat-sdk-chat
description: >-
  Uses the official GigaChat Python SDK for text generation: sync and async chat,
  streaming, message history, model choice, session caching, and token counting.
  Use when writing Python code directly against the gigachat package without
  LangChain or proxy compatibility layers.
---

# GigaChat SDK Chat

Use this skill for direct Python integration with `gigachat`.

## What this skill covers

- `GigaChat(...)` client initialization
- `chat`, `achat`, `stream`, `astream`
- message history and roles
- model selection
- token counting
- session caching with `X-Session-ID`
- practical error handling and retries

## Workflow

1. Confirm setup is already solved. If not, use `gigachat-setup`.
2. Prefer the official SDK over raw HTTP unless the user specifically asks for REST calls.
3. For stateless chat, pass a simple string.
4. For context, build an explicit `Chat(messages=[...])` payload.
5. Use streaming for incremental UX.
6. Use async only when concurrency is actually needed.
7. Use `tokens_count` before large prompts or cost-sensitive operations.
8. Prefer the simplest verified payload shape over inventing a more complex one.

## Read these references as needed

- For request patterns and streaming: `references/chat.md`
- For models, tokens, context caching, and retries: `references/models-and-tokens.md`

## Default output

- give the user the simplest working SDK pattern first
- use `Chat(messages=[...])` only when history or richer payloads are needed
- keep starter code minimal unless the user asks for a richer production pattern

## Boundaries

- Do not document custom tools or built-in functions here; use `gigachat-sdk-functions`.
- Do not document files or embeddings here; use `gigachat-sdk-files-embeddings`.
