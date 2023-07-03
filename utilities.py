from passlib.context import CryptContext
from jose import jwt, JWTError

# Mise en place du bouton d'authentification
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth')


pwd_context = CryptContext(schemes=["bcrypt"])

#Used during the Signup operation
def hash_password(clear_password:str):
    return pwd_context.hash(clear_password)


# Used during the Login / Auth operation
def verify_password(given_password, hashed_password):
    return pwd_context.verify(given_password, hashed_password)

# Used during Auth / Login
algo = "HS256"
secret = "5ae48e781d227cabc077167f64005ff949922d586157d6ae07078fee3f3ad170"

def generate_token(given_id:int):
    payload = {"customer_id": given_id}
    encoded_jwt = jwt.encode(payload, secret, algorithm=algo)
    print(encoded_jwt)
    return encoded_jwt


def decode_token(given_token:str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(given_token, secret, algorithms=algo)
        decoded_id = payload.get('customer_id')
    except JWTError :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )   
    return decoded_id