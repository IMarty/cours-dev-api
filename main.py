
from fastapi import FastAPI

import classes.models_orm # Import des ORM
from classes.database import database_engine # import du cursor/session de la DB

#Import des routers
import routers.router_products, routers.router_customers, routers.router_transactions, routers.router_auth

# Créer les tables si elles ne sont pas présente dans la DB
classes.models_orm.Base.metadata.create_all(bind=database_engine)

api_description = description = """
Watch API helps you do awesome stuff. 🚀

## Products

You will be able to:

* Create new product.
* Get products list.

## Customer 
You'll be able to signup and login

## Transaction
You'll be able to list and create transactions
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
    {
        "name": "Customers",
        "description": "Create and list customers of our API",
    },
    {
        "name": "Transactions",
        "description": "Create and list customer's transactions",
    },
]

#Lancement de l'API
app= FastAPI( 
    title="Watches API",
    description=api_description,
    openapi_tags=tags_metadata # tagsmetadata definit au dessus
    )

# Ajouter les routers dédiés
app.include_router(routers.router_products.router)
app.include_router(routers.router_customers.router)
app.include_router(routers.router_transactions.router)
app.include_router(routers.router_auth.router)