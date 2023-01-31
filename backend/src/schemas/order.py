from pydantic import BaseModel

from backend.src.schemas.user import User
from backend.src.schemas.product import Product


class Order(BaseModel):
    id: str | None = None
    user: User
    product: Product
    quantity: int
    is_delivery: bool = False
    delivery_address: str | None = None
    notes: str = "Sem observações."
