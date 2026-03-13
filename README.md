# GigaChat Codex Skills

Portable Codex skills for writing code against the GigaChat ecosystem.

This repository contains self-contained skill folders only:

- `gigachat-navigation`
- `gigachat-setup`
- `gigachat-sdk-chat`
- `gigachat-sdk-functions`
- `gigachat-sdk-files-embeddings`
- `langchain-gigachat`
- `gpt2giga`

Each skill folder contains:

- `SKILL.md`
- `references/` with detailed guidance loaded on demand

The skills are intentionally packaged without local verification scripts or workspace-specific state files. They are meant to be portable and usable by another agent as-is.

## Included Skills

### `gigachat-navigation`

Use first when the user is not sure whether to choose the native SDK, LangChain integration, or the compatibility proxy.

### `gigachat-setup`

Use for credentials, scopes, TLS certificates, environment variables, and connectivity troubleshooting.

### `gigachat-sdk-chat`

Use for direct Python integration with the official `gigachat` SDK for chat, streaming, tokens, and message history.

### `gigachat-sdk-functions`

Use for native function calling and tool-use loops in the official SDK.

### `gigachat-sdk-files-embeddings`

Use for uploads, file-backed prompts, multimodal constraints, and direct embeddings.

### `langchain-gigachat`

Use for LangChain-based chat, tools, embeddings, and RAG with GigaChat.

### `gpt2giga`

Use when an app must keep an OpenAI-compatible or Anthropic-compatible client and talk to GigaChat through the `gpt2giga` proxy.

## Installation

Install one or more skills by copying the folders into your Codex skills directory.

Project-local installation:

```bash
cp -R gigachat-navigation /path/to/project/.codex/skills/
cp -R gigachat-setup /path/to/project/.codex/skills/
```

User-level installation:

```bash
cp -R gigachat-navigation ~/.codex/skills/
cp -R gigachat-setup ~/.codex/skills/
```

You can also copy the whole repository contents into a skills directory if you want all of them available.

## Notes

- The skills use `verified`, `docs/code-backed`, and `inference` labels to communicate confidence.
- The file-modality rule is important across the set: keep one request limited to one file modality.
- `gpt2giga` is documented as a compatibility layer, not as a byte-for-byte replacement for OpenAI or Anthropic APIs.
