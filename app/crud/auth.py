from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt,JWTError
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.core.security import verify_password, create_access_token, oauth2_scheme, SECRET_KEY
from app.database.models import User
from fastapi import HTTPException

def response_token_validator(form: OAuth2PasswordRequestForm, db: Session):
    user = db.query(User).filter(User.unique_Code == int(form.username)).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    correct_password = verify_password(form.password, user.hashed_password)

    if not correct_password:
        raise HTTPException(status_code=401, detail="The User unique Code or Password is wrong")

    return create_access_token({"sub": str(user.id)})


def get_current_user(token:str = Depends(oauth2_scheme),db:Session=Depends(get_db))->User:

    try:
        pyload = jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
        user_id = pyload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    user = db.query(User).filter(User.id == int(user_id)).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user
