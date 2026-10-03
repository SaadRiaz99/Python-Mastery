import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent.parent / "todos.db"

SEED_TODOS = [
    ("Buy milk", 0, 1),
    ("Write report", 0, 2),
    ("Walk the dog", 1, 3),
    ("Pay bills", 0, 1),
    ("Read a book", 1, 2),
    ("Call the dentist", 0, 3),
    ("Water plants", 0, 2),
    ("Clean the kitchen", 1, 1),
    ("Plan the trip", 0, 2),
    ("Fix the bike", 0, 3),
    ("Learn FastAPI", 1, 1),
    ("Buy groceries", 0, 2),
]


def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0,
            priority INTEGER NOT NULL DEFAULT 2
        )
        """
    )
    conn.commit()
    count = conn.execute("SELECT COUNT(*) FROM todos").fetchone()[0]
    if count == 0:
        conn.executemany(
            "INSERT INTO todos (title, done, priority) VALUES (?, ?, ?)", SEED_TODOS
        )
        conn.commit()
    conn.close()


def fetch_all():
    conn = get_db()
    rows = conn.execute("SELECT * FROM todos ORDER BY id").fetchall()
    conn.close()
    return [dict(row) for row in rows]


async def fetch_all_async():
    return fetch_all()


def fetch_one(todo_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM todos WHERE id = ?", (todo_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def create_todo(title, priority=2):
    conn = get_db()
    conn.execute(
        "INSERT INTO todos (title, priority) VALUES (?, ?)", (title, priority)
    )
    conn.commit()
    conn.close()


def update_todo(todo_id, title, priority):
    conn = get_db()
    conn.execute(
        "UPDATE todos SET title = ?, priority = ? WHERE id = ?",
        (title, priority, todo_id),
    )
    conn.commit()
    conn.close()


def toggle_done(todo_id):
    conn = get_db()
    conn.execute(
        "UPDATE todos SET done = CASE done WHEN 1 THEN 0 ELSE 1 END WHERE id = ?",
        (todo_id,),
    )
    conn.commit()
    conn.close()


def delete_todo(todo_id):
    conn = get_db()
    conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
