# Implementation Plan for Follow-up Response Display

## Overview

This plan outlines the necessary changes to implement proper display of follow-up responses from the LLM in the Airflow Wingman UI. The goal is to create a new message box for follow-up responses after tool calls, improving the user experience by clearly separating initial responses from follow-up responses. The implementation must account for recursive tool calls, where a follow-up response may trigger additional tool calls, resulting in multiple levels of follow-up responses.

## Phase 1: Backend Changes (views.py)

### Goal
Modify the backend to send special events for follow-up responses that the frontend can recognize and handle appropriately.

### Tasks
1. Add a "follow_up_response_start" event to signal the beginning of a follow-up response
2. Add a "follow_up_response_chunk" event to wrap each follow-up response chunk
3. Add a "follow_up_response_complete" event to signal the end of a follow-up response

### Implementation Details

#### 1.1 Update _handle_streaming_response in views.py

```python
def _handle_streaming_response(self, client: LLMClient, data: dict) -> Response:
    try:
        logger.info("Beginning streaming response")
        streaming_response = client.chat_completion(
            messages=data["messages"], model=data["model"], temperature=data["temperature"], 
            max_tokens=data["max_tokens"], stream=True
        )

        def stream_response(cookie=None):
            complete_response = ""

            # Stream the initial response
            for chunk in streaming_response:
                if chunk:
                    complete_response += chunk
                    yield f"data: {chunk}\n\n"

            # Log the complete assembled response
            logger.info("COMPLETE RESPONSE START >>>")
            logger.info(complete_response)
            logger.info("<<< COMPLETE RESPONSE END")

            # Check for tool calls and make follow-up if needed
            if client.has_tool_calls(streaming_response):
                # Signal tool processing start - frontend should disable send button
                yield f"data: {json.dumps({'event': 'tool_processing_start'})}\n\n"

                logger.info("Response contains tool calls, making follow-up request")

                # Process tool calls and get follow-up response
                follow_up_response = client.process_tool_calls_and_follow_up(
                    streaming_response, 
                    data["messages"], 
                    data["model"], 
                    data["temperature"], 
                    data["max_tokens"], 
                    cookie=cookie,
                    stream=True
                )

                # Signal the start of a follow-up response
                yield f"data: {json.dumps({'event': 'follow_up_response_start', 'level': 1})}\n\n"

                # Stream the follow-up response
                follow_up_complete_response = ""
                for chunk in follow_up_response:
                    if chunk:
                        # Check if this is a special event JSON (for recursive tool calls)
                        try:
                            event_data = json.loads(chunk)
                            if isinstance(event_data, dict) and "event" in event_data:
                                # If this is a nested tool processing event, adjust the level
                                if event_data["event"] == "tool_processing_start":
                                    yield f"data: {json.dumps({'event': 'tool_processing_start', 'nested': True})}\n\n"
                                    continue
                                elif event_data["event"] == "tool_processing_complete":
                                    yield f"data: {json.dumps({'event': 'tool_processing_complete', 'nested': True})}\n\n"
                                    continue
                                # For nested follow-up responses, increment the level
                                elif event_data["event"] == "follow_up_response_start":
                                    yield f"data: {json.dumps({'event': 'follow_up_response_start', 'level': 2})}\n\n"
                                    continue
                                elif event_data["event"] == "follow_up_response_chunk":
                                    # Pass through with level information
                                    yield f"data: {json.dumps({'event': 'follow_up_response_chunk', 'content': event_data['content'], 'level': 2})}\n\n"
                                    continue
                                elif event_data["event"] == "follow_up_response_complete":
                                    yield f"data: {json.dumps({'event': 'follow_up_response_complete', 'content': event_data['content'], 'level': 2})}\n\n"
                                    continue
                                else:
                                    # Pass through other events
                                    yield f"data: {chunk}\n\n"
                                    continue
                        except json.JSONDecodeError:
                            # Not JSON, treat as normal content
                            pass
                        
                        follow_up_complete_response += chunk
                        # Wrap the chunk in a follow_up_response_chunk event
                        yield f"data: {json.dumps({'event': 'follow_up_response_chunk', 'content': chunk, 'level': 1})}\n\n"

                # Log the complete follow-up response
                logger.info("FOLLOW-UP RESPONSE START >>>")
                logger.info(follow_up_complete_response)
                logger.info("<<< FOLLOW-UP RESPONSE END")

                # Signal the end of the follow-up response
                yield f"data: {json.dumps({'event': 'follow_up_response_complete', 'content': follow_up_complete_response, 'level': 1})}\n\n"

                # Signal tool processing complete - frontend can re-enable send button
                yield f"data: {json.dumps({'event': 'tool_processing_complete'})}\n\n"

            # Send the complete response as a special event (for compatibility with existing code)
            complete_event = json.dumps({"event": "complete_response", "content": complete_response})
            yield f"data: {complete_event}\n\n"

            # Signal end of stream
            yield "data: [DONE]\n\n"

        return Response(stream_response(cookie=airflow_cookie), mimetype="text/event-stream", headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})
    except Exception as e:
        logger.error(f"Streaming error: {str(e)}")
        return jsonify({"error": str(e)}), 500
```

## Phase 2: Frontend Changes (wingman_chat.js)

### Goal
Modify the frontend to handle the new follow-up response events and create a new message box for follow-up responses.

### Tasks
1. Add event handlers for the new follow-up response events
2. Create a new message box for follow-up responses
3. Render follow-up response content in the new message box

### Implementation Details

#### 2.1 Update sendMessage function in wingman_chat.js

```javascript
async function sendMessage() {
    // ... existing code ...

    try {
        // ... existing code ...

        // Process the streaming response
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let fullResponse = '';
        
        // Reset any existing follow-up tracking
        window.followUpMessageDivs = {};
        window.followUpResponses = {};

        while (true) {
            const { value, done } = await reader.read();
            if (done) break;

            const chunk = decoder.decode(value);
            const lines = chunk.split('\n');

            for (const line of lines) {
                if (line.trim() === '') continue;

                if (line.startsWith('data: ')) {
                    const content = line.slice(6); // Remove 'data: ' prefix

                    // Check for special events or end marker
                    if (content === '[DONE]') {
                        console.log('Stream complete');

                        // Add assistant's response to history
                        if (fullResponse) {
                            messageHistory.push({
                                role: 'assistant',
                                content: fullResponse
                            });
                        }

                        // Follow-up responses are already added to history when they complete
                        continue;
                    }

                    // Try to parse as JSON for special events
                    try {
                        const parsed = JSON.parse(content);

                        // ... existing event handlers ...

                        // Handle follow-up response start event
                        if (parsed.event === 'follow_up_response_start') {
                            const level = parsed.level || 1;
                            console.log(`Follow-up response started (level ${level})`);
                            
                            // Create a new message div for the follow-up response
                            // Store the level as a data attribute for potential styling
                            const newMessageDiv = addMessage('', false);
                            newMessageDiv.dataset.followupLevel = level;
                            
                            // Track follow-up message divs by level
                            if (!window.followUpMessageDivs) {
                                window.followUpMessageDivs = {};
                            }
                            window.followUpMessageDivs[level] = newMessageDiv;
                            
                            // Track follow-up responses by level
                            if (!window.followUpResponses) {
                                window.followUpResponses = {};
                            }
                            window.followUpResponses[level] = '';
                            
                            continue;
                        }

                        // Handle follow-up response chunk event
                        if (parsed.event === 'follow_up_response_chunk') {
                            const level = parsed.level || 1;
                            console.log(`Received follow-up response chunk (level ${level})`);
                            
                            // Get the appropriate message div for this level
                            const targetMessageDiv = window.followUpMessageDivs?.[level];
                            if (!targetMessageDiv) {
                                console.error(`No message div found for follow-up level ${level}`);
                                continue;
                            }
                            
                            // Add the chunk to the follow-up response for this level
                            window.followUpResponses[level] += parsed.content;
                            
                            // Create a properly formatted display
                            if (!targetMessageDiv.classList.contains('pre-formatted')) {
                                targetMessageDiv.classList.add('pre-formatted');
                            }

                            // Always rebuild the entire content from the full follow-up response
                            try {
                                targetMessageDiv.innerHTML = marked.parse(window.followUpResponses[level]);
                            } catch (e) {
                                console.error(`Error parsing markdown in follow-up response level ${level}:`, e);
                                targetMessageDiv.textContent = window.followUpResponses[level];
                            }
                            continue;
                        }

                        // Handle follow-up response complete event
                        if (parsed.event === 'follow_up_response_complete') {
                            const level = parsed.level || 1;
                            console.log(`Follow-up response complete (level ${level})`);
                            
                            // Get the appropriate message div for this level
                            const targetMessageDiv = window.followUpMessageDivs?.[level];
                            if (!targetMessageDiv) {
                                console.error(`No message div found for follow-up level ${level}`);
                                continue;
                            }
                            
                            // Use the complete follow-up response from the backend
                            window.followUpResponses[level] = parsed.content;
                            
                            // Add this follow-up response to message history
                            messageHistory.push({
                                role: 'assistant',
                                content: window.followUpResponses[level]
                            });

                            // Use marked.js to render markdown
                            try {
                                // Configure marked options
                                marked.use({
                                    breaks: true,        // Add line breaks on single newlines
                                    gfm: true,           // Use GitHub Flavored Markdown
                                    headerIds: false,    // Don't add IDs to headers
                                    mangle: false,       // Don't mangle email addresses
                                });

                                // Render markdown to HTML
                                targetMessageDiv.innerHTML = marked.parse(window.followUpResponses[level]);
                            } catch (e) {
                                console.error(`Error rendering markdown for level ${level}:`, e);
                                // Fallback to innerText if markdown parsing fails
                                targetMessageDiv.innerText = window.followUpResponses[level];
                            }
                            continue;
                        }
                        
                        // Handle nested tool processing events
                        if (parsed.event === 'tool_processing_start' && parsed.nested) {
                            console.log('Nested tool processing started');
                            // Optionally show a nested processing indicator
                            continue;
                        }
                        
                        if (parsed.event === 'tool_processing_complete' && parsed.nested) {
                            console.log('Nested tool processing completed');
                            // Optionally hide a nested processing indicator
                            continue;
                        }

                        // ... existing event handlers ...

                        // Handle the complete response event
                        if (parsed.event === 'complete_response') {
                            // ... existing code ...
                            continue;
                        }

                        // If we have JSON that's not a special event, it might be content
                        currentMessageDiv.textContent += JSON.stringify(parsed);
                        fullResponse += JSON.stringify(parsed);
                    } catch (e) {
                        // Not JSON, handle as normal content
                        // ... existing code ...
                    }
                    // Scroll to bottom
                    chatMessages.scrollTop = chatMessages.scrollHeight;
                }
            }
        }
    } catch (error) {
        // ... existing error handling ...
    } finally {
        // ... existing cleanup ...
    }
}
```

## Implementation Approach

The implementation will focus on creating a clear separation between initial responses and follow-up responses in the UI. By using special events to signal the beginning and end of follow-up responses, we can create a more intuitive and user-friendly interface that makes it clear when the assistant is providing additional information after processing tool calls.

A key aspect of this implementation is handling recursive tool calls, where a follow-up response may trigger additional tool calls, resulting in multiple levels of follow-up responses. The frontend will track these levels using a data attribute on the message divs and maintain separate tracking for each level of follow-up response.

This approach maintains the synchronous nature of the Airflow Wingman plugin while improving the user experience by making the conversation flow more natural and easier to follow, even in complex scenarios with multiple levels of tool calls and follow-up responses.