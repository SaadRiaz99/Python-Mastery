# Python Tuples and Sets

# === TUPLES ===
# Tuples are immutable
point = (10, 20)
print(f'Point: {point}')
print(f'X: {point[0]}, Y: {point[1]}')

# Tuple unpacking
x, y = point
print(f'Unpacked: x={x}, y={y}')

# Named tuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f'Named: {p.x}, {p.y}')

# Tuple methods
numbers = (1, 2, 2, 3, 3, 3)
print(f'Count of 3: {numbers.count(3)}')
print(f'Index of 2: {numbers.index(2)}')

# === SETS ===
# Sets are unordered, unique elements
fruits = {'apple', 'banana', 'cherry'}
print(f'Fruits: {fruits}')

# Adding elements
fruits.add('orange')
print(f'After add: {fruits}')

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f'Union: {set1 | set2}')
print(f'Intersection: {set1 & set2}')
print(f'Difference: {set1 - set2}')
print(f'Symmetric diff: {set1 ^ set2}')

# Set comprehension
evens = {x for x in range(1, 21) if x % 2 == 0}
print(f'Evens: {evens}')

# Removing duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(numbers))
print(f'Original: {numbers}')
print(f'Unique: {unique}')

