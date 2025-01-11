# List Comprehension Patterns

# Basic
squares = [x**2 for x in range(10)]
print(f'Squares: {squares}')

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(f'Evens: {evens}')

# With if-else
labels = ['even' if x % 2 == 0 else 'odd' for x in range(6)]
print(f'Labels: {labels}')

# Nested
pairs = [(x, y) for x in range(3) for y in range(3)]
print(f'Pairs: {pairs}')

# Flatten matrix
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat = [num for row in matrix for num in row]
print(f'Flat: {flat}')

# Filter and transform
words = ['hello', 'world', 'python']
upper_lengths = [len(w.upper()) for w in words if len(w) > 4]
print(f'Lengths: {upper_lengths}')

