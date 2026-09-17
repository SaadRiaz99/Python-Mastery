# How to Analyse a Mistake Like an Engineer

## The request-flow map

For every FastAPI bug, trace this order:

```text
Client request
→ HTTP method and URL
→ request headers/body/path/query
→ Pydantic validation
→ dependencies
→ route function
→ service/business logic
→ database or external API
→ response model/status/body
```

The first stage that differs from expectation is usually where investigation begins.

## EVIDENCE method

### E — Establish expected behavior

Write the exact expected status code and body before editing code.

### V — Verify the failure

Reproduce it using `/docs`, curl, PowerShell, or a test. Copy the actual status code, response body and traceback.

### I — Isolate the failing layer

Ask whether the failure is in routing, validation, dependency, service, database, external API, or response serialization.

### D — Diagnose the root cause

A symptom is not a root cause.

- Symptom: API returned 422.
- Weak explanation: body is wrong.
- Root cause: schema requires `price: float`, but the request omitted `price`.

### E — Experiment with one change

Change one relevant thing. Do not rewrite the whole file.

### N — Normal and edge-case tests

Test at least:

- normal request
- missing/invalid input
- boundary value
- missing resource
- dependency failure, when relevant

### C — Confirm no regression

Rerun previous passing tests.

### E — Explain prevention

Examples:

- Add a Pydantic constraint.
- Add an API test.
- Use a specific exception.
- Add structured logging.
- Document a dependency contract.

## FastAPI status-code diagnosis

| Status | First place to inspect |
|---:|---|
| 404 | Path spelling, prefix, router inclusion, route order |
| 405 | HTTP method |
| 422 | Request schema, field names/types, path/query/body location |
| 401/403 | Authentication dependency and headers |
| 500 | Server traceback, service/database/external call |
| 200 with wrong data | Business logic and response serialization |

## Five questions before changing code

1. What exactly did I send?
2. What did FastAPI expect?
3. Which layer failed first?
4. What evidence proves my theory?
5. What smallest change fixes the root cause?

## Engineering report template

```text
Challenge:
Expected status/body:
Actual status/body:
Traceback or validation detail:
Failing layer:
Root cause:
Hypothesis:
Smallest change:
Normal test:
Edge-case test:
Regression test:
Prevention:
```

## Teacher rule

Do not say “FastAPI is not working.” Say:

> POST /products returns 422 because the JSON uses `product_name`, while the request model requires `name`.

That sentence tells another engineer what failed, where it failed and why.
