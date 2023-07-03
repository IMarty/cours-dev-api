from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from classes.database import get_cursor
from classes import models_orm
import utilities
from sqlalchemy.exc import IntegrityError

#Ajout du schema Oauth
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")


router= APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

# Exercice  post a new transaction
@router.get('')
async def list_transactions(token: Annotated[str, Depends(oauth2_scheme)], cursor: Session = Depends(get_cursor)):
    all_transactions = cursor.query(models_orm.Transactions).all()
    return all_transactions # data format à ajuster cela besoin

# Exercice get all transactions
class transaction_post(BaseModel):
    product_id:int

@router.post('', status_code=status.HTTP_201_CREATED)
async def create_transaction(
    token: Annotated[str, Depends(oauth2_scheme)], # Sécurisation par Auth 
    payload:transaction_post,
    cursor: Session = Depends(get_cursor)
    ):
    decoded_customer_id = utilities.decode_token(token)
    new_transaction= models_orm.Transactions(customer_id=decoded_customer_id, product_id=payload.product_id)
    try : 
        cursor.add(new_transaction)
        cursor.commit()
        cursor.refresh(new_transaction)
        return {'message' : f'New transaction added on {new_transaction.transaction_date} with id:{new_transaction.id}' }
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='the given product does not exist'
        )