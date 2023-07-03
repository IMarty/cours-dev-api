from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

#Used during the Signup operation
def hash_password(clear_password:str):
    return pwd_context.hash(clear_password)


# Used during the Login / Auth operation
def verify_password(given_password, hashed_password):
    return pwd_context.verify(given_password, hashed_password)