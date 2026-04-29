from passlib.context import CryptContext
from datetime import datetime,timedelta
from jose import jwt
from dotenv import load_dotenv

import os

load_dotenv()
myctx = CryptContext(schemes=["bcrypt"])

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM  = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def hash_password(password:str):

    return myctx.hash(password)


def verify_password(plain:str, hashed:str):
    
    return myctx.verify(plain,hashed)

def create_access_token(data:dict)-> str:
    data_copiado = data.copy()
    data_expiracao = (datetime.utcnow() + timedelta(minutes=30))
    data_copiado["exp"] = data_expiracao
    return jwt.encode(data_copiado,SECRET_KEY,algorithm=ALGORITHM)
    
