# Saad's Debugging Progress

For every day, record the bug in your own words before marking it complete.

## Current result

- Checked through: Day 8
- Day 7: Skipped
- Completed: 4
- Partial: 1
- Retry required: 2
- Current score: approximately 65%

| Day | Status | Error/cause I found | What I learned |
|---|---|---|---|
| 01 | Partial | A string and integer cannot be added directly. Inputs were changed to integers, but type hints do not convert runtime values. | Type hints describe expected types; they do not perform conversion. |
| 02 | Completed | The condition excluded the boundary age of 18 because it used `>`. | Use `>=` when the boundary value must be included. |
| 03 | Completed | `range(len(numbers) - 1)` stopped before processing the final item. | Check loop boundaries carefully to avoid off-by-one errors. |
| 04 | Completed | The percentage was not divided by 100, and the function did not return the calculated result. | Trace formulas and confirm that functions return their results. |
| 05 | Retry | The original requirement and assertions were changed; the second student's score was also increased. | Fix the implementation without changing the original expected behavior. |
| 06 | Retry | A bare `except` hides `ZeroDivisionError`, and `10 / 8` cannot test zero division. | Catch only the expected conversion error and keep original test cases unchanged. |
| 07 | Skipped | Skipped by request. | Complete later. |
| 08 | Completed | The transaction list was shared as a mutable class attribute. | Put mutable per-account state inside `__init__`. |
| 09 | Not started | | |
| 10 | Not started | | |
| 11 | Not started | | |
| 12 | Not started | | |
| 13 | Not started | | |
| 14 | Not started | | |
| 15 | Not started | | |

## Teacher feedback

Good progress on conditions, loops, functions, and object state. The next skill to strengthen is test discipline: do not change an assertion simply to make the program pass. Preserve the requirement, identify the root cause, and make the smallest possible correction.

## Debug report template

- Error type:
- File and line:
- Actual result:
- Expected result:
- Root cause:
- Smallest fix:
- How I verified it:
