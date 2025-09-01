# Metaclasses

class Meta(type):
    def __new__(cls, name, bases, dict):
        dict['class_id'] = id(cls)
        return super().__new__(cls, name, bases, dict)

class MyClass(metaclass=Meta):
    pass

print(f'Class ID: {MyClass.class_id}')

