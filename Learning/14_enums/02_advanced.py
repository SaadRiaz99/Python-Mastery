# Advanced Enums

from enum import Enum, auto

# String enum with methods
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

    @classmethod
    def from_hex(cls, hex_code):
        colors = {'#ff0000': cls.RED, '#00ff00': cls.GREEN, '#0000ff': cls.BLUE}
        return colors.get(hex_code.lower())

    def complementary(self):
        complements = {self.RED: self.GREEN, self.GREEN: self.RED, self.BLUE: self.RED}
        return complements[self]

print(Color.RED.complementary())

# Flag enum
from enum import Flag

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

    @classmethod
    def from_string(cls, perm_str):
        perms = perm_str.split('|')
        result = cls(0)
        for p in perms:
            result |= cls[p.upper()]
        return result

user_perm = Permission.READ | Permission.WRITE
print(f'Has read: {Permission.READ in user_perm}')
print(f'Has execute: {Permission.EXECUTE in user_perm}')

