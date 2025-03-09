# Making Tool Calling Provider-Agnostic in Airflow Wingman

## The Problem

Airflow Wingman currently supports multiple AI providers (OpenAI and Anthropic) for generating responses and executing tools. However, each provider has a different way of handling tool calls, especially in streaming mode. This creates challenges when we want to maintain a consistent approach across providers.

The specific issue we're facing is with Anthropic's tool use in streaming mode. When a user asks the AI to perform a task that requires using a tool (like listing DAGs or getting weather information), the Anthropic API sends special events in the stream that our code isn't properly detecting and handling.

## Why This Matters

1. **User Experience**: When tool calls aren't properly detected during streaming, users see incomplete or broken responses.

2. **Functionality**: Tools are a core feature of our application. If they don't work properly with all providers, it limits the usefulness of our application.

3. **Maintainability**: Having different handling logic for each provider makes our code harder to maintain and extend.

## Current Implementation Challenges

1. **Different Response Formats**: OpenAI and Anthropic have completely different formats for tool calls in their streaming responses:
   - OpenAI sends tool calls as part of delta chunks with properties like index, id, function name, and arguments
   - Anthropic uses event types like content_block_start, content_block_delta, and content_block_stop with specific event data

2. **Inconsistent Response Objects**: When streaming is enabled, the response objects from different providers have different structures and properties.

3. **Error Handling**: The current code tries to access properties that don't exist on certain response objects, causing errors.

4. **Tool Call Detection**: The current implementation can't properly detect tool calls in streaming mode for Anthropic.

## The Goal: Provider-Agnostic Tool Calling

We want to create a standardized approach to tool calling that works consistently across all providers, while keeping the LLM client code provider-agnostic. This means:

1. The LLM client shouldn't need to know which provider it's working with to handle tool calls correctly.

2. Each provider should handle its specific implementation details internally.

3. The interface between the LLM client and providers should be consistent regardless of the provider.

## Plan to Achieve Provider-Agnostic Tool Calling

### 1. Standardize Response Objects

Create a consistent response object format that works across providers:

- For non-streaming responses: Ensure all providers return a response object with a consistent structure
- For streaming responses: Ensure all providers return a tuple of (response_obj, generator) when requested

### 2. Provider-Specific Implementation

Each provider class (OpenAIProvider, AnthropicProvider) will:

- Handle its specific streaming format internally
- Detect tool calls in its own format
- Normalize the output to a consistent format that the LLM client can work with
- Signal tool use events to the frontend in a standardized way

### 3. Consistent Tool Call Detection

Implement a consistent way to detect tool calls:

- The has_tool_calls() method should work with response objects from any provider
- It should handle both streaming and non-streaming responses
- It should not rely on provider-specific properties

### 4. Standardized Tool Processing

Create a consistent approach to processing tool calls:

- Tool call extraction should work the same way regardless of provider
- Tool execution should be provider-agnostic
- Follow-up responses should be handled consistently

### 5. Frontend Integration

Ensure the frontend can handle tool calls consistently:

- The frontend should receive standardized events for tool processing
- It should not need to know which provider is being used
- The user experience should be consistent across providers

## Implementation Approach

1. **Fix Immediate Issues**: Address the current errors with Anthropic streaming responses.

2. **Refactor Provider Classes**: Update each provider to handle its specific format internally while presenting a consistent interface.

3. **Enhance LLM Client**: Ensure the LLM client works with the standardized interface without provider-specific code.

4. **Test Thoroughly**: Test with both providers in streaming and non-streaming modes to ensure consistent behavior.

## Benefits of This Approach

1. **Maintainability**: Adding new providers will be easier as they just need to implement the standardized interface.

2. **Reliability**: Consistent handling of tool calls will reduce errors and improve the user experience.

3. **Flexibility**: Users can switch between providers without experiencing different behavior.

4. **Future-Proofing**: As providers update their APIs, we only need to update the provider-specific code, not the entire application.

## Conclusion

By standardizing our approach to tool calling across providers, we'll create a more robust, maintainable, and user-friendly application. This will allow us to leverage the strengths of different AI providers while providing a consistent experience to our users.
