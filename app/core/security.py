import bcrypt
from datetime import datetime,timedelta
from jose import jwt
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer

import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM  = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

#Generates the hashed password
def hash_password(password:str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


#Validates the password
def verify_password(plain:str, hashed:str) -> bool:
    return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))

def create_access_token(data:dict)-> str:
    data_copiado = data.copy()
    data_expiracao = (datetime.utcnow() + timedelta(minutes=30))
    data_copiado["exp"] = data_expiracao
    return jwt.encode(data_copiado,SECRET_KEY,algorithm=ALGORITHM)
    
