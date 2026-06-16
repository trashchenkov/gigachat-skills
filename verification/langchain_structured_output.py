#!/usr/bin/env python3
from __future__ import annotations

from typing import Literal

import common


def run(args):
    common.require_live(args)
    common.require_gigachat_auth()
    pydantic = common.import_or_skip("pydantic")
    chat_models = common.import_or_skip("langchain_gigachat.chat_models")

    class SmokeResult(pydantic.BaseModel):
        """A tiny structured smoke-test result."""

        status: Literal["ok"] = pydantic.Field(description="Fixed status marker; must be ok")
        count: int = pydantic.Field(description="Small integer count returned by the model")

    llm = chat_models.GigaChat(model=args.model)
    structured = llm.with_structured_output(SmokeResult)
    result = structured.invoke("Return status ok and count 1")
    if getattr(result, "status", None) != "ok":
        raise RuntimeError(f"unexpected structured result: {result!r}")
    return {"message": "LangChain structured output returned parsed object", "count": result.count}


if __name__ == "__main__":
    common.main("langchain_structured_output.py smoke check", run)
