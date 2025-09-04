# itertools Recipes

import itertools

def take(n, iterable):
    return list(itertools.islice(iterable, n))

def flatten(list_of_lists):
    return list(itertools.chain.from_iterable(list_of_lists))

def unique_everseen(iterable, key=None):
    seen = set()
    for element in iterable:
        k = key(element) if key else element
        if k not in seen:
            seen.add(k)
            yield element

def chunked(iterable, n):
    it = iter(iterable)
    while True:
        chunk = list(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk

# Test
print(take(5, range(100)))
print(flatten([[1,2], [3,4], [5,6]]))
print(list(unique_everseen([1,1,2,2,3])))
print(list(chunked(range(10), 3)))

