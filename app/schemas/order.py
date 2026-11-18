from typing import List

from pydantic import BaseModel, Field


class OrderItemRequest(BaseModel):
    id: int = Field(..., gt=0, description="Product ID")
    qty: int = Field(..., gt=0, description="Quantity of product")


class OrderCreateRequest(BaseModel):
    user_id: int = Field(..., gt=0, description="User ID")
    items: List[OrderItemRequest] = Field(..., min_length=1, description="List of items")


class OrderCreateResponse(BaseModel):
    order_id: int
    user_id: int
    total: float
    items_count: int
    status: str
