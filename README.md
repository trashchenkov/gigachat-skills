# GigaChat Skills

Portable skill folders for AI coding agents that need to write code against the GigaChat ecosystem.

This repository is intentionally tool-agnostic. Different agent products expose reusable instructions in different ways:

- some support repository or team-level `skills`
- some rely on project instruction files
- some use custom modes, prompts, or MCP-connected workflows

This repository packages the GigaChat knowledge as self-contained skill folders so it can be adapted to any of those environments.

## What is included

- `gigachat-navigation`
- `gigachat-setup`
- `gigachat-sdk-chat`
- `gigachat-sdk-functions`
- `gigachat-sdk-files-embeddings`
- `langchain-gigachat`
- `gpt2giga`

Each folder contains:

- `SKILL.md` for trigger logic, workflow, and default behavior
- `references/` for detailed guidance loaded on demand

The repository does not include local verification harnesses or workspace-specific state files. It is meant to ship the reusable instruction layer only.

## Skills

### `gigachat-navigation`

Choose the right integration layer:

- native `gigachat` SDK
- `langchain-gigachat`
- `gpt2giga`

Use this first when the agent should decide which path fits the task.

### `gigachat-setup`

Use for:

- credentials
- OAuth scope selection
- TLS certificates
- environment variables
- connectivity troubleshooting

### `gigachat-sdk-chat`

Use for direct Python integration with the official `gigachat` SDK:

- chat
- streaming
- message history
- model selection
- token counting

### `gigachat-sdk-functions`

Use for native tool and function calling with the official SDK:

- function schemas
- tool selection
- second-turn tool result flow
- built-in function caveats

### `gigachat-sdk-files-embeddings`

Use for:

- file upload and lifecycle
- file-backed prompts
- multimodal constraints
- direct embeddings

### `langchain-gigachat`

Use for LangChain-based work with GigaChat:

- chat models
- tools
- structured output
- embeddings
- RAG

### `gpt2giga`

Use when an existing client must keep an OpenAI-style or Anthropic-style API and talk to GigaChat through the compatibility proxy.

## How to use this repository

There is no universal installation path across agent products.

Instead, use the repository in the way your agent environment expects reusable instructions to be provided:

1. Copy one or more skill folders into the place where your agent loads project or team skills.
2. If your tool does not support native skill folders, adapt the contents of `SKILL.md` and `references/` into that tool's project instruction mechanism.
3. Keep each skill folder intact so the workflow guidance and references stay together.

## Adapting to different agent tools

Typical patterns across modern coding agents include:

- repository-level instruction files
- reusable skill or module folders
- custom modes with tool selection and long-form instructions
- team-level shared prompts or agent bundles

This repository maps best to tools that support reusable instruction folders directly. For tools that do not, the content is still usable as a structured source of project guidance.

## Confidence labels

The skills use three confidence labels:

- `verified`: safe default behavior
- `docs/code-backed`: supported by documentation or implementation details, but not treated as the strongest default
- `inference`: useful recommendation, but not a hard guarantee

## Important cross-skill rule

For GigaChat file workflows, keep one request limited to one file modality.

Allowed:

- image + image
- audio + audio
- document + document

Avoid:

- image + audio
- image + pdf
- audio + pdf

If a user task spans multiple modalities, split the work into separate requests and combine results in application code.

## Notes

- `gpt2giga` is documented as a compatibility layer, not as a byte-for-byte replacement for OpenAI or Anthropic APIs.
- `langchain-gigachat` is for LangChain-native workflows; use the native SDK skills when LangChain is not needed.
- `gigachat-setup` should usually come before implementation-specific skills.
