"""Day 23 — FastAPI support-agent capstone

This challenge is deterministic and uses no paid API.

Expected:
- GET /health -> 200
- POST /chat body: {"message": "hello"} -> helpful general reply
- POST /chat body: {"message": "where is my order?", "order_id": 101}
  -> order status
- Unknown order -> 404, not 500
- Empty message -> 422
- Order lookup must run only for an order-related message
- Internal errors must not expose implementation details

Learning tips:
Trace:
request → schema → route → service decision → tool → exception mapping → response.

Do not hardcode a successful response for the tests. Repair the complete flow.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
ORDERS = {101: "shipped", 102: "processing"}


class ChatRequest(BaseModel):
    text: str
    order: int | None = None


def lookup_order(order_id: int):
    return ORDERS[order_id]


async def support_reply(message: str, order_id: int | None):
    if "order" in message:
        status = lookup_order(order_id)
        return {"reply": f"Order status: {status}"}
    status = lookup_order(order_id)
    return {"reply": f"Welcome. Order status: {status}"}


@app.get("/health")
def health():
    return {"status": True}


@app.post("/chat")
def chat(request: ChatRequest):
    return support_reply(request.message, request.order_id)
