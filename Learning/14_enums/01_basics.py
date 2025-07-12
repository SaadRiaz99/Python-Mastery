# Python Enums

from enum import Enum, auto

# Basic enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)

# Auto values
class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

print(Direction.NORTH)

# String enum
classHttpStatus(Enum):
    OK = '200'
    NOT_FOUND = '404'
    SERVER_ERROR = '500'

printHttpStatus.OK)

# Iterating enums
for color in Color:
    print(f'{color.name}: {color.value}')

# Finding by value
status = HttpStatus('200')
print(f'Status: {status.name}')

# Enum comparison
print(f'Is RED: {Color.RED == Color.RED}')
print(f'Is BLUE: {Color.RED == Color.BLUE}')

# Enum in function
def process_color(color: Color):
    match color:
        case Color.RED:
            print('Processing red')
        case Color.GREEN:
            print('Processing green')
        case Color.BLUE:
            print('Processing blue')

process_color(Color.RED)

# Functional API
Animal = Enum('Animal', ['DOG', 'CAT', 'BIRD'])
print(Animal.DOG)

# Enum with methods
classPlanet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS = (4.869e+24, 6.0518e6)
    EARTH = (5.976e+24, 6.37814e6)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    @property
    def surface_gravity(self):
        G = 6.67300E-11
        return G * self.mass / (self.radius ** 2)

print(f'Earth gravity: {Planet.EARTH.surface_gravity:.2f} m/s^2')

