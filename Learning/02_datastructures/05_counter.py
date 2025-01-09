# Counter
from collections import Counter

# Count elements
chars = Counter('hello world')
print(f'Chars: {chars}')
print(f'Most common 2: {chars.most_common(2)}')

# Count list items
fruits = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
fruit_count = Counter(fruits)
print(f'Fruits: {fruit_count}')
print(f'Apple count: {fruit_count[\
