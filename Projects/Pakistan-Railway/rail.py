import json
from pathlib import Path

class PakistanRailway:
    def __init__(self):
        self.data_file = Path(__file__).parent / 'pakrail.json'
        self.routes = self._load_data()

    def _load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {'stations': [], 'trains': []}

    def search_trains(self, source, destination):
        return [t for t in self.routes.get('trains', []) if t['source'].lower() == source.lower() and t['destination'].lower() == destination.lower()]

    def display_stations(self):
        for s in self.routes.get('stations', []):
            print(f'{s[\
