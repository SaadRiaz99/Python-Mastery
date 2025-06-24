# Python Generators

# Generator function
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Using generator
print('Counting:')
for num in count_up_to(5):
    print(num, end=' ')
print()

# Generator expression
squares = (x**2 for x in range(1, 6))
print(f'Squares: {list(squares)}')

# Infinite generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print('\\nFirst 10 Fibonacci:')
fib = fibonacci()
for _ in range(10):
    print(next(fib), end=' ')
print()

# Generator pipeline
def read_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

def filter_comments(lines):
    for line in lines:
        if not line.startswith('#'):
            yield line

def parse_csv(lines):
    for line in lines:
        yield line.split(',')

# File processing with generators
def process_large_file(filename):
    '''Memory efficient file processing'''
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

# Send values to generator
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

# Using send
acc = accumulator()
next(acc)  # Prime the generator
print(f'Total after 5: {acc.send(5)}')
print(f'Total after 3: {acc.send(3)}')
print(f'Total after 10: {acc.send(10)}')

# Generator utilities
def take(n, iterable):
    for i, item in enumerate(iterable):
        if i >= n:
            break
        yield item

def first(iterable):
    return next(iter(iterable), None)

def chunk(iterable, size):
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

# Test utilities
numbers = range(1, 100)
print(f'First 5: {list(take(5, numbers))}')
print(f'First even: {first(x for x in range(100) if x % 2 == 0)}')
print(f'Chunks: {list(chunk(range(10), 3))}')

