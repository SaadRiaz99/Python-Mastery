import httpx
from typing import Any, Dict, Optional

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
WEATHER_CODE_MAP = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


async def geocode_city(city: str) -> Optional[Dict[str, Any]]:
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            GEOCODING_URL,
            params={"name": city, "count": 1, "language": "en", "format": "json"},
        )
        response.raise_for_status()
        data = response.json()
        results = data.get("results") or []
        return results[0] if results else None


async def get_weather(city: str = "Berlin") -> Dict[str, Any]:
    location = await geocode_city(city)
    if not location:
        raise ValueError(f"Could not find location data for '{city}'.")

    latitude = location["latitude"]
    longitude = location["longitude"]
    display_name = location.get("name", city)
    country = location.get("country", "")

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            FORECAST_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current_weather": "true",
                "timezone": "auto",
            },
        )
        response.raise_for_status()
        forecast = response.json()

    current = forecast.get("current_weather")
    if not current:
        raise ValueError(f"No current weather available for '{city}'.")

    weather_description = WEATHER_CODE_MAP.get(current.get("weathercode"), "Unknown weather")
    summary = (
        f"Current weather in {display_name}, {country}: "
        f"{current['temperature']}°C, {weather_description}, "
        f"wind {current['windspeed']} m/s from {current['winddirection']}°.")

    return {
        "location": {
            "name": display_name,
            "country": country,
            "latitude": latitude,
            "longitude": longitude,
        },
        "current_weather": current,
        "summary": summary,
    }

if __name__ == "__main__":
    import asyncio
    import sys

    city = sys.argv[1] if len(sys.argv) > 1 else input("Which city do you want weather for? ").strip()
    if not city:
        print("City name is required to get weather.")
        sys.exit(1)

    weather = asyncio.run(get_weather(city))
    print(weather)
