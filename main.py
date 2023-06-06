from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI() #variable names for the server

@app.get("/")
async def root():
    return {"message":"coucou les amis"}

productsList = [
            {"productName":"Rolex Submariner", "productPrice":11130},
            {"productName":"Ulysse Nardin Dual Time", "productPrice":6015}
        ]

@app.get("/products")
async def getProducts():
    return {
        "products": productsList,
        "limit": 10,
        "total": 2,
        "skip":0
    }
    
# Data Models / Schema / DTO
class Product (BaseModel):
    productName: str
    productPrice: float # datatypes : https://docs.pydantic.dev/latest/usage/types/
    availability: bool = True # default / optionel
    rating: Optional[int] # Completement optionnel


@app.post("/products")
async def create_post(payload: Product):
    print(payload.productName)
    productsList.append(payload.dict())
    return {"message":f"New watch added sucessfully : {payload.productName}"} 