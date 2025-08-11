from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)

class LoginResponse(BaseModel):
    ok: bool

class Message(BaseModel):
    message: str