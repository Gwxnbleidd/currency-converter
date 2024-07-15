from typing import Annotated
from fastapi import (APIRouter, Response, Request, 
                     HTTPException, status, Depends)
from fastapi.security import OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
import bcrypt

from app.api.shemas import UsersShemas, RegisterForm
from app.core.security import create_jwt_token, decode_jwt_token
from app.database.orm import add_user, get_user_from_db

COOKIE_KEY = 'cookie_for_auth'
auth_rout = APIRouter(prefix='/auth')


def hash_password(password: bytes):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)

def get_user_from_token(request: Request, response: Response):
    try:
        token = request.cookies.get(COOKIE_KEY)
        payload = decode_jwt_token(token)
        username = payload.get('sub')
        if username:
            if payload.get('active'):
                return username
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='The user is blocked')        
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
    except InvalidTokenError:
        request.cookies.pop(COOKIE_KEY)
        response.delete_cookie(COOKIE_KEY)
        # разобраться что не так
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')


@auth_rout.post('/register')
def register_user(creditials: Annotated[RegisterForm, Depends()]):
    creditials.password = hash_password(bytes(creditials.password, encoding='utf-8'))
    add_user(creditials)
    return {f'Welcome, {creditials.username}'}

@auth_rout.post('/login')
def login_user(response: Response, creditials: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = get_user_from_db(creditials.username)
    creditials.password = bytes(creditials.password, encoding='utf-8')
    if bcrypt.checkpw(creditials.password, user.password):
        token = create_jwt_token({'sub': user.username, 'email': user.email, 'active': user.active})
        response.set_cookie(COOKIE_KEY, token)
        return {'message': 'Successfull!'}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect password!')