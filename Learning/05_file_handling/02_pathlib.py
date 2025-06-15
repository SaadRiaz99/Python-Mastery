# Python pathlib - Modern Path Handling

from pathlib import Path

# Creating paths
current = Path('.')
home = Path.home()
project = Path('my_project')
file_path = Path('folder/subfolder/file.txt')

print(f'Current: {current}')
print(f'Home: {home}')
print(f'Project: {project}')

# Path properties
p = Path('/home/user/documents/file.txt')
print(f'Name: {p.name}')
print(f'Stem: {p.stem}')
print(f'Suffix: {p.suffix}')
print(f'Parent: {p.parent}')
print(f'Root: {p.root}')

# Path operations
new_path = current / 'folder' / 'subfolder' / 'file.txt'
print(f'Joined: {new_path}')

# Path methods
test_file = Path('test.txt')

# Create file
test_file.touch()
print(f'Exists: {test_file.exists()}')
print(f'Is file: {test_file.is_file()}')
print(f'Is dir: {test_file.is_dir()}')

# Write content
test_file.write_text('Hello from pathlib!')
print(f'Content: {test_file.read_text()}')

# Get absolute path
print(f'Absolute: {test_file.absolute()}')

# List directory
for item in Path('.').iterdir():
    print(f'  {item.name}')

# Glob patterns
python_files = list(Path('.').glob('*.py'))
print(f'Python files: {python_files}')

# Clean up
test_file.unlink()
print(f'File deleted: {not test_file.exists()}')

