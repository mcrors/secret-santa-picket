from tornado.web import RequestHandler
from repositories.user_repository import UserRepository

from utils import check_version, serialize


class UserHandler(RequestHandler):

    @check_version
    def get(self, version, user_id=None):
        user_repository = UserRepository()
        if user_id:
            response = user_repository.get(user_id)
        else:
            users = [serialize(user) for user in user_repository.list()]
            response = {'users': users}
        self.write(response)

    @check_version
    def put(self, version):
        user = self.request.body
        self.write(user)

