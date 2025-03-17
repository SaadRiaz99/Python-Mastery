import requests
from datetime import datetime

class WeatherAgent:
    def __init__(self):
        self.base_url = 'https://api.open-meteo.com/v1'
        self.geocoding_url = 'https://geocoding-api.open-meteo.com/v1'

    def get_weather(self, city):
        geo = requests.get(f'{self.geocoding_url}/search', params={'name': city, 'count': 1}).json()
        if not geo.get('results'):
            return {'error': f'City {city} not found'}
        lat = geo['results'][0]['latitude']
        lon = geo['results'][0]['longitude']
        weather = requests.get(f'{self.base_url}/forecast', params={
            'latitude': lat, 'longitude': lon,
            'current': 'temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code'
        }).json()
        current = weather['current']
        return {
            'city': geo['results'][0].get('name', city),
            'temperature': current['temperature_2m'],
            'humidity': current['relative_humidity_2m'],
            'wind_speed': current['wind_speed_10m'],
            'timestamp': datetime.now().isoformat()
        }

def main():
    agent = WeatherAgent()
    while True:
        city = input('Enter city (or quit): ')
        if city.lower() == 'quit': break
        weather = agent.get_weather(city)
        if 'error' in weather:
            print(f'Error: {weather[\
