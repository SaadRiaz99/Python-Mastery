import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent.parent / "school.db"

SUBJECTS = ["Math", "Science", "English", "History"]

SEED_ASSIGNMENTS = [
    ("Algebra worksheet", "Math", 1, 1),
    ("Book report", "English", 2, 0),
    ("Lab safety quiz", "Science", 3, 1),
    ("History timeline", "History", 1, 0),
    ("Geometry problems", "Math", 2, 1),
    ("Poem analysis", "English", 3, 0),
    ("Chemistry pre-lab", "Science", 2, 0),
    ("Map skills quiz", "History", 1, 1),
    ("Essay outline", "English", 1, 0),
    ("Physics review", "Science", 3, 0),
    ("Statistics homework", "Math", 2, 1),
    ("Civics reading", "History", 3, 0),
]


def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            subject TEXT NOT NULL DEFAULT 'Math',
            difficulty INTEGER NOT NULL DEFAULT 2,
            submitted INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
    count = conn.execute("SELECT COUNT(*) FROM assignments").fetchone()[0]
    if count == 0:
        conn.executemany(
            "INSERT INTO assignments (title, subject, difficulty, submitted) "
            "VALUES (?, ?, ?, ?)",
            SEED_ASSIGNMENTS,
        )
        conn.commit()
    conn.close()


def fetch_all():
    conn = get_db()
    rows = conn.execute("SELECT * FROM assignments ORDER BY id").fetchall()
    conn.close()
    return [dict(row) for row in rows]


async def fetch_all_async():
    return fetch_all()


def fetch_one(assignment_id):
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM assignments WHERE id = ?", (assignment_id,)
    ).fetchone()
    conn.close()
    return dict(row) if row else None


def create_assignment(title, subject, difficulty=2):
    conn = get_db()
    conn.execute(
        "INSERT INTO assignments (title, subject, difficulty) VALUES (?, ?, ?)",
        (title, subject, difficulty),
    )
    conn.commit()
    conn.close()


def update_assignment(assignment_id, title, subject, difficulty):
    conn = get_db()
    conn.execute(
        "UPDATE assignments SET title = ?, subject = ?, difficulty = ? WHERE id = ?",
        (title, subject, difficulty, assignment_id),
    )
    conn.commit()
    conn.close()


def toggle_submitted(assignment_id):
    conn = get_db()
    conn.execute(
        "UPDATE assignments SET submitted = CASE submitted WHEN 1 THEN 0 ELSE 1 END "
        "WHERE id = ?",
        (assignment_id,),
    )
    conn.commit()
    conn.close()


def delete_assignment(assignment_id):
    conn = get_db()
    conn.execute("DELETE FROM assignments WHERE id = ?", (assignment_id,))
    conn.commit()
    conn.close()
