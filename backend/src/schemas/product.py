from pydantic import BaseModel

from backend.src.schemas.user import User


class Product(BaseModel):
    id: str | None = None
    name: str
    details: str
    price: float
    is_available: bool = False
    user: User
