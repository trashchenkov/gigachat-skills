#!/usr/bin/env python3
from __future__ import annotations

import common


def run(args):
    common.require_live(args)
    common.require_gigachat_auth()
    lc_messages = common.import_or_skip("langchain_core.messages")
    tools_mod = common.import_or_skip("langchain_core.tools")
    chat_models = common.import_or_skip("langchain_gigachat.chat_models")

    @tools_mod.tool
    def get_weather(city: str) -> str:
        """Get current weather for a city."""
        return f"{city}: 20C"

    llm = chat_models.GigaChat(model=args.model).bind_tools([get_weather])
    response = llm.invoke([lc_messages.HumanMessage(content="Use the tool for weather in Moscow")])
    tool_calls = getattr(response, "tool_calls", None) or []
    if not tool_calls:
        raise RuntimeError(f"no LangChain tool call returned: {response!r}")
    return {"message": "LangChain tool binding returned tool_calls", "tool_calls": len(tool_calls)}


if __name__ == "__main__":
    common.main("langchain_tools.py smoke check", run)
