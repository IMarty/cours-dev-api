
from fastapi import FastAPI

import models_orm # Import des ORM
from database import database_engine # import du cursor/session de la DB

#Import des routers
import router_products

# Créer les tables si elles ne sont pas présente dans la DB
models_orm.Base.metadata.create_all(bind=database_engine)

#Lancement de l'API
app= FastAPI()

# Ajouter les routers dédiés
app.include_router(router_products.router)