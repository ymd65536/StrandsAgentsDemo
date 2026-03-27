from strands.agent.a2a_agent import A2AAgent

# Create an A2AAgent pointing to a remote A2A server
a2a_agent = A2AAgent(endpoint="http://localhost:9000")

try:
    # Invoke it just like a regular Agent
    result = a2a_agent("How is the weather today?", stream=True)
    # print(result.message)
    # {'role': 'assistant', 'content': [{'text': '10^6 = 1,000,000'}]}
    if result.message.get("content"):
        contents = result.message["content"]
        for content in contents:
            if content.get("text"):
                print(content["text"])
except Exception as e:
    print(f"Error: {e.message}")

