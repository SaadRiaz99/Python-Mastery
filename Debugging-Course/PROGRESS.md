# Saad's Debugging Course Progress

> Teacher-reviewed against the actual code committed in `Debugging-Course/challenges/`.

## Current Result

| Field | Result |
|---|---|
| Reviewed through | Day 15 |
| Completed | 8 days |
| Partial understanding | 3 days |
| Retry required | 4 days |
| Current score | **108/150 — 72%** |
| Current level | Improving beginner → early intermediate |
| Promotion status | Revision required before final completion |

## Day-by-Day Assessment

| Day | Topic | Status | Score | Teacher observation |
|---|---|---|---:|---|
| 01 | Types and input | Partial | 6/10 | The function works with integers, but the original string-input problem was avoided instead of proving conversion. Type hints do not convert runtime values. |
| 02 | Conditions | Completed | 10/10 | The age boundary was correctly changed to `>= 18`. |
| 03 | Loops | Completed | 10/10 | The off-by-one error was fixed and every number is processed. |
| 04 | Functions | Completed | 9/10 | Formula and return flow are correct. Temporary debug output can now be removed. |
| 05 | Collections | Retry | 3/10 | The original requirement/test data was changed and Sumaiya's score was also increased. Only the requested student's record should change. |
| 06 | Exceptions | Retry | 2/10 | Bare `except` hides programming errors, and `10 / 8` does not test zero division. |
| 07 | Files and paths | Retry | 4/10 | The path still depends on the current working directory, so the main reliability requirement is not met. |
| 08 | OOP state | Completed | 9/10 | Instance state is correctly created in `__init__`. The unused class-level mutable list should be removed. |
| 09 | Imports and `__name__` | Partial | 7/10 | Demo is guarded, but top-level assertion/print still run during import. Importing should have no unexpected output. |
| 10 | Optional JSON fields | Partial | 6/10 | Valid JSON loads, but optional fields are still accessed with `[]`; missing `city` would raise `KeyError`. |
| 11 | Decorators | Completed | 10/10 | `@wraps` is used and the wrapper correctly returns the wrapped function's result. |
| 12 | Generators | Completed | 10/10 | `yield`, loop condition and increment correctly produce 1, 2, 3 lazily. |
| 13 | Async Python | Completed | 9/10 | Coroutines are awaited and real values collected. Later, learn `asyncio.gather()` for concurrent independent calls. |
| 14 | Testing and logging | Completed | 10/10 | Formula, assertions and useful logging are correct. |
| 15 | Capstone | Retry | 4/10 | Order items remain shared at class level, and the test passes `500` percent instead of the required `10` percent, so the assertion fails. |

## Strong Areas

- Conditions and boundary checks
- Loop boundaries
- Function arguments and return values
- Decorator return flow
- Generator execution
- Basic async/await
- Assertions and logging

## Three Concepts to Strengthen

### 1. Preserve the Requirement and Tests

A debugger fixes the implementation—not the expected result just to make a test pass.

Use this discipline:

1. Read the requirement.
2. Keep the original assertion unchanged.
3. Reproduce the failure.
4. Change the smallest implementation detail.
5. Run the same assertion again.

This is the main issue in Days 05, 06 and 15.

### 2. Catch Only Expected Exceptions

A bare `except:` hides unrelated bugs.

Ask:

- Which operation can fail?
- Which exact exception represents invalid user input?
- Which exception represents a programming or system failure that should remain visible?

Day 06 must demonstrate this difference.

### 3. Understand Ownership and Side Effects

State and code must belong in the correct place:

- Per-object mutable data belongs in `__init__`.
- Demo/test code should not execute when a module is imported.
- File paths should be based on the script location, not the terminal's current directory.
- Optional dictionary fields need safe access.

This connects Days 07, 08, 09, 10 and 15.

## Required Revision Order

### Revision 1 — Day 05: Collections

Goal: update only Ali's score without changing another student's score or the original assertions.

Evidence required:

- Print both records before the update.
- Apply one update.
- Assert Ali changed.
- Assert the other student did not change.
- Explain whether the nested dictionaries are separate objects.

### Revision 2 — Day 06: Exceptions

Goal: invalid text input returns `None`, but division by zero remains visible.

Evidence required:

- Test valid division.
- Test invalid string input.
- Test zero division.
- Name every exception you intentionally catch.
- Do not use bare `except`.

### Revision 3 — Day 07: Reliable Paths

Goal: the script must work from the repository root and from the challenge directory.

Evidence required:

- Build the path using `Path(__file__)`.
- Ensure the data directory exists.
- Run the file from two working directories.
- Record both commands and outputs.

### Revision 4 — Day 15: Capstone

Goal: complete the order system without changing the stated requirements.

Evidence required:

- Each `Order` owns its own items list.
- Unknown products raise `ValueError`.
- Zero/negative quantities raise `ValueError`.
- Subtotal is 5000.
- A 10% discount returns 4500.
- Create a second order to prove item lists are not shared.

## Quick Concept Checks

Answer these in your own words before asking for a full solution:

1. Why does `name: str` not convert an integer to a string automatically?
2. What is the difference between `except ValueError` and bare `except`?
3. Why is a list defined on a class shared, while `self.items = []` is per object?
4. What executes when Python imports a module?
5. When should `dict.get("city")` be preferred over `dict["city"]`?
6. What is the difference between returning a list and yielding values?
7. Why can `asyncio.gather()` be faster than awaiting independent calls one by one?

## Teacher Guidance

Saad, tum code ko dekh kar common syntax aur flow bugs solve kar rahe ho—especially functions, decorators, generators aur async mein improvement clear hai. Lekin professional debugging ka standard sirf `Day passed` print hona nahi hai. Requirement, original tests aur edge cases ko preserve karna zaroori hai.

Ab tumhara focus hona chahiye:

- **30% concept reading**
- **70% coding, debugging and proof**
- Har bug ke liye: **symptom → root cause → smallest fix → test → prevention**
- AI se pehle hint lo; final code tab dekho jab apna attempt aur reasoning likh chuke ho.

## Promotion Rule

Course complete tab mark hoga jab:

- Days 05, 06, 07 and 15 pass,
- Days 01, 09 and 10 ke partial concepts explain aur correct hon,
- all original assertions/requirements are preserved,
- and every corrected day includes at least one edge-case test.

## Debug Report Template

```text
Day:
Error type:
File and line:
Actual result:
Expected result:
Root cause:
Smallest fix:
Normal test:
Edge-case test:
How I verified it:
How I will prevent it next time:
```

_Last teacher review: 13 September 2026._
