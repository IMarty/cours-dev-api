from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from classes.database import get_cursor
from classes import models_orm

router= APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

# Exercice  post a new transaction
@router.get('')
async def list_transactions(cursor: Session = Depends(get_cursor)):
    all_transactions = cursor.query(models_orm.Transactions).all()
    return all_transactions # data format à ajuster cela besoin

# Exercice get all transactions
@router.post('', status_code=status.HTTP_201_CREATED)
async def create_transaction(cursor: Session = Depends(get_cursor)):
    new_transaction= models_orm.Transactions(customer_id=1, product_id=1)
    cursor.add(new_transaction)
    cursor.commit()
    cursor.refresh(new_transaction)
    return {'message' : f'New transaction added on {new_transaction.transaction_date} with id:{new_transaction.id}' }
