# Pathlib Patterns

from pathlib import Path
import json
import csv

# Config file pattern
def load_config(config_path: Path) -> dict:
    if config_path.exists():
        return json.loads(config_path.read_text())
    return {}

# Project structure
def create_project_structure(base: Path, name: str):
    dirs = ['src', 'tests', 'docs']
    for d in dirs:
        (base / name / d).mkdir(parents=True, exist_ok=True)
    (base / name / 'README.md').touch()
    (base / name / 'requirements.txt').touch()

# File organizer
def organize_files(source: Path, dest: Path):
    extensions = {
        '.py': 'python',
        '.js': 'javascript',
        '.txt': 'text',
    }
    for file in source.iterdir():
        if file.is_file():
            folder = extensions.get(file.suffix, 'other')
            (dest / folder).mkdir(exist_ok=True)
            file.rename(dest / folder / file.name)

# Search patterns
def find_large_files(path: Path, size_mb: int = 1):
    threshold = size_mb * 1024 * 1024
    return [f for f in path.rglob('*') if f.is_file() and f.stat().st_size > threshold]

print('Pathlib patterns defined!')

