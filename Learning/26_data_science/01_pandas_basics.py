# Pandas Basics

import pandas as pd

# Series
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print('Series:')
print(s)

# DataFrame from dict
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print('\nDataFrame:')
print(df)

# Basic operations
print(f'\nMean age: {df[\
