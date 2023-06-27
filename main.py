
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import models
from database import get_cusor, database_engine


# Créer les tables si elles ne sont pas présente dans la DB
models.Base.metadata.create_all(bind=database_engine)

app= FastAPI()



@app.get('/products')
async def get_products(cursor: Session= Depends(get_cusor)):
    print(cursor.query(models.Products))
    all_products = cursor.query(models.Products).all()
    return {
        "products": all_products,
        "limit": 10,
        "total": 2,
        "skip":0
    } 