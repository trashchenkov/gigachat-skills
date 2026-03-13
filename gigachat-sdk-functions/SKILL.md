---
name: gigachat-sdk-functions
description: >-
  Uses function calling with the official GigaChat Python SDK: custom functions,
  built-in functions like text2image, function_call modes, response parsing, and
  returning tool results back to the model. Use when building agents or tool-use
  flows directly on top of gigachat.
---

# GigaChat SDK Functions

Use this skill when the model must call tools.

## What this skill covers

- `functions` schema design
- `function_call` modes
- handling `finish_reason == "function_call"`
- sending function results back with role `function`
- built-in functions such as `text2image`
- function schema validation

## Workflow

1. Start with a normal `Chat(messages=[...])` payload.
2. Add `functions=[...]` with flat explicit schema fields.
3. Use `function_call="auto"` unless you need strict forcing.
4. If the model returns a function call, execute the tool in your code.
5. Append assistant function-call output and the function result message, then call the model again.
6. Validate broken schemas before blaming the model.
7. Prefer the smallest complete two-step tool loop that satisfies the task.

## Read these references as needed

- For custom and built-in function patterns: `references/function-calling.md`

## Default output

- include the full two-step tool loop, not only the first model call
- avoid complex schema constructs as the default
- state explicitly when a built-in returns file references rather than inline bytes

## Boundaries

- Do not cover LangChain tool wrappers here; use `langchain-gigachat`.
- Do not cover OpenAI-compatible tool mapping here; use `gpt2giga`.
