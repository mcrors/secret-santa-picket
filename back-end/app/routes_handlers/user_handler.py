from tornado.web import RequestHandler
from repositories.user_repository import UserRepository

from utils import check_version


class UserHandler(RequestHandler):

    @check_version
    def get(self, version, user_id=None):
        user_repository = UserRepository()
        if user_id:
            user = user_repository.get(user_id)
            self.write(user)
        else:
            users = [user.serialize() for user in user_repository.list()]
            response = {'users': users}
            self.write(response)

