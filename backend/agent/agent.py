from langchain.agents import create_agent
from dotenv import load_dotenv


import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from mcp_client.client import client
from langchain.chat_models import init_chat_model
import asyncio

load_dotenv()
async def main():
        try:
            tools = await client.get_tools()

            model = init_chat_model(
                model="gemini-3.1-flash-lite", 
                model_provider="google-genai",
                temperature=0.4,
                max_tokens=2500
            )

            agent = create_agent(
                model=model,    tools=tools)
            
            result = await agent.ainvoke({
                "messages": [{"role": "user", "content": "What is 2 + 2?"}]
            })
            print(f"Math Response {result["messages"][-1].content}")

            result = await agent.ainvoke({
                "messages": [{"role": "user", "content": "What is the weather in california?"}]
            })
            print(f"Weather Response: {result["messages"][-1].content}")
        except Exception as e:
             print("An Error occuered during the execution")
             print(e)


if __name__ == "__main__":
    asyncio.run(main())


