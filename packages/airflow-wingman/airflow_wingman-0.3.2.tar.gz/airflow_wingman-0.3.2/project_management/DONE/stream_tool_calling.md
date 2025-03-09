# Implementing Tool Calling with Streaming Responses

## Current Problem

The Airflow Wingman plugin currently faces a limitation in how it processes responses from AI models:

1. **In non-streaming mode**: Tool calls are properly detected, executed, and followed up with a response that includes the tool results.

2. **In streaming mode**: The response is streamed directly to the user without processing any tool calls, which means the AI can request a tool, but the tool will never be executed.

This creates a situation where users must choose between:
- Fast, incremental responses (streaming) without tool functionality
- Full tool functionality but slower, all-at-once responses (non-streaming)

The issue is in the core `chat_completion` method in `llm_client.py`:

```python
# If streaming, return the generator directly
if stream:
    logger.info(f"Using streaming response from {self.provider_name}")
    return self.provider.get_streaming_content(response)

# For non-streaming responses, handle tool calls if present
if self.provider.has_tool_calls(response):
    # Tool handling code here...
```

When streaming is enabled, the function returns early and the tool handling code is never executed.

## Technical Challenge

Implementing tool calls with streaming presents several challenges:

1. **Early Detection**: Tool calls might appear partway through a streaming response.
2. **Buffering**: We need to capture the complete response while streaming to detect tool calls.
3. **State Management**: We need to track the conversation state while streaming.
4. **User Experience**: Users should see a seamless experience, not separate responses.

## Implementation Plan

We'll implement a hybrid approach that maintains streaming's responsiveness while adding tool call functionality. This will be done in phases:

### Phase 1: Stream-then-Tool Approach

In this initial implementation, we'll:
1. Stream the initial response to the user in real-time
2. Simultaneously collect the complete response
3. After streaming completes, check for tool calls
4. If tool calls exist, execute them and make a follow-up request
5. Stream the follow-up response to the user

#### Changes Required:

**1. Modify `views.py`:**
- Collect complete response while streaming
- After streaming finishes, check for tool calls
- If tool calls exist, make a second request and stream that too

**2. Add a method to `llm_client.py`:**
- Create a new method for post-streaming tool call processing
- Process tool calls and make follow-up requests

**3. Preserve original response in providers:**
- Ensure the original response is accessible for tool call extraction

### Phase 1.5: UI/UX Enhancement - Disable Send Button During Processing

To prevent users from sending new messages while tool calls are being processed (which could lead to confusion or race conditions), we'll implement a frontend enhancement:

**1. Signal tool processing state to frontend:**
- Send a special SSE event that indicates tool processing has started
- Send another event when tool processing is complete

**2. Disable the send button during tool processing:**
- When tool processing starts, disable the send button
- Re-enable the button when processing completes or on error

#### Implementation Details:

**1. Add special SSE events in `views.py`:**

```python
def stream_response():
    # ... existing code ...
    
    # Check for tool calls and make follow-up if needed
    if client.provider.has_tool_calls(response_obj):
        # Signal tool processing start - frontend should disable send button
        yield f"data: {{\"event\": \"tool_processing_start\"}}\n\n"
        
        logger.info("Response contains tool calls, making follow-up request")
        # ... tool processing ...
        
        # Signal tool processing complete - frontend can re-enable send button
        yield f"data: {{\"event\": \"tool_processing_complete\"}}\n\n"
    
    # Signal end of stream
    yield "data: [DONE]\n\n"
```

**2. Update frontend JavaScript to handle these events:**

```javascript
eventSource.onmessage = function(event) {
  try {
    const data = JSON.parse(event.data);
    
    // Handle special events
    if (data.event === "tool_processing_start") {
      // Disable send button
      document.getElementById("send-button").disabled = true;
      
      // Optionally show a processing indicator
      showProcessingIndicator("Processing tool calls...");
      return;
    }
    
    if (data.event === "tool_processing_complete") {
      // Re-enable send button
      document.getElementById("send-button").disabled = false;
      
      // Hide processing indicator if shown
      hideProcessingIndicator();
      return;
    }
    
    // Normal message handling...
  } catch (e) {
    // Not JSON, handle as regular message chunk
    if (event.data === "[DONE]") {
      // Streaming is complete
      eventSource.close();
      
      // Make sure button is enabled when complete
      document.getElementById("send-button").disabled = false;
    } else {
      // Process chunk...
    }
  }
};
```

**3. Add visual feedback for the user:**

```css
/* CSS for processing indicator */
.processing-indicator {
  display: none;
  background-color: #f0f8ff;
  padding: 8px 12px;
  border-radius: 4px;
  margin: 8px 0;
  font-style: italic;
}

.processing-indicator.visible {
  display: block;
}
```

**Benefits of this approach:**
- Prevents user confusion by disabling input during processing
- Provides visual feedback about what's happening
- Maintains the stateful context of the conversation
- Prevents race conditions from multiple simultaneous requests

**Potential challenges:**
- Requires coordination between backend and frontend
- Needs proper error handling to ensure the button isn't permanently disabled

### Phase 2: Enhanced Streaming with Tool Calls

In a more advanced implementation (future work), we could:
1. Stream until a tool call is detected
2. Pause streaming, showing a "processing" indicator
3. Execute the tool
4. Resume streaming with the tool results included

This would require more complex state management but provide a more seamless experience.

## Implementation Sketch for Phase 1

### Step 1: Update the `_handle_streaming_response` method in `views.py`:

```python
def _handle_streaming_response(self, client: LLMClient, data: dict) -> Response:
    """Handle streaming response."""
    try:
        logger.info("Beginning streaming response")
        response_obj, generator = client.chat_completion_with_storage(
            messages=data["messages"], 
            model=data["model"], 
            temperature=data["temperature"], 
            max_tokens=data["max_tokens"]
        )

        def stream_response():
            complete_response = ""
            
            # Stream the initial response
            for chunk in generator:
                if chunk:
                    complete_response += chunk
                    yield f"data: {chunk}\n\n"
            
            # Log the complete assembled response
            logger.info(f"COMPLETE RESPONSE START >>>")
            logger.info(complete_response)
            logger.info(f"<<< COMPLETE RESPONSE END")
            
            # Check for tool calls and make follow-up if needed
            if client.provider.has_tool_calls(response_obj):
                logger.info("Response contains tool calls, making follow-up request")
                
                follow_up_response = client.process_tool_calls_and_follow_up(
                    response_obj, 
                    data["messages"],
                    data["model"],
                    data["temperature"],
                    data["max_tokens"]
                )
                
                yield f"data: \n\n**Processing tool calls...**\n\n"
                
                # Stream the follow-up response
                for chunk in follow_up_response:
                    if chunk:
                        yield f"data: {chunk}\n\n"
            
            # Signal end of stream
            yield "data: [DONE]\n\n"

        return Response(stream_response(), mimetype="text/event-stream", 
                       headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})
    except Exception as e:
        logger.error(f"Streaming error: {str(e)}")
        return jsonify({"error": str(e)}), 500
```

### Step 2: Add new methods to `llm_client.py`:

```python
def chat_completion_with_storage(self, messages, model, temperature=0.7, max_tokens=None):
    """
    Send a chat completion request that returns both the response object and a streaming generator.
    """
    provider_tools = self.provider.convert_tools(self.airflow_tools)
    
    try:
        logger.info(f"Sending chat completion request to {self.provider_name} with model: {model}")
        response = self.provider.create_chat_completion(
            messages=messages, 
            model=model, 
            temperature=temperature, 
            max_tokens=max_tokens, 
            stream=True, 
            tools=provider_tools
        )
        logger.info(f"Received streaming response from {self.provider_name}")
        
        # Return both the original response object and the generator
        return response, self.provider.get_streaming_content(response)
    except Exception as e:
        error_msg = f"Error in {self.provider_name} API call: {str(e)}\n{traceback.format_exc()}"
        logger.error(error_msg)
        return None, (yield f"Error: {str(e)}")

def process_tool_calls_and_follow_up(self, response, messages, model, temperature, max_tokens):
    """
    Process tool calls from a response and make a follow-up request.
    Returns a generator for streaming the follow-up response.
    """
    try:
        # Process tool calls and get results
        cookie = session.get("airflow_cookie")
        if not cookie:
            error_msg = "No Airflow cookie available"
            logger.error(error_msg)
            yield f"Error: {error_msg}"
            return
            
        tool_results = self.provider.process_tool_calls(response, cookie)
        
        # Make follow-up request with tool results
        logger.info("Making follow-up request with tool results")
        follow_up_response = self.provider.create_follow_up_completion(
            messages=messages, 
            model=model, 
            temperature=temperature, 
            max_tokens=max_tokens, 
            tool_results=tool_results, 
            original_response=response,
            stream=True
        )
        
        # Return a generator for streaming the follow-up response
        return self.provider.get_streaming_content(follow_up_response)
    except Exception as e:
        error_msg = f"Error processing tool calls: {str(e)}\n{traceback.format_exc()}"
        logger.error(error_msg)
        yield f"Error: {str(e)}"
```

### Step 3: Update the provider class to support the new workflow:

- Modify `create_follow_up_completion` to support streaming
- Ensure `has_tool_calls` works with the stored response object

## Considerations and Challenges

1. **User Experience**: Users will see a delay between the initial response and the follow-up, which may not be ideal.

2. **Error Handling**: Need robust error handling to ensure the streaming doesn't break if tool execution fails.

3. **Provider Support**: Different LLM providers have different APIs for tool calling, so each provider implementation may need custom handling.

4. **Stateful Processing**: This approach requires maintaining state across multiple requests.

## Future Work (Phase 2 and Beyond)

1. **Real-time Tool Calling**: Implement a more sophisticated approach that can interrupt streaming when tool calls are detected.

2. **Tool Call Batching**: Group multiple tool calls together to minimize the number of follow-up requests.

3. **Parallel Tool Execution**: Execute multiple tools in parallel to reduce waiting time.

4. **UI Improvements**: Add visual indicators when tools are being executed.

5. **Streaming with Function Calling**: Explore LLM providers that natively support streaming with function calling for a more integrated experience.
