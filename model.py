from sqlalchemy.orm import mapped_column, Mapped

from app.database.engine import Base

class UsersTable(Base):
    __tablename__ = 'users'

    id: Mapped[int] =  mapped_column(primary_key= True)
    username: Mapped[str]
    hashed_password: Mapped[bytes]
    email: Mapped[str]
    active: Mapped[bool]

