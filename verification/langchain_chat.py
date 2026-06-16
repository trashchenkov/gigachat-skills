#!/usr/bin/env python3
from __future__ import annotations

import common


def run(args):
    common.require_live(args)
    common.require_gigachat_auth()
    lc_messages = common.import_or_skip("langchain_core.messages")
    chat_models = common.import_or_skip("langchain_gigachat.chat_models")
    llm = chat_models.GigaChat(model=args.model)
    response = llm.invoke([lc_messages.HumanMessage(content="Reply with one short sentence: langchain ok")])
    text = getattr(response, "content", "")
    if not text:
        raise RuntimeError("empty LangChain response")
    return {"message": "LangChain GigaChat returned text", "text_preview": str(text)[:120]}


if __name__ == "__main__":
    common.main("langchain_chat.py smoke check", run)
