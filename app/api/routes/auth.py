from fastapi import APIRouter


router = APIRouter(
    prefix="/auth/login",
    tags=["auth"],
)
