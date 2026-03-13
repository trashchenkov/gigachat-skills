# Feature Matrix

Use this matrix as the canonical summary of what downstream skills should treat as default behavior.

## Confidence labels

- `verified`: exercised locally in this workspace
- `docs/code-backed`: supported by repository code or docs, but not exercised locally here
- `verified caution`: exercised locally, but should not be treated as a safe default

## Matrix

| Feature | gigachat | langchain-gigachat | gpt2giga | Confidence | Verified by |
|---|---|---|---|---|---|
| Basic chat | yes | yes | yes | verified | `gigachat_chat.py`, `langchain_chat.py`, `gpt2giga_openai_http.py`, `gpt2giga_anthropic_http.py` |
| Streaming | yes | yes | yes | verified | `gigachat_stream.py`, `langchain_stream.py`, `gpt2giga_openai_http.py` |
| Embeddings | yes | yes | yes | verified | `gigachat_embeddings.py`, `langchain_embeddings.py`, `gpt2giga_embeddings_http.py` |
| Function calling or tool selection | yes | yes | yes | verified | `gigachat_functions.py`, `langchain_tools.py`, `gpt2giga_tools_http.py` |
| Final tool loop execution | yes | partial | partial | verified caution | `gigachat_functions.py` |
| File upload | yes | via underlying client | n/a as native feature | verified | `gigachat_files.py`, `langchain_file_context_single.py` |
| Single image understanding | yes | yes | docs/code-backed | verified for SDK and LangChain | `gigachat_file_context_single.py`, `langchain_file_context_single.py` |
| Single audio understanding | yes | yes | docs/code-backed | verified for SDK and LangChain | `gigachat_file_context_single.py --file wav`, `langchain_file_context_single.py --file wav` |
| Single PDF understanding | yes | yes | docs/code-backed | verified for SDK and LangChain | `gigachat_file_context_single.py --file pdf`, `langchain_file_context_single.py --file pdf` |
| Multi-image comparison | yes | yes | docs/code-backed | verified for SDK and LangChain | `gigachat_compare_images.py`, `langchain_compare_images.py` |
| Structured output | docs/code-backed | yes | n/a | verified for LangChain | `langchain_structured_output.py` |
| Mixed modalities in one request | unreliable | unreliable | not verified | verified caution | `gigachat_files_context.py` |
| Mixed modalities across turns | unreliable | unreliable | not tested | verified caution for SDK and LangChain | `gigachat_multiturn_mixed_context.py`, `langchain_multiturn_mixed_context.py` |
| OpenAI-compatible clients | no | no | yes | verified | `gpt2giga_openai_http.py` |
| Anthropic-compatible clients | no | no | yes | verified | `gpt2giga_anthropic_http.py` |

## Agent rules derived from the matrix

- Choose the simplest row with `verified` coverage before considering `docs/code-backed` paths.
- Treat `verified caution` rows as constraints, not as green lights.
- Do not assume `gpt2giga` matches native OpenAI or Anthropic behavior byte-for-byte.
- Do not assume mixed-modality support unless the exact combination is locally verified.

## Notes

- `langchain-gigachat` file flows currently rely on the underlying SDK client for upload and delete.
- `gpt2giga` is a compatibility layer, not a replacement for the native SDK surface.
- Full multi-step tool execution belongs to the outer client or agent runtime for LangChain and `gpt2giga`.
