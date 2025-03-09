I got tool calls working on streaming calls to chatcompletion last weekend. It was a pain, as it’s not documented, and it’s unclear what’s happening when you dump the chunks to text. Plus there may be multiple tool/function calls in a single response now. It’s doable, though, and it does work. The relevant snippet is this:

```python
tool_calls = []

# build up the response structs from the streamed response, simultaneously sending message chunks to the browser
for chunk in response:
    delta = chunk.choices[0].delta
    #app.logger.info(f"chunk: {delta}")

    if delta and delta.content:
        # content chunk -- send to browser and record for later saving
        socket.send(json.dumps({'type': 'message response', 'text': delta.content }))
        newsessionrecord["content"] += delta.content

    elif delta and delta.tool_calls:
        tcchunklist = delta.tool_calls
        for tcchunk in tcchunklist:
            if len(tool_calls) <= tcchunk.index:
                tool_calls.append({"id": "", "type": "function", "function": { "name": "", "arguments": "" } })
            tc = tool_calls[tcchunk.index]

            if tcchunk.id:
                tc["id"] += tcchunk.id
            if tcchunk.function.name:
                tc["function"]["name"] += tcchunk.function.name
            if tcchunk.function.arguments:
                tc["function"]["arguments"] += tcchunk.function.arguments
```