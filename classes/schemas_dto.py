from datetime import datetime
from pydantic import BaseModel

# DTO : Data Transfert Object ou Schema
# Représente la structure de la données (data type) en entrée ou en sortie de notre API.

class Product_POST_Body (BaseModel):
    productName: str
    productPrice: float

class Product_PATCH_Body (BaseModel):
    newFeatured: bool

class Product_GETID_Response(BaseModel): # format de sortie (response)
    id: int
    name: str
    price: str
    featured: bool
    class Config: # Lors des réponses, nous avons souvant à utiliser les données sortie de notre database. La Config ORM nous permet de "choisir" les columnes à montrer. 
        orm_mode= True

class Customer_POST_Body (BaseModel):
    customerEmail:str
    customerPassword: str

class Customer_response (BaseModel): 
    id: int
    email:str
    create_at: datetime
    # not sending the password
    class Config: # Importante pour la traduction ORM -> DTO
        orm_mode= True      
        