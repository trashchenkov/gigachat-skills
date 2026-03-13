---
name: gigachat-navigation
description: >-
  Routes work across the GigaChat ecosystem: official gigachat SDK,
  langchain-gigachat, and gpt2giga. Use when deciding which layer to choose,
  how capabilities differ, which limitations are verified, and which skill or
  reference path to use next.
---

# GigaChat Navigation

Use this skill first when the user is unsure which GigaChat integration layer fits the task.

## What this skill covers

- choosing between `gigachat`, `langchain-gigachat`, and `gpt2giga`
- mapping user intent to the right skill
- understanding verified capabilities and limitations
- choosing the right implementation skill next

## Workflow

1. Classify the task by integration style, not by API buzzwords.
2. If the user is writing a native Python integration, prefer `gigachat`.
3. If the app already uses LangChain primitives, use `langchain-gigachat`.
4. If the client must keep an OpenAI-compatible or Anthropic-compatible SDK, use `gpt2giga`.
5. If more than one layer could work, choose the simplest locally verified path.
6. For files, keep one request limited to one modality.
7. Prefer the simplest verified path described in the relevant skill and references.

## Read these references as needed

- For routing logic: `references/decision-rules.md`
- For verified feature coverage: `references/feature-matrix.md`

## Default output

- name the recommended layer explicitly
- state why the other layers are not the default
- point to the next implementation skill or reference file

## Boundaries

- This skill helps choose and navigate.
- It does not replace the implementation skills for SDK chat, files, LangChain, or proxy work.
