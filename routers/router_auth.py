from fastapi import APIRouter, HTTPException, status, Depends
from classes import schemas_dto, database, models_orm
from sqlalchemy.orm import Session
import utilities

# Formulaire de lancement du OAuth /auth
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/auth',
    tags=["Auth"]
)


@router.post('', status_code=status.HTTP_201_CREATED)
async def auth_customer(
        payload : OAuth2PasswordRequestForm= Depends(), 
        cursor: Session= Depends(database.get_cursor)
    ):
    print(payload.__dict__)
    # 1. Recup les crédentials (username car il provient du formulaire par default de FastAPI)
    corresponding_customer = cursor.query(models_orm.Customers).filter(models_orm.Customers.email == payload.username).first()
    # 2. Vérifier dans la DB si user exist
    if(not corresponding_customer):
         raise HTTPException(
             status_code=status.HTTP_404_NOT_FOUND,
             detail='email not good'
         )
    # # 3. Vérif sur passwork hashé (Bad practice (normalement 404 dans les deux cas))
    valid_pwd = utilities.verify_password(
        payload.password,
        corresponding_customer.password
     )
    if(not valid_pwd):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='password not good' 
        ) 
    # # 4. Génération du JWT
    token = utilities.generate_token(corresponding_customer.id)
    print(token)
    return token