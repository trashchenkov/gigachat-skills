# Embeddings

Use this file for direct SDK embeddings and retrieval-oriented indexing.

## Default path

1. Pick one embeddings model for the whole index.
2. Batch texts into practical request sizes.
3. Use the same model for query and document embeddings within one index.
4. If the task is LangChain RAG, switch to `langchain-gigachat`.

Status: `verified`

## Main embeddings models

- `Embeddings`
- `Embeddings-2`
- `EmbeddingsGigaR`
- `GigaEmbeddings-3B-2025-09`

Status: `docs/code-backed`

## Model choice rules

- use `EmbeddingsGigaR` as the default retrieval model
- use `Embeddings` when compatibility or simplicity matters more than retrieval quality
- do not mix vectors from different embeddings models inside one vector store

Status: `docs/code-backed`

## Minimal example

```python
from gigachat import GigaChat

with GigaChat() as client:
    result = client.embeddings(
        ["Hello world", "Machine learning is useful"],
        model="EmbeddingsGigaR",
    )
    print(len(result.data[0].embedding))
```

Status: `verified`

## Practical guidance

- pass the embeddings model to `embeddings(...)`
- batch texts instead of sending one request per short string
- embeddings billing is separate from text generation

Status: `docs/code-backed`

## Retrieval note

Instruction-style prefixes can help query embeddings in some retrieval setups. Apply such prefixes to queries, not to stored documents.

Status: `inference`

## Batching guidance

- keep batch sizes practical rather than maximal
- for very large offline jobs, prefer async or batch-oriented processing over synchronous per-document loops

Status: `inference`
