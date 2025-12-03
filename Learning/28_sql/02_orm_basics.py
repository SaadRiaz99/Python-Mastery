from dataclasses import dataclass
from typing import Optional

@dataclass
class Model:
    id: Optional[int] = None

    def save(self):
        print(f'Saving {self.__class__.__name__} with id={self.id}')

    def delete(self):
        print(f'Deleting {self.__class__.__name__} with id={self.id}')

@dataclass
class User(Model):
    name: str = ''
    email: str = ''

@dataclass
class Post(Model):
    title: str = ''
    content: str = ''
    author_id: int = 0

user = User(name='Saad', email='saad@example.com')
user.id = 1
user.save()

post = Post(title='Hello', content='World', author_id=1)
post.id = 1
post.save()

user.delete()
post.delete()
