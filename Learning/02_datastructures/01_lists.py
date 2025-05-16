# Python Lists

# Creating lists
fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'hello', 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]

print(f'Fruits: {fruits}')
print(f'Numbers: {numbers}')
print(f'Mixed: {mixed}')
print(f'Nested: {nested}')

# Accessing elements
print(f'First fruit: {fruits[0]}')
print(f'Last fruit: {fruits[-1]}')
print(f'Slice: {fruits[0:2]}')

# Modifying lists
fruits.append('orange')
print(f'After append: {fruits}')

fruits.insert(1, 'mango')
print(f'After insert: {fruits}')

fruits.remove('banana')
print(f'After remove: {fruits}')

popped = fruits.pop()
print(f'Popped: {popped}')
print(f'After pop: {fruits}')

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f'Original: {numbers}')
print(f'Sorted: {sorted(numbers)}')
print(f'Count of 1: {numbers.count(1)}')
print(f'Index of 5: {numbers.index(5)}')
print(f'Length: {len(numbers)}')

# List comprehension
squares = [x**2 for x in range(1, 11)]
print(f'Squares: {squares}')

evens = [x for x in range(1, 21) if x % 2 == 0]
print(f'Evens: {evens}')

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f'Combined: {combined}')
print(f'Repeated: {[0] * 5}')

