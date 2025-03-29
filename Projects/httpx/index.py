from weatheragent.agent import WeatherAgent
import asyncio

def main():
    agent = WeatherAgent()
    while True:
        city = input('Enter city (or quit): ')
        if city.lower() == 'quit': break
        weather = asyncio.run(agent.get_weather(city))
        print(weather)

if __name__ == '__main__':
    main()
