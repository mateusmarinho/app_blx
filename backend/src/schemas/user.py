from pydantic import BaseModel

# from backend.src.schemas.product import Product


class User(BaseModel):
    id: int | None = None
    username: str
    password: str
    phone: str

    class Config:
        orm_mode = True
