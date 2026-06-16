#!/usr/bin/env python3
from __future__ import annotations

import common


def run(args):
    common.require_live(args)
    common.require_gigachat_auth()
    lc_messages = common.import_or_skip("langchain_core.messages")
    chat_models = common.import_or_skip("langchain_gigachat.chat_models")
    llm = chat_models.GigaChat(model=args.model)
    chunks = list(llm.stream([lc_messages.HumanMessage(content="Say: langchain stream ok")]))
    text = "".join(str(getattr(chunk, "content", "")) for chunk in chunks)
    if not text.strip():
        raise RuntimeError("empty LangChain stream response")
    return {"message": "LangChain stream returned chunks", "chunks": len(chunks)}


if __name__ == "__main__":
    common.main("langchain_stream.py smoke check", run)
