from functools import wraps

from errors.secret_santa_exceptions import InvalidVersionError


VALID_VERSIONS = ["1"]


def check_version(func: callable):

    @wraps(func)
    def wrapper(*pargs, **kwargs):
        if "version" in kwargs.keys():
            if _is_valid_version(kwargs["version"]):
                func(*pargs, **kwargs)
            else:
                raise InvalidVersionError(422)
    return wrapper


def _is_valid_version(version: str):
    return version in VALID_VERSIONS
