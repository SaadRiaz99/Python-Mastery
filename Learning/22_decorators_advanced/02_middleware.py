# Middleware Pattern

from functools import wraps
import time

class Middleware:
    def __init__(self):
        self.middlewares = []

    def add(self, func):
        self.middlewares.append(func)
        return func

    def execute(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            context = {'args': args, 'kwargs': kwargs}
            for mw in self.middlewares:
                context = mw(context)
            return func(**context.get('kwargs', {}))
        return wrapper

middleware = Middleware()

@middleware.add
def auth_check(context):
    print('Auth check passed')
    return context

@middleware.add
def rate_limit(context):
    print('Rate limit passed')
    return context

@middleware.execute
def protected_route(user_id):
    return f'Hello user {user_id}'

print(protected_route(user_id=123))

