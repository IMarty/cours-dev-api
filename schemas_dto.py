from datetime import datetime
from pydantic import BaseModel
# DTO : Data Transfert Object


class Product_POST_Body (BaseModel):
    productName: str
    productPrice: float


class Product_PATCH_Body (BaseModel):
    newFeature: bool

class Customer_POST_Body (BaseModel):
    customerEmail:str
    customerPassword: str

class Customer_response (BaseModel):
    id: int
    email:str
    create_at: datetime
    class Config: # Importante pour la traduction ORM->DTO
        orm_mode= True