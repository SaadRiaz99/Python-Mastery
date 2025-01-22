import json
import uuid
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).resolve().parent / 'data'

def _ensure_dir():
    DATA_DIR.mkdir(exist_ok=True)

def _load(table):
    _ensure_dir()
    path = DATA_DIR / f'{table}.json'
    if not path.exists():
        return []
    with open(path, 'r') as f:
        return json.load(f)

def _save(table, rows):
    _ensure_dir()
    path = DATA_DIR / f'{table}.json'
    with open(path, 'w') as f:
        json.dump(rows, f, indent=2)

class LocalClient:
    def table(self, name):
        return LocalTable(name)

class LocalTable:
    def __init__(self, table):
        self._table = table
    def select(self, fields='*'):
        return LocalQuery(self._table)
    def insert(self, rows):
        if isinstance(rows, dict):
            rows = [rows]
        return LocalInsertQuery(self._table, rows)
    def update(self, fields):
        return LocalUpdateQuery(self._table, fields)
    def delete(self):
        return LocalDeleteQuery(self._table)

class LocalQuery:
    def __init__(self, table):
        self._table = table
        self._rows = _load(table)
        self._filters = []
    def eq(self, field, value):
        self._filters.append((field, value))
        return self
    def order(self, field, desc=False):
        return self
    def execute(self):
        result = list(self._rows)
        for field, value in self._filters:
            result = [r for r in result if r.get(field) == value]
        return _Result(result)

class LocalInsertQuery:
    def __init__(self, table, rows):
        self._table = table
        self._rows = rows
    def execute(self):
        existing = _load(self._table)
        new_rows = []
        for row in self._rows:
            if 'id' not in row:
                row['id'] = str(uuid.uuid4())
            if 'created_at' not in row:
                row['created_at'] = datetime.utcnow().isoformat()
            existing.append(row)
            new_rows.append(row)
        _save(self._table, existing)
        return _Result(new_rows)

class LocalUpdateQuery:
    def __init__(self, table, fields):
        self._table = table
        self._fields = fields
        self._filters = []
    def eq(self, field, value):
        self._filters.append((field, value))
        return self
    def execute(self):
        rows = _load(self._table)
        for row in rows:
            if all(row.get(f) == v for f, v in self._filters):
                row.update(self._fields)
        _save(self._table, rows)
        return _Result([])

class LocalDeleteQuery:
    def __init__(self, table):
        self._table = table
        self._filters = []
    def eq(self, field, value):
        self._filters.append((field, value))
        return self
    def execute(self):
        rows = _load(self._table)
        remaining = [r for r in rows if not all(r.get(f) == v for f, v in self._filters)]
        _save(self._table, remaining)
        return _Result([])

class _Result:
    def __init__(self, data):
        self.data = data
