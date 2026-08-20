from agent import Agent, function_tool, input_guardrail, output_guardrail

from .weather import get_weather


@function_tool
async def weather_tool(city: str):
    """Get current weather for a city."""
    if not city or not city.strip():
        raise ValueError("City name is required to get weather.")
    return await get_weather(city.strip())


weather_Agent = Agent(
    name="Weather Agent",
    instructions="""You are a weather agent that retrieves current weather information for a requested city.
    Use the provided weather_tool to fetch weather details and return the response clearly.
    If the city name is missing or ambiguous, ask the user to clarify before calling the tool.
    """,
    description="An agent that can get the current weather for a city.",
    tools=[weather_tool],
    input_guardrail=input_guardrail,
    output_guardrail=output_guardrail,
)