# FastAPI Debugging Phase — Days 16 to 23

This is Phase 2 of Saad's debugging course. It is slightly more advanced than the Python phase.

## Goal

Learn to diagnose FastAPI problems like an engineer:

- 422 request validation errors
- 404 and 405 routing errors
- incorrect status codes and hidden server errors
- dependency injection and authentication failures
- blocking code inside async routes
- data/session lifecycle problems
- failing API tests
- a small Agentic AI-style support API

## Study rule

Do not replace the challenge with fresh code. Reproduce the bug, write evidence, then make the smallest fix.

## Daily 90-minute routine

| Time | Work |
|---:|---|
| 15 min | Read goal, route and schema |
| 20 min | Reproduce request and capture evidence |
| 20 min | Trace request → validation → route → service → response |
| 20 min | Apply one focused fix |
| 10 min | Test normal and failure cases |
| 5 min | Update `PROGRESS.md` and error report |

## Course map

| Day | Topic | Main engineering skill |
|---|---|---|
| 16 | Validation and 422 | Compare JSON body with Pydantic schema |
| 17 | Routing and 404/405 | Check path, method, parameter type and route order |
| 18 | HTTPException and status codes | Separate client errors from server errors |
| 19 | Dependencies and auth | Trace dependency execution before route execution |
| 20 | Async and blocking work | Identify event-loop blocking and missing awaits |
| 21 | Data/session lifecycle | Own state correctly and avoid hidden global behavior |
| 22 | API testing | Use TestClient to prove normal and edge cases |
| 23 | Support-agent API capstone | Debug the complete API request flow |

## Setup

From the repository root:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r Debugging-Course\fastapi_phase\requirements.txt
cd Debugging-Course\fastapi_phase
```

Run a challenge:

```powershell
python -m uvicorn challenges.day_16_validation:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Run tests:

```powershell
python -m pytest -q
```

## Passing rule

A day passes only when:

1. You explain the root cause.
2. Normal request works.
3. At least one invalid request is tested.
4. Requirement and tests are not changed.
5. You record prevention guidance.
