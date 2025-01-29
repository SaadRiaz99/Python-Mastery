# Advanced Comprehensions

# Nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Transpose
transposed = [[row[i] for row in matrix] for i in range(3)]
print(f'Transposed: {transposed}')

# Flatten with condition
data = [[1, 2, 0], [3, 0, 4], [0, 5, 6]]
non_zero = [x for row in data for x in row if x != 0]
print(f'Non-zero: {non_zero}')

# Dictionary from two lists
keys = ['name', 'age', 'city']
values = ['Saad', 25, 'Karachi']
user = {k: v for k, v in zip(keys, values)}
print(f'User: {user}')

# Group by condition
items = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
small = {k: v for k, v in items if v <= 2}
large = {k: v for k, v in items if v > 2}
print(f'Small: {small}')
print(f'Large: {large}')

# Walrus operator in comprehension
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = [y for x in data if (y := x ** 2) > 20]
print(f'Filtered: {results}')

