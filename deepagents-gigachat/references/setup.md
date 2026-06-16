# Setup

Use this file when installing or configuring the public `deepagents-gigachat` package.

## Default path

1. Install `deepagents-gigachat` in the same environment as `deepagents` or `deepagents-code`.
2. Configure GigaChat credentials through environment variables.
3. Let Deep Agents discover the profile automatically through Python package entry points.
4. For `deepagents-code`, configure the `gigachat` provider in `~/.deepagents/config.toml`.

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

## Minimal `deepagents-code` provider shape

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

## Decision rules

- If the user uses Deep Agents or `deepagents-code`, install `deepagents-gigachat` instead of manually rewriting prompts.
- If the user only uses LangChain messages/chains, use `langchain-gigachat` instead.
- If profile discovery fails, first check that `deepagents-gigachat` is installed in the exact Python environment that runs Deep Agents.

Status: `source-backed`
