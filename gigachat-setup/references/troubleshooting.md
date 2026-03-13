# Troubleshooting

Use this order before changing business logic or prompt structure.

## Diagnostic order

1. Verify TLS and CA bundle handling.
2. Verify OAuth token acquisition.
3. Verify `get_models()` or a minimal chat call.
4. Only then debug payload complexity, files, function calling, LangChain wrappers, or proxy behavior.

Status: `verified`

## SSL errors

Typical symptom:

- `SSL: CERTIFICATE_VERIFY_FAILED`

Check in this order:

1. Is the Russian Trusted Root CA installed?
2. Is `GIGACHAT_CA_BUNDLE_FILE` pointing to the right file?
3. Is the process using the expected Python environment?
4. Is the code relying on `verify_ssl_certs=True` without the CA present?

Status: `verified`

## Auth errors

Typical causes:

- base64 key built incorrectly
- wrong `scope`
- expired access token
- malformed `Authorization` header

Status: `docs/code-backed`

## 429 and throughput issues

- individual accounts are heavily limited
- business accounts have higher concurrency
- use retries with backoff for transient overload

Status: `docs/code-backed`

## Content-policy refusals

Refusals and moderation-style stops should be diagnosed separately from auth, TLS, and schema failures.

Status: `inference`

## When code is not the problem

Do not rewrite payload logic until basic connectivity is known-good.
Most early failures come from one of these:

- wrong scope
- missing CA bundle
- bad auth header construction
- expired token
