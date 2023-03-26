from pydantic import BaseModel


class SimpleProduct(BaseModel):
    id: int | None = None
    name: str
    details: str
    price: float
    is_available: bool = False
    dimensions: str | None = None

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int | None = None
    username: str
    password: str
    phone: str
    products: list[SimpleProduct] | None

    class Config:
        orm_mode = True


class SimpleUser(BaseModel):
    id: int | None = None
    username: str
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
    user: SimpleUser | None

    class Config:
        orm_mode = True
