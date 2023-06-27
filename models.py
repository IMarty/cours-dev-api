from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

# Class de base pour créer les models
Base= declarative_base()

class Products(Base):
    __tablename__= "product"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)
    featured = Column(Boolean, nullable=True, server_default='TRUE')
    created_at= Column(TIMESTAMP(timezone=True), nullable=False, server_default='now()')