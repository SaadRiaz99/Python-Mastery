# Python Classes and Objects

# Basic class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    def bark(self):
        return f'{self.name} says Woof!'

    def learn_trick(self, trick):
        self.tricks.append(trick)
        return f'{self.name} learned {trick}!'

    def show_tricks(self):
        return f'{self.name} knows: {', '.join(self.tricks)}'

# Creating objects
dog1 = Dog('Buddy', 'Golden Retriever')
dog2 = Dog('Max', 'German Shepherd')

print(dog1.bark())
print(dog2.bark())

print(dog1.learn_trick('sit'))
print(dog1.learn_trick('roll over'))
print(dog1.show_tricks())

# Class with properties
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

circle = Circle(5)
print(f'Radius: {circle.radius}')
print(f'Area: {circle.area:.2f}')
print(f'Circumference: {circle.circumference:.2f}')

circle.radius = 10
print(f'New Area: {circle.area:.2f}')

