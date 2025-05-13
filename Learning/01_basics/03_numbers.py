# Python Numbers and Math

# Basic operations
a = 15
b = 4

print(f'Add: {a} + {b} = {a + b}')
print(f'Sub: {a} - {b} = {a - b}')
print(f'Mul: {a} * {b} = {a * b}')
print(f'Div: {a} / {b} = {a / b}')
print(f'Floor: {a} // {b} = {a // b}')
print(f'Mod: {a} % {b} = {a % b}')
print(f'Power: {a} ** {b} = {a ** b}')

# Math functions
import math

print(f'PI: {math.pi}')
print(f'E: {math.e}')
print(f'Sqrt: {math.sqrt(16)}')
print(f'Ceil: {math.ceil(4.3)}')
print(f'Floor: {math.floor(4.7)}')
print(f'Abs: {abs(-10)}')
print(f'Min: {min(5, 3, 8, 1)}')
print(f'Max: {max(5, 3, 8, 1)}')
print(f'Sum: {sum([1, 2, 3, 4, 5])}')

# Random numbers
import random

print(f'Random int: {random.randint(1, 100)}')
print(f'Random float: {random.random()}')
print(f'Random choice: {random.choice([1, 2, 3, 4, 5])}')
print(f'Random sample: {random.sample(range(1, 50), 6)}')

