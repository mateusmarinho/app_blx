from sqlalchemy import update, delete
from sqlalchemy.orm import Session

from backend.src.schemas import schemas
from backend.src.infra.sqlalchemy.models import models


class RepositoryProduct():
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: schemas.Product):
        db_product = models.Product(
            name=product.name,
            details=product.details,
            price=product.price,
            is_available=product.is_available,
            dimensions=product.dimensions,
            user_id=product.user_id,
        )

        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)

        return db_product

    def get_all(self):
        products = self.db.query(models.Product).all()
        return products

    def update_product(self, product: schemas.Product):
        stmt = (
            update(models.Product)
            .where(models.Product.id == product.id)
            .values(
                name=product.name,
                details=product.details,
                price=product.price,
                is_available=product.is_available,
                dimensions=product.dimensions,
                user_id=product.user_id,
            )
        )
        
        self.db.execute(stmt)
        self.db.commit()

        return product

    def remove(self, product_id: int):
        stmt = delete(models.Product).where(models.Product.id == product_id)
        self.db.execute(stmt)
        self.db.commit()
