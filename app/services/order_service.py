from fastapi import HTTPException

from app.schemas.order import OrderCreateRequest, OrderCreateResponse


class OrderService:
    """
    Service for creating orders and calculating totals.
    """

    def __init__(self) -> None:
        self.products = {
            1: {"name": "Laptop", "price": 1000.00},
            2: {"name": "Mouse", "price": 50.00},
            3: {"name": "Keyboard", "price": 100.00},
        }

    def create_order(self, order: OrderCreateRequest, current_user_id: int) -> OrderCreateResponse:
        """
        Create an order for the current user.

        Args:
            order: Validated order creation request.
            current_user_id: ID of authenticated user.

        Returns:
            OrderCreateResponse: Created order data.

        Raises:
            HTTPException: If access is forbidden or product not found.
        """
        if order.user_id != current_user_id:
            raise HTTPException(status_code=403, detail="Forbidden: cannot create order for another user")

        total = 0.0

        for item in order.items:
            product = self.products.get(item.id)
            if product is None:
                raise HTTPException(status_code=404, detail=f"Product with id={item.id} not found")

            total += product["price"] * item.qty

        return OrderCreateResponse(
            order_id=101,
            user_id=order.user_id,
            total=round(total, 2),
            items_count=len(order.items),
            status="created",
        )
