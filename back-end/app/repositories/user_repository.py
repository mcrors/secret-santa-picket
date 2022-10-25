from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from data_access.db_schema import DatabaseEngine

from models.user import User


class UserRepository:

    def __init__(self):
        self._db_engine = DatabaseEngine.get_database_engine()

    def add(self, user: User) -> User:
        session = Session(self._db_engine)
        session.add(user)
        session.flush()
        session.commit()
        return User(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            created_date=user.created_date
        )

    def list(self) -> List[User]:
        session = Session(self._db_engine)
        stmt = select(User)
        result = []
        for user in session.execute(stmt):
            result.append(user[0])
        return result

    def update(self, user: User) -> None:
        pass

    def get(self, id: int) -> User:
        pass

    def delete(self, user: User) -> None:
        pass

