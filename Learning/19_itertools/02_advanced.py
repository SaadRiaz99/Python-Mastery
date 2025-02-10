# Advanced Itertools

import itertools
import operator

# Combinations with groupby
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4), ('C', 5)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    items = list(group)
    print(f'{key}: {items}')

# Chain from iterables
nested = [[1, 2], [3, 4], [5, 6]]
flat = list(itertools.chain.from_iterable(nested))
print(f'Flat: {flat}')

# Product (Cartesian product)
suits = ['H', 'D', 'C', 'S']
ranks = ['A', '2', '3', '4', '5']
deck = list(itertools.product(suits, ranks))
print(f'Deck size: {len(deck)}')

# Combinations with replacement
s = list(itertools.combinations_with_replacement('AB', 3))
print(f'Comb with replacement: {s}')

# Starmap
pairs = [(2, 3), (4, 5), (6, 7)]
squared = list(itertools.starmap(operator.pow, pairs))
print(f'Squared: {squared}')

# Tee - create independent iterators
iter1, iter2 = itertools.tee(range(5))
print(f'Iterator 1: {list(iter1)}')
print(f'Iterator 2: {list(iter2)}')

