# Anthropic Tool Use Streaming Issue

## Problem Description

We've identified an issue with our handling of Anthropic API streaming responses that contain tool use events. Currently, our implementation is not properly detecting and handling tool use events in streaming mode, which prevents the LLM from using tools during chat interactions.

### Current Behavior

1. When a user sends a message that should trigger a tool use (e.g., "list my dags"), the Anthropic API correctly generates a streaming response that includes a tool_use event.
2. However, our streaming response handler in `AnthropicProvider.get_streaming_content()` is only looking for text content and ignores tool_use events.
3. After the streaming response is complete, we check for tool calls in the complete response object, but by then it's too late to properly handle the tool use in streaming mode.

### Sample Anthropic Tool Use Event Structure

The Anthropic API sends tool use events in the following format during streaming:

```
event: content_block_start
data: {"type":"content_block_start","index":1,"content_block":{"type":"tool_use","id":"toolu_01T1x1fJ34qAmk2tNTrN7Up6","name":"get_weather","input":{}}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":"{\"location\": \"San Francisco, CA\", \"unit\": \"fahrenheit\"}"}}

event: content_block_stop
data: {"type":"content_block_stop","index":1}

event: message_delta
data: {"type":"message_delta","delta":{"stop_reason":"tool_use","stop_sequence":null},"usage":{"output_tokens":89}}

event: message_stop
data: {"type":"message_stop"}
```

## Root Cause

The root cause of the issue is in the `get_streaming_content()` method in the `AnthropicProvider` class. This method is responsible for processing streaming responses from the Anthropic API, but it only handles text content and doesn't detect or process tool_use events.

Specifically:
1. The method only looks for content_block_delta events with text content
2. It doesn't recognize or handle tool_use events
3. It doesn't capture the complete response object for later tool call processing

## Proposed Solution

To fix this issue, we need to enhance our streaming response handler to detect and handle tool_use events in real-time. Here's a high-level approach:

1. **Enhance the `get_streaming_content()` method**:
   - Detect content_block_start events with type "tool_use"
   - Capture tool_use events and their parameters
   - Send a special marker in the stream when a tool_use event is detected
   - Continue building the complete response object for later processing

2. **Modify the frontend to handle tool_use markers**:
   - Recognize the special tool_use markers in the stream
   - Display an appropriate UI indication that a tool is being used
   - Disable user input while tools are being processed

3. **Update the `has_tool_calls()` method**:
   - Ensure it can detect tool_use events in both streaming and non-streaming responses
   - Make it more robust to different response formats

4. **Improve logging**:
   - Add detailed logging of streaming events to help debug issues
   - Log the complete structure of tool_use events when they're detected

## Implementation Steps

1. **Update AnthropicProvider.get_streaming_content()**:
   - Add detection for content_block_start events with type "tool_use"
   - When a tool_use event is detected, yield a special JSON-formatted message
   - Continue capturing the complete response for later processing

2. **Update the streaming response handler in views.py**:
   - Modify the _handle_streaming_response method to handle tool_use markers
   - Ensure the complete response object is properly constructed

3. **Update the frontend JavaScript**:
   - Add handling for the special tool_use markers
   - Update the UI to show when tools are being used

4. **Add comprehensive logging**:
   - Log the structure of all streaming events
   - Add specific logging for tool_use events


## Additional Considerations

- We should consider adding a fallback mechanism for when streaming tool use detection fails
