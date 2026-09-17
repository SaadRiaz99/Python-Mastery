"""Day 22 — Let tests reproduce the API bug

Run from Debugging-Course/fastapi_phase:
    python -m pytest tests/test_day_22_products.py -q

Rules:
- Do not weaken or delete the tests.
- Fix this application.
- Add one extra edge-case test after the supplied tests pass.

Learning tip:
A failing test has three useful parts: request setup, actual response and expected
assertion. First reproduce one failure alone, then inspect response.status_code
and response.json().
"""

from fastapi import FastAPI

app = FastAPI()
products: dict[int, dict] = {}


@app.post("/products")
def create_product(payload: dict):
    product_id = len(products)
    product = {"id": product_id, **payload}
    products[product_id] = product
    return product


@app.get("/products/{product_id}")
def get_product(product_id: int):
    return products.get(product_id)
