# Python Magic Methods

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String representation
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Addition
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Subtraction
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Multiplication
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # Length
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

    # Comparison
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return len(self) < len(other)

    # Get item (indexing)
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError('Index out of range')

    # Contains
    def __contains__(self, value):
        return value == self.x or value == self.y

# Usage
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f'v1: {v1}')
print(f'v2: {v2}')
print(f'v1 + v2: {v1 + v2}')
print(f'v1 - v2: {v1 - v2}')
print(f'v1 * 3: {v1 * 3}')
print(f'Length of v1: {len(v1)}')
print(f'v1 == v2: {v1 == v2}')
print(f'v1 < v2: {v1 < v2}')
print(f'v1[0]: {v1[0]}')
print(f'3 in v1: {3 in v1}')

