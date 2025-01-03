# None Type
result = None
print(f'Type: {type(result)}')
print(f'Is None: {result is None}')
print(f'Is not None: {result is not None}')

def find_user(id):
    if id == 1:
        return {'name': 'Saad'}
    return None

user = find_user(1)
if user is not None:
    print(f'Found: {user[\
