from fastapi import APIRouter, Header

from app.schemas.order import OrderCreateRequest, OrderCreateResponse
from app.services.order_service import OrderService

router = APIRouter(prefix="/api/orders", tags=["orders"])

order_service = OrderService()


@router.post("", response_model=OrderCreateResponse)
def create_order(
    order: OrderCreateRequest,
    x_user_id: int = Header(..., alias="X-User-Id"),
) -> OrderCreateResponse:
    """
    Create a new order for authenticated user.
    """
    return order_service.create_order(order, current_user_id=x_user_id)
