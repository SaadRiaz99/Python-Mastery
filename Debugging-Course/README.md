# Python Debugging Course — 15 Days

This course is practice-first. Every Python file contains one or more intentional bugs. Your job is to diagnose and fix them.

## How to study each day

1. Read the goal and expected result at the top of the file.
2. Run the file: `python Debugging-Course/challenges/day_01_types.py`
3. Read the final traceback line first.
4. Write down: error type, file/line, cause, and proposed fix.
5. Change only what is needed.
6. Run it again until every `assert` passes.
7. Mark the day in `PROGRESS.md`.

Do not search for a finished solution immediately. Use `print()`, `type()`, `repr()`, tracebacks, breakpoints, and small experiments.

## Course map

| Day | Topic | Main debugging skill |
|---|---|---|
| 1 | Types and input | Inspect values and convert types |
| 2 | Conditions | Trace Boolean logic |
| 3 | Loops | Find boundary/off-by-one errors |
| 4 | Functions | Follow arguments and return values |
| 5 | Lists and dictionaries | Inspect keys, indexes, and mutation |
| 6 | Exceptions | Catch only expected failures |
| 7 | Files and paths | Use safe paths and context managers |
| 8 | OOP | Trace instance state |
| 9 | Imports | Understand module names and entry points |
| 10 | JSON data | Validate external data |
| 11 | Decorators | Preserve and return wrapped results |
| 12 | Generators | Understand lazy execution |
| 13 | Async Python | Await coroutines correctly |
| 14 | Testing and logging | Reproduce bugs with evidence |
| 15 | Capstone | Debug a small order system |

## Useful commands

```powershell
git clone https://github.com/SaadRiaz99/Python-Mastery.git
cd Python-Mastery
python Debugging-Course/challenges/day_01_types.py
python -m pdb Debugging-Course/challenges/day_04_functions.py
```

Start with Day 1 and solve in order. The assertions are your built-in checks: no assertion error means the task is complete.
