# Flask Basics

# Simulated Flask-like patterns
class FlaskApp:
    def __init__(self):
        self.routes = {}

    def route(self, path, methods=['GET']):
        def decorator(f):
            self.routes[(path, tuple(methods))] = f
            return f
        return decorator

    def handle(self, path, method='GET'):
        handler = self.routes.get((path, (method,)))
        if handler:
            return handler()
        return 'Not Found'

app = FlaskApp()

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST'])
def users():
    return 'Users list'

@app.route('/users/<id>')
def user(id):
    return f'User {id}'

# Test
print(app.handle('/'))
print(app.handle('/users'))
print(app.handle('/users/123'))

