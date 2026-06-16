# Benchmarks And Caveats

Use this file when discussing evidence quality, benchmark results, or limitations of `deepagents-gigachat`.

## Benchmark evidence

The public README reports a `harness-bench-fast` result for `GigaChat-3-Ultra`:

- without the profile: `164 / 231` (`71.0%`)
- with the profile: `195 / 231` (`84.4%`)
- reported uplift: `+13.4 percentage points`

Treat this as upstream benchmark evidence, not as local verification in this repository.

Status: `source-backed`

## What `harness-bench-fast` is

`harness-bench-fast` is described as a self-contained 231-task benchmark for file-operation and coding-agent work. Tasks are mechanically verified rather than judged by another LLM.

This is useful evidence for agent-harness behavior, but it is not a dependency of `gigachat-skills` and should not be copied into this repo as a full benchmark suite unless explicitly requested.

Status: `source-backed`

## Caveats

- The Deep Agents profiles API is beta.
- `deepagents-gigachat` is beta and targets Python 3.12+.
- Benchmark numbers may depend on model version, backend mode, tool semantics, prompts, and environment.
- The profile currently assumes default filesystem path behavior (`virtual_mode=False`).
- Installing the package is not enough if Deep Agents is launched from a different Python environment.

Status: `source-backed caution`

## Practical rules

- Include benchmark numbers only with source attribution and caveats.
- Do not claim local reproduction unless `harness-bench-fast` was actually run.
- Prefer lightweight smoke checks in this repository; use `harness-bench-fast` only when the task is specifically benchmark reproduction or profile evaluation.
- If a user asks whether the profile is worth using, recommend it for Deep Agents + GigaChat by default, while naming beta/path caveats.

Status: `source-backed`
