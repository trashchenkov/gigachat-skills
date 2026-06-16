#!/usr/bin/env python3
from __future__ import annotations

import json

import common


def run(args):
    common.require_live(args)
    common.require_gigachat_auth()
    gigachat_models = common.import_or_skip("gigachat.models")
    with common.native_client(args.model) as client:
        # Compatibility SDK surface used by the current skill; future updates may
        # add a primary chat-completions version next to this smoke.
        Function = getattr(gigachat_models, "Function")
        FunctionParameters = getattr(gigachat_models, "FunctionParameters")
        Chat = getattr(gigachat_models, "Chat")
        Messages = getattr(gigachat_models, "Messages")
        MessagesRole = getattr(gigachat_models, "MessagesRole")
        tool = Function(
            name="get_weather",
            description="Get current weather for a city",
            parameters=FunctionParameters(
                type="object",
                properties={"city": {"type": "string", "description": "City name"}},
                required=["city"],
            ),
        )
        payload = Chat(
            messages=[Messages(role=MessagesRole.USER, content="Use the tool for weather in Moscow")],
            functions=[tool],
            function_call="auto",
        )
        response = client.chat(payload)
    choice = response.choices[0]
    called = getattr(choice, "finish_reason", None) == "function_call" or bool(getattr(choice.message, "function_call", None))
    if not called:
        raise RuntimeError(f"model did not return a function call: {json.dumps(str(response)[:500])}")
    return {"message": "native function calling returned a tool call"}


if __name__ == "__main__":
    common.main("gigachat_functions.py smoke check", run)
