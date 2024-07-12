from typing import Annotated, Any
from pydantic import BaseModel, EmailStr
from fastapi import Form
from datetime import datetime

class UsersShemas(BaseModel):
    username: str 
    password: bytes | str
    email: EmailStr 
    active: bool = True

class AnswerConvertCurrencies(BaseModel):
    input_data: dict[str,Any]
    result: float
    rate: float

class AnswerActualCurrencies(BaseModel):
    base: str
    date: datetime
    rates: dict[str, float]

class AnswerListCurrencies(BaseModel):
    answer: dict[str,str]
