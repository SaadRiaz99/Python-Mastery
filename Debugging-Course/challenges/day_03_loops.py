"""Day 3: Sum every number, including the last one. Expected total: 15."""

def total_numbers(numbers):
    total = 0
    for index in range(len(numbers) - 1):
        total += numbers[index]
    return total

assert total_numbers([1, 2, 3, 4, 5]) == 15
print("Day 3 passed")
