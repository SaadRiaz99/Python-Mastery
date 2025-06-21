# Python Decorators

import time
from functools import wraps

# Simple decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start:.4f} seconds')
        return result
    return wrapper

# Decorator with arguments
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Logging decorator
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with {args}, {kwargs}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result}')
        return result
    return wrapper

# Validate arguments
def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f'Negative value not allowed: {arg}')
        return func(*args, **kwargs)
    return wrapper

# Using decorators
@timer
def slow_function():
    time.sleep(0.1)
    return 'Done!'

@repeat(times=3)
def greet(name):
    print(f'Hello, {name}!')

@log
def add(a, b):
    return a + b

@validate_positive
def square_root(x):
    return x ** 0.5

# Test
print(slow_function())
greet('Saad')
result = add(3, 4)
print(square_root(16))
# print(square_root(-16))  # Would raise ValueError

