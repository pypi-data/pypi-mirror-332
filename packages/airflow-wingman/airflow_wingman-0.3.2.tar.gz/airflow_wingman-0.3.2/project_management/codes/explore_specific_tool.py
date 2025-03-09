#!/usr/bin/env python
"""
Script to explore a specific Airflow tool structure from airflow-mcp-server.
"""

import os
import json
import pprint
import asyncio

from airflow_mcp_server.config import AirflowConfig
from airflow_mcp_server.tools.tool_manager import get_airflow_tools, get_tool


async def explore_specific_tool(tool_name="get_task_instances"):
    # Set up configuration
    base_url = os.environ.get("AIRFLOW_BASE_URL", "http://localhost:8080/api/v1")
    auth_token = os.environ.get("AUTH_TOKEN", "YWRtaW46YWRtaW4=")

    config = AirflowConfig(
        base_url=base_url,
        cookie=None,
        auth_token=auth_token
    )

    # Get all Airflow tools first
    print("Fetching all tools...")
    tools = await get_airflow_tools(config=config, mode="safe")
    
    # Find the specific tool by name
    print(f"Looking for tool: {tool_name}...")
    tool = next((t for t in tools if t.name == tool_name), None)

    if not tool:
        print(f"Tool {tool_name} not found.")
        return

    print(f"\nTool name: {tool.name}")
    print(f"Tool description: {tool.description}")
    
    # Check for input schema
    if hasattr(tool, 'inputSchema'):
        print("\nInput Schema:")
        pprint.pprint(tool.inputSchema)
        
        # Extract parameters from input schema
        if 'properties' in tool.inputSchema:
            print("\nParameters extracted from input schema:")
            for param_name, param_info in tool.inputSchema['properties'].items():
                required = 'required' in tool.inputSchema and param_name in tool.inputSchema['required']
                print(f"  {param_name}:")
                print(f"    Type: {param_info.get('type', 'any')}")
                print(f"    Description: {param_info.get('description', 'No description')}")
                print(f"    Required: {required}")
                print(f"    Default: {param_info.get('default', 'No default')}")
                if 'enum' in param_info:
                    print(f"    Enum values: {param_info['enum']}")
                print()
    else:
        print("\nNo input schema found.")
    
    # Check for other attributes
    print("\nAll attributes:")
    for attr in dir(tool):
        if not attr.startswith('_'):  # Skip private attributes
            try:
                value = getattr(tool, attr)
                if not callable(value):  # Skip methods
                    print(f"{attr}: {value}")
            except Exception as e:
                print(f"{attr}: Error accessing - {str(e)}")


# Run the async function
if __name__ == "__main__":
    # Try a tool that likely has more parameters
    asyncio.run(explore_specific_tool("get_task_instances"))
