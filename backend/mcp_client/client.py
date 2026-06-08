from langchain_mcp_adapters.client import MultiServerMCPClient
import sys
import os
PYTHON = sys.executable
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATH_SERVER = os.path.join(BASE_DIR, "mcp-servers", "mathserver.py")
print(f"Python: {PYTHON}")
print(f"Math server path: {MATH_SERVER}")
print(f"Server file exists: {os.path.exists(MATH_SERVER)}")
client = MultiServerMCPClient(
        {
        "math": {
                "command": PYTHON,
                "args": [MATH_SERVER],
                "transport": "stdio",
                },
        "weather": {
                # Make sure you start your weather server on port 8000
                "url": "http://localhost:8000/mcp",
                "transport": "http",
                }
        }
    )