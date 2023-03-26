from pydantic import BaseModel

from backend.src.schemas.user import User


class Product(BaseModel):
    id: int | None = None
    name: str
    details: str
    price: float
    is_available: bool = False
    dimensions: str | None = None
    user_id: int
    user: User | None

    class Config:
        orm_mode = True
