I apologize for trying to directly modify the code without explaining first. You're right - I should explain the changes needed and let you implement them.

Based on my analysis, here are the changes I recommend to fix the user message formatting issue:

1. Add CSS styling for markdown elements:
    - Add specific styling for code blocks, lists, headings, etc. in your CSS file
    - This will ensure that markdown elements are properly styled in both user and assistant messages
2. Update the JavaScript to wrap the parsed markdown in a container:
    - In the addMessage function, wrap the parsed markdown in a div with a specific class
    - This will help ensure consistent styling between user and assistant messages

Here's the specific code you would need to add to your CSS file:

```css
/* Markdown content styling */
.markdown-content code {
    background-color: #f0f0f0;
    padding: 2px 4px;
    border-radius: 3px;
    font-family: monospace;
}

.markdown-content pre {
    background-color: #f8f8f8;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ddd;
    overflow-x: auto;
}

.markdown-content pre code {
    background-color: transparent;
    padding: 0;
    border-radius: 0;
}

.markdown-content p {
    margin-bottom: 10px;
}

.markdown-content ul, .markdown-content ol {
    margin-left: 20px;
    margin-bottom: 10px;
}

.markdown-content h1, .markdown-content h2, .markdown-content h3, 
.markdown-content h4, .markdown-content h5, .markdown-content h6 {
    margin-top: 15px;
    margin-bottom: 10px;
}
```
And here's how you would modify the addMessage function in your JavaScript file:

```javascript
function addMessage(content, isUser) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'message-user' : 'message-assistant'}`;

    try {
        // Configure marked options
        marked.use({
            breaks: true,
            gfm: true,
            headerIds: false,
            mangle: false,
        });
        
        // Create a container for the markdown content
        const markdownContainer = document.createElement('div');
        markdownContainer.className = 'markdown-content';
        
        // Parse the content and add it to the container
        markdownContainer.innerHTML = marked.parse(content);
        
        // Add the container to the message div
        messageDiv.appendChild(markdownContainer);
    } catch (e) {
        console.error('Error rendering markdown:', e);
        messageDiv.innerText = content;
    }

    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    return messageDiv;
}
```
You would also need to update the streaming response handler to use the same approach:

```javascript
// In the complete response handler:
try {
    marked.use({
        breaks: true,
        gfm: true,
        headerIds: false,
        mangle: false,
    });
    
    const markdownContainer = document.createElement('div');
    markdownContainer.className = 'markdown-content';
    markdownContainer.innerHTML = marked.parse(fullResponse);
    
    // Clear existing content and add the container
    currentMessageDiv.innerHTML = '';
    currentMessageDiv.appendChild(markdownContainer);
} catch (e) {
    console.error('Error rendering markdown:', e);
    currentMessageDiv.innerText = fullResponse;
}

// And similarly for the streaming content handler
```
These changes should help ensure that both user and assistant messages are formatted consistently with proper markdown styling.