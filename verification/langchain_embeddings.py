#!/usr/bin/env python3
from __future__ import annotations

import common


def run(args):
    common.require_live(args)
    common.require_gigachat_auth()
    emb_mod = common.import_or_skip("langchain_gigachat.embeddings")
    embeddings = emb_mod.GigaChatEmbeddings(model=args.embeddings_model)
    vectors = embeddings.embed_documents(["hello", "world"])
    if not vectors or not vectors[0]:
        raise RuntimeError("empty LangChain embeddings result")
    return {"message": "LangChain embeddings returned vectors", "vectors": len(vectors), "dimensions": len(vectors[0])}


if __name__ == "__main__":
    common.main("langchain_embeddings.py smoke check", run)
