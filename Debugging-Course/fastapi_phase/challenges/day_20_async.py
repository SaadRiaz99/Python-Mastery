"""Day 20 — Async routes, blocking work and missing await

Expected:
- GET /reports/7 -> 200
- Response: {"report_id": 7, "ready": true}
- Independent requests should not block the event loop with time.sleep()

Learning tips:
- async def returns a coroutine when called; it becomes a value after await.
- Blocking sleep inside async code freezes other work on the event loop.
- Inspect type(result) or repr(result) if serialization fails.

Do not remove async merely to hide the problem.
"""

import asyncio
import time

from fastapi import FastAPI

app = FastAPI()


async def build_report(report_id: int):
    time.sleep(0.2)
    return {"report_id": report_id, "ready": True}


@app.get("/reports/{report_id}")
async def get_report(report_id: int):
    report = build_report(report_id)
    return report
