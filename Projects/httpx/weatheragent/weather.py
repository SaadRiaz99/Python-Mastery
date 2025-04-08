from dataclasses import dataclass
from typing import Optional

@dataclass
class WeatherData:
    city: str = ''
    temperature: float = 0.0
    humidity: float = 0.0
    wind_speed: float = 0.0
    timestamp: str = ''
    error: Optional[str] = None

    @classmethod
    def error(cls, message):
        return cls(error=message)
