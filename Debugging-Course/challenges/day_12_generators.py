"""Day 12: Generate 1, 2, 3 without returning early."""

def count_to(limit : int):
    number = 1
    while number <= limit:
        yield number
        number += 1

assert list(count_to(3)) == [1, 2, 3]
print("Day 12 passed")
