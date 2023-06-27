from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import models_orm, schemas_dto, database, utilities

router = APIRouter(
    prefix='/customers',
)

@router.post('', response_model=schemas_dto.Customer_response, status_code= status.HTTP_201_CREATED)
async def create_customer(
    payload: schemas_dto.Customer_POST_Body, 
    cursor: Session = Depends(database.get_cursor),
    ):
    try: 
        hashed_password = utilities.hash_password(payload.customerPassword)
        new_customer= models_orm.Customers(password=hashed_password, email= payload.customerEmail)
        cursor.add(new_customer)
        cursor.commit()
        cursor.refresh(new_customer)
        # return {'message':f'The customer has been created with the id: {new_customer.id}'}
        return new_customer
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists" 
        )