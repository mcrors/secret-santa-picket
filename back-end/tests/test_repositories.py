import pytest
from sqlalchemy.engine.base import Engine

from errors.secret_santa_exceptions import UserNotFoundError
from models.user import User
from repositories.user_repository import UserRepository


@pytest.fixture
def user_john_smith():
    return User(first_name='John', last_name='Smith', email='smithy@email.com')


def test_can_add_user_to_repository(
    engine_with_schema: Engine, user_john_smith: User
)  -> None:
    user_repository = UserRepository()
    user_from_db = user_repository.add(user_john_smith)
    assert user_from_db.id == 1
    assert user_from_db.public_id == user_john_smith.public_id


def test_list_all_users_is_empty_list_when_no_users_have_been_added(
    engine_with_schema: Engine
) -> None:
    user_repository = UserRepository()
    result = user_repository.list()
    assert len(result) == 0


def test_can_get_user_by_public_id(
    engine_with_schema: Engine, user_john_smith: User
) -> None:
    user_repository = UserRepository()
    user_repository.add(user_john_smith)
    retrieved_user = user_repository.get(user_john_smith.public_id)
    assert user_john_smith == retrieved_user


def test_can_update_user_data(
    engine_with_schema: Engine, user_john_smith: User
) -> None:
    user_repository = UserRepository()
    user_repository.add(user_john_smith)
    user_john_smith.first_name='Steve'
    user_repository.update(user_john_smith)
    retrieved_user = user_repository.get(user_john_smith.public_id)
    assert retrieved_user.first_name == 'Steve'


def test_can_delete_user_from_repository(
    engine_with_schema: Engine, user_john_smith: User
) -> None:
    user_repository = UserRepository()
    user_repository.add(user_john_smith)
    user_repository.delete(user_john_smith)
    retrieved_user = user_repository.get(user_john_smith.public_id)
    assert retrieved_user is None


def test_delete_user_that_doesnt_exist_raises_user_not_found_error(
    engine_with_schema: Engine, user_john_smith: User
) -> None:
    user_repository = UserRepository()
    with pytest.raises(UserNotFoundError):
        user_repository.delete(user_john_smith)


def test_update_user_that_doesnt_exist_raises_user_not_found_error(
    engine_with_schema: Engine, user_john_smith: User
) -> None:
    user_repository = UserRepository()
    with pytest.raises(UserNotFoundError):
        user_repository.update(user_john_smith)


def test_can_handle_none_type(engine_with_schema: Engine) -> None:
    user_repository = UserRepository()
    not_a_user = User(first_name='rory', last_name='houlihan', email='asjdfklsa@fjkdlsa.com')
    second_time = User(first_name='rory', last_name='houlihan', email='asjdfklsa@fjkdlsa.com')
    user_repository.add(not_a_user)
    the_one_we_look_for = None
    for user in user_repository.list():
        if user.email == second_time.email:
            the_one_we_look_for = user
            break
    user_repository.delete(the_one_we_look_for)

