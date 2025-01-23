# Database Context Manager

from contextlib import contextmanager

class MockDB:
    def __init__(self):
        self.connected = False
        self.data = {}

    def connect(self):
        self.connected = True
        print('Connected to database')

    def disconnect(self):
        self.connected = False
        print('Disconnected from database')

    def execute(self, query):
        if not self.connected:
            raise RuntimeError('Not connected')
        print(f'Executing: {query}')
        return []

@contextmanager
def database():
    db = MockDB()
    db.connect()
    try:
        yield db
    finally:
        db.disconnect()

with database() as db:
    db.execute('SELECT * FROM users')
    db.execute('INSERT INTO users VALUES (1, \
