import datetime
from sqlalchemy.orm import Session
from models.user import User


def test_can_get_user_objects_from_database(session: Session):
    created_date = datetime.datetime(2022, 1, 1, 12, 0)
    session.execute(
        "INSERT into users (id, first_name, last_name, email, created_date) VALUES "
        '(1, "rory", "houlihan", "rhoulihan@email.com", "2022-01-01 12:00:00")'
    )
    expected = [
        User(
            id=1,
            first_name="rory",
            last_name="houlihan",
            email="rhoulihan@email.com",
            created_date=created_date
        )
    ]
    result = session.query(User).all()
    assert result == expected

