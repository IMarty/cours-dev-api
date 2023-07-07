from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from classes import models_orm, schemas_dto, database
import utilities
from typing import List


router = APIRouter(
    prefix='/customers',
    tags=['Customers']
)

@router.post('', response_model=schemas_dto.Customer_response, status_code= status.HTTP_201_CREATED)
async def create_customer(
    payload: schemas_dto.Customer_POST_Body, 
    cursor: Session = Depends(database.get_cursor),
    ):
    try: 
        # 1. On ne stock pas le mot de pass "en claire" mais le hash
        hashed_password = utilities.hash_password(payload.customerPassword) 
        # 2. Creation d'un object ORM pour être injecté dans la DB 
        new_customer= models_orm.Customers(password=hashed_password, email= payload.customerEmail)
        # 3. Send query
        cursor.add(new_customer) 
        # 4. Save the staged changes
        cursor.commit() 
        # Pour obtenir l'identifiant
        cursor.refresh(new_customer) 
        return new_customer # not a python dict -> donc il faut un mapping
    except IntegrityError: # Se déclanche si un utilisateur possède déjà la même email (unique=True)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists" 
        )
    
@router.get('', response_model=List[schemas_dto.Customer_response])
async def get_all_customers(cursor: Session = Depends(database.get_cursor)):
    all_customers = cursor.query(models_orm.Customers).all()
    return all_customers

# Exercice not an actual use case
@router.get('/{customer_id}', response_model=schemas_dto.Customer_response)
async def get_user_by_id(customer_id:int, cursor: Session = Depends(database.get_cursor)):
    corresponding_customer = cursor.query(models_orm.Customers).filter(models_orm.Customers.id == customer_id).first()
    if(corresponding_customer):
        return corresponding_customer
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'No user with id:{customer_id}'
        )