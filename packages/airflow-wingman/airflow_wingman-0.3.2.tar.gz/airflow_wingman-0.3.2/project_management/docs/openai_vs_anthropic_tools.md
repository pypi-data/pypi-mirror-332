# Comparison of Tool Implementation: OpenAI vs Anthropic

This document outlines the major differences in how OpenAI and Anthropic implement function calling/tool usage in their respective APIs.

## 1. Tool Definition Structure

**OpenAI:**
- Uses a nested structure with `type` and `function` fields
- Tool definitions include `name`, `description`, and `parameters` inside the `function` object
- Parameters use JSON Schema format with `properties` and `required` fields

```json
{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get weather information",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City name"}
            },
            "required": ["location"]
        }
    }
}
```

**Anthropic:**
- Uses a flatter structure with top-level fields
- Tool definitions include `name`, `description`, and `input_schema` directly
- Input schema is a standard JSON Schema object

```json
{
    "name": "get_weather",
    "description": "Get weather information",
    "input_schema": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "City name"}
        },
        "required": ["location"]
    }
}
```

## 2. Response Format

**OpenAI:**
- Tool calls are in a separate `tool_calls` field of the message object
- Each tool call has an `id`, `type`, and `function` with `name` and `arguments`
- Tool calls are distinct from the message content

```python
message = response.choices[0].message
if hasattr(message, 'tool_calls') and message.tool_calls:
    for tool_call in message.tool_calls:
        tool_id = tool_call.id
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
```

**Anthropic:**
- Tool calls are part of the message content as blocks with `type: "tool_use"`
- Each tool use block has an `id`, `name`, and `input` object
- Tool calls are integrated with other content blocks in the response

```python
for block in response.content:
    if isinstance(block, dict) and block.get('type') == 'tool_use':
        tool_id = block.get('id')
        tool_name = block.get('name')
        tool_input = block.get('input', {})
```

## 3. Tool Results Format

**OpenAI:**
- Tool results are sent as messages with a special `role: "tool"`
- Each tool result includes a `tool_call_id` reference to the original tool call
- Results are added as separate messages in the conversation history

```python
tool_messages = []
for tool_call_id, result in tool_results.items():
    tool_messages.append({
        "role": "tool",
        "tool_call_id": tool_call_id,
        "content": result.get("result", str(result))
    })
```

**Anthropic:**
- Tool results are sent as content blocks with `type: "tool_result"`
- Each result includes a `tool_use_id` reference to the original tool use
- Results are added as content blocks in a user message

```python
tool_result_blocks = []
for tool_id, result in tool_results.items():
    tool_result_blocks.append({
        "type": "tool_result",
        "tool_use_id": tool_id,
        "content": result.get("result", str(result))
    })
```

## 4. Message Structure

**OpenAI:**
- Uses the standard ChatML format with `role` and `content` fields
- System, user, assistant, and tool messages are all separate messages
- Tool calls and results are handled as special message types

**Anthropic:**
- Has a different message format that requires conversion from ChatML
- System messages are handled as user messages with special formatting
- Tool results are embedded within content blocks rather than separate messages

## 5. Implementation Implications

These differences highlight why we need separate provider implementations that handle the specific requirements of each API while maintaining a consistent interface for our application. Our provider classes abstract away these differences by:

1. Converting between our internal tool representation and provider-specific formats
2. Handling the different message structures and content formats
3. Processing tool calls and results in a provider-specific way
4. Providing a unified interface for the rest of the application

This abstraction layer allows us to support multiple LLM providers without changing the core application logic.
