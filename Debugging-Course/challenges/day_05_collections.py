"""Day 5: Increase only Ali's score without changing Ahmed's score."""

students = {
    "Ali": {"score": 70},
    "Ahmed": {"score": 80},
}

ali_record = students["Ahmed"]
ali_record["score"] += 5

assert students["Ali"]["score"] == 75
assert students["Ahmed"]["score"] == 80
print("Day 5 passed")
