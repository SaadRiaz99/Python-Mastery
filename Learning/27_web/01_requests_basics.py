# HTTP Requests

import json

# Simulated requests module usage
class MockResponse:
    def __init__(self, data, status=200):
        self._data = data
        self.status_code = status

    def json(self):
        return self._data

    def text(self):
        return json.dumps(self._data)

# GET request simulation
def get(url):
    print(f'GET {url}')
    return MockResponse({'users': [{'id': 1, 'name': 'Alice'}]})

# POST request simulation
def post(url, data):
    print(f'POST {url}')
    return MockResponse({'id': 2, **data}, 201)

# Usage
response = get('https://api.example.com/users')
print(f'Status: {response.status_code}')
print(f'Data: {response.json()}')

response = post('https://api.example.com/users', {'name': 'Bob'})
print(f'Created: {response.json()}')

