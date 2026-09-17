from fastapi.testclient import TestClient

from challenges.day_22_testing import app, products

client = TestClient(app)


def setup_function():
    products.clear()


def test_create_product_returns_201_and_id_one():
    response = client.post("/products", json={"name": "Keyboard"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Keyboard"}


def test_get_missing_product_returns_404():
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_created_product_can_be_retrieved():
    created = client.post("/products", json={"name": "Mouse"}).json()
    response = client.get(f"/products/{created['id']}")
    assert response.status_code == 200
    assert response.json()["name"] == "Mouse"
