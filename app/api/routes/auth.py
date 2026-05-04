from fastapi import APIRouter

from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.crud.auth import  response_token_validator
from app.database.connection import get_db
from app.schemas.auth import TokenResponse,LoginRequest

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest,db:Session=Depends(get_db)):
    token = response_token_validator(request,db)

    return  {"access_token":token,"token_type":"bearer"}