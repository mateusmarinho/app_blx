from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from backend.src.schemas.schemas import Product, User, SimpleUser
# from backend.src.schemas.user import User
# from backend.src.schemas.product import Product
from backend.src.infra.sqlalchemy.repositories.product import RepositoryProduct
from backend.src.infra.sqlalchemy.repositories.user import RepositoryUser
from backend.src.infra.sqlalchemy.config.database import create_db, get_db

create_db()

app = FastAPI()

# CORS
origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.delete("/products/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    RepositoryProduct(db).remove(product_id)
    return {"message": "Produto removido!"}


# Users routes
@app.get("/users", response_model=list[SimpleUser])
def get_all_users(db: Session = Depends(get_db)):
    users = RepositoryUser(db).get_all()
    return users


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=SimpleUser)
def create_user(user: User, db: Session = Depends(get_db)):
    new_user = RepositoryUser(db).create(user)
    return new_user
