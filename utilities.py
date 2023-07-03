from passlib.context import CryptContext
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"])

#Used during the Signup operation
def hash_password(clear_password:str):
    return pwd_context.hash(clear_password)


# Used during the Login / Auth operation
def verify_password(given_password, hashed_password):
    return pwd_context.verify(given_password, hashed_password)

# Used during Auth / Login
def generate_token(given_id:int):
    algo = "HS256"
    payload = {"customer_id": given_id}
    secret = "5ae48e781d227cabc077167f64005ff949922d586157d6ae07078fee3f3ad170"
    encoded_jwt = jwt.encode(payload, secret, algorithm=algo)
    print(encoded_jwt)
    return encoded_jwt


