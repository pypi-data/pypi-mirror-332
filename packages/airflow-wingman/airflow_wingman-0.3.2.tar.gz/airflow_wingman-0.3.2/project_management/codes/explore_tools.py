#!/usr/bin/env python
"""
Script to explore Airflow tools structure from airflow-mcp-server.
"""

import os
import json
import pprint
import asyncio

from airflow_mcp_server.config import AirflowConfig
from airflow_mcp_server.tools.tool_manager import get_airflow_tools, get_tool


async def explore_tools():
    # Set up configuration
    base_url = os.environ.get("AIRFLOW_BASE_URL", "http://localhost:8080/api/v1")
    auth_token = os.environ.get("AUTH_TOKEN", "YWRtaW46YWRtaW4=")

    config = AirflowConfig(
        base_url=base_url,
        cookie=None,
        auth_token=auth_token
    )

    # Get all Airflow tools
    print("Fetching Airflow tools...")
    tools = await get_airflow_tools(config=config, mode="safe")

    print(f"\nFound {len(tools)} tools:")
    for i, tool in enumerate(tools):
        print(f"{i+1}. {tool.name}: {tool.description}")

    # Examine the first tool in detail if available
    if tools:
        print("\nExamining first tool in detail:")
        tool = tools[0]
        
        print(f"Tool name: {tool.name}")
        print(f"Tool description: {tool.description}")
        
        # Check for parameters
        if hasattr(tool, 'parameters'):
            print("\nParameters:")
            pprint.pprint(tool.parameters)
        else:
            print("\nNo parameters found.")
        
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
        
        # Try to convert to dict if possible
        print("\nTrying to convert to dict:")
        try:
            if hasattr(tool, 'to_dict'):
                tool_dict = tool.to_dict()
                print(json.dumps(tool_dict, indent=2))
            else:
                print("No to_dict method found.")
        except Exception as e:
            print(f"Error converting to dict: {str(e)}")
    else:
        print("No tools found to examine.")


# Run the async function
if __name__ == "__main__":
    asyncio.run(explore_tools())
