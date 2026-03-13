# Decision Rules

Use this file to choose the simplest verified path before writing code.

## Confidence

- `verified`: routing rules aligned with confirmed behavior
- `docs/code-backed`: supported by repository code or docs, but not the default path for new code here
- `inference`: cautious recommendation derived from verified behavior

## Default routing order

1. If the user controls a Python app and does not need framework compatibility, use `gigachat`.
2. If the app already uses LangChain primitives, use `langchain-gigachat`.
3. If the client must keep an OpenAI-compatible or Anthropic-compatible SDK, use `gpt2giga`.
4. If more than one layer could work, choose the simplest verified path.

Status: `verified`

## Choose by task shape

### Use `gigachat`

- when you control the Python application
- when you need explicit control over auth, retries, payloads, files, or function calling
- when you want the clearest debugging path

Status: `verified`

### Use `langchain-gigachat`

- when the app is already built on LangChain
- when you need LangChain messages, runnables, tool binding, embeddings, or RAG
- when wrapper-level abstractions matter more than raw SDK control

Status: `verified`

### Use `gpt2giga`

- when the client already speaks OpenAI API or Anthropic Messages API
- when migration cost matters more than native SDK control
- when compatibility with tools like Cursor or Aider is the main requirement

Status: `verified`

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

Status: `verified`

## Mixed-modality context rule

Do not rely on mixed-modality carryover inside one dialogue.

What is verified:

- single image works
- single audio works
- single PDF works
- multi-image comparison works
- mixed modalities in one request are unreliable
- mixed modalities across turns are unreliable

Status: `verified`

## Practical routing table

- direct Python integration -> `gigachat-sdk-*`
- LangChain RAG or LangChain agents -> `langchain-gigachat`
- OpenAI-compatible or Anthropic-compatible client -> `gpt2giga`
- image comparison -> `gigachat-sdk-files-embeddings` or `langchain-gigachat`
- image + audio in one user task -> split into separate requests

Status: `verified`
