from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain.agents.middleware import PIIMiddleware
from dotenv import load_dotenv
load_dotenv()
import os

# Nemotron 3 Super — efficient reasoning and agentic tasks
call_llm = ChatNVIDIA(model="nvidia/nemotron-3-super-120b-a12b",
                api_key=os.getenv("LLMAPI")
                )




