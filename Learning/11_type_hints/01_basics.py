# Python Type Hints

from typing import List, Dict, Tuple, Optional, Union, Callable

# Basic types
def greet(name: str) -> str:
    return f'Hello, {name}!'

def add(a: int, b: int) -> int:
    return a + b

# Collection types
def process_items(items: List[str]) -> List[str]:
    return [item.upper() for item in items]

def get_user(id: int) -> Dict[str, Union[str, int]]:
    return {'id': id, 'name': 'Saad', 'age': 25}

# Optional and Union
def find_user(id: int) -> Optional[str]:
    if id == 1:
        return 'Saad'
    return None

def process(value: Union[int, str]) -> str:
    return str(value)

# Type aliases
Vector = List[float]
Matrix = List[Vector]

def dot_product(v1: Vector, v2: Vector) -> float:
    return sum(a * b for a, b in zip(v1, v2))

# Callable types
def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

def double(x: int) -> int:
    return x * 2

# TypedDict
from typing import TypedDict

class UserDict(TypedDict):
    name: str
    age: int
    email: Optional[str]

def create_user(name: str, age: int) -> UserDict:
    return {'name': name, 'age': age}

# Generic types
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# Using typed stack
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())

# Function annotations
def complex_function(
    required: str,
    optional: int = 0,
    *args: float,
    **kwargs: str
) -> Tuple[str, int]:
    return (required, optional)

print(greet('Saad'))
print(add(5, 3))
print(process_items(['hello', 'world']))
print(find_user(1))
print(find_user(2))

