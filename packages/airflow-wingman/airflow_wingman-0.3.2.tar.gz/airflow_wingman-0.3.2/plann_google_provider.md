# Google Provider Implementation Plan for Airflow Wingman

## Overview
This document outlines the plan for implementing a Google Gemini provider for the Airflow Wingman plugin. This provider will allow users to use Google's Gemini models (like Gemini 2.0 Flash) with function calling capabilities similar to the existing OpenAI provider.

## Requirement
The Airflow Wingman plugin must remain entirely synchronous. Any async operations need to be wrapped in synchronous functions.

## Components Needed

### 1. GoogleProvider Class
A new class that implements the `BaseLLMProvider` interface, similar to the existing `OpenAIProvider` class.

### 2. Tool Conversion
A mechanism to convert Airflow tools to the format expected by Google's Gemini API.

### 3. Message Format Conversion
A way to convert messages between Airflow's format and Google Gemini's format.

## Key Differences from OpenAI

### API Client
- Uses `google-genai` instead of `openai` Python library
- Different initialization pattern (no base_url, just API key)

### Function/Tool Calling
- Google uses `function_declarations` within a tools array
- Function call responses appear in `part.function_call` attribute
- Arguments are accessed through `function_call.args` instead of `function_call.arguments`

### Configuration
- Uses `GenerateContentConfig` object for configuration
- System messages handled through `system_instruction` parameter
- Tools are configured differently than in OpenAI

### Response Structure
- Responses structured in `candidates[0].content.parts`
- Tool calls accessed through `part.function_call`
- Different attribute names for extracting content

## Implementation Details

### Client Initialization
- Create a Google Gemini client using the provided API key

### Tool Conversion
- Convert Airflow tools to Google Gemini's expected format
- Map Airflow function definitions to Google's function_declarations format

### Creating Chat Completions
- Handle message conversion
- Set up proper configuration with tools
- Handle streaming vs. non-streaming requests

### Processing Tool Calls
- Extract tool calls from responses
- Format tool results in Google's expected format
- Create follow-up completions with tool results

### Handling Responses
- Extract content from responses
- Handle streaming responses properly
- Maintain compatibility with Airflow Wingman's expected formats

## Implementation Workflow

1. Create the basic GoogleProvider class structure
2. Implement tool conversion functionality
3. Implement message format conversion
4. Implement chat completion functionality
5. Implement tool call extraction and processing
6. Implement follow-up completion with tool results
7. Handle streaming responses
8. Test with Airflow Wingman

## Notes

- All operations must remain synchronous for compatibility with Airflow Wingman
- Error handling should be robust and similar to the OpenAI provider
- Logging should be consistent with the current approach
