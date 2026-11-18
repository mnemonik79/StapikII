from fastapi import FastAPI

from app.routers.orders import router as orders_router

app = FastAPI(
    title="Order Processing Service",
    description="Modernized API for processing orders from legacy PHP script",
    version="1.0.0",
)

app.include_router(orders_router)
