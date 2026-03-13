---
name: gigachat-setup
description: >-
  Configures access to GigaChat API: registration, authorization key, OAuth scope,
  SSL certificates, environment variables, and common connectivity failures. Use
  when setting up GigaChat access for SDK, LangChain, or gpt2giga, or when fixing
  auth, TLS, or scope issues.
---

# GigaChat Setup

Use this skill whenever the task starts with "how do I connect to GigaChat?".

## What this skill covers

- Project setup on `developers.sber.ru`
- Building the authorization key from `client_id:client_secret`
- Choosing the right `scope`
- TLS certificates for the Russian Trusted Root CA
- Base environment variables shared by `gigachat`, `langchain-gigachat`, and `gpt2giga`
- First-pass troubleshooting for auth, SSL, and rate-limit failures

## Workflow

1. If the user does not yet have credentials, guide them through registration and project creation.
2. If the user has `client_id` and `client_secret`, generate the base64 authorization key.
3. Confirm the account type and pick `GIGACHAT_API_PERS`, `GIGACHAT_API_B2B`, or `GIGACHAT_API_CORP`.
4. Configure TLS verification correctly before suggesting `verify_ssl_certs=False`.
5. Verify connectivity with `get_models()` or a minimal chat call before debugging application code.
6. For SDK or proxy usage, prefer environment variables over hardcoded secrets.
7. If a request fails, classify it in this order: TLS, auth, scope, rate limit, then content policy.

## Read these references as needed

- For setup, env vars, token flow, and certificates: `references/auth-and-certs.md`
- For common failures and diagnosis: `references/troubleshooting.md`

## Default output

- prefer CA bundle setup over disabling TLS verification
- treat connectivity as solved only after a minimal code-level check succeeds
- send the user to the implementation skill only after setup is known-good

## Boundaries

- Do not explain chat payload design here; use `gigachat-sdk-chat`.
- Do not explain function calling here; use `gigachat-sdk-functions`.
- Do not explain LangChain wrappers here; use `langchain-gigachat`.
- Do not explain proxy routing here; use `gpt2giga`.
