# Python Context Managers

# Custom context manager with class
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(f'Error occurred: {exc_val}')
        return False  # Don't suppress exceptions

# Using the context manager
with FileManager('test.txt', 'w') as f:
    f.write('Hello, Context Managers!')

print('File closed properly!')

# Context manager with contextlib
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f'Took {end - start:.4f} seconds')

# Using the context manager
with timer():
    import time
    time.sleep(0.1)

# Database connection example
@contextmanager
def database_connection(url):
    print(f'Connecting to {url}')
    connection = {'url': url, 'connected': True}
    try:
        yield connection
    finally:
        connection['connected'] = False
        print('Disconnected')

with database_connection('postgres://localhost/mydb') as conn:
    print(f'Connected: {conn[\
