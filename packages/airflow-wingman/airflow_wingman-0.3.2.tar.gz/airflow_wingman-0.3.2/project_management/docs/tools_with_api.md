# Tools Integration with LLM APIs

This document outlines how to integrate tools (function calling) with different LLM providers: OpenAI and Anthropic.

## OpenAI Tools Integration

OpenAI implements tools as "function calling" where the model can request to call external functions.

### Defining Tools for OpenAI

Tools are defined as objects with the following structure:

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The unit of temperature"
                    }
                },
                "required": ["location"]
            }
        }
    }
]
```

### Making a Request with Tools

```python
from openai import OpenAI

client = OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "user", "content": "What's the weather like in San Francisco?"}
    ],
    tools=tools
)
```

### Handling Tool Calls

When the model decides to use a tool, it will return a response with `tool_calls`:

```python
message = response.choices[0].message
if hasattr(message, 'tool_calls') and message.tool_calls:
    # Process tool calls
    tool_results = {}
    for tool_call in message.tool_calls:
        tool_call_id = tool_call.id
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        
        # Execute the function
        result = execute_function(function_name, arguments)
        tool_results[tool_call_id] = result
    
    # Create a new message with the tool results
    tool_messages = []
    for tool_call_id, result in tool_results.items():
        tool_messages.append({
            "role": "tool",
            "tool_call_id": tool_call_id,
            "content": json.dumps(result)
        })
    
    # Make a second request with the tool results
    second_response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "user", "content": "What's the weather like in San Francisco?"},
            {"role": "assistant", "content": None, "tool_calls": [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments
                    }
                } for tc in message.tool_calls
            ]},
            *tool_messages
        ]
    )
```

## Anthropic Tools Integration

Anthropic's Claude models use a different approach for tools, integrating them directly into the message structure.

### Defining Tools for Anthropic

```python
tools = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA"
                }
            },
            "required": ["location"]
        }
    }
]
```

### Making a Request with Tools

```python
from anthropic import Anthropic

client = Anthropic(api_key="your-api-key")

response = client.messages.create(
    model="claude-3-opus-20240229",
    messages=[
        {"role": "user", "content": "What's the weather like in San Francisco?"}
    ],
    tools=tools
)
```

### Handling Tool Use

When Claude uses a tool, it returns a response with a `tool_use` block in the content:

```python
message = response.content
tool_use_blocks = [block for block in message if block.get("type") == "tool_use"]

if tool_use_blocks:
    # Process tool use blocks
    tool_results = []
    for block in tool_use_blocks:
        tool_id = block["id"]
        tool_name = block["name"]
        tool_input = block["input"]
        
        # Execute the tool
        result = execute_tool(tool_name, tool_input)
        
        # Add tool result
        tool_results.append({
            "type": "tool_result",
            "tool_use_id": tool_id,
            "content": json.dumps(result)
        })
    
    # Make a second request with the tool results
    second_response = client.messages.create(
        model="claude-3-opus-20240229",
        messages=[
            {"role": "user", "content": "What's the weather like in San Francisco?"},
            {"role": "assistant", "content": tool_use_blocks},
            {"role": "user", "content": tool_results}
        ]
    )
```

## Key Differences

1. **Tool Definition Structure**:
   - OpenAI uses `type`, `function.name`, `function.description`, and `function.parameters`
   - Anthropic uses `name`, `description`, and `input_schema`

2. **Response Format**:
   - OpenAI returns tool calls in a separate `tool_calls` field
   - Anthropic includes tool use as content blocks with `type: "tool_use"`

3. **Tool Results**:
   - OpenAI uses a special `role: "tool"` with `tool_call_id` reference
   - Anthropic uses content blocks with `type: "tool_result"` and `tool_use_id` reference

4. **Message Structure**:
   - OpenAI separates tool calls from the message content
   - Anthropic integrates tools directly into the message content structure

## Implementation Considerations

When building a system that supports both APIs:

1. Create an abstraction layer that maps between the two formats
2. Handle the different response structures appropriately
3. Maintain consistent tool definitions that can be converted between formats
4. Consider the different authentication and client initialization requirements
