# Verification smoke scripts

This folder contains the lightweight scripts referenced by
`gigachat-navigation/references/feature-matrix.md`.

They are **smoke checks**, not a full benchmark suite. By default scripts do
not call external services. Pass `--live` to run real checks against GigaChat or
a local `gpt2giga` proxy.

## Common environment

Native SDK / LangChain checks need one of:

- `GIGACHAT_CREDENTIALS`
- `GIGACHAT_USER` + `GIGACHAT_PASSWORD`
- an already-supported SDK token/auth environment

Proxy checks use:

- `GPT2GIGA_BASE_URL` (default: `http://127.0.0.1:8000/v1`)
- `GPT2GIGA_API_KEY` or `OPENAI_API_KEY` (default test key for local dev)

## Examples

```bash
python verification/gigachat_chat.py --live --json
python verification/langchain_chat.py --live --json
python verification/gpt2giga_openai_http.py --live --json
python verification/gigachat_file_context_single.py --live --file-kind image --json
python verification/gigachat_file_context_single.py --live --file-kind audio --json
python verification/gigachat_file_context_single.py --live --file-kind pdf --json
```

A missing dependency, missing credentials, or stopped proxy returns `SKIP` with
a reason and exit code `0`. A failed live behavior check returns `FAIL` and exit
code `1`.
