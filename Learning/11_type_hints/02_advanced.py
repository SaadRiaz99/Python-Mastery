# Advanced Type Hints

from typing import TypeVar, Generic, Protocol, runtime_checkable

T = TypeVar('T')

# Generic class
class Stack(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T):
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# Protocol (structural subtyping)
@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str:
        return 'Drawing circle'

class Square:
    def draw(self) -> str:
        return 'Drawing square'

def draw_shape(shape: Drawable):
    print(shape.draw())

# Type checking
circle = Circle()
print(isinstance(circle, Drawable))
draw_shape(circle)
draw_shape(Square())

# Literal types
from typing import Literal

def set_mode(mode: Literal['read', 'write', 'append']):
    print(f'Mode: {mode}')

set_mode('read')

