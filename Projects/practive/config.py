import os

from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "ollama")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

AGENT_NAME = "Bus Journey Assistant"
AGENT_TEMPERATURE = float(os.getenv("AGENT_TEMPERATURE", "0.2"))
