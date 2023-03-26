from pydantic import BaseModel


class User(BaseModel):
    id: int | None = None
    username: str
    password: str
    phone: str

    class Config:
        orm_mode = True


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


class CustomProduct(BaseModel):
    id: int | None = None
    name: str

    class Config:
        orm_mode = True
