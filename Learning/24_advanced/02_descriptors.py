# Descriptors

class Validator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError(f'{self.name} must be int')
        obj.__dict__[self.name] = value

class Person:
    age = Validator()

p = Person()
p.age = 25
print(f'Age: {p.age}')

