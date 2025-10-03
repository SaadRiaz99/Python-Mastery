# Advanced Typing

from typing import TypeVar, Generic, Protocol, runtime_checkable
from typing import TypedDict, Literal, Final, Annotated

T = TypeVar('T')

# Generic container
class Stack(Generic[T]):
    def __init__(self):
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

# Protocol
@runtime_checkable
class Comparable(Protocol):
    def __lt__(self, other) -> bool: ...

# TypedDict
class UserDict(TypedDict):
    name: str
    age: int
    email: str | None

# Literal
def set_mode(mode: Literal['read', 'write', 'append']) -> None:
    print(f'Mode: {mode}')

# Final
MAX_SIZE: Final = 100

# Annotated
from typing import Annotated
PositiveInt = Annotated[int, 'must be positive']

def add(a: PositiveInt, b: PositiveInt) -> PositiveInt:
    return a + b

# Usage
stack: Stack[int] = Stack()
stack.push(1)
stack.push(2)
print(f'Popped: {stack.pop()}')
set_mode('read')
print(f'Max: {MAX_SIZE}')

