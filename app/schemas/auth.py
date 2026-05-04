from pydantic import BaseModel,Field


class LoginRequest(BaseModel):
    name:str = Field(min_length=4)
    password: str = Field(min_length=5)

class TokenResponse(BaseModel):
    access_token: str = Field(...)
    token_type: str = "bearer"