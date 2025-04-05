import httpx
from datetime import datetime
from .weather import WeatherData

class WeatherAgent:
    def __init__(self):
        self.base_url = 'https://api.open-meteo.com/v1'
        self.geocoding_url = 'https://geocoding-api.open-meteo.com/v1'

    async def get_weather(self, city):
        async with httpx.AsyncClient() as client:
            geo = await client.get(f'{self.geocoding_url}/search', params={'name': city, 'count': 1})
            geo_data = geo.json()
            if not geo_data.get('results'):
                return WeatherData(error=f'City {city} not found')
            lat = geo_data['results'][0]['latitude']
            lon = geo_data['results'][0]['longitude']
            weather = await client.get(f'{self.base_url}/forecast', params={
                'latitude': lat, 'longitude': lon,
                'current': 'temperature_2m,relative_humidity_2m,wind_speed_10m'
            })
            current = weather.json()['current']
            return WeatherData(
                city=geo_data['results'][0].get('name', city),
                temperature=current['temperature_2m'],
                humidity=current['relative_humidity_2m'],
                wind_speed=current['wind_speed_10m'],
                timestamp=datetime.now().isoformat()
            )
