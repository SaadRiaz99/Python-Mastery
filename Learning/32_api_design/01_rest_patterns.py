REST_PATTERNS = {
    'GET /users': 'List all users',
    'GET /users/{id}': 'Get user by ID',
    'POST /users': 'Create new user',
    'PUT /users/{id}': 'Update user',
    'DELETE /users/{id}': 'Delete user',
    'GET /users/{id}/posts': 'Get user posts',
    'POST /auth/login': 'Login',
    'POST /auth/logout': 'Logout',
}

HTTP_STATUS = {
    200: 'OK',
    201: 'Created',
    204: 'No Content',
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not Found',
    500: 'Internal Server Error',
}

for endpoint, desc in REST_PATTERNS.items():
    print(f'{endpoint}: {desc}')
