from typing import Optional
from fastapi import FastAPI, Body, HTTPException, Response, status
from pydantic import BaseModel

# Description
api_description = description = """ 
Watch API helps you do awesome stuff. 

## Products

You will be able to :
* Create new product.
* Get products list.
"""

# Liste des tags utilises dans la doc
tags_metadata = [
    {
        "name" : "Products",
        "description" : " Manage Products. So _Fancy_ they have their own docs.",
        "externalDocs" : {
            "description" :"Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]


app = FastAPI(
    title="Watch API",
    description=api_description,
    openapi_tags=tags_metadata # tagsmetadat est defnit au dessus
) #variable names for the server

@app.get("/")
async def root():
    return {"message":"coucou les amis"}

productsList = [
            {"productName":"Rolex Submariner", "productPrice":11130},
            {"productName":"Ulysse Nardin Dual Time", "productPrice":6015}
        ]

@app.get("/products", tags=["Products"])
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


@app.post("/products", tags=["Products"])
async def create_post(payload: Product, response:Response):
    print(payload.productName)
    productsList.append(payload.dict())
    response.status_code = status.HTTP_201_CREATED
    return {"message":f"New watch added sucessfully : {payload.productName}"} 


@app.get("/products/{product_id}", tags=["Products"])
async def get_product(product_id: int, response:Response):
    try: 
        corresponding_product = productsList[product_id - 1] #parce id commence à 1 et index commence à 0
        return corresponding_product
    except:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
# DELETE : base du endpoint

@app.delete("/products/{product_id}", tags=["Products"])
async def delete_product(product_id: int, response:Response): 
    try: 
        productsList.pop(product_id -1)
        response.status_code = status.HTTP_204_NO_CONTENT
        return
    except:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail = "Prodcut not found"
        )

#PUT (ajoputer mais sur exister -> remplacer)

@app.put("/products/{product_id}", tags=["Products"])
async def replace_product(product_id: int, payload: Product, response:Response ):
    try: 
        productsList[product_id - 1] = payload.dict()
        return {"message" : f"Watch updated successfully : {payload.productName}"}
    except:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="Product not found"

        )
        