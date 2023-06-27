
from fastapi import FastAPI

import models_orm # Import des ORM
from database import database_engine # import du cursor/session de la DB

#Import des routers
import router_products

# Créer les tables si elles ne sont pas présente dans la DB
models_orm.Base.metadata.create_all(bind=database_engine)

api_description = description = """
Watch API helps you do awesome stuff. 🚀

## Products

You will be able to:

* Create new product.
* Get products list.
"""

# Liste des tags utilises dans la doc
tags_metadata = [
    {
        "name": "Products",
        "description": "Manage Products. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

#Lancement de l'API
app= FastAPI( 
    title="Watch API",
    description=api_description,
    openapi_tags=tags_metadata # tagsmetadata definit au dessus
    )

# Ajouter les routers dédiés
app.include_router(router_products.router)