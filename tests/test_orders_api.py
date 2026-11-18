from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_order_api_success():
    payload = {
        "user_id": 15,
        "items": [
            {"id": 1, "qty": 2},
            {"id": 3, "qty": 1},
        ],
    }

    response = client.post(
        "/api/orders",
        json=payload,
        headers={"X-User-Id": "15"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["order_id"] == 101
    assert data["user_id"] == 15
    assert data["total"] == 2100.0
    assert data["items_count"] == 2
    assert data["status"] == "created"


def test_create_order_api_forbidden():
    payload = {
        "user_id": 15,
        "items": [{"id": 1, "qty": 1}],
    }

    response = client.post(
        "/api/orders",
        json=payload,
        headers={"X-User-Id": "99"},
    )

    assert response.status_code == 403
    assert response.json()["detail"] == "Forbidden: cannot create order for another user"


def test_create_order_api_not_found():
    payload = {
        "user_id": 15,
        "items": [{"id": 999, "qty": 1}],
    }

    response = client.post(
        "/api/orders",
        json=payload,
        headers={"X-User-Id": "15"},
    )

    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_create_order_api_validation_error():
    payload = {
        "user_id": 15,
        "items": [],
    }

    response = client.post(
        "/api/orders",
        json=payload,
        headers={"X-User-Id": "15"},
    )

    assert response.status_code == 422
