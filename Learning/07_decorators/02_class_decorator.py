# Class Decorators

def add_repr(cls):
    def __repr__(self):
        attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
        return f'{cls.__name__}({attrs})'
    cls.__repr__ = __repr__
    return cls

@add_repr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p)

# Timer class decorator
import time

def timer_class(cls):
    original_init = cls.__init__
    def new_init(self, *args, **kwargs):
        start = time.time()
        original_init(self, *args, **kwargs)
        print(f'{cls.__name__} initialized in {time.time()-start:.4f}s')
    cls.__init__ = new_init
    return cls

@timer_class
class SlowClass:
    def __init__(self):
        time.sleep(0.1)

obj = SlowClass()

