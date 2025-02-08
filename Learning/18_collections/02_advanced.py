# Advanced Collections

from collections import ChainMap, UserDict, UserList

# ChainMap - combine dicts
defaults = {'color': 'red', 'user': 'guest'}
environment = {'user': 'admin'}
config = ChainMap(environment, defaults)

print(f'User: {config[\
