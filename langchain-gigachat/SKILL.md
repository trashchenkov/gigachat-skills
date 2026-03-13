---
name: langchain-gigachat
description: >-
  Uses GigaChat through LangChain primitives: chat models, embeddings, message
  conversion, streaming, tool binding, and RAG workflows. Use when building
  LangChain chains, agents, or retrieval pipelines on top of GigaChat instead of
  calling the raw SDK directly.
---

# LangChain GigaChat

Use this skill when the user is building with LangChain abstractions, not raw `gigachat`.

## What this skill covers

- `langchain-gigachat` installation and initialization
- chat model usage through LangChain messages and runnables
- embeddings through `GigaChatEmbeddings`
- tool binding and structured outputs where supported
- RAG setup using LangChain vector stores
- practical wrapper behavior around the underlying SDK

## Workflow

1. If credentials and TLS are not configured, use `gigachat-setup`.
2. If the task does not need LangChain primitives, prefer `gigachat-sdk-*` skills.
3. Initialize `GigaChat` or `GigaChatEmbeddings` with the same auth inputs as the SDK.
4. Work with LangChain message objects, not raw GigaChat payloads, unless debugging conversion.
5. For RAG, pair `GigaChatEmbeddings` with a vector store and keep retrieval logic in LangChain.
6. Avoid double retries when LangChain and the SDK both retry.
7. Prefer the simplest verified LangChain pattern before adding wrapper-specific complexity.

## Read these references as needed

- For chat models and message/tool behavior: `references/chat-models.md`
- For embeddings and RAG patterns: `references/embeddings-rag.md`

## Default output

- keep the user inside LangChain abstractions unless there is a wrapper boundary bug
- do not mix raw SDK code into normal LangChain starter examples
- call out wrapper caveats instead of assuming full parity with generic LangChain behavior

## Boundaries

- Do not explain OpenAI-compatible base URLs here; use `gpt2giga`.
