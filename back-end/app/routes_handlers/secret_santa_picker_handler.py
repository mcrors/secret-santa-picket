from tornado.web import RequestHandler

class SecretSantaPickerHandler(RequestHandler):

    def write_error(self, status_code: int, **kwargs: Any) -> None:

        _, err, _ = kwargs['exc_info']
        self.set_status(status_code)
        if err.description:
            self.write_json(err.description)
        self.finish()

