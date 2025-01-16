# Advanced JSON

import json

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        return super().default(obj)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Saad', 25)
json_str = json.dumps(user, cls=CustomEncoder, indent=2)
print(f'JSON: {json_str}')

# Parse back
data = json.loads(json_str)
print(f'Parsed: {data}')

# Working with files
data = {'users': [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]}
with open('users.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('users.json', 'r') as f:
    loaded = json.load(f)
    print(f'Loaded: {loaded}')

