"""Day 10: Read optional JSON fields safely."""

import json

payload = '{"name": "Saad", "city" : "Jhang" , "skills": ["Python", "FastAPI"]}'
profile = json.loads(payload)

city = profile["city"]
assert city == "Jhang"
assert len(profile["skills"]) == 2
print("Day 10 passed")
