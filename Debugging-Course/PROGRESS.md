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

## Next Phase

The next learning stage is available in [FastAPI Debugging Phase](fastapi_phase/README.md).

Start Phase 2 after revising Days 05, 06, 07 and 15. The FastAPI phase is intentionally a little more advanced and focuses on reading HTTP errors, request validation, dependencies, async behavior, testing and API architecture.

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

1. Read the requirement.
2. Keep the original assertion unchanged.
3. Reproduce the failure.
4. Change the smallest implementation detail.
5. Run the same assertion again.

### 2. Catch Only Expected Exceptions

A bare `except:` hides unrelated bugs. Identify the exact operation and exception before handling it.

### 3. Understand Ownership and Side Effects

- Per-object mutable data belongs in `__init__`.
- Demo/test code should not execute during import.
- File paths should be based on the script location.
- Optional dictionary fields need safe access.

## Required Revision Order

1. **Day 05:** Change only Ali's score and preserve the original test.
2. **Day 06:** Invalid text returns `None`, but zero division remains visible.
3. **Day 07:** Use `Path(__file__)` and test from two working directories.
4. **Day 15:** Give every `Order` its own list and preserve the 10% discount requirement.

## Teacher Guidance

Saad, tum common syntax aur flow bugs solve kar rahe ho—especially functions, decorators, generators aur async mein improvement clear hai. Professional debugging ka standard sirf `Day passed` print hona nahi hai. Requirement, original tests aur edge cases preserve karna zaroori hai.

- **30% concept reading**
- **70% coding, debugging and proof**
- Har bug: **symptom → root cause → smallest fix → test → prevention**
- AI se pehle hint lo; final code tab dekho jab apna attempt aur reasoning likh chuke ho.

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

_Last teacher review: 17 September 2026._
