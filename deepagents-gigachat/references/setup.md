# Setup

Use this file when installing or configuring the public `deepagents-gigachat` package.

## Default path

1. Install `deepagents-gigachat` in the same environment as `deepagents` or `deepagents-code`.
2. Configure GigaChat credentials through environment variables.
3. Let Deep Agents discover the profile automatically through Python package entry points.
4. For `deepagents-code`, configure a provider in `~/.deepagents/config.toml`
   that matches the chosen auth mode.

Status: `source-backed`

## Package requirements

The public package metadata indicates:

- package: `deepagents-gigachat`
- Python: `>=3.12`
- dependencies include `deepagents>=0.5.4`, `langchain-gigachat>=0.5.0`, and `python-dotenv>=1.2.2`
- package maturity: beta

Status: `source-backed`

## Install

```bash
pip install deepagents-gigachat
```

For `deepagents-code`, install the profile into the same tool environment as the CLI:

```bash
uv tool install deepagents-code --with langchain-gigachat,deepagents-gigachat
```

Status: `source-backed`

## Credentials

Use the same GigaChat environment conventions as `langchain-gigachat`. The profile and the underlying `langchain-gigachat` model use standard `GIGACHAT_*` variables from the process environment when they are already loaded, so do not duplicate credentials in code or config unless overriding them intentionally.


```bash
export GIGACHAT_CREDENTIALS="<base64-encoded auth key>"
# or
export GIGACHAT_USER="<client id>"
export GIGACHAT_PASSWORD="<client secret>"
```

Optional runtime settings commonly include:

```bash
export GIGACHAT_BASE_URL="https://gigachat.sberdevices.ru/v1"
export GIGACHAT_MODEL="GigaChat-3-Ultra"
export GIGACHAT_VERIFY_SSL_CERTS=True
```

Use `GIGACHAT_VERIFY_SSL_CERTS=False` only for local/dev situations where certificate setup is intentionally deferred.

Status: `source-backed`

## Profile discovery

`deepagents-gigachat` registers a package entry point:

```toml
[project.entry-points."deepagents.harness_profiles"]
gigachat = "deepagents_gigachat:register_harness"
```

After installation, Deep Agents discovers the profile automatically. The package entry point is named `gigachat`; the harness profile is registered for provider keys `gigachat` and `giga`.

Status: `source-backed`

## Minimal `deepagents-code` provider shape for auth-key credentials

Use this shape when `GIGACHAT_CREDENTIALS` is populated with the base64
authorization key. In this mode `api_key_env = "GIGACHAT_CREDENTIALS"` is
correct and lets `deepagents-code` pass its early provider credential check.

```toml
[models]
default = "gigachat:GigaChat-3-Ultra"

[models.providers.gigachat]
models = ["GigaChat-3-Ultra", "GigaChat-2-Max", "GigaChat-Max", "GigaChat-Pro", "GigaChat"]
class_path = "langchain_gigachat.chat_models.gigachat:GigaChat"
api_key_env = "GIGACHAT_CREDENTIALS"

[models.providers.gigachat.params]
base_url = "https://gigachat.sberdevices.ru/v1"
verify_ssl_certs = true
timeout = 600

[models.providers.gigachat.profile]
tool_calling = true
default_model_hint = "GigaChat-3-Ultra"
```

Status: `source-backed`

## `deepagents-code` provider shape for login/password auth

Use a separate provider without `api_key_env` when the environment authenticates
with `GIGACHAT_USER` and `GIGACHAT_PASSWORD` instead of
`GIGACHAT_CREDENTIALS`. `deepagents-code` performs an early credential-readiness
check for providers that declare `api_key_env`; if `api_key_env =
"GIGACHAT_CREDENTIALS"` is present and that variable is empty, the CLI can fail
before `langchain-gigachat` receives `GIGACHAT_USER` / `GIGACHAT_PASSWORD`.

```bash
export GIGACHAT_BASE_URL="https://gigachat.ift.sberdevices.ru/v1"
export GIGACHAT_USER="<login>"
export GIGACHAT_PASSWORD="<password>"
export GIGACHAT_VERIFY_SSL_CERTS=False
unset GIGACHAT_CREDENTIALS
```

```toml
[models]
default = "gigachat_ift_login:GigaChat-3.5-430B-A28B"

[models.providers.gigachat_ift_login]
models = ["GigaChat-3.5-430B-A28B", "GigaChat-3-Ultra", "GigaChat-3-Pro"]
class_path = "langchain_gigachat.chat_models.gigachat:GigaChat"

[models.providers.gigachat_ift_login.params]
timeout = 600
verify_ssl_certs = false
max_retries = 1

[models.providers.gigachat_ift_login.profile]
tool_calling = true
default_model_hint = "GigaChat-3.5-430B-A28B"
```

Do not write real passwords into `config.toml`. Keep them in process
environment variables or a local secret loader, then run for example:

```bash
deepagents-code -M gigachat_ift_login:GigaChat-3.5-430B-A28B -n "ping"
```

Status: `smoke-covered`

## Running `deepagents-code` without the GigaChat harness profile

`deepagents-code` can connect to GigaChat without the `deepagents-gigachat`
harness profile as long as `langchain-gigachat` is installed in the same Python
environment and the provider uses `class_path =
"langchain_gigachat.chat_models.gigachat:GigaChat"`.

Use this deliberately for a plain baseline or when profile discovery is being
debugged:

```toml
[models]
default = "gigachat_plain:GigaChat-3.5-430B-A28B"

[models.providers.gigachat_plain]
models = ["GigaChat-3.5-430B-A28B", "GigaChat-3-Ultra", "GigaChat-3-Pro"]
class_path = "langchain_gigachat.chat_models.gigachat:GigaChat"

[models.providers.gigachat_plain.params]
timeout = 600
verify_ssl_certs = false
max_retries = 1
```

Then run:

```bash
deepagents-code -M gigachat_plain:GigaChat-3.5-430B-A28B -n "ping"
```

This is a connectivity/runtime baseline, not the recommended production Deep
Agents setup. Without the harness profile, Deep Agents will not get
GigaChat-specific prompt, tool-description, and middleware adjustments. Expect
simple chat and basic file tasks to work if the model supports the needed
behavior, but tool-heavy agentic tasks may be less stable or score lower.

To use the harness profile, prefer provider keys registered by
`deepagents-gigachat` (`gigachat` or `giga`) and install the profile package in
the exact environment that launches `deepagents-code`.

Status: `smoke-covered`

## Decision rules

- If the user uses Deep Agents or `deepagents-code`, install `deepagents-gigachat` instead of manually rewriting prompts.
- If the user only uses LangChain messages/chains, use `langchain-gigachat` instead.
- If profile discovery fails, first check that `deepagents-gigachat` is installed in the exact Python environment that runs Deep Agents.
- If `deepagents-code` works with `GIGACHAT_CREDENTIALS` but not with
  `GIGACHAT_USER` / `GIGACHAT_PASSWORD`, check whether the provider declares
  `api_key_env`; for login/password auth use a custom-class provider without
  `api_key_env`.
- If the goal is a no-profile baseline, use a non-registered provider key such
  as `gigachat_plain`; if the goal is the GigaChat harness profile, use
  `gigachat` or `giga`.

Status: `source-backed`
