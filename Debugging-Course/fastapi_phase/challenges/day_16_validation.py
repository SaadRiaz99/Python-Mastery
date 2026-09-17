"""Day 16 — Request validation and HTTP 422

Run:
    python -m uvicorn challenges.day_16_validation:app --reload

Required request (do not change it):
    POST /products
    {"name": "Keyboard", "price": 2500, "stock": 4}

Expected:
    HTTP 201
    {"name": "Keyboard", "price": 2500.0, "stock": 4}

Invalid price <= 0 must return 422.

Learning tip:
A 422 usually means routing succeeded, but the incoming data did not match
FastAPI's expected schema. Read response.json()["detail"] before editing code.

Do not rename the required JSON fields to match the broken model.
"""

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class ProductCreate(BaseModel):
    product_name: str
    cost: float
    available: int


@app.post("/products", status_code=status.HTTP_200_OK)
def create_product(product: ProductCreate):
    return product
