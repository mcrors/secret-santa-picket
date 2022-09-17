from dataclasses import asdict
from functools import wraps
import json

from tornado.web import RequestHandler

from db_handlers.user_table import UserTable
from errors.secret_santa_exceptions import InvalidVersionError


VALID_VERSIONS = ["1"]


def is_valid_version(version: str):
    return version in VALID_VERSIONS


def check_version(func: callable):

    @wraps(func)
    def wrapper(*pargs, **kwargs):
        if "version" in kwargs.keys():
            if is_valid_version(kwargs["version"]):
                func(*pargs, **kwargs)
            else:
                raise InvalidVersionError(404)
    return wrapper


class UserHandler(RequestHandler):

    @check_version
    def get(self, version, user_id=None):
        print(f"user id is{user_id}")
        users = UserTable().select(user_id)
        if users:
            response = json.dumps([asdict(user) for user in users])
        else:
            response = json.dumps({"message": "user not found"})
        self.write(response)

