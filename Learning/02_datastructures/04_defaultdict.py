# defaultdict
from collections import defaultdict

# Group by first letter
words = ['apple', 'banana', 'avocado', 'blueberry', 'cherry']
d = defaultdict(list)
for word in words:
    d[word[0]].append(word)
print(dict(d))

# Count with defaultdict
text = 'hello world hello python'
counter = defaultdict(int)
for word in text.split():
    counter[word] += 1
print(dict(counter))

# Set defaultdict
students = defaultdict(set)
students['math'].add('Alice')
students['math'].add('Bob')
students['science'].add('Alice')
print(dict(students))

