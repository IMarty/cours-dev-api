
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session 

import models # Import des ORM
from database import get_cusor, database_engine # import du cursor/session de la DB


# Créer les tables si elles ne sont pas présente dans la DB
models.Base.metadata.create_all(bind=database_engine)

app= FastAPI()


# Read
@app.get('/products')
async def get_products(cursor: Session= Depends(get_cusor)):
    print(cursor.query(models.Products)) # Requète SQL générée
    all_products = cursor.query(models.Products).all() # Lancement de la requête
    return {
        "products": all_products,
        "limit": 10,
        "total": 2,
        "skip":0
    }

# Exercice :  @app.get('/products/{product_id}')
# db.query(models.BlogPosts).filter(models.BlogPosts.id == blog_id).first()
# Connecter à votre propre Database URL

# CREATE / DELETE / UPDATE