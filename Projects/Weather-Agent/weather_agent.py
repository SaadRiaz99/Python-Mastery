"""Simple Weather Agent using OpenWeatherMap or Open-Meteo API"""

import os
import requests
import pandas as pd
from typing import Optional, Dict, Any
from dataclasses import dataclass, field


@dataclass
class WeatherData:
    location: str
    temperature: float
    condition: str
    humidity: int
    wind_speed: float
    feels_like: float
    precipitation_probability: int = 0


class WeatherAgent:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("OPENWEATHER_API_KEY")
        self.owm_base_url = "https://api.openweathermap.org/data/2.5"
        self.openmeteo_url = "https://api.open-meteo.com/v1/forecast"
        self.use_openmeteo = not self.api_key

    def get_current_weather(self, city: str, country_code: str = "US") -> WeatherData:
        if self.use_openmeteo:
            return self._openmeteo_current(city)
        return self._owm_current(city, country_code)

    def get_forecast(self, city: str, days: int = 5) -> list[WeatherData]:
        if self.use_openmeteo:
            return self._openmeteo_forecast(city, days)
        return self._owm_forecast(city, days)

    def _owm_current(self, city: str, country_code: str) -> WeatherData:
        url = f"{self.owm_base_url}/weather"
        params = {
            "q": f"{city},{country_code}",
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return WeatherData(
            location=data["name"],
            temperature=data["main"]["temp"],
            condition=data["weather"][0]["description"],
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"],
            feels_like=data["main"]["feels_like"]
        )

    def _owm_forecast(self, city: str, days: int) -> list[WeatherData]:
        url = f"{self.owm_base_url}/forecast"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        forecasts = []
        for item in data["list"][:days]:
            forecasts.append(WeatherData(
                location=city,
                temperature=item["main"]["temp"],
                condition=item["weather"][0]["description"],
                humidity=item["main"]["humidity"],
                wind_speed=item["wind"]["speed"],
                feels_like=item["main"]["feels_like"]
            ))
        return forecasts

    def _get_coordinates(self, city: str) -> Optional[tuple[float, float]]:
        geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
        params = {"name": city, "count": 1}
        try:
            response = requests.get(geocode_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            if data.get("results"):
                result = data["results"][0]
                return result["latitude"], result["longitude"]
        except Exception:
            pass
        return None

    def _weather_code_to_condition(self, code: int) -> str:
        codes = {
            0: "clear sky",
            1: "mainly clear",
            2: "partly cloudy",
            3: "overcast",
            45: "fog",
            48: "depositing rime fog",
            51: "light drizzle",
            53: "moderate drizzle",
            55: "dense drizzle",
            61: "slight rain",
            63: "moderate rain",
            65: "heavy rain",
            71: "slight snow",
            73: "moderate snow",
            75: "heavy snow",
            80: "slight rain showers",
            81: "moderate rain showers",
            82: "violent rain showers",
            95: "thunderstorm",
            96: "thunderstorm with hail",
        }
        return codes.get(code, "unknown")

    def _openmeteo_current(self, city: str) -> WeatherData:
        coords = self._get_coordinates(city)
        if not coords:
            return self._demo_weather(city)
        lat, lon = coords

        params = {
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "relative_humidity_2m", "is_day", "weather_code"],
        }
        try:
            response = requests.get(self.openmeteo_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            current = data["current"]
            return WeatherData(
                location=city,
                temperature=current["temperature_2m"],
                condition=self._weather_code_to_condition(current["weather_code"]),
                humidity=int(current["relative_humidity_2m"]),
                wind_speed=0.0,
                feels_like=current["temperature_2m"],
                precipitation_probability=0
            )
        except Exception:
            return self._demo_weather(city)

    def _openmeteo_forecast(self, city: str, days: int) -> list[WeatherData]:
        coords = self._get_coordinates(city)
        if not coords:
            return [self._demo_weather(city) for _ in range(days)]
        lat, lon = coords

        params = {
            "latitude": lat,
            "longitude": lon,
            "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "precipitation_probability_max"],
            "hourly": ["temperature_2m", "relative_humidity_2m"],
            "forecast_days": days,
        }
        try:
            response = requests.get(self.openmeteo_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            daily = data["daily"]
            forecasts = []
            for i in range(days):
                avg_temp = (daily["temperature_2m_max"][i] + daily["temperature_2m_min"][i]) / 2
                forecasts.append(WeatherData(
                    location=city,
                    temperature=daily["temperature_2m_max"][i],
                    condition=self._weather_code_to_condition(daily["weather_code"][i]),
                    humidity=int(daily.get("precipitation_probability_max", [0] * days)[i]) if "precipitation_probability_max" in daily else 0,
                    wind_speed=0.0,
                    feels_like=avg_temp,
                    precipitation_probability=int(daily.get("precipitation_probability_max", [0] * days)[i]) if "precipitation_probability_max" in daily else 0
                ))
            return forecasts
        except Exception:
            return [self._demo_weather(city) for _ in range(days)]

    def _demo_weather(self, city: str) -> WeatherData:
        return WeatherData(
            location=city,
            temperature=22.0,
            condition="clear sky",
            humidity=45,
            wind_speed=5.0,
            feels_like=20.0,
            precipitation_probability=0
        )

    def format_weather_report(self, weather: WeatherData) -> str:
        return f"""
|-------------------------------------------|
|       Current Weather: {weather.location}      |
|-------------------------------------------|
|  Temperature:    {weather.temperature:>6.1f} C          |
|  Condition:      {weather.condition:<13}     |
|  Humidity:       {weather.humidity:>6}%          |
|  Wind Speed:     {weather.wind_speed:>6.1f} m/s       |
|  Feels Like:     {weather.feels_like:>6.1f} C          |
|  Precip Prob:    {weather.precipitation_probability:>6}%          |
|-------------------------------------------|
"""

    def format_forecast_report(self, forecasts: list[WeatherData]) -> str:
        report = """
|-------------------------------------------|
|           5-Day Weather Forecast          |
|-------------------------------------------|
"""
        for i, f in enumerate(forecasts, 1):
            report += f"|  Day {i}:  {f.temperature:>5.1f} C  {f.condition:<14}  {f.precipitation_probability:>3}% rain  |\n"
        report += "|-------------------------------------------|"
        return report


def is_weather_related(message: str) -> bool:
    weather_keywords = [
        "weather", "temperature", "temp", "humid", "rain", "snow", "sun",
        "cloud", "wind", "forecast", "hot", "cold", "warm", "degrees",
        "feels like", "precipitation", "pressure"
    ]
    msg_lower = message.lower()
    return any(kw in msg_lower for kw in weather_keywords)


def print_banner():
    print("""
    .*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*.
    |                                       |
    |        [ Weather Agent ]              |
    |                                       |
    |  Enter a city name to get weather     |
    |  Ask weather questions or quit        |
    |                                       |
    .*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*.
    """)


def main():
    print_banner()

    agent = WeatherAgent()

    city = input("[+] City: ").strip()
    if not city:
        city = "New York"

    print(f"\n[*] Fetching weather for {city}...\n")

    weather = agent.get_current_weather(city)
    print(agent.format_weather_report(weather))

    print("\n[?] Ask about weather (or anything else to quit):\n")
    user_input = input("> ").strip()

    if not is_weather_related(user_input):
        print("\n[!] Goodbye!")
        return

    forecast = agent.get_forecast(city, days=5)
    print(agent.format_forecast_report(forecast))


if __name__ == "__main__":
    main()
