
from fastapi import FastAPI

# Documentation
from documentation.description import api_description
from documentation.tags import tags_metadata


# Database 
from classes.database import database_engine 
import classes.models_orm # Import des ORM

#Import des routers
import routers.router_products, routers.router_customers, routers.router_transactions, routers.router_auth

# Créer les tables si elles ne sont pas présente dans la DB
classes.models_orm.Base.metadata.create_all(bind=database_engine)





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