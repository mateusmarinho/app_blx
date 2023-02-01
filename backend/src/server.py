from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from backend.src.schemas.schemas import Product
from backend.src.infra.sqlalchemy.repositories.product import RepositoryProduct
from backend.src.infra.sqlalchemy.config.database import create_db, get_db

create_db()

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "API is running!"}


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    products = RepositoryProduct(db).get_all()
    return products


@app.post("/products")
def create_product(product: Product, db: Session = Depends(get_db)):
    new_product = RepositoryProduct(db).create(product)
    return new_product
