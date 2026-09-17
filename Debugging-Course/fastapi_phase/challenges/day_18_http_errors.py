"""Day 18 — HTTPException and response contracts

Expected:
- GET /orders/1 -> 200
- GET /orders/99 -> 404 with a useful detail message
- DELETE /orders/1 -> 204 with no response body

Learning tip:
A client-facing missing resource is not an unhandled Python KeyError. Translate
known domain failures into an intentional HTTP response. Do not catch every
exception and return HTTP 200.

Record both the HTTP response and server traceback before fixing.
"""

from fastapi import FastAPI

app = FastAPI()
orders = {1: {"id": 1, "status": "processing"}}


@app.get("/orders/{order_id}")
def get_order(order_id: int):
    if order_id not in orders:
        raise ValueError("Order does not exist")
    return orders[order_id]


@app.delete("/orders/{order_id}")
def delete_order(order_id: int):
    deleted = orders.pop(order_id)
    return {"deleted": deleted}
