# Pytest Style Testing

# These functions would be tested with pytest
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]

def factorial(n):
    if n < 0:
        raise ValueError('Negative not allowed')
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Test assertions (would use pytest)
assert add(2, 3) == 5
assert add(-1, 1) == 0
assert multiply(3, 4) == 12
assert divide(10, 2) == 5.0
assert is_palindrome('racecar') == True
assert is_palindrome('hello') == False
assert factorial(5) == 120
assert factorial(0) == 1
print('All tests passed!')

