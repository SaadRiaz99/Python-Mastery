# Python Dataclasses

from dataclasses import dataclass, field
from typing import List

# Basic dataclass
@dataclass
class Point:
    x: float
    y: float

p1 = Point(3, 4)
p2 = Point(3, 4)
print(f'p1: {p1}')
print(f'p1 == p2: {p1 == p2}')

# Dataclass with defaults
@dataclass
class User:
    name: str
    age: int
    email: str = ''
    is_active: bool = True

user = User('Saad', 25)
print(f'User: {user}')

# Dataclass with field
@dataclass
class Product:
    name: str
    price: float
    tags: List[str] = field(default_factory=list)
    id: int = field(default=0)

product = Product('Laptop', 999.99)
print(f'Product: {product}')

# Frozen dataclass (immutable)
@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int

red = Color(255, 0, 0)
# red.r = 100  # Would raise FrozenInstanceError
print(f'Color: {red}')

# Dataclass with methods
@dataclass
class Rectangle:
    width: float
    height: float

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def scale(self, factor: float) -> 'Rectangle':
        return Rectangle(self.width * factor, self.height * factor)

rect = Rectangle(10, 5)
print(f'Area: {rect.area}')
print(f'Perimeter: {rect.perimeter}')
print(f'Scaled: {rect.scale(2)}')

# Dataclass with post-init
@dataclass
class Circle:
    radius: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = 3.14159 * self.radius ** 2

circle = Circle(5)
print(f'Circle: radius={circle.radius}, area={circle.area:.2f}')

