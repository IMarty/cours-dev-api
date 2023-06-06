from typing import Optional
from fastapi import FastAPI, Body, HTTPException, Response, status
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
async def create_post(payload: Product, response:Response):
    print(payload.productName)
    productsList.append(payload.dict())
    response.status_code = status.HTTP_201_CREATED
    return {"message":f"New watch added sucessfully : {payload.productName}"} 


@app.get("/products/{product_id}")
async def get_product(product_id: int, response:Response):
    try: 
        corresponding_product = productsList[product_id - 1] #parce id commence à 1 et index commence à 0
        return corresponding_product
    except:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
