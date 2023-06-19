from dataclasses import asdict
from datetime import datetime
from functools import wraps
from typing import Callable, Dict, Optional, Protocol

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


class DataclassProtocol(Protocol):
    __dataclass_fields__: Dict
    __dataclass_params__: Dict
    __post_init__: Optional[Callable]


def serialize(obj: DataclassProtocol):
    result = {}
    for key, value in asdict(obj).items():
        result[key] = value if not isinstance(value, datetime) else str(value)
    return result

