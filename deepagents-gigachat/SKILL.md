---
name: deepagents-gigachat
description: >-
  Uses the public deepagents-gigachat HarnessProfile package to run Deep Agents
  or deepagents-code with GigaChat-specific prompts, tool descriptions, and
  middleware. Use when building Deep Agents workflows on top of GigaChat or when
  configuring model/provider profiles for deepagents.
---

# Deep Agents GigaChat

Use this skill when the user is running `deepagents`, `deepagents-code`, or a Deep Agents app with GigaChat models.

## What this skill covers

- installing `deepagents-gigachat` into the same environment as Deep Agents
- automatic harness profile discovery through `deepagents.harness_profiles`
- provider keys `gigachat` and `giga`
- `deepagents-code` model configuration for `langchain-gigachat`
- profile behavior: prompt replacement, tool-description overrides, and `think` middleware
- benchmark and filesystem/backend caveats

## Workflow

1. Confirm the user is working with Deep Agents. If not, use `gigachat-navigation` first.
2. Configure ordinary GigaChat credentials through `gigachat-setup` / `langchain-gigachat` conventions.
3. Install `deepagents-gigachat` in the same Python environment as `deepagents` or `deepagents-code`.
4. Let the profile auto-register; do not duplicate the profile in application code unless debugging discovery.
5. For `deepagents-code`, configure provider/model entries under `~/.deepagents/config.toml`.
6. Treat the profile API as beta and keep backend/path assumptions explicit.
7. Use benchmark numbers as upstream evidence, not as local verification.

## Read these references as needed

- For install and configuration: `references/setup.md`
- For what the profile changes: `references/profile-behavior.md`
- For benchmark evidence and caveats: `references/benchmarks-and-caveats.md`

## Default output

- state that this is a Deep Agents harness-profile path, not raw SDK usage
- show the smallest install/config snippet that matches the user's runtime
- call out Python/version/backend caveats before promising behavior
- route non-Deep-Agents GigaChat work back to `gigachat-sdk-*`, `langchain-gigachat`, or `gpt2giga`

## Boundaries

- Do not use this skill for ordinary LangChain chains or RAG; use `langchain-gigachat`.
- Do not use this skill for OpenAI/Anthropic-compatible proxy work; use `gpt2giga`.
- Do not claim benchmark improvements are locally reproduced unless the benchmark was actually run.
