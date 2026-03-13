# Config

Use this file when the goal is compatibility, not a native SDK integration.

## Default path

1. Decide whether the proxy is for local development, Docker deployment, or production.
2. Configure GigaChat auth separately from proxy auth.
3. Point the client SDK at the proxy base URL.
4. In production, enable proxy API-key auth and keep TLS verification enabled for GigaChat.

Status: `verified`

## Main startup modes

- local Python process
- Docker
- Docker with reverse proxy

`gpt2giga` loads `.env` automatically. It also supports `--env-path` for explicit config-file selection.

Status: `docs/code-backed`

## Key proxy variables

- `GPT2GIGA_HOST`
- `GPT2GIGA_PORT`
- `GPT2GIGA_MODE`
- `GPT2GIGA_ENABLE_API_KEY_AUTH`
- `GPT2GIGA_API_KEY`
- `GPT2GIGA_PASS_MODEL`
- `GPT2GIGA_PASS_TOKEN`
- `GPT2GIGA_EMBEDDINGS`

Status: `docs/code-backed`

## Shared GigaChat variables

- `GIGACHAT_CREDENTIALS`
- `GIGACHAT_SCOPE`
- `GIGACHAT_VERIFY_SSL_CERTS`
- `GIGACHAT_CA_BUNDLE_FILE`
- `GIGACHAT_MODEL`

Status: `docs/code-backed`

## Security rules

For production:

- set `GPT2GIGA_MODE=PROD`
- enable proxy API-key auth
- use TLS directly or behind a reverse proxy
- keep `GIGACHAT_VERIFY_SSL_CERTS=True`
- avoid passing secrets through CLI flags

Status: `docs/code-backed`

## Pass-token mode

If enabled, the proxy can forward client-supplied auth to GigaChat. Use this when many clients should carry their own GigaChat credentials instead of sharing one proxy credential.

Status: `docs/code-backed`

## Decision rules

- one internal app with shared backend credentials -> keep auth in proxy env vars
- many end users with separate GigaChat access -> use pass-token mode
- public exposure -> require proxy API-key auth even if GigaChat auth is also present

Status: `verified`
