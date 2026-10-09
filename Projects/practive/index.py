import asyncio

from agents import Agent, ModelSettings, Runner
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel
from openai import AsyncOpenAI, OpenAIError

from config import (
    AGENT_NAME,
    AGENT_TEMPERATURE,
    OLLAMA_API_KEY,
    OLLAMA_BASE_URL,
    OLLAMA_MODEL,
)


ollama_client = AsyncOpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key=OLLAMA_API_KEY,
)
ollama_model = OpenAIChatCompletionsModel(
    model=OLLAMA_MODEL,
    openai_client=ollama_client,
)

bus_journey_agent = Agent(
    name=AGENT_NAME,
    instructions="""
    You are a friendly assistant that helps people plan bus journeys.

    Ask for the starting point, destination, travel date, and preferred departure
    time when needed. Give practical planning advice and remind travelers to
    check the operator's current schedule, fare, ticket conditions, and bus stop.

    You do not have access to live bus schedules, fares, seat availability, or
    booking systems. Never invent those details or claim to book a ticket. Be
    clear when information needs to be confirmed with the bus operator.
    Keep your answers clear, concise, and focused on the user's journey.
    """,
    model=ollama_model,
    model_settings=ModelSettings(temperature=AGENT_TEMPERATURE),
)


async def main() -> None:
    print(f"{AGENT_NAME} (using Ollama: {OLLAMA_MODEL})")
    print("Tell me about your bus journey. Type 'quit' or 'exit' to stop.")

    conversation_history = []
    try:
        while True:
            user_message = input("\nYou: ").strip()
            if user_message.lower() in {"quit", "exit"}:
                print("Goodbye!")
                break
            if not user_message:
                continue

            try:
                result = await Runner.run(
                    bus_journey_agent,
                    conversation_history
                    + [{"role": "user", "content": user_message}],
                )
            except OpenAIError as error:
                print(
                    "Could not reach Ollama. Check that Ollama is running, "
                    f"the model '{OLLAMA_MODEL}' is installed, and the "
                    f"settings in .env are correct. Details: {error}"
                )
                continue

            conversation_history = result.to_input_list()
            print(f"\nAssistant: {result.final_output}")
    finally:
        await ollama_client.close()


if __name__ == "__main__":
    asyncio.run(main())
