from typing import Optional, Union

from resources.user import User

class UserTable:

    def __init__(self):
        self._user_data = [
            User(
                id=1,
                first_name="Rory",
                last_name="Houlihan",
                email="rhoulihan@email.com",
                created_ts="2022-01-01",
                updated_ts=None
            ),
            User(
                id=2,
                first_name="Fiona",
                last_name="Gaze",
                email='fionagaze@email.com',
                created_ts="2022-01-01",
                updated_ts=None
            )
        ]

    def select(self, id: Optional[int]=None) -> Union[User, list[User]]:
        if id:
            print(id)
            id = int(id)
            result = [
                user
                for user in self._user_data
                if user.id == id
            ]
            return result
        else:
            return self._user_data

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
