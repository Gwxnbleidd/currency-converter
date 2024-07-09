from sqlalchemy import select
from fastapi import HTTPException, status

import sys
sys.path.append('/home/dmitry/Учеба/FastAPI проекты/Конвертатор валют')
from app.database.engine import engine,Base, session_factory
from app.database.model import UsersTable
from app.api.shemas import UsersShemas

def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def add_user(credentials: UsersShemas):
    with session_factory() as session:
        # Проверяем есть ли такой пользователь
        query = select(UsersTable.username).select_from(UsersTable).filter_by(username = credentials.username)
        res = session.execute(query)
        if not res.fetchone():
            session.add(UsersTable(username=credentials.username, hashed_password=credentials.password, email=credentials.email, active=credentials.active))
            session.commit()
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='A user with the same name already exists!')

def get_user_from_db(name: str):
    with session_factory() as session:
        res = session.execute(select('*').select_from(UsersTable).filter_by(username=name))
        user = res.fetchone()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
        else:
            return UsersShemas(username = user.username, password = user.hashed_password, email=user.email, active=user.active)
