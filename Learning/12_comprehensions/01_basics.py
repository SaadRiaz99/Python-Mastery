# Python Comprehensions

# List comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic
squares = [x**2 for x in numbers]
print(f'Squares: {squares}')

# With condition
evens = [x for x in numbers if x % 2 == 0]
print(f'Evens: {evens}')

# With transformation
processed = [x * 2 + 1 for x in numbers if x > 5]
print(f'Processed: {processed}')

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(f'Flat: {flat}')

# Dictionary comprehension
names = ['Saad', 'Ali', 'Ahmed']
scores = [85, 92, 78]

name_scores = {name: score for name, score in zip(names, scores)}
print(f'Name scores: {name_scores}')

# With condition
passed = {name: score for name, score in name_scores.items() if score >= 80}
print(f'Passed: {passed}')

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
print(f'Combined: {combined}')

# Set comprehension
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x**2 for x in numbers}
print(f'Unique squares: {unique_squares}')

# Generator expression (memory efficient)
sum_of_squares = sum(x**2 for x in range(1000))
print(f'Sum of squares: {sum_of_squares}')

# Nested comprehension
transposed = [[row[i] for row in matrix] for i in range(3)]
print(f'Transposed: {transposed}')

# Complex example
text = 'Hello World'
word_lengths = {word: len(word) for word in text.split()}
print(f'Word lengths: {word_lengths}')

