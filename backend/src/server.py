from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from backend.src.schemas.schemas import Product, User
# from backend.src.schemas.user import User
# from backend.src.schemas.product import Product
from backend.src.infra.sqlalchemy.repositories.product import RepositoryProduct
from backend.src.infra.sqlalchemy.repositories.user import RepositoryUser
from backend.src.infra.sqlalchemy.config.database import create_db, get_db

create_db()

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "API is running!"}


# Products routes
@app.get("/products", response_model=list[Product])
def get_all_products(db: Session = Depends(get_db)):
    products = RepositoryProduct(db).get_all()
    return products


@app.post("/products", status_code=status.HTTP_201_CREATED, response_model=Product)
def create_product(product: Product, db: Session = Depends(get_db)):
    new_product = RepositoryProduct(db).create(product)
    return new_product


@app.put("/products")
def update_product(product: Product, db: Session = Depends(get_db)):
    updated_product = RepositoryProduct(db).update_product(product)
    return updated_product


# Users routes
@app.get("/users", response_model=list[User])
def get_all_users(db: Session = Depends(get_db)):
    users = RepositoryUser(db).get_all()
    return users


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    new_user = RepositoryUser(db).create(user)
    return new_user
