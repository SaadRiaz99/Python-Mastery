# Bus Journey Assistant

A command-line bus journey planning assistant powered by a local Ollama model
through Ollama's OpenAI-compatible Chat Completions API. It can help organize
journey details and offer general travel-planning advice; it does not have live
timetable, fare, availability, or booking access.

## Setup

1. Install [Ollama](https://ollama.com/download) and start it.
2. From this project folder, download the configured model:

   ```powershell
   ollama pull llama3.2
   ```

3. Create and activate a virtual environment, then install dependencies:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

4. Check `.env` and adjust `OLLAMA_BASE_URL` or `OLLAMA_MODEL` if needed.
   Local Ollama uses `http://localhost:11434/v1` by default.
5. Start the assistant:

   ```powershell
   python index.py
   ```

Type `quit` or `exit` to end the conversation. The assistant keeps earlier
messages in the current session so you can refine a journey plan.
