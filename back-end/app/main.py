import asyncio

import tornado.web

from app_config import AppConfig
from repositories import bootstrap_repository
from routes_handlers.user_handler import UserHandler


def make_app() -> tornado.web.Application:
    return tornado.web.Application([
        (r"/api/v(?P<version>[0-9])/user", UserHandler),
        (r"/api/v(?P<version>[0-9])/user/(?P<user_id>[0-9]+)", UserHandler)
    ], debug=True)


async def main(config: AppConfig) -> None:
    bootstrap_repository(config)
    app = make_app()
    app.listen(8080)
    await asyncio.Event().wait()


if __name__ == "__main__":
    config = AppConfig()
    asyncio.run(main(config))

