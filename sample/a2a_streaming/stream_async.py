import asyncio
from strands.agent.a2a_agent import A2AAgent
from a2a.types import Message, TaskArtifactUpdateEvent

async def main():
    a2a_agent = A2AAgent(endpoint="http://localhost:9000")

    async for event in a2a_agent.stream_async("Explain quantum computing"):
        print("Received event:", event.keys(), end=",")
        print("Event type:", event.get("type"))
        if event.get("type") == "a2a_stream":
            a2a_event = event["event"]
            # Handle Message response
            if isinstance(a2a_event, Message):
                for part in a2a_event.parts:
                    if hasattr(part, "root") and hasattr(part.root, "text"):
                        print(part.root.text, end="", flush=True)
            # Handle streaming tuple (Task, UpdateEvent)
            elif isinstance(a2a_event, tuple) and len(a2a_event) == 2:
                _, update_event = a2a_event
                if isinstance(update_event, TaskArtifactUpdateEvent):
                    for part in (update_event.artifact.parts or []):
                        if hasattr(part, "root") and hasattr(part.root, "text"):
                            print(part.root.text, end="", flush=True)
        elif "result" in event:
            print()

asyncio.run(main())
