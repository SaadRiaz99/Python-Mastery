"""Day 10: Read optional JSON fields safely."""

import json

payload = '{"name": "Saad", "skills": ["Python", "FastAPI"]}'
profile = json.loads(payload)

city = profile["city"]
assert city == "Unknown"
assert len(profile["skills"]) == 2
print("Day 10 passed")
