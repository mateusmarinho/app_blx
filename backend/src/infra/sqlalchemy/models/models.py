from sqlalchemy import Column, Integer, String, Float, Boolean

from backend.src.infra.sqlalchemy.config.database import Base


# A classe aqui funcona como uma instância de um modelo do ORM 
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    is_available = Column(Boolean)
