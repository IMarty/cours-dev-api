from typing import Optional
from pydantic import BaseModel
# DTO : Data Transfert Object

class Product_POST_Body (BaseModel):
    productName: str
    productPrice: float

class Product_PATCH_Body (BaseModel):
    newFeature: bool