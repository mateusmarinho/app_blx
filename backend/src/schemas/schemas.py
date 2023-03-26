from pydantic import BaseModel


class Product(BaseModel):
    id: str | None = None
    name: str
    details: str
    price: float
    is_available: bool = False

    class Config:
        orm_mode = True


class CustomProduct(BaseModel):
    id: str | None = None
    name: str

    class Config:
        orm_mode = True
