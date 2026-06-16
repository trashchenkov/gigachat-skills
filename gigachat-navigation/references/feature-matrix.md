# Feature Matrix

Use this matrix as the canonical summary of what downstream skills should treat as default behavior.

## Confidence labels

- `smoke-covered`: covered by listed smoke script(s); run with `--live` to reproduce against configured services
- `source-backed`: supported by upstream docs, release notes, package metadata, or implementation notes, but not covered by these smoke scripts
- `caution`: evidence exists, but the row is a constraint or caveat rather than a safe default

## Matrix

| Feature | gigachat | langchain-gigachat | gpt2giga | deepagents-gigachat | Confidence | Evidence |
|---|---|---|---|---|---|---|
| Basic chat | yes | yes | yes | via Deep Agents harness | smoke-covered | `verification/gigachat_chat.py`, `verification/langchain_chat.py`, `verification/gpt2giga_openai_http.py`, `verification/gpt2giga_anthropic_http.py` |
| Streaming | yes | yes | yes | via Deep Agents harness | smoke-covered | `verification/gigachat_stream.py`, `verification/langchain_stream.py`, `verification/gpt2giga_openai_http.py` |
| Embeddings | yes | yes | yes | n/a | smoke-covered | `verification/gigachat_embeddings.py`, `verification/langchain_embeddings.py`, `verification/gpt2giga_embeddings_http.py` |
| Function calling or tool selection | yes | yes | yes | via Deep Agents harness | smoke-covered | `verification/gigachat_functions.py`, `verification/langchain_tools.py`, `verification/gpt2giga_tools_http.py` |
| Final tool loop execution | yes | partial | partial | via Deep Agents harness | caution | `verification/gigachat_functions.py` |
| File upload | yes | via underlying client | n/a as native feature | via underlying GigaChat model/backend; profile caveats apply | smoke-covered | `verification/gigachat_files.py`, `verification/langchain_file_context_single.py` |
| Single image understanding | yes | yes | source-backed | via underlying GigaChat model/backend; profile caveats apply | smoke-covered for SDK/LangChain setup | `verification/gigachat_file_context_single.py`, `verification/langchain_file_context_single.py` |
| Single audio understanding | yes | yes | source-backed | via underlying GigaChat model/backend; profile caveats apply | smoke-covered for SDK/LangChain setup | `verification/gigachat_file_context_single.py --file-kind audio`, `verification/langchain_file_context_single.py --file-kind audio` |
| Single PDF understanding | yes | yes | source-backed | via underlying GigaChat model/backend; profile caveats apply | smoke-covered for SDK/LangChain setup | `verification/gigachat_file_context_single.py --file-kind pdf`, `verification/langchain_file_context_single.py --file-kind pdf` |
| Multi-image comparison | yes | yes | source-backed | via underlying GigaChat model/backend; profile caveats apply | smoke-covered for SDK/LangChain setup | `verification/gigachat_compare_images.py`, `verification/langchain_compare_images.py` |
| Structured output | source-backed | yes | source-backed | n/a | smoke-covered for LangChain | `verification/langchain_structured_output.py` |
| Mixed modalities in one request | unreliable | unreliable | not smoke-covered | via underlying GigaChat model/backend; profile caveats apply | caution | `verification/gigachat_files_context.py` |
| Mixed modalities across turns | unreliable | unreliable | not tested | via underlying GigaChat model/backend; profile caveats apply | caution | `verification/gigachat_multiturn_mixed_context.py`, `verification/langchain_multiturn_mixed_context.py` |
| OpenAI-compatible clients | no | no | yes | n/a | smoke-covered | `verification/gpt2giga_openai_http.py` |
| Anthropic-compatible clients | no | no | yes | n/a | smoke-covered | `verification/gpt2giga_anthropic_http.py` |
| Deep Agents HarnessProfile | n/a | underlying model wrapper | n/a | yes | source-backed | `deepagents-gigachat` package metadata and README |

## Agent rules derived from the matrix

- Choose the simplest row with `smoke-covered` coverage before considering `source-backed` paths.
- Treat `caution` rows as constraints, not as green lights.
- Do not assume `gpt2giga` matches native OpenAI or Anthropic behavior byte-for-byte.
- Do not assume mixed-modality support unless the exact combination is smoke-covered.

## Notes

- `langchain-gigachat` file flows currently rely on the underlying SDK client for upload and delete.
- `gpt2giga` is a compatibility layer, not a replacement for the native SDK surface.
- Full multi-step tool execution belongs to the outer client or agent runtime for LangChain, `gpt2giga`, and Deep Agents.
- Deep Agents harness/profile behavior belongs to `deepagents-gigachat`.
