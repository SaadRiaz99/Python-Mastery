"""Day 11: A decorator must return the wrapped function's value."""

from functools import wraps

def log_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")
        function(*args, **kwargs)
    return wrapper

@log_call
def multiply(first, second):
    return first * second

assert multiply(4, 5) == 20
print("Day 11 passed")
