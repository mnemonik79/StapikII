import pytest
from fastapi import HTTPException

from app.schemas.order import OrderCreateRequest, OrderItemRequest
from app.services.order_service import OrderService


def test_create_order_success():
    service = OrderService()
    order = OrderCreateRequest(
        user_id=15,
        items=[
            OrderItemRequest(id=1, qty=2),
            OrderItemRequest(id=3, qty=1),
        ],
    )

    result = service.create_order(order, current_user_id=15)

    assert result.order_id == 101
    assert result.user_id == 15
    assert result.total == 2100.00
    assert result.items_count == 2
    assert result.status == "created"


def test_create_order_forbidden():
    service = OrderService()
    order = OrderCreateRequest(
        user_id=15,
        items=[OrderItemRequest(id=1, qty=1)],
    )

    with pytest.raises(HTTPException) as exc_info:
        service.create_order(order, current_user_id=99)

    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "Forbidden: cannot create order for another user"


def test_create_order_product_not_found():
    service = OrderService()
    order = OrderCreateRequest(
        user_id=15,
        items=[OrderItemRequest(id=999, qty=1)],
    )

    with pytest.raises(HTTPException) as exc_info:
        service.create_order(order, current_user_id=15)

    assert exc_info.value.status_code == 404
    assert "not found" in exc_info.value.detail
