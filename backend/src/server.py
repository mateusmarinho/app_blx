from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from backend.src.schemas.schemas import Product, CustomProduct
from backend.src.infra.sqlalchemy.repositories.product import RepositoryProduct
from backend.src.infra.sqlalchemy.config.database import create_db, get_db

create_db()

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "API is running!"}


@app.get("/products", status_code=status.HTTP_200_OK, response_model=list[CustomProduct])
def get_all_products(db: Session = Depends(get_db)):
    products = RepositoryProduct(db).get_all()
    return products


@app.post("/products", status_code=status.HTTP_201_CREATED, response_model=Product)
def create_product(product: Product, db: Session = Depends(get_db)):
    new_product = RepositoryProduct(db).create(product)
    return new_product
