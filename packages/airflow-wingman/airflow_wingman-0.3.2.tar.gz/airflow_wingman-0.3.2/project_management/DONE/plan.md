# Implementation Plan for Multi-Provider LLM Support in Airflow Wingman

Based on the restructuring documents and the existing code in airflow-mcp-server, I'll create a phase-by-phase implementation plan that follows a logical progression while ensuring the codebase remains functional throughout the transition.

## Phase 1: Setup Provider-Agnostic Tool Representation

1. **Leverage Existing Tool Models**
   - Use the existing `Tool` class from `mcp.types` that's already used in airflow-mcp-server
   - Create conversion utilities in `tools/conversion.py` to standardize tool formats between providers
   - No need to create new tool models as we'll use the existing ones

2. **Establish Base Provider Interface**
   - Create `providers/base.py` with the `BaseLLMProvider` abstract class
   - Define required methods: `convert_tools`, `create_chat_completion`, `process_tool_calls`, etc.
   - Add utility methods for response processing

## Phase 2: Implement Provider-Specific Adapters

1. **Create OpenAI Provider**
   - Implement `providers/openai_provider.py` extending `BaseLLMProvider`
   - Add tool conversion for OpenAI format
   - Implement API request formatting and response parsing
   - Handle tool call execution

2. **Create Anthropic Provider**
   - Implement `providers/anthropic_provider.py` extending `BaseLLMProvider`
   - Add tool conversion for Anthropic format
   - Implement API request formatting and response parsing
   - Handle tool use blocks execution

3. **Create Provider Factory**
   - Implement `providers/__init__.py` with factory function to instantiate providers
   - Support OpenAI, Anthropic, and OpenRouter (via OpenAI with custom base URL)

## Phase 3: Refactor LLMClient

1. **Update LLMClient**
   - Refactor `llm_client.py` to use the provider-based approach
   - Move provider-specific logic to the adapters
   - Implement provider selection based on model or explicit provider parameter
   - Update chat completion method to handle tool calls through the provider

2. **Update Tool Execution Logic**
   - Keep the existing tool execution logic in `tools.py`
   - Ensure it works with arguments from any provider format
   - Standardize error handling and response formatting

## Phase 4: Update Views and Prompt Engineering

1. **Update Views**
   - Modify `views.py` to support provider selection
   - Update request validation to handle provider-specific parameters
   - Implement streaming and non-streaming response handlers for all providers

2. **Update Prompt Engineering**
   - Remove tool descriptions from system prompts in `prompt_engineering.py`
   - Focus on general instructions about Airflow Wingman's capabilities
   - Create provider-specific prompt variations if needed

## Phase 6: Deployment and Monitoring

1. **Deployment**
   - Build the plugin with `uv build`
   - Copy the wheel file to the astro folder
   - Restart the development environment

2. **Monitoring**
   - Monitor for any issues or errors
   - Collect feedback on provider performance
   - Address any bugs or edge cases

## Implementation Notes

1. **Synchronous Approach**: Ensure all operations remain synchronous as per the project requirements. If async functions from MCP server need to be called, wrap them in synchronous functions.

2. **Backward Compatibility**: Maintain backward compatibility with existing configurations to avoid disrupting current users.

3. **Error Handling**: Implement robust error handling for each provider, as they may have different error formats and requirements.

4. **Reuse Existing Models**: Leverage the existing models from airflow-mcp-server rather than creating new ones.

5. **Testing Throughout**: Implement tests at each phase to ensure functionality is maintained.
