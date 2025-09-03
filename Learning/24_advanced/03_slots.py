# __slots__

class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointNoSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

import sys
p1 = PointSlots(1, 2)
p2 = PointNoSlots(1, 2)

print(f'With slots: {sys.getsizeof(p1)} bytes')
print(f'Without slots: {sys.getsizeof(p2)} bytes')
print(f'Has dict: {hasattr(p1, \
