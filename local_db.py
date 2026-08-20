import json
import uuid
from pathlib import Path
from datetime import datetime


DATA_DIR = Path(__file__).resolve().parent / "data"


def _ensure_dir():
    DATA_DIR.mkdir(exist_ok=True)


def _load(table: str) -> list[dict]:
    _ensure_dir()
    path = DATA_DIR / f"{table}.json"
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(table: str, rows: list[dict]):
    _ensure_dir()
    path = DATA_DIR / f"{table}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)


class LocalQuery:
    def __init__(self, table: str):
        self._table = table
        self._rows = _load(table)
        self._filters: list[tuple[str, str, any]] = []
        self._order_by: str | None = None
        self._order_desc: bool = False
        self._select_fields: str | None = None

    def select(self, fields: str = "*"):
        self._select_fields = fields
        return self

    def eq(self, field: str, value):
        self._filters.append(("eq", field, value))
        return self

    def order(self, field: str, desc: bool = False):
        self._order_by = field
        self._order_desc = desc
        return self

    def _apply_filters(self) -> list[dict]:
        result = list(self._rows)
        for op, field, value in self._filters:
            if op == "eq":
                result = [r for r in result if r.get(field) == value]
        if self._order_by:
            reverse = self._order_desc
            result.sort(key=lambda r: r.get(self._order_by, ""), reverse=reverse)
        return result

    def execute(self):
        data = self._apply_filters()
        return _Result(data)


class LocalInsertQuery:
    def __init__(self, table: str, rows: list[dict]):
        self._table = table
        self._rows = rows

    def execute(self):
        existing = _load(self._table)
        new_rows = []
        for row in self._rows:
            if "id" not in row:
                row["id"] = str(uuid.uuid4())
            if "created_at" not in row:
                row["created_at"] = datetime.utcnow().isoformat()
            existing.append(row)
            new_rows.append(row)
        _save(self._table, existing)
        return _Result(new_rows)


class LocalUpdateQuery:
    def __init__(self, table: str, fields: dict):
        self._table = table
        self._fields = fields
        self._filters: list[tuple[str, str, any]] = []

    def eq(self, field: str, value):
        self._filters.append((field, value))
        return self

    def execute(self):
        rows = _load(self._table)
        updated = []
        for row in rows:
            match = all(row.get(f) == v for f, v in self._filters)
            if match:
                row.update(self._fields)
                updated.append(row)
        _save(self._table, rows)
        return _Result(updated)


class LocalDeleteQuery:
    def __init__(self, table: str):
        self._table = table
        self._filters: list[tuple[str, str, any]] = []

    def eq(self, field: str, value):
        self._filters.append((field, value))
        return self

    def execute(self):
        rows = _load(self._table)
        remaining = []
        for row in rows:
            match = all(row.get(f) == v for f, v in self._filters)
            if not match:
                remaining.append(row)
        _save(self._table, remaining)
        return _Result([])


class _Result:
    def __init__(self, data: list[dict]):
        self.data = data


class LocalTable:
    def __init__(self, table: str):
        self._table = table

    def select(self, fields: str = "*"):
        return LocalQuery(self._table).select(fields)

    def insert(self, rows):
        if isinstance(rows, dict):
            rows = [rows]
        return LocalInsertQuery(self._table, rows)

    def update(self, fields: dict):
        return LocalUpdateQuery(self._table, fields)

    def delete(self):
        return LocalDeleteQuery(self._table)


class LocalClient:
    def table(self, name: str):
        return LocalTable(name)
