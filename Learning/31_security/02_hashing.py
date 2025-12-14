import hashlib
import secrets

def simple_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return salt, password_hash.hex()

def verify_password(password, salt, stored_hash):
    _, password_hash = hash_password(password, salt)
    return password_hash == stored_hash

password = 'mypassword123'
salt, hashed = hash_password(password)
print(f'Hashed: {hashed}')

is_valid = verify_password(password, salt, hashed)
print(f'Valid: {is_valid}')
