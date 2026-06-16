# Decision Rules

Use this file to choose the simplest smoke-covered path before writing code.

## Confidence

- `smoke-covered`: routing rule has a lightweight verification script where practical
- `source-backed`: routing rule is supported by upstream docs, package metadata, or source
- `inference`: cautious recommendation derived from evidence

## Default routing order

1. If the user controls a Python app and does not need framework compatibility, use `gigachat`.
2. If the app already uses LangChain primitives, use `langchain-gigachat`.
3. If the client must keep an OpenAI-compatible or Anthropic-compatible SDK, use `gpt2giga`.
4. If the task is Deep Agents or `deepagents-code` harness behavior, use `deepagents-gigachat`.
5. If more than one layer could work, choose the simplest smoke-covered or source-backed path.

Status: `smoke-covered`

## Choose by task shape

### Use `gigachat`

- when you control the Python application
- when you need explicit control over auth, retries, payloads, files, or function calling
- when you want the clearest debugging path

Status: `smoke-covered`

### Use `langchain-gigachat`

- when the app is already built on LangChain
- when you need LangChain messages, runnables, tool binding, embeddings, or RAG
- when wrapper-level abstractions matter more than raw SDK control

Status: `smoke-covered`

### Use `deepagents-gigachat`

Choose `deepagents-gigachat` when:

- the app runs through Deep Agents or `deepagents-code`
- the user asks about HarnessProfile, provider profiles, or model profile behavior
- GigaChat-specific Deep Agents prompts, tool descriptions, or middleware matter
- benchmark/profile caveats affect the implementation

Status: `source-backed`

### Use `gpt2giga`

- when the client already speaks OpenAI API or Anthropic Messages API
- when migration cost matters more than native SDK control
- when compatibility with tools like Cursor or Aider is the main requirement

Status: `smoke-covered`

## File modality rule

Attach files of only one modality per request.

Good:

- image + image
- audio + audio
- document + document

Avoid:

- image + audio
- image + pdf
- audio + pdf

If the task needs multiple modalities, split it into separate requests and combine results in application code.

Status: `smoke-covered`

## Mixed-modality context rule

Do not rely on mixed-modality carryover inside one dialogue.

What is smoke-covered:

- single image works
- single audio works
- single PDF works
- multi-image comparison works
- mixed modalities in one request are unreliable
- mixed modalities across turns are unreliable

Status: `smoke-covered`

## Practical routing table

- direct Python integration -> `gigachat-sdk-*`
- LangChain RAG or LangChain agents -> `langchain-gigachat`
- OpenAI-compatible or Anthropic-compatible client -> `gpt2giga`
- Deep Agents / `deepagents-code` with GigaChat -> `deepagents-gigachat`
- image comparison -> `gigachat-sdk-files-embeddings` or `langchain-gigachat`
- image + audio in one user task -> split into separate requests

Status: `smoke-covered`
