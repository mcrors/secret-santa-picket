import tornado

class SecretSantaPickerError(tornado.web.HTTPError):
    pass


class InvalidVersionError(SecretSantaPickerError):
    pass


class DatabaseNotConfiguredError():
    pass


class SecretSantaRepositoryError(SecretSantaPickerError):
    pass


class UserNotFoundError(SecretSantaRepositoryError):
    pass

