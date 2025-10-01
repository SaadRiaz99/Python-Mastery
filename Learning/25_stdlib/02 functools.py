# functools

from functools import lru_cache, partial, reduce, wraps

# lru_cache
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f'Fib(10): {fibonacci(10)}')
print(f'Cache info: {fibonacci.cache_info()}')

# partial
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(f'Square: {square(5)}')
print(f'Cube: {cube(5)}')

# reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f'Product: {product}')

# total_ordering
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

s1 = Student('Alice', 90)
s2 = Student('Bob', 85)
print(f'Alice > Bob: {s1 > s2}')

