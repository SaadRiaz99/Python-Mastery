# Factory Pattern

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return 'Woof!'

class Cat(Animal):
    def speak(self):
        return 'Meow!'

class Bird(Animal):
    def speak(self):
        return 'Tweet!'

class AnimalFactory:
    @staticmethod
    def create(animal_type):
        animals = {'dog': Dog, 'cat': Cat, 'bird': Bird}
        return animals.get(animal_type.lower())()

# Usage
factory = AnimalFactory()
for animal_type in ['dog', 'cat', 'bird']:
    animal = factory.create(animal_type)
    print(f'{animal_type}: {animal.speak()}')

