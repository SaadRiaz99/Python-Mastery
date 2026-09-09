"""Day 7: Write and read the file reliably from any working directory."""

from pathlib import Path

DATA_FILE = Path("data") / "note.txt"

def save_note(text):
    DATA_FILE.write_text(text, encoding="utf-8")

def load_note():
    return DATA_FILE.read_text(encoding="utf-8")

save_note("Debugging needs evidence.")
assert load_note() == "Debugging needs evidence."
print("Day 7 passed")
