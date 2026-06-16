#!/usr/bin/env python3
from __future__ import annotations

import common


def run(args):
    common.require_live(args)
    payload = {
        "model": args.model,
        "messages": [{"role": "user", "content": "Use get_weather for Moscow"}],
        "tools": [
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get current weather for a city",
                    "parameters": {
                        "type": "object",
                        "properties": {"city": {"type": "string"}},
                        "required": ["city"],
                    },
                },
            }
        ],
        "tool_choice": "auto",
        "max_tokens": 64,
    }
    result = common.post_json(f"{args.base_url.rstrip('/')}/chat/completions", payload, args.api_key)
    message = result.get("choices", [{}])[0].get("message", {})
    calls = message.get("tool_calls") or []
    if not calls:
        raise RuntimeError(f"no OpenAI-compatible tool call returned: {result}")
    return {"message": "gpt2giga OpenAI-compatible tool call returned", "tool_calls": len(calls)}


if __name__ == "__main__":
    common.main("gpt2giga_tools_http.py smoke check", run)
