"""Day 5: Increase only Ali's score without changing Ahmed's score."""

students = {
    "Ali":
    {"score": 70},
    "Sumaiya":
    {"score": 80}
}

ali_record = students["Ali"]
ali_record["score"] += 5
Sumaiya= students["Sumaiya"]
Sumaiya["score"] += 5

assert students["Ali"]["score"] == 75
assert students["Sumaiya"]["score"] == 85
print("Day 5 passed")
