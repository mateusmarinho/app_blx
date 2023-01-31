from pydantic import BaseModel

from backend.src.schemas.product import Product
from backend.src.schemas.order import Order


class User(BaseModel):
    id: str | None = None
    name: str
    phone: str
    password: str
    my_products: list[Product]
    my_sells: list[Order]
    my_orders: list[Order]
