# Python Functions

# Basic function
def greet(name):
    return f'Hello, {name}!'

print(greet('Saad'))

# Default parameters
def greet_default(name, greeting='Hello'):
    return f'{greeting}, {name}!'

print(greet_default('Saad'))
print(greet_default('Saad', 'Hi'))

# Multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9])
print(f'Min: {minimum}, Max: {maximum}')

# *args and **kwargs
def total(*args):
    return sum(args)

print(f'Total: {total(1, 2, 3, 4, 5)}')

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

show_info(name='Saad', age=25, city='Karachi')

# Lambda functions
square = lambda x: x ** 2
print(f'Square: {square(5)}')

add = lambda x, y: x + y
print(f'Add: {add(3, 4)}')

# Map and filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f'Squared: {squared}')

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f'Evens: {evens}')

# Scope
x = 'global'
def scope_demo():
    x = 'local'
    print(f'Inside: {x}')

scope_demo()
print(f'Outside: {x}')

# Closure
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)
print(f'Double 5: {double(5)}')
print(f'Triple 5: {triple(5)}')

