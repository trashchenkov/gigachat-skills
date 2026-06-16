# Embeddings And RAG

Use this file for LangChain-native embeddings and retrieval pipelines.

## Default path

1. Use `GigaChatEmbeddings` when the retrieval pipeline already lives in LangChain.
2. Keep chunking, vector store logic, and retrieval policy in LangChain.
3. Keep auth, certs, and connectivity concerns in setup/config.
4. If the task is only direct embeddings, use `gigachat-sdk-files-embeddings` instead.

Status: `source-backed`

## Embeddings

```python
from langchain_gigachat.embeddings import GigaChatEmbeddings

# Credentials and TLS settings are read from standard GIGACHAT_* env vars
# when they are already loaded.
embeddings = GigaChatEmbeddings(model="EmbeddingsGigaR")
```

Pass explicit constructor arguments only when overriding the environment. Use `verify_ssl_certs=False` only for local/dev certificate troubleshooting.

Status: `smoke-covered`

## Query and document embedding

- `embed_documents([...])`
- `embed_query("...")`
- async variants are available

Status: `source-backed`

## Wrapper behavior

- the wrapper batches by cumulative character count and part count
- sync and async methods are available
- query-prefix behavior may be available for retrieval tuning
- keep the same embeddings model for query and document vectors in one index

Status: `source-backed`

## RAG sketch

```python
from langchain_chroma import Chroma
from langchain_core.documents import Document

docs = [Document(page_content="Cats are independent animals.")]
store = Chroma.from_documents(docs, embedding=embeddings)
results = store.similarity_search("cat")
```

Status: `source-backed`

## Practical rules

- use `EmbeddingsGigaR` by default for retrieval unless there is a reason not to
- add query prefixes only when the retrieval setup benefits from them
- do not move retrieval policy into the model layer
- use Deep Agents profile guidance only when an actual Deep Agents harness is involved

Status: `source-backed`
