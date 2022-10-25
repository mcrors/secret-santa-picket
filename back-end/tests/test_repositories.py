from sqlalchemy.engine.base import Engine
from models.user import User
from repositories.user_repository import UserRepository


def test_can_add_user_to_repository(engine_with_schema: Engine)  -> None:
    user = User(
        first_name='Rory',
        last_name='Houlihan',
        email='rhoulihan@protonamil.com'
    )
    user_repository = UserRepository()
    user_from_db = user_repository.add(user)
    assert user_from_db.id == 1

