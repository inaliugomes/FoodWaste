from passlib.context import CryptContext

myctx = CryptContext(schemes=["bcrypt"])

def hash_password(password:str):

    return myctx.hash(password)


def verify_password(plain:str, hashed:str):
    
    return myctx.verify(plain,hashed)


