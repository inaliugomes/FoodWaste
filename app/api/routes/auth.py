from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.crud.auth import response_token_validator
from app.database.connection import get_db
from app.schemas.auth import TokenResponse

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/login", response_model=TokenResponse)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = response_token_validator(form, db)

    return {"access_token": token, "token_type": "bearer"}