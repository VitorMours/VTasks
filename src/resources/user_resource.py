from flask_restx import Namespace, Resource
from ..services.impl.user_service_impl import UserServiceImpl
from ..utils.api import user_serializer
bp = Namespace("user", description="Api resource to access the users data")

@bp.route("/")
@bp.response(404, "User not found")
@bp.response(405, "HTTP Method not allowed")
class UserList(Resource):
    @bp.doc("Get all the users data")
    def get(self):
        users = UserServiceImpl.get_all_users()
        return user_serializer(users)

    @bp.doc("Create a new user with body data")
    def post(self):
        return {"Creating":"user"}

@bp.route("/<int:id>")
@bp.param("id", "The user identifier")
@bp.response(404, "User not found")
class User(Resource):
    def get(self, id):
        return {"Returning specific user"}
