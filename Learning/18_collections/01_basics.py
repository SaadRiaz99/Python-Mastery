# Python Collections Module

from collections import Counter, defaultdict, namedtuple, OrderedDict, deque

# Counter
text = 'hello world hello python hello'
word_count = Counter(text.split())
print(f'Word count: {word_count}')
print(f'Most common 2: {word_count.most_common(2)}')

# Counter with list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
num_count = Counter(numbers)
print(f'Number count: {num_count}')

# defaultdict
def_dict = defaultdict(list)
words = ['apple', 'banana', 'avocado', 'blueberry', 'cherry']
for word in words:
    first_letter = word[0]
    def_dict[first_letter].append(word)
print(f'Grouped: {dict(def_dict)}')

# defaultdict with int
counter = defaultdict(int)
for char in 'hello world':
    counter[char] += 1
print(f'Char count: {dict(counter)}')

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f'Point: {p}')
print(f'x: {p.x}, y: {p.y}')

# OrderedDict (Python 3.7+ dict maintains order)
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
print(f'OrderedDict: {od}')

# deque (double-ended queue)
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(f'Deque: {dq}')
dq.pop()
dq.popleft()
print(f'After pops: {dq}')

# deque with maxlen
dq_max = deque(maxlen=3)
dq_max.extend([1, 2, 3])
dq_max.append(4)  # Removes 1
print(f'Maxlen deque: {dq_max}')

