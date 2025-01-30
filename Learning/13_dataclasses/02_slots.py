# Dataclass Slots and Frozen

from dataclasses import dataclass, field

# Slots for memory efficiency
@dataclass(slots=True)
class Point:
    x: float
    y: float

p = Point(1, 2)
print(f'Point: {p}')

# Frozen (immutable)
@dataclass(frozen=True, order=True)
class Student:
    sort_index: float = field(init=False, repr=False)
    name: str
    grade: float

    def __post_init__(self):
        self.sort_index = self.grade

s1 = Student('Alice', 95)
s2 = Student('Bob', 85)
print(f'Sorted: {s1 < s2}')

# Dataclass with factory
@dataclass
class Config:
    settings: dict = field(default_factory=dict)
    tags: list = field(default_factory=list)

c1 = Config()
c2 = Config()
print(f'Different factories: {c1.settings is not c2.settings}')

