from pydantic import BaseModel,Field


class LoginRequest(BaseModel):
    unique_Code:int = Field(...,ge=1000,le=9999)
    password: str = Field(min_length=5)

class TokenResponse(BaseModel):
    access_token: str = Field(...)
    token_type: str = "bearer"