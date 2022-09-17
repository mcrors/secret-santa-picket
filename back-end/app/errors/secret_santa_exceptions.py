import tornado

class SecretSantaPickerError(tornado.web.HTTPError):
    pass


class InvalidVersionError(SecretSantaPickerError):
    pass

