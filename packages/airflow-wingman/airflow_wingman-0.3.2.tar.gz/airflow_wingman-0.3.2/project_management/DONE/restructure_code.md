# Code Restructuring for Multi-Provider LLM Support

This document outlines a plan to restructure the Airflow Wingman codebase to support multiple LLM providers (OpenAI, Anthropic, and OpenRouter) with a focus on proper tool integration.

## Current Architecture Analysis

The current architecture is primarily designed for OpenAI, with the following components:

1. **LLMClient**: A client class that handles API calls to OpenAI
2. **Tools Module**: Contains functions to convert Airflow tools to OpenAI format and execute them
3. **Views**: Flask views that handle HTTP requests and use the LLMClient
4. **Prompt Engineering**: Contains prompts and instructions with tool descriptions embedded

## Key Issues to Address

1. The code currently only supports OpenAI's tool format
2. Tools are embedded in the instructions prompt, which is redundant when using the API's tool parameters
3. No support for Anthropic's different tool format
4. No abstraction layer to handle different provider APIs

## Proposed Architecture

### 1. Provider-Agnostic Tool Representation

Create a unified internal tool representation that can be converted to provider-specific formats:

```python
class AirflowTool:
    def __init__(self, name, description, input_schema):
        self.name = name
        self.description = description
        self.input_schema = input_schema  # JSON Schema object
```

### 2. Provider-Specific Adapters

Create adapters for each provider to handle:
- Tool format conversion
- API request formatting
- Response parsing
- Tool call execution

```python
class BaseLLMProvider:
    def convert_tools(self, airflow_tools):
        """Convert internal tool representation to provider format"""
        raise NotImplementedError
        
    def create_chat_completion(self, messages, model, temperature, max_tokens, stream, tools):
        """Make API request to provider"""
        raise NotImplementedError
        
    def process_tool_calls(self, response, cookie):
        """Process tool calls from response"""
        raise NotImplementedError
```

Implement specific providers:

```python
class OpenAIProvider(BaseLLMProvider):
    def __init__(self, api_key, base_url=None):
        # Support custom base_url for OpenRouter
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        
    def convert_tools(self, airflow_tools):
        # Convert to OpenAI format
        return [
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.input_schema
                }
            }
            for tool in airflow_tools
        ]
        
    # Implement other methods...

class AnthropicProvider(BaseLLMProvider):
    def __init__(self, api_key):
        self.client = Anthropic(api_key=api_key)
        
    def convert_tools(self, airflow_tools):
        # Convert to Anthropic format
        return [
            {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.input_schema
            }
            for tool in airflow_tools
        ]
        
    # Implement other methods...
```

### 3. Factory for Provider Selection

Create a factory to instantiate the appropriate provider:

```python
def create_llm_provider(provider_name, api_key, base_url=None):
    if provider_name == "openai":
        return OpenAIProvider(api_key, base_url)  # Fix: Pass base_url to OpenAIProvider
    elif provider_name == "anthropic":
        return AnthropicProvider(api_key)
    elif provider_name == "openrouter":
        # OpenRouter uses OpenAI's API format with a different base URL
        return OpenAIProvider(api_key, base_url="https://openrouter.ai/api/v1")
    else:
        raise ValueError(f"Unsupported provider: {provider_name}")
```

### 4. Updated LLMClient

Refactor the LLMClient to use the provider-based approach:

```python
class LLMClient:
    def __init__(self, provider_name, api_key, base_url=None):
        self.provider = create_llm_provider(provider_name, api_key, base_url)
        self.airflow_tools = []
        
    def set_airflow_tools(self, tools):
        self.airflow_tools = tools
        
    def chat_completion(self, messages, model, temperature=0.7, max_tokens=None, stream=False):
        # Convert tools to provider-specific format
        provider_tools = self.provider.convert_tools(self.airflow_tools)
        
        # Make API request
        response = self.provider.create_chat_completion(
            messages=messages,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=stream,
            tools=provider_tools
        )
        
        # Process tool calls if present
        if self.provider.has_tool_calls(response):
            # Get cookie from session
            cookie = session.get("airflow_cookie")
            if not cookie:
                return {"error": "No Airflow cookie available"}
                
            # Process tool calls
            tool_results = self.provider.process_tool_calls(response, cookie)
            
            # Create follow-up request with tool results
            final_response = self.provider.create_follow_up_completion(
                messages=messages,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                tool_results=tool_results,
                original_response=response
            )
            
            return {"content": self.provider.get_content(final_response)}
        else:
            return {"content": self.provider.get_content(response)}
```

### 5. Tool Execution

Keep the tool execution logic in the tools.py file but make it provider-agnostic:

```python
def execute_airflow_tool(tool_name, arguments, cookie):
    """Execute an Airflow tool with the given arguments."""
    # This function remains largely unchanged
    # It executes tools based on name and arguments, regardless of provider
```

### 6. Updated Views

Update the views to support provider selection:

```python
def chat_completion(self):
    """Handle chat completion requests."""
    try:
        data = self._validate_chat_request(request.get_json())
        
        # Store cookie if provided
        if data.get("cookie"):
            session["airflow_cookie"] = data["cookie"]
            
        # Get available Airflow tools
        airflow_tools = []
        if session.get("airflow_cookie"):
            try:
                airflow_tools = list_airflow_tools(session["airflow_cookie"])
            except Exception as e:
                print(f"Error fetching Airflow tools: {str(e)}")
                
        # Extract provider from model name or use explicit provider
        provider_name = data.get("provider") or self._get_provider_from_model(data["model"])
        
        # Create client with appropriate provider
        client = LLMClient(provider_name, data["api_key"])
        client.set_airflow_tools(airflow_tools)
        
        # Handle response
        if data["stream"]:
            return self._handle_streaming_response(client, data)
        else:
            return self._handle_regular_response(client, data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
```

### 7. Updated Prompt Engineering

Remove tool descriptions from the system prompt since they'll be provided via the API:

```python
INSTRUCTIONS = {
    "default": """You are Airflow Wingman, a helpful AI assistant integrated into Apache Airflow.
You have deep knowledge of Apache Airflow's architecture, DAGs, operators, and best practices.
The Airflow version being used is >=2.10.

You have access to Airflow API tools that you can use to fetch information and help users understand and manage their Airflow environment.
"""
}
```

## Implementation Steps

1. **Create Tool Representation**:
   - Define a unified internal representation for tools
   - Update the tool listing function to return this representation

2. **Create Provider Adapters**:
   - Implement the base provider interface
   - Create concrete implementations for OpenAI and Anthropic

3. **Update LLMClient**:
   - Refactor to use the provider-based approach
   - Move provider-specific logic to the adapters

4. **Update Views**:
   - Add provider selection logic
   - Update request validation

5. **Update Prompt Engineering**:
   - Remove tool descriptions from prompts
   - Focus on general instructions

6. **Testing**:
   - Test with each provider
   - Verify tool functionality

## Benefits of This Approach

1. **Clean Separation of Concerns**:
   - Provider-specific code is isolated in adapters
   - Core logic remains provider-agnostic

2. **Extensibility**:
   - Easy to add new providers by implementing the adapter interface
   - Common functionality is shared

3. **Improved Maintainability**:
   - Changes to one provider don't affect others
   - Easier to update when provider APIs change

4. **Better User Experience**:
   - Consistent behavior across providers
   - Tools work properly with each provider's format

## Proposed File Structure

Here's the proposed file structure for the restructured codebase:

```
src/airflow_wingman/
│
├── __init__.py                 # Plugin entry point
│
├── llm_client.py               # Main LLM client (provider-agnostic)
│
├── providers/                  # Provider-specific implementations
│   ├── __init__.py             # Provider factory
│   ├── base.py                 # Base provider interface
│   ├── openai_provider.py      # OpenAI implementation (also used for OpenRouter)
│   └── anthropic_provider.py   # Anthropic implementation
│
├── tools/                      # Tool-related functionality
│   ├── __init__.py             # Tool exports
│   ├── models.py               # Tool data models
│   ├── airflow_tools.py        # Airflow tool listing and execution
│   └── conversion.py           # Provider-agnostic tool conversion utilities
│
├── views.py                    # Flask views
├── prompt_engineering.py       # Prompt templates (without tool descriptions)
├── llms_models.py              # LLM model definitions
└── notes.py                    # Interface messages
```

This structure separates concerns clearly:

1. The `providers` directory contains all provider-specific code, making it easy to add new providers.
2. OpenRouter uses the OpenAI provider with a custom base URL rather than having its own implementation.
3. The `tools` directory contains tool-related functionality, including the unified tool representation.
4. The main `llm_client.py` acts as a facade, delegating to the appropriate provider.
5. The views and other components remain largely unchanged, just updated to work with the new architecture.
