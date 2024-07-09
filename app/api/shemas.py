from typing import Annotated
from pydantic import BaseModel, EmailStr
from fastapi import Form

class UsersShemas(BaseModel):
    username: str 
    password: bytes | str
    email: EmailStr 
    active: bool = True
