from fastapi import APIRouter, HTTPException, status, Depends
from classes import schemas_dto, database, models_orm
from sqlalchemy.orm import Session
import utilities

router = APIRouter(
    prefix='/auth',
    tags=["Auth"]
)


@router.post('', status_code=status.HTTP_201_CREATED)
async def auth_customer(payload : schemas_dto.Auth_Customer_POST, cursor: Session= Depends(database.get_cursor)):
    # 1. Recup les crédentials
    corresponding_customer = cursor.query(models_orm.Customers).filter(models_orm.Customers.email == payload.email).first()
    # 2. Vérifier dans la DB si user exist
    if(not corresponding_customer):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='email not good'
        )
    # 3. Vérif sur passwork hashé (Bad practice (normalement 404 dans les deux cas))
    valid_pwd = utilities.verify_password(
        payload.password,
        corresponding_customer.password
    )
    if(not valid_pwd):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='password not good' 
        ) 
    # 4. Génération du JWT
    token = utilities.generate_token(corresponding_customer.id)
    return token