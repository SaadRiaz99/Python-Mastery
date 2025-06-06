# Python Inheritance

# Base class
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f'{self.name} says {self.sound}'

    def __str__(self):
        return f'{self.name} ({self.__class__.__name__})'

# Derived classes
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, 'Woof!')
        self.breed = breed

    def fetch(self, item):
        return f'{self.name} fetches the {item}'

class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, 'Meow!')
        self.indoor = indoor

    def purr(self):
        return f'{self.name} purrs...'

# Polymorphism
animals = [
    Dog('Buddy', 'Golden'),
    Cat('Whiskers'),
    Dog('Max', 'Shepherd'),
    Cat('Luna', indoor=False),
]

for animal in animals:
    print(animal.speak())
    print(animal)

# Duck typing
class Duck:
    def quack(self):
        return 'Quack!'

class Person:
    def quack(self):
        return 'I am quacking like a duck!'

def make_it_quack(duck):
    print(duck.quack())

make_it_quack(Duck())
make_it_quack(Person())

