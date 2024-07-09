from pydantic import BaseModel, EmailStr

class UsersShemas(BaseModel):
    username: str
    password: bytes
    email: EmailStr
    active: bool = True
