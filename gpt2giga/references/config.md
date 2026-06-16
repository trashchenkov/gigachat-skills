# Config

Use this file when the goal is compatibility, not a native SDK integration.

## Default path

1. Decide whether the proxy is for local development, Docker deployment, or production.
2. Configure GigaChat auth separately from proxy auth.
3. Point the client SDK at the proxy base URL.
4. In production, enable proxy API-key auth and keep TLS verification enabled for GigaChat.

Status: `source-backed`

## Main startup modes

- local Python process: `uv tool install gpt2giga && gpt2giga`
- Docker Compose DEV profile
- Docker Compose PROD profile behind a reverse proxy / TLS boundary

Default local address in stable documentation: `http://localhost:8090`.

Status: `source-backed`

## Route prefixes

Stable docs describe routes mounted at root and under versioned prefixes. For example:

- `/chat/completions`
- `/v1/chat/completions`
- `/v2/chat/completions`

`/v1` forces the GigaChat v1 contract; `/v2` forces the v2 contract. Root routes use proxy configuration.

Status: `source-backed`

## Key proxy variables

Common proxy variables include:

- `GPT2GIGA_HOST`
- `GPT2GIGA_PORT`
- `GPT2GIGA_MODE`
- `GPT2GIGA_ENABLE_API_KEY_AUTH`
- `GPT2GIGA_API_KEY`
- `GPT2GIGA_GIGACHAT_API_MODE`
- model pass-through / model selection variables from the active release
- logging, metrics, and traffic-log variables from the deployment docs

Check the installed version's configuration docs before copying preview-only variables.

Status: `source-backed`

## Shared GigaChat variables

- `GIGACHAT_CREDENTIALS`
- `GIGACHAT_USER` / `GIGACHAT_PASSWORD`
- `GIGACHAT_SCOPE`
- `GIGACHAT_VERIFY_SSL_CERTS`
- `GIGACHAT_CA_BUNDLE_FILE`
- `GIGACHAT_BASE_URL`
- `GIGACHAT_MODEL`

Status: `source-backed`

## Security rules

For production:

- set production mode
- enable proxy API-key auth
- use TLS directly or behind a reverse proxy
- keep `GIGACHAT_VERIFY_SSL_CERTS=True`
- avoid passing secrets through CLI flags
- avoid exposing DEV-only docs/log endpoints publicly

Status: `source-backed`

## Pass-token mode

If enabled by the deployed version/config, the proxy can forward client-supplied auth to GigaChat. Use this only when many clients should carry their own GigaChat credentials instead of sharing one proxy credential.

Status: `source-backed`

## Stable vs pre-release guidance

Use stable package documentation as the default. Mention alpha/pre-release features only in a clearly labeled preview section and do not make them default recommendations.

Status: `source-backed caution`

## Decision rules

- one internal app with shared backend credentials -> keep auth in proxy env vars
- many end users with separate GigaChat access -> consider pass-token mode after checking the installed version
- public exposure -> require proxy API-key auth even if GigaChat auth is also present
- Deep Agents harness/profile configuration -> use `deepagents-gigachat`, not `gpt2giga`

Status: `source-backed`
