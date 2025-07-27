# Python Itertools

import itertools

# Infinite iterators
counter = itertools.count(start=1, step=2)
print('Count:', [next(counter) for _ in range(5)])

cycler = itertools.cycle(['A', 'B', 'C'])
print('Cycle:', [next(cycler) for _ in range(7)])

repeater = itertools.repeat('Hello', 3)
print('Repeat:', list(repeater))

# Terminating iterators
print('Chain:', list(itertools.chain([1, 2], [3, 4], [5, 6])))

print('Compress:', list(itertools.compress('ABCDEF', [1, 0, 1, 0, 1, 0])))

print('Dropwhile:', list(itertools.dropwhile(lambda x: x < 5, [1, 3, 6, 2, 1])))

print('Takewhile:', list(itertools.takewhile(lambda x: x < 5, [1, 3, 6, 2, 1])))

print('Filterfalse:', list(itertools.filterfalse(lambda x: x % 2, range(10))))

# Combinatoric iterators
print('Product:', list(itertools.product('AB', '12')))

print('Permutations:', list(itertools.permutations('ABC', 2)))

print('Combinations:', list(itertools.combinations('ABC', 2)))

print('Combinations with replacement:', list(itertools.combinations_with_replacement('ABC', 2)))

# Groupby
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4), ('A', 5)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(f'{key}: {list(group)}')

# Accumulate
import operator
numbers = [1, 2, 3, 4, 5]
print('Accumulate (sum):', list(itertools.accumulate(numbers)))
print('Accumulate (mul):', list(itertools.accumulate(numbers, operator.mul)))

# Starmap
pairs = [(2, 3), (4, 5), (6, 7)]
print('Starmap:', list(itertools.starmap(operator.mul, pairs)))

