from typing import Annotated
from fastapi import (APIRouter, Response, Request, 
                     HTTPException, status, Depends)
from fastapi.security import OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
import bcrypt

from app.api.shemas import UsersShemas
from app.core.security import create_jwt_token, decode_jwt_token

COOKIE_KEY = 'cookie_for_auth'
auth_rout = APIRouter(prefix='/auth')

db = []
sessions = {}

def hash_password(password: bytes):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)
    

def get_user_from_db(username: str):
    for user in db:
        if user.username == username:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

def get_user_from_token(request: Request):
    try:
        token = request.cookies.get(COOKIE_KEY)
        payload = decode_jwt_token(token)
        user = payload.get('sub')
        if user:
            return user
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
    except InvalidTokenError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Invalid token: {e}')

@auth_rout.post('/register')
def register_user(creditials: UsersShemas):
    creditials.password = hash_password(bytes(creditials.password))
    db.append(creditials)
    return {f'Welcome, {creditials.username}'}

@auth_rout.post('/login')
def login_user(response: Response, creditials: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = get_user_from_db(creditials.username)
    creditials.password = bytes(creditials.password, encoding='utf-8')
    if bcrypt.checkpw(creditials.password, user.password):
        token = create_jwt_token({'sub': user.username, 'email': user.email})
        sessions[token] = user
        response.set_cookie(COOKIE_KEY, token)
        return {'message': 'Successfull!'}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect password!')