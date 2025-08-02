# Singleton Design Pattern

# Method 1: Using __new__
class Singleton1:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Method 2: Using decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Singleton2:
    def __init__(self):
        self.value = 42

# Method 3: Using metaclass
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton3(metaclass=SingletonMeta):
    def __init__(self):
        self.value = 100

# Testing
s1 = Singleton1()
s2 = Singleton1()
print(f'Singleton1 same instance: {s1 is s2}')

s3 = Singleton2()
s4 = Singleton2()
print(f'Singleton2 same instance: {s3 is s4}')

s5 = Singleton3()
s6 = Singleton3()
print(f'Singleton3 same instance: {s5 is s6}')

# Practical example - Database connection
class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = 'Connected to database'
        return self.connection

db1 = Database()
db2 = Database()
print(f'Database same instance: {db1 is db2}')
print(f'Connection: {db1.connect()}')

