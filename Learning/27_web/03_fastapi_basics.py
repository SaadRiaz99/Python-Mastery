class FastAPIApp:
    def __init__(self):
        self.routes = []

    def get(self, path):
        def decorator(f):
            self.routes.append(('GET', path, f))
            return f
        return decorator

    def post(self, path):
        def decorator(f):
            self.routes.append(('POST', path, f))
            return f
        return decorator

app = FastAPIApp()

@app.get('/')
def root():
    return {'message': 'Hello World'}

@app.get('/users/{user_id}')
def get_user(user_id: int):
    return {'user_id': user_id, 'name': 'Saad'}

@app.post('/users')
def create_user(name: str):
    return {'id': 1, 'name': name}

for method, path, handler in app.routes:
    print(f'{method} {path} -> {handler()}')
