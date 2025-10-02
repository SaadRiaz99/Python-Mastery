# contextlib

from contextlib import contextmanager, suppress, redirect_stdout, ExitStack
from io import StringIO

# contextmanager
@contextmanager
def managed_resource():
    print('Acquiring resource')
    resource = {'status': 'active'}
    try:
        yield resource
    finally:
        print('Releasing resource')

with managed_resource() as res:
    print(f'Using: {res}')

# suppress
with suppress(FileNotFoundError):
    import os
    os.remove('nonexistent.txt')
print('Continued')

# redirect_stdout
with StringIO() as output:
    with redirect_stdout(output):
        print('This is captured')
    captured = output.getvalue()
print(f'Captured: {captured.strip()}')

# ExitStack
with ExitStack() as stack:
    files = [stack.enter_context(open(f'file{i}.txt', 'w')) for i in range(3)]
    print(f'Opened {len(files)} files')

