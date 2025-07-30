# Advanced pathlib Usage

from pathlib import Path
import os

# Current directory
cwd = Path.cwd()
print(f'Current: {cwd}')

# Home directory
home = Path.home()
print(f'Home: {home}')

# Path construction
project_dir = Path('my_project')
src_dir = project_dir / 'src'
main_file = src_dir / 'main.py'
print(f'Main file: {main_file}')

# Path properties
p = Path('/home/user/documents/report.txt')
print(f'Name: {p.name}')
print(f'Stem: {p.stem}')
print(f'Suffix: {p.suffix}')
print(f'Parent: {p.parent}')
print(f'Root: {p.root}')
print(f'Parts: {p.parts}')

# Creating directories
test_dir = Path('test_directory')
test_dir.mkdir(exist_ok=True)
(test_dir / 'subdir1').mkdir(exist_ok=True)
(test_dir / 'subdir2').mkdir(exist_ok=True)

# Create files
(test_dir / 'file1.txt').write_text('Hello from file1')
(test_dir / 'file2.txt').write_text('Hello from file2')
(test_dir / 'subdir1' / 'file3.txt').write_text('Hello from file3')

# List directory
print('Directory contents:')
for item in sorted(test_dir.iterdir()):
    print(f'  {item.name} ({
