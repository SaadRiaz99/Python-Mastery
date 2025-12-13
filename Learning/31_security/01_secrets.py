import os

def get_secret(key, default=None):
    return os.getenv(key, default)

class SecretManager:
    def __init__(self):
        self._secrets = {}

    def set(self, key, value):
        self._secrets[key] = value

    def get(self, key):
        return self._secrets.get(key)

manager = SecretManager()
manager.set('api_key', 'secret123')
print(f'API Key: {manager.get(\
