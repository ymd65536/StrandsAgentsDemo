from strands.agent.a2a_agent import A2AAgent

# Create an A2AAgent pointing to a remote A2A server
a2a_agent = A2AAgent(endpoint="http://localhost:9000")

try:
    # Invoke it just like a regular Agent
    result = a2a_agent("Show me 10 ^ 6")
    print(result.message)
    # {'role': 'assistant', 'content': [{'text': '10^6 = 1,000,000'}]}
except Exception as e:
    print(f"Error: {e}")

