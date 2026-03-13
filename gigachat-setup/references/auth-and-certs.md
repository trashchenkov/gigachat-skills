# Auth And Certs

Use this file to get connectivity working before debugging application code.

## Confidence

- `verified`: reflected in local environment usage and project setup patterns
- `docs/code-backed`: supported by local docs or repository code, but not necessarily exercised in this workspace during this pass
- `inference`: recommendation derived from repeated failure patterns

## Default path

1. Build the base64 authorization key from `client_id:client_secret`.
2. Pick the correct `GIGACHAT_API_*` scope for the account type.
3. Configure TLS verification with the Russian Trusted Root CA.
4. Verify connectivity with `get_models()` or a minimal chat call.
5. Only use `verify_ssl_certs=False` for explicitly local or temporary work.

Status: `verified`

## Core endpoints

- OAuth token: `https://ngw.devices.sberbank.ru:9443/api/v2/oauth`
- REST API base: `https://gigachat.devices.sberbank.ru/api/v1/`

Status: `docs/code-backed`

## Authorization model

1. Build the authorization key from `client_id:client_secret`, encoded as base64.
2. Send it to the OAuth endpoint with `Authorization: Basic <base64_key>`.
3. Include `RqUID: <uuid>` and `scope=<GIGACHAT_API_...>`.
4. Use the returned `access_token` as `Authorization: Bearer <token>` for API calls.
5. Token lifetime is 30 minutes.

Status: `docs/code-backed`

## Scope selection

- `GIGACHAT_API_PERS`: individuals
- `GIGACHAT_API_B2B`: business prepaid packages
- `GIGACHAT_API_CORP`: business pay-as-you-go

If scope does not match the account type, auth usually fails even if credentials are valid.

Status: `docs/code-backed`

## Environment variables

- `GIGACHAT_CREDENTIALS`
- `GIGACHAT_SCOPE`
- `GIGACHAT_BASE_URL`
- `GIGACHAT_AUTH_URL`
- `GIGACHAT_VERIFY_SSL_CERTS`
- `GIGACHAT_CA_BUNDLE_FILE`
- `GIGACHAT_ACCESS_TOKEN`
- `GIGACHAT_USER`
- `GIGACHAT_PASSWORD`

Status: `docs/code-backed`

## Certificate rule

GigaChat depends on the Russian Trusted Root CA. Without it, certificate validation failures are common.

Preferred approaches:

1. Install the CA into the system trust store.
2. Append the CA to `certifi`.
3. Pass the CA path explicitly with `ca_bundle_file` or `GIGACHAT_CA_BUNDLE_FILE`.

Fallback for development only:

- `verify_ssl_certs=False`

Status: `verified`

## Minimal connectivity check

Use this as the first code-level check after env and cert setup.

```python
from gigachat import GigaChat

with GigaChat(
    credentials="<base64_auth_key>",
    scope="GIGACHAT_API_PERS",
    ca_bundle_file="/path/to/russian_trusted_root_ca.pem",
) as client:
    print(client.get_models())
```

Status: `docs/code-backed`

## Next step

After the minimal connectivity check succeeds, continue in the implementation skill that matches the integration layer:

- native SDK chat or files -> `gigachat-sdk-*`
- LangChain integration -> `langchain-gigachat`
- compatibility proxy -> `gpt2giga`
