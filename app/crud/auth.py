from app.schemas.auth import LoginRequest
from sqlalchemy.orm import Session
from app.core.security import verify_password, create_access_token
from app.database.models import User
from fastapi import HTTPException

def response_token_validator(request:LoginRequest,db:Session,):
    user = db.query(User).filter(User.unique_Code == request.unique_Code).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    correct_password = verify_password(request.password, user.hashed_password)

    if not correct_password:
        raise HTTPException(status_code=401, detail="Incorrect Password")

    return create_access_token({"sub": str(user.id)})
