# Server-Sent Events (SSE) Format Explained

SSE (Server-Sent Events) is a standard for streaming updates from a server to a client over HTTP. Let me explain the specific elements you asked about:

## What is `data: `?

The `data: ` prefix is a core part of the SSE protocol:

- **Purpose**: It marks the beginning of an event's data payload
- **Format**: Each line starting with `data: ` contains content to be delivered to the client
- **Processing**: When using JavaScript's `EventSource` API, the content after `data: ` becomes the `event.data` property

In your code:
```python
yield f"data: {chunk}\n\n"
```

The `data: ` prefix tells the browser "this is actual content to deliver to the client application." The browser's `EventSource` implementation automatically strips this prefix and delivers just the content to your JavaScript event handler.

## What is `[DONE]`?

`[DONE]` is not part of the SSE standard itself, but is a convention used by many AI APIs (including OpenAI and Anthropic):

- **Purpose**: It signals the end of a streaming response
- **Convention**: When the client receives `data: [DONE]`, it knows the server has finished sending all chunks
- **Implementation**: Your code sends this as the final message:
  ```python
  yield "data: [DONE]\n\n"
  ```

Your frontend JavaScript should have code that looks for this marker to know when the complete response has been received, typically something like:

```javascript
eventSource.onmessage = function(event) {
  if (event.data === "[DONE]") {
    // Streaming is complete, close the connection
    eventSource.close();
    // Maybe do some final UI updates
  } else {
    // Process the chunk of data
    // Append to existing content, update UI, etc.
  }
};
```

## The Double Newlines (`\n\n`)

You'll notice `\n\n` at the end of each yield statement:

- **Purpose**: In SSE, events are separated by double newlines
- **Format**: `data: content\n\n`
- **Multiple Fields**: A single event can have multiple data fields, each on its own line with a `data: ` prefix

The browser's `EventSource` implementation knows that a double newline means "this event is complete, deliver it to the application."

## Complete SSE Message Structure

A complete SSE message can include:

```
event: eventName
id: messageID
retry: reconnectionTime
data: your actual content here

```

In your implementation, you're only using the `data:` field, which is the most essential part.

This is why the streaming messages are showing up in your UI - each chunk is being sent as a proper SSE event that the browser knows how to process and deliver to your JavaScript code.
