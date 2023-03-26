from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from backend.src.infra.sqlalchemy.config.database import Base


class User(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    phone = Column(String)
    products = relationship("Product", back_populates="user")


# A classe aqui funcona como uma instância de um modelo do ORM 
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    is_available = Column(Boolean)
    dimensions = Column(String)
    user_id = Column(Integer, ForeignKey("usuarios.id", name="fk_usuario"))
    user = relationship("User", back_populates="products")
