import logging
from strands import Agent
from strands.models import BedrockModel
from strands_tools.calculator import calculator
from strands.multiagent.a2a import A2AServer

logging.basicConfig(level=logging.INFO)

bedrcok_model = BedrockModel(
    model_id="anthropic.claude-3-5-sonnet-20240620-v1:0"
)

# Create a Strands agent
strands_agent =  Agent(
    model=bedrcok_model,
    name="Calculator Agent",
    description="A calculator agent that can perform basic arithmetic operations.",
    tools=[calculator],
    callback_handler=None
)

# Create A2A server (streaming enabled by default)
a2a_server = A2AServer(agent=strands_agent)

# Start the server
a2a_server.serve()
