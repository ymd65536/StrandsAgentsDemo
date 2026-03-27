import asyncio
from strands.agent.a2a_agent import A2AAgent

async def main():
    a2a_agent = A2AAgent(endpoint="http://localhost:9000")
    result = await a2a_agent.invoke_async("Calculate the square root of 144")
    if 'content'in result.message:
        contents = result.message['content']
        for content in contents:
            print(content['text'])

asyncio.run(main())
