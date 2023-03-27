from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.src.schemas.schemas import Product
from backend.src.infra.sqlalchemy.repositories.product import RepositoryProduct
from backend.src.infra.sqlalchemy.config.database import get_db

router = APIRouter()


@router.get("/products", response_model=list[Product])
def get_all_products(db: Session = Depends(get_db)):
    products = RepositoryProduct(db).get_all()
    return products


@router.post(
        "/products", status_code=status.HTTP_201_CREATED, response_model=Product
)
def create_product(product: Product, db: Session = Depends(get_db)):
    new_product = RepositoryProduct(db).create(product)
    return new_product


@router.put("/products")
def update_product(product: Product, db: Session = Depends(get_db)):
    updated_product = RepositoryProduct(db).update_product(product)
    return updated_product


@router.delete("/products/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    RepositoryProduct(db).remove(product_id)
    return {"message": "Produto removido!"}
