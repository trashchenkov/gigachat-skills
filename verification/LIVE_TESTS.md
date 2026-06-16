# Live Smoke Evidence

This file records public-safe live smoke evidence for the lightweight scripts in
this repository. Do not include credentials, tokens, local secret paths, or raw
request/response payloads here.

## 2026-06-16

Environment shape:

- GigaChat credentials and settings were loaded from local `GIGACHAT_*` environment variables.
- `gigachat==0.2.1`, `langchain-gigachat==0.5.1`, and `deepagents-gigachat==0.0.2` were checked in a disposable virtual environment.
- `gpt2giga` proxy checks used a temporary local proxy on `127.0.0.1` and the same public smoke scripts.
- No secrets or local env-file paths are required to reproduce the command shapes below.

Native SDK / LangChain live results:

| Script | Result |
|---|---|
| `verification/gigachat_chat.py --live --json` | pass |
| `verification/gigachat_stream.py --live --json` | pass |
| `verification/gigachat_embeddings.py --live --json` | pass, vector dimension `2560` |
| `verification/gigachat_functions.py --live --json` | pass, tool call returned |
| `verification/langchain_chat.py --live --json` | pass |
| `verification/langchain_stream.py --live --json` | pass |
| `verification/langchain_embeddings.py --live --json` | pass, vector dimension `2560` |
| `verification/langchain_tools.py --live --json` | pass, tool call returned |
| `verification/langchain_structured_output.py --live --json` | pass |
| `verification/gigachat_files.py --live --json` | pass, file ID returned |
| `verification/gigachat_file_context_single.py --live --file-kind image --json` | pass, file ID returned |

`gpt2giga` live results:

| Script | Result |
|---|---|
| `verification/gpt2giga_openai_http.py --live --json` | pass |
| `verification/gpt2giga_anthropic_http.py --live --json` | pass |
| `verification/gpt2giga_embeddings_http.py --live --json` | pass |
| `verification/gpt2giga_tools_http.py --live --json` | pass, tool call returned |

Notes:

- One alternate local proxy configuration returned an upstream `404 No such model` for embeddings while chat/tool routes worked. A second proxy run using the same environment shape as the successful native embeddings run passed embeddings. Treat embeddings failures as potentially model/account/config-specific before changing skill guidance.
- File-context smoke scripts currently verify upload/file-ID prerequisites, not full semantic understanding of file contents.
