# Profile Behavior

Use this file to explain what `deepagents-gigachat` changes at runtime.

## Default rule

Treat `deepagents-gigachat` as a model/provider harness profile for Deep Agents. It changes the agent harness around GigaChat; it is not a replacement for the GigaChat API, `langchain-gigachat`, or `gpt2giga`.

Status: `source-backed`

## What the profile changes

Upstream documentation says the profile:

- replaces the default Deep Agents system prompt with a GigaChat-tuned prompt
- rewrites descriptions for file and shell tools such as `ls`, `read_file`, `write_file`, `glob`, `grep`, `edit_file`, and `execute`
- adds a `think` middleware tool for structured intermediate reasoning
- registers under provider keys `gigachat` and `giga`

Status: `source-backed`

## Why this matters

Deep Agents performance depends on more than the chat model call. The profile aligns the harness prompt, tool descriptions, and middleware with GigaChat tool-calling behavior. This is why Deep Agents + GigaChat should not be treated as just another `GigaChat(...)` constructor example.

Status: `source-backed`

## Provider keys

Use model specs such as:

```text
gigachat:GigaChat-3-Ultra
gigachat:GigaChat-2-Max
giga:GigaChat-3-Ultra
```

The `giga` key is a compatibility alias. Prefer `gigachat` in new examples unless an existing environment already uses `giga`.

Status: `source-backed`

## Discovery and debugging

Normal path:

1. Install `deepagents-gigachat`.
2. Start Deep Agents in the same environment.
3. Select or configure a `gigachat:*` model.
4. Let entry-point discovery load the profile.

If the profile appears absent:

- verify package installation in the active environment
- verify the provider key in the model spec is `gigachat` or `giga`
- check whether the model wrapper reports provider metadata that allows Deep Agents to match the profile
- avoid copying profile internals into app code unless debugging a discovery bug

Status: `source-backed`

## Backend/path caveat

The public README states that the current profile is tuned for default `FilesystemBackend` behavior with `virtual_mode=False`. Its prompts and filesystem tool descriptions assume real absolute workspace paths.

If a project uses a virtual filesystem backend or custom tool path semantics, verify behavior before treating the profile as a safe default.

Status: `source-backed caution`
