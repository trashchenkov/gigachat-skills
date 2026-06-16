# GigaChat Skills

Portable skill folders for AI coding agents that need to write code against the GigaChat API and the GigaChain set of solutions.

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
- `deepagents-gigachat`

Each folder contains:

- `SKILL.md` for trigger logic, workflow, and default behavior
- `references/` for detailed guidance loaded on demand

The repository includes lightweight verification smoke scripts under `verification/` for claims summarized in the feature matrix. It does not include workspace-specific state files or a full benchmark suite; the skill folders remain the reusable instruction layer.

## Skills

### `gigachat-navigation`

Choose the right integration layer:

- native `gigachat` SDK
- `langchain-gigachat`
- `gpt2giga`
- `deepagents-gigachat`

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

### `deepagents-gigachat`

Use when building or configuring Deep Agents / `deepagents-code` with GigaChat harness profiles:

- profile package installation
- provider keys and auto-registration
- `deepagents-code` model config
- profile behavior and benchmark caveats


## Verification smoke scripts

The `verification/` folder contains lightweight scripts referenced by `gigachat-navigation/references/feature-matrix.md`. They are not a full benchmark suite. By default they avoid live API calls; pass `--live` when credentials or a local `gpt2giga` proxy are configured.

Examples:

```bash
python verification/gigachat_chat.py --live --json
python verification/langchain_chat.py --live --json
python verification/gpt2giga_openai_http.py --live --json
```

See `verification/LIVE_TESTS.md` for the latest public-safe live smoke evidence.

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

- `smoke-covered`: covered by a lightweight script in `verification/`; run with `--live` to reproduce against configured services
- `source-backed`: supported by upstream documentation, release notes, or source code
- `caution`: supported by evidence but unsafe as a default recommendation
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
- `deepagents-gigachat` is for Deep Agents harness/profile behavior; use it only when Deep Agents or `deepagents-code` is in scope.
- `gigachat-setup` should usually come before implementation-specific skills.
