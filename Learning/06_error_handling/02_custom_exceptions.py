# Custom Exceptions

class AppError(Exception):
    pass

class ValidationError(AppError):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f'{field}: {message}')

class NotFoundError(AppError):
    def __init__(self, resource, id):
        self.resource = resource
        self.id = id
        super().__init__(f'{resource} with id {id} not found')

class DuplicateError(AppError):
    pass

def create_user(name, email, existing_emails):
    if email in existing_emails:
        raise DuplicateError(f'Email {email} already exists')
    if not name:
        raise ValidationError('name', 'Name is required')
    return {'name': name, 'email': email}

try:
    create_user('', 'test@example.com', ['test@example.com'])
except ValidationError as e:
    print(f'Validation: {e}')
except DuplicateError as e:
    print(f'Duplicate: {e}')

