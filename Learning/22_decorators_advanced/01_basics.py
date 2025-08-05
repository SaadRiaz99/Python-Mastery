# Advanced Decorator Patterns

from functools import wraps
import time

# Class-based decorator
class Timer:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f'{self.func.__name__} took {end - start:.4f} seconds')
        return result

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return lambda *args, **kwargs: self(obj, *args, **kwargs)

@Timer
def slow_function():
    time.sleep(0.1)
    return 'Done'

# Decorator with arguments
def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f'Attempt {attempt + 1} failed: {e}')
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.1)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError('Random failure')
    return 'Success!'

# Memoization decorator
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Decorator class
class Validate:
    def __init__(self, func):
        wraps(func)(self)

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return lambda *args, **kwargs: self.__call__(obj, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print(f'Validating call to {self.name}')
        return self.__wrapped__(*args, **kwargs)

# Test
print(slow_function())
print(f'Fibonacci(10): {fibonacci(10)}')

