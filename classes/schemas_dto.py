from datetime import datetime
from pydantic import BaseModel
# DTO : Data Transfert Object


class Product_POST_Body (BaseModel):
    productName: str
    productPrice: float


class Product_PATCH_Body (BaseModel):
    newFeatured: bool

class Product_GETID_Response(BaseModel):
    id: int
    name: str
    price: str
    featured: bool
    class Config:
        orm_mode= True

class Customer_POST_Body (BaseModel):
    customerEmail:str
    customerPassword: str

class Customer_response (BaseModel):
    id: int
    email:str
    create_at: datetime
    # not sending the password
    class Config: # Importante pour la traduction ORM->DTO
        orm_mode= True