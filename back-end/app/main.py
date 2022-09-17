import asyncio

import tornado.web

from routes_handlers.user_handler import UserHandler


class MainHandler(tornado.web.RequestHandler):
    """The main handler"""
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/api/v(?P<version>[0-9])/user", UserHandler),
        (r"/api/v(?P<version>[0-9])/user/(?P<user_id>[0-9]+)", UserHandler)
    ], debug=True)


async def main():
    app = make_app()
    app.listen(8080)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())

