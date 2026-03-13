# Function Calling

Use this file when the model must select or call tools through the native SDK.

## Default path

1. Start with a normal `Chat(messages=[...])` payload.
2. Add `functions=[...]` with a flat JSON-schema-like definition.
3. Use `function_call="auto"` by default.
4. If the model returns `finish_reason == "function_call"`, execute the tool in application code.
5. Send a second request containing the original user message, the assistant function call, and the `function` result message.

Status: `verified`

## Function call modes

- `"auto"`: model decides whether to call a function
- `"none"`: forbid all function calls
- `{"name": "function_name"}`: force a specific function

Use `"auto"` unless the product flow requires a forced tool.

Status: `docs/code-backed`

## Minimal custom function example

```python
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole, Function, FunctionParameters

weather_function = Function(
    name="get_weather",
    description="Get current weather for a city",
    parameters=FunctionParameters(
        type="object",
        properties={
            "city": {"type": "string", "description": "City name"},
            "units": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "Temperature units",
            },
        },
        required=["city"],
    ),
)

payload = Chat(
    messages=[Messages(role=MessagesRole.USER, content="What's the weather in Moscow?")],
    functions=[weather_function],
    function_call="auto",
)

with GigaChat() as client:
    response = client.chat(payload)
    choice = response.choices[0]
    if choice.finish_reason == "function_call":
        print(choice.message.function_call.name)
        print(choice.message.function_call.arguments)
```

Status: `verified`

## Returning tool results

After your code executes the function, send a second request with:

1. the original user message
2. the assistant message containing `function_call`
3. a `function` role message containing the serialized result

Do not expect the SDK or model to complete the multi-step loop for you.

Status: `verified`

## Built-in functions

Documented built-ins include:

- `text2image`
- `text2model3d`

Built-ins may return file references rather than inline bytes. Download generated assets through the files API.

Status: `docs/code-backed`

## Schema rules

- prefer flat object schemas with primitive fields and enums
- avoid `allOf`, `anyOf`, and complex unions as the default path
- add strong descriptions to the function and each parameter
- keep tool names stable and explicit

Status: `docs/code-backed`

## Validation

When schema correctness is uncertain, use the validation endpoint instead of blaming the model first:

- `POST /functions/validate`

Status: `docs/code-backed`
