from typing import List

from sqlalchemy import select, update
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session

from data_access.db_schema import DatabaseEngine
from errors.secret_santa_exceptions import UserNotFoundError
from models.user import User


class UserRepository:

    def __init__(self):
        self._db_engine = DatabaseEngine.get_database_engine()

    def add(self, user: User) -> User:
        with Session(self._db_engine) as session:
            session.add(user)
            session.flush()
            session.commit()
            return User(
                id=user.id,
                public_id=user.public_id,
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                created_date=user.created_date
            )

    def list(self) -> List[User]:
        with Session(self._db_engine) as session:
            stmt = select(User)
            result = []
            for user in session.execute(stmt):
                result.append(user[0])
        return result

    def update(self, user: User) -> User:
        with Session(self._db_engine) as session:
            rowcount = session.execute(
                update(User)
                .where(User.public_id == user.public_id)
                .values(
                    email=user.email,
                    first_name=user.first_name,
                    last_name=user.last_name
                )
            ).rowcount
            if rowcount > 0:
                session.flush()
                session.commit()
                return user
            else:
                raise UserNotFoundError(
                    f"The user {user} was not found in the database"
                )

    def get(self, public_id: str) -> User | None:
        with Session(self._db_engine) as session:
            stmt = select(User).where(User.public_id == public_id)
            user = session.execute(stmt).first()
            return user[0] if user else None

    def get_user_by_email(self, email: str) -> User | None:
        with Session(self._db_engine) as session:
            stmt = select(User).where(User.email == email)
            user = session.execute(stmt).first()
            return user[0] if user else None

    def delete(self, user: User) -> User:
        with Session(self._db_engine) as session:
            try:
                session.delete(user) # what error is thrown if the user doesn't exist, or if user is not of type user
                session.flush()
                session.commit()
                return user
            except InvalidRequestError as exc:
                raise UserNotFoundError(
                    f"The user {user} could not be found in the database"
                )

