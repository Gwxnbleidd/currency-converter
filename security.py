import jwt
from datetime import datetime, timedelta
from app.core.config import SECRET_KEY,ALGORITHM

def create_jwt_token(payload: dict):
    on_decode = payload.copy()
    expired_time = datetime.utcnow() + timedelta(minutes=1)
    on_decode['exp'] = expired_time
    return jwt.encode(on_decode, SECRET_KEY, ALGORITHM)

def decode_jwt_token(token):
    return jwt.decode(token, SECRET_KEY, ALGORITHM)