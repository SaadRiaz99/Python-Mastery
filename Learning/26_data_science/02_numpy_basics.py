# NumPy Basics

import numpy as np

# Arrays
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print('1D Array:', arr1d)
print('2D Array:', arr2d)

# Operations
print(f'Sum: {arr1d.sum()}')
print(f'Mean: {arr1d.mean()}')
print(f'Max: {arr1d.max()}')

# Broadcasting
print(f'Doubled: {arr1d * 2}')
print(f'Squared: {arr1d ** 2}')

# Linspace
x = np.linspace(0, 10, 5)
print(f'Linspace: {x}')

# Random
rand_arr = np.random.rand(3, 3)
print(f'Random:\\n{rand_arr}')

