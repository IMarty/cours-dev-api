from typing import Optional
from fastapi import FastAPI, Body, HTTPException, Response, status
from pydantic import BaseModel

import psycopg2
from psycopg2.extras import RealDictCursor

# Connexion DB
connexion = psycopg2.connect(
    host="dpg-ci8rn3h8g3nfuca2vvc0-a.frankfurt-postgres.render.com",
    database="shop_wapi_render",
    user="igor_render",
    password="5lGQuN1kIVPqR4x6GD7a7Z7EpW9ja2GQ",
    cursor_factory=RealDictCursor
)
cursor= connexion.cursor()



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
    # Requete SQL
    cursor.execute("SELECT * FROM product")
    dbProducts= cursor.fetchall()
    return {
        "products": dbProducts,
        "limit": 10,
        "total": 2,
        "skip":0
    }
    
# Data Models / Schema / DTO
class Product (BaseModel):
    productName: str
    productPrice: float # datatypes : https://docs.pydantic.dev/latest/usage/types/
    # availability: bool = True # default / optionel
    # rating: Optional[int] # Completement optionnel


@app.post("/products")
async def create_post(payload: Product, response:Response):
    print(payload.productName)
    cursor.execute("INSERT INTO product (name, price) VALUES (%s,%s) RETURNING *;", (payload.productName, payload.productPrice))
    connexion.commit() # Save in the DB (Comme F6 dans PGAdmin)
    response.status_code = status.HTTP_201_CREATED
    return {"message":f"New watch added sucessfully : {payload.productName}"} 


@app.get("/products/{product_id}")
async def get_product(product_id: int, response:Response):
    try: 
        cursor.execute(f"SELECT * FROM product WHERE id={product_id}")
        corresponding_product = cursor.fetchone()
        if (corresponding_product):
            return corresponding_product
        else:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )
    except:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )


@app.put("/products/{product_id}")
async def update_product(product_id: int,payload: Product):
    cursor.execute(
        'UPDATE product SET name=%s, price=%s WHERE id=%s RETURNING *;',
        (payload.productName, payload.productPrice, product_id )
    )
    # test= cursor.fetchone()
    # print(test)
    connexion.commit()

    return {"message":f"Watch sucessfully updated: {payload.productName}"} 
@app.delete('/products/{product_id}')
async def delete_product(product_id:int):
    cursor.execute(
        "DELETE FROM product WHERE id=%s RETURNING *;",
        (product_id,) # don't touch this code, it work and I don't know why
    )
    connexion.commit()
    return {"message":f"Watch deleted updated"} 